
---

1. 分层治理：把“风格”拆成三层

---

层级	职责	技术实现	变动频率	
① 全局基础色	背景、文字、边框、禁用色等	QPalette	低（仅随深浅主题切换）	
② 组件微交互	悬停、按下、圆角、阴影	QSS ::hover/:pressed	中	
③ 品牌/业务皮肤	主色、强调色、圆角大小、字号	QSS 变量 + 模板	高（运营随时换皮肤）	

---

2. 主题切换：让颜色“可配置”it cl

---

- 拒绝硬编码色值 → 使用 CSS 变量（Qt ≥ 6.2 已支持 qproperty 绑定，但 QSS 本身不支持变量）。
- 推荐做法：用 Jinja2 / mustache 把 `.qss` 当模板渲染，颜色抽成 JSON 配置文件。

目录示例：

```
res/
 ├─ themes/
 │   ├─ light.json      # 浅色主题变量
 │   ├─ dark.json       # 深色主题变量
 │   └─ brand.json      # 品牌定制变量（可选）
 ├─ styles/
 │   ├─ base.qss.j2     # 基础组件样式模板
 │   └─ widgets.qss.j2  # 业务控件模板
```

light.json（片段）

```json
{
  "bg_primary": "#ffffff",
  "bg_secondary": "#f5f5f5",
  "accent": "#2196F3",
  "radius": "6px"
}
```

base.qss.j2

```css
QWidget {
    background: {{ bg_primary }};
}
QPushButton {
    background: {{ accent }};
    border-radius: {{ radius }};
}
```

构建阶段（或运行阶段缓存）执行：

```bash
python build_styles.py light.json base.qss.j2 > dist/light.qss
```

---

3. 资源管理：让设计师能直接改图

---

- 所有图标、插画、动画统一用 Qt Resource System（`.qrc`）打包；设计师只需替换 `res/icons/` 下的 svg/png，无需改代码。
- 在 QSS 中通过 `url(:/icons/...)` 引用，保证路径随资源自动更新。

---

4. 代码骨架（可直接用）

---

main.py

```python
from pathlib import Path
from PySide6.QtWidgets import QApplication
from core.theme_manager import ThemeManager      # 见下方
from ui.main_window import MainWindow

app = QApplication([])
tm = ThemeManager(folder=Path("res/themes"))
tm.apply("light")                                # 首次加载
window = MainWindow()
window.show()
app.exec()
```

core/theme_manager.py

```python
from pathlib import Path
from jinja2 import Template
from PySide6.QtWidgets import QApplication

class ThemeManager:
    def __init__(self, folder: Path):
        self.folder = folder
        self._cache = {}          # key -> qss string

    def _render(self, name: str) -> str:
        if name in self._cache:
            return self._cache[name]
        var_path = self.folder / f"{name}.json"
        tpl_path = self.folder.parent / "styles" / "base.qss.j2"
        vars = json.loads(var_path.read_text())
        tpl = Template(tpl_path.read_text())
        qss = tpl.render(**vars)
        self._cache[name] = qss
        return qss

    def apply(self, name: str):
        QApplication.instance().setStyleSheet(self._render(name))
```

---

5.  checklist（上线前自查）

---

检查项	是否完成	
所有色值均来自 JSON，无硬编码	✅	
深色/浅色/高对比 三套主题一键切换	✅	
悬停/禁用/聚焦/错误 四种伪状态全部覆盖	✅	
字号、圆角、间距抽成变量，方便 UI 走查	✅	
图标统一走 qrc，设计师替换即可	✅	
样式文件按组件拆分，单文件不超过 300 行	✅	

---

6. 进阶：一键打包主题编辑器

---

把 JSON 变量直接生成一个 QPropertySheet 界面，让运营同学拖拖颜色就能实时预览并导出新的 `.qss`，无需重启 App。实现成本 ≈ 半天，收益 = 无限皮肤。

---

一句话总结

“用 QPalette 管颜色，用 QSS 管状态，用模板引擎管变量，用 qrc 管资源”——照此范式，10 万行级的 PySide6 项目也能在 5 分钟内换完全局主题。