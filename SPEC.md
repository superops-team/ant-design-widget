# Ant Design Widget (ADW) 开发规范

## 1. 项目概述

Ant Design Widget (ADW) 是一个基于 Ant Design 设计语言的 Python GUI 组件库，构建于 PySide6/PyQt6 之上，提供一系列可复用的 Widget，帮助开发者快速构建界面美观的桌面应用程序。

### 1.1 设计理念

本项目遵循 Ant Design 的四大设计价值观：
- **自然**：追求自然的交互体验，降低用户认知成本
- **确定性**：提供高确定性、低合作熵的界面状态
- **意义感**：连接用户工作使命，创造有意义的人机交互
- **生长性**：用发展的眼光做设计，考虑人机共同生长

同时遵循 Robin Williams 的四大设计原则：
- **对比 (Contrast)**：通过大小、颜色、位置等对比突出重要元素
- **重复 (Repetition)**：重复使用设计元素增强视觉统一性
- **对齐 (Alignment)**：确保界面元素有序排列，营造整洁感
- ** proximity)**：相关元素靠近排列，建立清晰的视觉关系

## 2. 技术栈与环境

### 2.1 Python 版本
- 主要支持 Python 3.8+
- 开发环境使用 Python 3.12

### 2.2 GUI 框架
- 主要支持 PySide6
- 兼容 PyQt6

### 2.3 依赖管理
- 使用 `uv` 进行虚拟环境管理和依赖安装
- 依赖声明在 `requirements.txt` 文件中

### 2.4 开发工具
- IDE: 推荐使用 VSCode 或 PyCharm
- 代码格式化: black
- 代码检查: flake8
- 类型检查: mypy

## 3. 目录结构规划

```
adw/
├── __init__.py
├── common/              # 通用工具和基类
│   ├── __init__.py
│   ├── constants.py     # 常量定义
│   ├── utils.py         # 工具函数
│   └── base.py          # 基础组件类
├── components/          # 组件实现
│   ├── __init__.py
│   ├── dialog/          # 对话框组件
│   ├── layout/          # 布局组件
│   ├── navigation/      # 导航组件
│   ├── widgets/         # 基础控件
│   └── ...
├── styles/              # 样式管理
│   ├── __init__.py
│   ├── theme.py         # 主题管理
│   ├── colors.py        # 颜色定义
│   ├── typography.py    # 字体排版
│   └── icons/           # 图标资源
├── i18n/                # 国际化支持
│   ├── __init__.py
│   ├── en_US.py         # 英文翻译
│   ├── zh_CN.py         # 中文翻译
│   └── ...
└── ...
```

## 4. 组件协议

### 4.1 基础组件类
所有组件应继承自基础组件类，确保统一的接口和行为：

```python
class BaseWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()
        self._setup_style()
        self._setup_signals()
    
    def _setup_ui(self):
        """设置UI元素"""
        pass
    
    def _setup_style(self):
        """设置样式"""
        pass
    
    def _setup_signals(self):
        """设置信号槽连接"""
        pass
    
    def apply_theme(self, theme):
        """应用主题"""
        pass
    
    def retranslate_ui(self):
        """重新翻译UI文本"""
        pass
```

### 4.2 组件命名规范
- 类名采用 PascalCase 命名法，如 `Button`, `InputField`
- 模块名采用 snake_case 命名法，如 `button.py`, `input_field.py`
- 常量采用 UPPER_SNAKE_CASE 命名法，如 `PRIMARY_COLOR`, `FONT_SIZE_LARGE`

### 4.3 组件属性
所有组件应支持以下核心属性：
- `size`: 组件尺寸 (small, medium, large)
- `variant`: 组件变体 (filled, outlined, text)
- `color`: 组件颜色 (primary, secondary, success, warning, error)
- `disabled`: 是否禁用
- `loading`: 是否加载中

### 4.4 组件事件
所有组件应支持以下核心事件：
- `clicked`: 点击事件
- `changed`: 值改变事件
- `focused`: 获得焦点事件
- `blurred`: 失去焦点事件

