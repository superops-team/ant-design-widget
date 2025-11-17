# Button 按钮组件

按钮用于开始一个即时操作。

## 设计指南

按钮意味着一个操作（或一系列操作）。点击按钮会触发相应的业务逻辑。

在 Ant Design 中提供五种类型的按钮：

1. **主按钮 (Primary)**：用于主要操作，每个区域最多只有一个主按钮
2. **默认按钮 (Default)**：用于没有优先级的一系列操作
3. **虚线按钮 (Dashed)**：通常用于添加操作
4. **文字按钮 (Text)**：用于次要操作
5. **链接按钮 (Link)**：用于外部链接

还有四种附加属性：
1. **危险 (danger)**：用于风险操作，如删除或授权
2. **幽灵 (ghost)**：用于复杂背景的情况，通常用于首页
3. **禁用 (disabled)**：当操作不可用时
4. **加载中 (loading)**：在按钮中添加加载指示器，避免多次提交

## 组件属性 (API)

### Button Props

| 属性 | 说明 | 类型 | 默认值 | 版本 |
| --- | --- | --- | --- | --- |
| block | 将按钮宽度调整为其父宽度 | boolean | false |  |
| danger | 设置危险按钮 | boolean | false |  |
| disabled | 按钮失效状态 | boolean | false |  |
| ghost | 幽灵属性，使按钮背景透明 | boolean | false |  |
| href | 点击跳转的地址，指定此属性 button 的行为和 a 链接一致 | string | - |  |
| htmlType | 设置 button 原生的 type 值 | `submit` \| `button` \| `reset` | `button` |  |
| icon | 设置按钮的图标组件 | ReactNode | - |  |
| loading | 设置按钮载入状态 | boolean \| { delay: number } | false |  |
| shape | 设置按钮形状 | `circle` \| `round` | - |  |
| size | 设置按钮大小 | `large` \| `middle` \| `small` | `middle` |  |
| target | 相当于 a 标签的 target 属性，href 存在时生效 | string | - |  |
| type | 设置按钮类型 | `primary` \| `dashed` \| `link` \| `text` \| `default` | `default` |  |
| onClick | 点击按钮时的回调 | (event) => void | - |  |

## 使用示例

### 基本用法

```python
from adw.components.widgets.button import Button

# 主按钮
primary_btn = Button(text="Primary Button", type="primary")

# 默认按钮
default_btn = Button(text="Default Button", type="default")

# 虚线按钮
dashed_btn = Button(text="Dashed Button", type="dashed")

# 文字按钮
text_btn = Button(text="Text Button", type="text")

# 链接按钮
link_btn = Button(text="Link Button", type="link")
```

### 按钮尺寸

```python
# 大按钮
large_btn = Button(text="Large Button", size="large")

# 默认按钮
default_btn = Button(text="Default Button", size="middle")

# 小按钮
small_btn = Button(text="Small Button", size="small")
```

### 危险按钮

```python
# 危险主按钮
danger_primary_btn = Button(text="Danger Primary", type="primary", danger=True)

# 危险默认按钮
danger_default_btn = Button(text="Danger Default", danger=True)
```

### 禁用状态

```python
disabled_btn = Button(text="Disabled Button", disabled=True)
```

### 加载中状态

```python
loading_btn = Button(text="Loading Button", loading=True)
```

### 幽灵按钮

```python
ghost_btn = Button(text="Ghost Button", ghost=True)
```

### 块级按钮

```python
block_btn = Button(text="Block Button", block=True)
```

### 带图标的按钮

```python
# 图标按钮
icon_btn = Button(icon="search")

# 带文字的图标按钮
icon_text_btn = Button(text="Search", icon="search")
```

## 注意事项

1. 当按钮包含两个中文字符时，会在字符之间自动添加空格（排除 Text 按钮和 Link 按钮）
2. 主按钮在一个区域内应该唯一
3. 链接按钮的行为与 `<a>` 标签一致，支持 href 和 target 属性
4. 加载状态会阻止用户的连续点击操作