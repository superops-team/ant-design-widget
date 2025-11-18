# 样式系统设计文档

## 概述

本样式系统基于 Ant Design 色彩规范设计，提供一套可复用的色彩、排版和间距系统，支持多主题扩展。

## 色彩系统

### 主色彩

Ant Design 的主色彩包括以下12种基础色彩：

1. **蓝色 (Blue)** - `#1890ff` - 主色
2. **紫色 (Purple)** - `#722ed1` 
3. **青色 (Cyan)** - `#13c2c2`
4. **绿色 (Green)** - `#52c41a`
5. **品红色 (Magenta)** - `#eb2f96`
6. **红色 (Red)** - `#f5222d`
7. **橙色 (Orange)** - `#fa8c16`
8. **黄色 (Yellow)** - `#fadb14`
9. **火山色 (Volcano)** - `#fa541c`
10. **金色 (Gold)** - `#faad14`
11. **柠檬色 (Lime)** - `#a0d911`
12. **极光绿 (Geek Blue)** - `#2f54eb`

### 功能色彩

功能色彩用于传达特定的语义信息：

- **成功色**: `#52c41a` (绿色)
- **警告色**: `#faad14` (金色)
- **错误色**: `#ff4d4f` (红色)
- **信息色**: `#1890ff` (蓝色)

### 中性色彩

中性色彩用于文本、背景和边框：

- **标题文本**: `rgba(0, 0, 0, 0.85)`
- **正文文本**: `rgba(0, 0, 0, 0.65)`
- **辅助文本**: `rgba(0, 0, 0, 0.45)`
- **禁用文本**: `rgba(0, 0, 0, 0.25)`
- **边框**: `#d9d9d9`
- **分割线**: `#f0f0f0`
- **背景色**: `#f5f5f5`
- **卡片背景**: `#ffffff`

## 排版系统

### 字体家族

```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
```

### 字体大小

- **超大标题**: 38px
- **大标题**: 24px
- **中标题**: 18px
- **小标题**: 14px
- **正文**: 14px
- **辅助文字**: 12px

### 字体粗细

- **细体**: 300
- **常规**: 400
- **粗体**: 600

## 间距系统

采用 8px 网格系统：

- **微小间距**: 4px
- **小间距**: 8px
- **中等间距**: 16px
- **大间距**: 24px
- **超大间距**: 32px
- **巨大间距**: 48px

## 主题系统

支持亮色和暗色主题切换：

### 亮色主题 (默认)

- **背景色**: `#ffffff`
- **卡片背景**: `#ffffff`
- **边框色**: `#d9d9d9`
- **文本色**: `rgba(0, 0, 0, 0.85)`

### 暗色主题

- **背景色**: `#141414`
- **卡片背景**: `#1f1f1f`
- **边框色**: `#424242`
- **文本色**: `rgba(255, 255, 255, 0.85)`

## 使用指南

### 颜色使用

```python
from adw.styles.colors import ColorPalette

# 获取主色
primary_color = ColorPalette.get_primary_color()
# 获取成功色
success_color = ColorPalette.get_success_color()
# 获取特定颜色的色阶
blue_5 = ColorPalette.get_color('blue', 5)
```

### 排版使用

```python
from adw.styles.typography import Typography

# 获取标题样式
title_font = Typography.get_title_font()
# 获取正文样式
body_font = Typography.get_body_font()
```

### 间距使用

```python
from adw.styles.spacing import Spacing

# 获取中等间距
medium_spacing = Spacing.get_medium()
# 获取自定义间距
custom_spacing = Spacing.get_spacing(2)  # 16px
```