## 5. 样式管理系统

### 5.1 主题系统
实现基于主题的样式管理，支持亮色和暗色主题切换：

```python
class Theme:
    def __init__(self, name, is_dark=False):
        self.name = name
        self.is_dark = is_dark
        self.colors = {}
        self.typography = {}
        self.spacing = {}
    
    def get_color(self, key):
        return self.colors.get(key)
    
    def get_font(self, key):
        return self.typography.get(key)
```

### 5.2 颜色规范
遵循 Ant Design 颜色体系：
- 主色: `#1890ff` (蓝)
- 成功色: `#52c41a` (绿)
- 警告色: `#faad14` (黄)
- 错误色: `#ff4d4f` (红)
- 中性色: 用于文本、背景、边框等

### 5.3 排版规范
- 字体家族: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif`
- 字体大小: 
  - 超大标题: 38px
  - 大标题: 24px
  - 中标题: 18px
  - 小标题: 14px
  - 正文: 14px
  - 辅助文字: 12px

### 5.4 间距规范
采用 8px 网格系统：
- 微小间距: 4px
- 小间距: 8px
- 中等间距: 16px
- 大间距: 24px
- 超大间距: 32px

## 6. 国际化 (i18n) 支持

### 6.1 多语言管理
支持中英文切换，预留扩展其他语言的能力：

```python
class I18nManager:
    def __init__(self, locale='zh_CN'):
        self.locale = locale
        self.translations = {}
        self._load_translations()
    
    def _load_translations(self):
        # 加载对应语言的翻译文件
        pass
    
    def translate(self, key, **kwargs):
        # 翻译文本，支持参数替换
        pass
    
    def set_locale(self, locale):
        # 切换语言
        pass
```

### 6.2 翻译文本组织
翻译文本按功能模块组织，便于维护：
- common: 通用文本
- components: 组件相关文本
- dialog: 对话框文本
- validation: 验证提示文本

## 7. 布局系统

### 7.1 栅格系统
基于 24 栅格系统实现响应式布局：
- 支持列宽设置 (1-24)
- 支持偏移量设置
- 支持响应式断点 (xs, sm, md, lg, xl, xxl)

### 7.2 弹性布局
提供 Flexbox 布局组件：
- 支持主轴和交叉轴对齐
- 支持伸缩因子设置
- 支持换行控制

### 7.3 布局组件
- Row: 行容器
- Col: 列容器
- Space: 间距组件
- Divider: 分割线组件

## 8. 测试规范

### 8.1 单元测试
- 使用 pytest 作为测试框架
- 每个组件至少包含基本功能测试
- 测试覆盖率目标 80%+

### 8.2 UI 测试
- 使用 pytest-qt 进行 Qt 相关测试
- 验证组件渲染正确性
- 验证事件处理逻辑

### 8.3 集成测试
- 验证组件间协作
- 验证主题切换功能
- 验证国际化功能

## 9. 文档规范

### 9.1 组件文档
每个组件应包含完整文档：
- 组件说明
- 属性列表及说明
- 使用示例
- 注意事项

### 9.2 示例代码
提供丰富的示例代码展示组件用法：
- 基础用法
- 不同尺寸
- 不同状态
- 组合使用

## 10. 发布规范

### 10.1 版本管理
遵循语义化版本规范 (SemVer)：
- 主版本号: 不兼容的API修改
- 次版本号: 向后兼容的功能性新增
- 修订号: 向后兼容的问题修正

### 10.2 发布流程
1. 更新版本号
2. 更新 CHANGELOG
3. 运行测试套件
4. 构建发布包
5. 发布到 PyPI

## 11. 质量保证

### 11.1 代码审查
- 所有代码变更需经过代码审查
- 遵循编码规范
- 确保测试覆盖

### 11.2 持续集成
- 自动化运行测试
- 自动化代码质量检查
- 自动生成文档

### 11.3 性能监控
- 组件渲染性能监控
- 内存使用监控
- 响应时间监控