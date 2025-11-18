#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ant Design 风格的 Grid 栅格组件
"""

from typing import Optional, Union, Dict, List, Any
from adw.styles.spacing import Spacing
from adw.styles.theme import ThemeManager
from adw.styles.breakpoints import Breakpoint

# 动态导入 PySide6 或 PyQt6
try:
    from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy
    from PySide6.QtCore import Qt, QSize
except ImportError:
    try:
        from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy
        from PyQt6.QtCore import Qt, QSize
    except ImportError:
        raise ImportError("Requires either PySide6 or PyQt6")


class Row(QWidget):
    """
    Row 行组件
    用于创建水平排列的列容器
    """
    
    def __init__(
        self,
        align: str = "top",  # top, middle, bottom, stretch
        gutter: Union[int, Dict[str, int], List[int]] = 0,
        justify: str = "start",  # start, end, center, space-around, space-between, space-evenly
        wrap: bool = True,
        parent: Optional[QWidget] = None
    ):
        """
        初始化行组件
        
        Args:
            align: 垂直对齐方式
            gutter: 栅格间隔
            justify: 水平排列方式
            wrap: 是否自动换行
            parent: 父级组件
        """
        super().__init__(parent)
        
        # 存储属性
        self._align = align
        self._gutter = gutter
        self._justify = justify
        self._wrap = wrap
        
        # 创建布局
        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._layout)
        
        # 设置对象名称用于样式
        self.setObjectName("adw-row")
        
        # 初始化UI
        self._setup_ui()
        
    def _setup_ui(self):
        """设置UI样式"""
        # 设置对齐方式
        if self._justify == "start":
            self._layout.setAlignment(Qt.AlignLeft)
        elif self._justify == "end":
            self._layout.setAlignment(Qt.AlignRight)
        elif self._justify == "center":
            self._layout.setAlignment(Qt.AlignCenter)
        elif self._justify == "space-around":
            self._layout.setSpacing(Spacing.get_md())
        elif self._justify == "space-between":
            self._layout.setSpacing(Spacing.get_lg())
        elif self._justify == "space-evenly":
            self._layout.setSpacing(Spacing.get_xl())
            
        # 设置垂直对齐
        if self._align == "top":
            self._layout.setAlignment(Qt.AlignTop)
        elif self._align == "middle":
            self._layout.setAlignment(Qt.AlignVCenter)
        elif self._align == "bottom":
            self._layout.setAlignment(Qt.AlignBottom)
        elif self._align == "stretch":
            self._layout.setAlignment(Qt.AlignStretch)
            
        # 设置换行
        if not self._wrap:
            self._layout.setSizeConstraint(QHBoxLayout.SetFixedSize)
            
        # 设置间距
        self._update_gutter()
        
        # 应用样式
        self._apply_style()
        
    def _update_gutter(self):
        """更新间距"""
        if isinstance(self._gutter, int):
            # 单一数值
            self._layout.setSpacing(self._gutter)
        elif isinstance(self._gutter, dict):
            # 响应式对象
            # 这里简化处理，实际应该根据屏幕尺寸动态调整
            default_gutter = self._gutter.get('md', Spacing.get_md())
            self._layout.setSpacing(default_gutter)
        elif isinstance(self._gutter, list) and len(self._gutter) >= 2:
            # 数组形式 [水平间距, 垂直间距]
            self._layout.setSpacing(self._gutter[0])
            
    def _apply_style(self):
        """应用样式"""
        # 获取当前主题设置
        settings = ThemeManager.get_theme_settings()
        
        style = f"""
        QWidget#adw-row {{
            background-color: transparent;
            margin: 0;
            padding: 0;
        }}
        """
        self.setStyleSheet(style)
        
    def add_widget(self, widget: QWidget):
        """添加子组件"""
        self._layout.addWidget(widget)
        
    def add_col(self, col: 'Col'):
        """添加列组件"""
        self._layout.addWidget(col)
        
    # 属性的 getter 和 setter 方法
    def get_align(self) -> str:
        """获取垂直对齐方式"""
        return self._align
        
    def set_align(self, align: str):
        """设置垂直对齐方式"""
        self._align = align
        self._setup_ui()
        
    def get_gutter(self) -> Union[int, Dict[str, int], List[int]]:
        """获取栅格间隔"""
        return self._gutter
        
    def set_gutter(self, gutter: Union[int, Dict[str, int], List[int]]):
        """设置栅格间隔"""
        self._gutter = gutter
        self._update_gutter()
        
    def get_justify(self) -> str:
        """获取水平排列方式"""
        return self._justify
        
    def set_justify(self, justify: str):
        """设置水平排列方式"""
        self._justify = justify
        self._setup_ui()
        
    def get_wrap(self) -> bool:
        """获取是否自动换行"""
        return self._wrap
        
    def set_wrap(self, wrap: bool):
        """设置是否自动换行"""
        self._wrap = wrap
        self._setup_ui()


class Col(QWidget):
    """
    Col 列组件
    必须放在 Row 组件内部使用
    """
    
    def __init__(
        self,
        span: int = 0,
        offset: int = 0,
        pull: int = 0,
        push: int = 0,
        order: int = 0,
        flex: Optional[Union[str, int]] = None,
        xs: Optional[Union[int, Dict[str, Any]]] = None,
        sm: Optional[Union[int, Dict[str, Any]]] = None,
        md: Optional[Union[int, Dict[str, Any]]] = None,
        lg: Optional[Union[int, Dict[str, Any]]] = None,
        xl: Optional[Union[int, Dict[str, Any]]] = None,
        xxl: Optional[Union[int, Dict[str, Any]]] = None,
        widget: Optional[QWidget] = None,
        parent: Optional[QWidget] = None
    ):
        """
        初始化列组件
        
        Args:
            span: 栅格占位格数 (0-24)
            offset: 栅格左侧的间隔格数
            pull: 栅格向左移动格数
            push: 栅格向右移动格数
            order: 栅格顺序
            flex: flex 布局属性
            xs: <576px 响应式栅格
            sm: ≥576px 响应式栅格
            md: ≥768px 响应式栅格
            lg: ≥992px 响应式栅格
            xl: ≥1200px 响应式栅格
            xxl: ≥1600px 响应式栅格
            widget: 包含的子组件
            parent: 父级组件
        """
        super().__init__(parent)
        
        # 存储属性
        self._span = span
        self._offset = offset
        self._pull = pull
        self._push = push
        self._order = order
        self._flex = flex
        self._responsive = {
            Breakpoint.XS: xs,
            Breakpoint.SM: sm,
            Breakpoint.MD: md,
            Breakpoint.LG: lg,
            Breakpoint.XL: xl,
            Breakpoint.XXL: xxl
        }
        self._widget = widget
        
        # 设置对象名称用于样式
        self.setObjectName("adw-col")
        
        # 创建布局
        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._layout)
        
        # 初始化UI
        self._setup_ui()
        
    def _setup_ui(self):
        """设置UI样式"""
        # 添加子组件
        if self._widget:
            self._layout.addWidget(self._widget)
            
        # 设置顺序
        if self._order > 0:
            self._layout.setStretch(self._layout.indexOf(self._widget) if self._widget else 0, self._order)
            
        # 应用样式
        self._apply_style()
        
    def _apply_style(self):
        """应用样式"""
        # 获取当前主题设置
        settings = ThemeManager.get_theme_settings()
        
        # 计算宽度百分比 (基于24栅格)
        width_percent = (self._span / 24 * 100) if self._span > 0 else 0
        
        # 计算偏移量
        offset_percent = (self._offset / 24 * 100) if self._offset > 0 else 0
        
        style = f"""
        QWidget#adw-col {{
            background-color: transparent;
            margin: 0;
            padding: 0;
        }}
        """
        
        # 设置宽度和偏移
        if width_percent > 0:
            style += f"QWidget#adw-col {{ width: {width_percent}%; }}"
            
        if offset_percent > 0:
            style += f"QWidget#adw-col {{ margin-left: {offset_percent}%; }}"
            
        self.setStyleSheet(style)
        
    def _get_responsive_span(self) -> int:
        """获取响应式栅格跨度"""
        # 这里简化处理，实际应该根据屏幕尺寸动态调整
        # 优先级: xs < sm < md < lg < xl < xxl
        for bp in [Breakpoint.XS, Breakpoint.SM, Breakpoint.MD, 
                   Breakpoint.LG, Breakpoint.XL, Breakpoint.XXL]:
            if self._responsive[bp] is not None:
                value = self._responsive[bp]
                if isinstance(value, int):
                    return value
                elif isinstance(value, dict) and 'span' in value:
                    return value['span']
        return self._span
        
    # 属性的 getter 和 setter 方法
    def get_span(self) -> int:
        """获取栅格占位格数"""
        return self._span
        
    def set_span(self, span: int):
        """设置栅格占位格数"""
        self._span = max(0, min(24, span))  # 限制在0-24之间
        self._apply_style()
        
    def get_offset(self) -> int:
        """获取栅格左侧间隔格数"""
        return self._offset
        
    def set_offset(self, offset: int):
        """设置栅格左侧间隔格数"""
        self._offset = max(0, min(24, offset))  # 限制在0-24之间
        self._apply_style()
        
    def get_pull(self) -> int:
        """获取栅格向左移动格数"""
        return self._pull
        
    def set_pull(self, pull: int):
        """设置栅格向左移动格数"""
        self._pull = pull
        # 实现向左移动的逻辑
        
    def get_push(self) -> int:
        """获取栅格向右移动格数"""
        return self._push
        
    def set_push(self, push: int):
        """设置栅格向右移动格数"""
        self._push = push
        # 实现向右移动的逻辑
        
    def get_order(self) -> int:
        """获取栅格顺序"""
        return self._order
        
    def set_order(self, order: int):
        """设置栅格顺序"""
        self._order = order
        self._setup_ui()
        
    def get_flex(self) -> Optional[Union[str, int]]:
        """获取flex布局属性"""
        return self._flex
        
    def set_flex(self, flex: Optional[Union[str, int]]):
        """设置flex布局属性"""
        self._flex = flex
        # 实现flex布局逻辑
        
    def get_widget(self) -> Optional[QWidget]:
        """获取包含的子组件"""
        return self._widget
        
    def set_widget(self, widget: Optional[QWidget]):
        """设置包含的子组件"""
        # 清除现有组件
        for i in reversed(range(self._layout.count())): 
            self._layout.itemAt(i).widget().setParent(None)
            
        self._widget = widget
        if widget:
            self._layout.addWidget(widget)