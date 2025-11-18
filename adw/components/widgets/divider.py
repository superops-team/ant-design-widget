#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ant Design 风格的 Divider 组件
"""

from typing import Optional, Union
from adw.styles.colors import ColorPalette
from adw.styles.typography import Typography, TypographyScale
from adw.styles.spacing import Spacing

# 动态导入 PySide6 或 PyQt6
try:
    from PySide6.QtWidgets import QWidget, QFrame, QHBoxLayout, QVBoxLayout, QLabel
    from PySide6.QtCore import Qt
    from PySide6.QtGui import QFont
except ImportError:
    try:
        from PyQt6.QtWidgets import QWidget, QFrame, QHBoxLayout, QVBoxLayout, QLabel
        from PyQt6.QtCore import Qt
        from PyQt6.QtGui import QFont
    except ImportError:
        raise ImportError("Requires either PySide6 or PyQt6")


class Divider(QFrame):
    """
    Ant Design 风格的分割线组件
    
    支持水平和垂直分割线，可带文本显示
    """

    def __init__(
        self,
        text: Optional[str] = None,
        parent: Optional[QWidget] = None,
        type: str = "horizontal",  # horizontal, vertical
        dashed: bool = False,
        orientation: str = "center",  # left, right, center
        orientation_margin: Optional[Union[int, str]] = None,
        plain: bool = True,
    ):
        """
        初始化分割线组件
        
        Args:
            text: 分割线中显示的文本
            parent: 父级组件
            type: 分割线类型 (horizontal, vertical)
            dashed: 是否为虚线
            orientation: 文本位置 (left, right, center)
            orientation_margin: 文本与最近边界的间距
            plain: 文本是否为普通样式
        """
        super().__init__(parent)
        
        # 存储属性
        self._text = text
        self._type = type
        self._dashed = dashed
        self._orientation = orientation
        self._orientation_margin = orientation_margin
        self._plain = plain
        
        # 设置对象名称用于样式
        self.setObjectName(f"adw-divider-{type}")
        
        # 初始化UI
        self._setup_ui()

    def _setup_ui(self):
        """设置UI样式"""
        if self._type == "horizontal":
            self.setFrameShape(QFrame.Shape.HLine if hasattr(QFrame, 'Shape') else QFrame.HLine)
            self.setLayout(QHBoxLayout())
        else:
            self.setFrameShape(QFrame.Shape.VLine if hasattr(QFrame, 'Shape') else QFrame.VLine)
            self.setLayout(QVBoxLayout())
            
        # 设置分割线样式
        self._update_style()
        
        # 如果有文本，添加文本显示
        if self._text and self._type == "horizontal":
            self._setup_text()
            
    def _update_style(self):
        """更新分割线样式 - 使用样式系统"""
        # 获取当前主题设置
        theme = ColorPalette.get_theme()
        
        # 基础样式
        if self._dashed:
            frame_shape = QFrame.Shape.HLine if hasattr(QFrame, 'Shape') else QFrame.HLine
            frame_shadow = QFrame.Shadow.Plain if hasattr(QFrame, 'Shadow') else QFrame.Plain
            if self._type == "vertical":
                frame_shape = QFrame.Shape.VLine if hasattr(QFrame, 'Shape') else QFrame.VLine
            # 设置框架样式
            self.setFrameStyle(frame_shape | frame_shadow)
            # 设置虚线样式需要通过样式表
            self.setStyleSheet(f"""
                QFrame {{
                    color: {ColorPalette.get_border_color()};
                    border-style: dashed;
                    border-width: 1px 0 0 0;
                    margin: {Spacing.get_lg()}px 0;
                }}
            """)
        else:
            frame_shape = QFrame.Shape.HLine if hasattr(QFrame, 'Shape') else QFrame.HLine
            frame_shadow = QFrame.Shadow.Sunken if hasattr(QFrame, 'Shadow') else QFrame.Sunken
            if self._type == "vertical":
                frame_shape = QFrame.Shape.VLine if hasattr(QFrame, 'Shape') else QFrame.VLine
            # 设置框架样式
            self.setFrameStyle(frame_shape | frame_shadow)
            
            # 设置样式表
            style = f"""
            QFrame {{
                color: {ColorPalette.get_border_color()};
                margin: 0;
                padding: 0;
            }}
            """
            
            if self._type == "horizontal":
                style += f"QFrame {{ margin: {Spacing.get_lg()}px 0; }}"
            else:
                style += f"QFrame {{ margin: 0 {Spacing.get_sm()}px; }}"
                
            self.setStyleSheet(style)
        
    def _setup_text(self):
        """设置文本显示 - 使用样式系统"""
        # 清除现有布局
        for i in reversed(range(self.layout().count())): 
            self.layout().itemAt(i).widget().setParent(None)
            
        # 创建文本标签
        label = QLabel(self._text)
        
        # 设置文本样式
        if not self._plain:
            font = label.font()
            body_font = Typography.get_body_font()
            font.setBold(True)
            font.setPointSize(body_font.size)
            label.setFont(font)
        else:
            font = label.font()
            body_font = Typography.get_body_font()
            font.setPointSize(body_font.size)
            label.setFont(font)
            
        # 设置文本颜色
        label.setStyleSheet(f"""
            color: {ColorPalette.get_text_color()};
            background-color: {ColorPalette.get_background_color()};
            padding: 0 {Spacing.get_sm()}px;
        """)
            
        # 根据对齐方式添加布局
        if self._orientation == "left":
            self.layout().addSpacing(self._get_margin_value())
            self.layout().addWidget(label)
            self.layout().addStretch()
        elif self._orientation == "right":
            self.layout().addStretch()
            self.layout().addWidget(label)
            self.layout().addSpacing(self._get_margin_value())
        else:  # center
            self.layout().addStretch()
            self.layout().addWidget(label)
            self.layout().addStretch()
            
    def _get_margin_value(self) -> int:
        """获取边距值"""
        if self._orientation_margin is None:
            return 0
        if isinstance(self._orientation_margin, int):
            return self._orientation_margin
        if isinstance(self._orientation_margin, str) and self._orientation_margin.isdigit():
            return int(self._orientation_margin)
        return 0

    # 属性的 getter 和 setter 方法
    def get_text(self) -> Optional[str]:
        """获取文本"""
        return self._text
        
    def set_text(self, text: Optional[str]):
        """设置文本"""
        self._text = text
        if text and self._type == "horizontal":
            self._setup_text()
        else:
            # 清除文本显示
            for i in reversed(range(self.layout().count())): 
                self.layout().itemAt(i).widget().setParent(None)
        
    def get_type(self) -> str:
        """获取分割线类型"""
        return self._type
        
    def set_type(self, type: str):
        """设置分割线类型"""
        self._type = type
        self.setObjectName(f"adw-divider-{type}")
        self._setup_ui()
        
    def get_dashed(self) -> bool:
        """获取虚线状态"""
        return self._dashed
        
    def set_dashed(self, dashed: bool):
        """设置虚线状态"""
        self._dashed = dashed
        self._update_style()
        
    def get_orientation(self) -> str:
        """获取文本位置"""
        return self._orientation
        
    def set_orientation(self, orientation: str):
        """设置文本位置"""
        self._orientation = orientation
        if self._text and self._type == "horizontal":
            self._setup_text()
            
    def get_orientation_margin(self) -> Optional[Union[int, str]]:
        """获取文本边距"""
        return self._orientation_margin
        
    def set_orientation_margin(self, margin: Optional[Union[int, str]]):
        """设置文本边距"""
        self._orientation_margin = margin
        if self._text and self._type == "horizontal":
            self._setup_text()
            
    def get_plain(self) -> bool:
        """获取普通样式状态"""
        return self._plain
        
    def set_plain(self, plain: bool):
        """设置普通样式状态"""
        self._plain = plain
        if self._text and self._type == "horizontal":
            self._setup_text()