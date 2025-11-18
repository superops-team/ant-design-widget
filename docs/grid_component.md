# Grid 栅格组件

24 栅格系统，用于创建响应式布局。

## 设计理念

在多数业务情况下，Ant Design 需要在设计区域内解决大量信息收纳的问题，因此在 12 栅格系统的基础上，我们将整个设计建议区域按照 24 等分的原则进行划分。

划分之后的信息区块我们称之为『盒子』。建议横向排列的盒子数量最多四个，最少一个。

## 组件属性 (API)

### Row Props

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| align | 垂直对齐方式 | `top` \| `middle` \| `bottom` \| `stretch` | `top` |
| gutter | 栅格间隔，可以写成像素值或支持响应式的对象写法来设置水平间隔或水平+垂直间隔 | number \| object \| array | 0 |
| justify | 水平排列方式 | `start` \| `end` \| `center` \| `space-around` \| `space-between` \| `space-evenly` | `start` |
| wrap | 是否自动换行 | boolean | true |

### Col Props

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| flex | flex 布局属性 | string \| number | - |
| offset | 栅格左侧的间隔格数，间隔内不可以有栅格 | number | 0 |
| order | 栅格顺序 | number | 0 |
| pull | 栅格向左移动格数 | number | 0 |
| push | 栅格向右移动格数 | number | 0 |
| span | 栅格占位格数，为 0 时相当于 display: none | number | - |
| xs | `<576px` 响应式栅格 | number \| object | - |
| sm | `≥576px` 响应式栅格 | number \| object | - |
| md | `≥768px` 响应式栅格 | number \| object | - |
| lg | `≥992px` 响应式栅格 | number \| object | - |
| xl | `≥1200px` 响应式栅格 | number \| object | - |
| xxl | `≥1600px` 响应式栅格 | number \| object | - |

## 使用示例

### 基础栅格

```python
from adw.components.layout.grid import Row, Col

# 基本栅格布局
row = Row()
row.add_widget(Col(span=12, widget=QLabel("col-12")))
row.add_widget(Col(span=12, widget=QLabel("col-12")))

# 三等分布局
row2 = Row()
row2.add_widget(Col(span=8, widget=QLabel("col-8")))
row2.add_widget(Col(span=8, widget=QLabel("col-8")))
row2.add_widget(Col(span=8, widget=QLabel("col-8")))
```

### 区块间隔

```python
# 设置栅格间隔
row = Row(gutter=16)
row.add_widget(Col(span=6, widget=QLabel("col-6")))
row.add_widget(Col(span=6, widget=QLabel("col-6")))
row.add_widget(Col(span=6, widget=QLabel("col-6")))
row.add_widget(Col(span=6, widget=QLabel("col-6")))

# 响应式间隔
row2 = Row(gutter={'xs': 8, 'sm': 16, 'md': 24, 'lg': 32})
row2.add_widget(Col(span=6, widget=QLabel("col-6")))
row2.add_widget(Col(span=6, widget=QLabel("col-6")))
row2.add_widget(Col(span=6, widget=QLabel("col-6")))
row2.add_widget(Col(span=6, widget=QLabel("col-6")))

# 垂直间隔
row3 = Row(gutter=[16, 24])
```

### 左右偏移

```python
# 列偏移
row = Row()
row.add_widget(Col(span=8, widget=QLabel("col-8")))
row.add_widget(Col(span=8, offset=8, widget=QLabel("col-8")))
```

### 栅格排序

```python
# 列排序
row = Row()
row.add_widget(Col(span=18, push=6, widget=QLabel("col-18 col-push-6")))
row.add_widget(Col(span=6, pull=18, widget=QLabel("col-6 col-pull-18")))
```

### 排版对齐

```python
# 水平对齐
row_start = Row(justify="start")
row_center = Row(justify="center")
row_end = Row(justify="end")
row_space_between = Row(justify="space-between")
row_space_around = Row(justify="space-around")

# 垂直对齐
row_top = Row(align="top")
row_middle = Row(align="middle")
row_bottom = Row(align="bottom")
```

### 响应式布局

```python
# 响应式栅格
col = Col(
    xs=24,     # <576px 显示24格
    sm=12,     # ≥576px 显示12格
    md=8,      # ≥768px 显示8格
    lg=6,      # ≥992px 显示6格
    widget=QLabel("Responsive Column")
)
```

## 样式系统集成

Grid 组件完全基于 ADW 样式系统实现：
- 使用 `Spacing` 进行间距管理
- 使用 `Breakpoint` 进行响应式断点管理
- 支持主题切换

## 注意事项

1. Row 组件用于创建水平排列的列容器
2. Col 组件必须放在 Row 组件内部
3. 栅格系统基于 24 等分
4. 支持响应式布局
5. 支持 Flex 布局的各种对齐方式