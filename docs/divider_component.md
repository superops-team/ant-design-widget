# Divider 分割线组件

分割线用于区隔内容。

## 设计指南

分割线用于将内容分成不同的部分，常用于：
1. 分隔文章的不同章节
2. 分隔行内文本和链接，如表格的操作列

## 组件属性 (API)

### Divider Props

| 属性 | 说明 | 类型 | 默认值 | 版本 |
| --- | --- | --- | --- | --- |
| children | 分割线中显示的文本 | str | - |  |
| type | 分割线类型 | `horizontal` \| `vertical` | `horizontal` |  |
| dashed | 是否为虚线 | bool | False |  |
| orientation | 文本位置 | `left` \| `right` \| `center` | `center` |  |
| orientationMargin | 文本与最近边界的间距，仅在 orientation 为 left 或 right 时有效 | int \| str | - |  |
| plain | 文本是否为普通样式 | bool | True |  |

## 使用示例

### 水平分割线

```python
from adw.components.widgets.divider import Divider

# 基本水平分割线
divider = Divider()

# 带文本的水平分割线
divider_with_text = Divider(text="文本")

# 带文本的水平分割线（左对齐）
divider_left = Divider(text="左对齐文本", orientation="left")

# 带文本的水平分割线（右对齐）
divider_right = Divider(text="右对齐文本", orientation="right")

# 虚线分割线
dashed_divider = Divider(dashed=True)
```

### 垂直分割线

```python
# 垂直分割线
vertical_divider = Divider(type="vertical")
```

### 普通样式文本

```python
# 普通样式文本
plain_divider = Divider(text="普通文本", plain=True)
```

### 主题支持

Divider 组件支持 Ant Design 的主题系统，可以自动适应亮色和暗色主题：

```python
from adw.styles.theme import set_theme, ThemeType

# 切换到暗色主题
set_theme(ThemeType.DARK)

# 切换到亮色主题
set_theme(ThemeType.LIGHT)
```

## 样式系统集成

Divider 组件完全基于 ADW 样式系统实现：
- 使用 `ColorPalette` 进行颜色管理
- 使用 `Typography` 进行字体管理
- 使用 `Spacing` 进行间距管理
- 支持主题切换

## 注意事项

1. 水平分割线是默认类型
2. 垂直分割线主要用于分隔行内元素
3. 当设置 orientationMargin 时，orientation 必须为 left 或 right
4. plain 属性控制文本是否使用普通样式而非标题样式