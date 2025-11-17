#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ant Design 风格的 Button 组件
"""

from typing import Optional, Callable, Union

# 动态导入 PySide6 或 PyQt6
try:
    from PySide6.QtWidgets import QPushButton, QWidget
    from PySide6.QtCore import Qt, QSize, Signal as pyqtSignal
    from PySide6.QtGui import QIcon
    Signal = pyqtSignal
except ImportError:
    try:
        from PyQt6.QtWidgets import QPushButton, QWidget
        from PyQt6.QtCore import Qt, QSize, pyqtSignal
        from PyQt6.QtGui import QIcon
        Signal = pyqtSignal
    except ImportError:
        raise ImportError("Requires either PySide6 or PyQt6")

class Button(QPushButton):
    """
    Ant Design 风格的按钮组件
    
    支持多种类型、尺寸、状态的按钮
    """

    # 点击信号
    clicked_signal = Signal()

    def __init__(
        self,
        text: str = "",
        parent: Optional[QWidget] = None,
        type: str = "default",  # primary, dashed, text, link, default
        size: str = "middle",  # large, middle, small
        icon: Optional[str] = None,
        danger: bool = False,
        disabled: bool = False,
        loading: bool = False,
        ghost: bool = False,
        block: bool = False,
        shape: Optional[str] = None,  # circle, round
        html_type: str = "button",  # submit, button, reset
        href: Optional[str] = None,
        target: Optional[str] = None,
        on_click: Optional[Callable] = None,
    ):
        """
        初始化按钮组件
        
        Args:
            text: 按钮文本
            parent: 父级组件
            type: 按钮类型 (primary, dashed, text, link, default)
            size: 按钮尺寸 (large, middle, small)
            icon: 图标
            danger: 是否为危险按钮
            disabled: 是否禁用
            loading: 是否加载中
            ghost: 是否幽灵按钮
            block: 是否块级按钮
            shape: 按钮形状 (circle, round)
            html_type: 原生 button 类型 (submit, button, reset)
            href: 链接地址
            target: 链接打开方式
            on_click: 点击回调函数
        """
        super().__init__(text, parent)
        
        # 存储属性
        self._type = type
        self._size = size
        self._icon = icon
        self._danger = danger
        self._disabled = disabled
        self._loading = loading
        self._ghost = ghost
        self._block = block
        self._shape = shape
        self._html_type = html_type
        self._href = href
        self._target = target
        
        # 设置对象名称用于样式
        self.setObjectName(f"adw-button-{type}")
        
        # 初始化UI
        self._setup_ui()
        
        # 设置初始状态
        self.setDisabled(disabled)
        self.set_loading(loading)
        
        # 连接信号
        self.clicked.connect(self._on_clicked)
        if on_click:
            self.clicked_signal.connect(on_click)

    def _setup_ui(self):
        """设置UI样式"""
        # 设置按钮样式
        self._update_style()
        
        # 设置尺寸
        self._update_size()
        
        # 设置形状
        self._update_shape()
        
        # 设置块级按钮
        if self._block:
            self.setMinimumWidth(200)  # 默认最小宽度
            
    def _update_style(self):
        """更新按钮样式"""
        # 基础样式
        style = """
        QPushButton {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            border: 1px solid #d9d9d9;
            background-color: #fff;
            color: rgba(0, 0, 0, 0.85);
            padding: 4px 15px;
            border-radius: 2px;
        }
        
        QPushButton:hover {
            border-color: #40a9ff;
            background-color: #fff;
            color: #40a9ff;
        }
        
        QPushButton:pressed {
            border-color: #096dd9;
            background-color: #e6f7ff;
            color: #096dd9;
        }
        
        QPushButton:disabled {
            border-color: #d9d9d9;
            background-color: #f5f5f5;
            color: rgba(0, 0, 0, 0.25);
        }
        """
        
        # 根据类型设置样式
        if self._type == "primary":
            style += """
            QPushButton {
                background-color: #1890ff;
                border-color: #1890ff;
                color: #fff;
            }
            
            QPushButton:hover {
                background-color: #40a9ff;
                border-color: #40a9ff;
                color: #fff;
            }
            
            QPushButton:pressed {
                background-color: #096dd9;
                border-color: #096dd9;
                color: #fff;
            }
            
            QPushButton:disabled {
                background-color: #f5f5f5;
                border-color: #d9d9d9;
                color: rgba(0, 0, 0, 0.25);
            }
            """
            
        elif self._type == "dashed":
            style += """
            QPushButton {
                border-style: dashed;
                border-color: #d9d9d9;
                background-color: #fff;
                color: rgba(0, 0, 0, 0.85);
            }
            """
            
        elif self._type == "text":
            style += """
            QPushButton {
                border: none;
                background-color: transparent;
                color: #1890ff;
                padding: 4px 0;
            }
            
            QPushButton:hover {
                background-color: rgba(0, 0, 0, 0.018);
                color: #40a9ff;
            }
            
            QPushButton:pressed {
                background-color: rgba(0, 0, 0, 0.028);
                color: #096dd9;
            }
            
            QPushButton:disabled {
                background-color: transparent;
                color: rgba(0, 0, 0, 0.25);
            }
            """
            
        elif self._type == "link":
            style += """
            QPushButton {
                border: none;
                background-color: transparent;
                color: #1890ff;
                padding: 4px 0;
                text-decoration: underline;
            }
            
            QPushButton:hover {
                background-color: transparent;
                color: #40a9ff;
            }
            
            QPushButton:pressed {
                background-color: transparent;
                color: #096dd9;
            }
            
            QPushButton:disabled {
                background-color: transparent;
                color: rgba(0, 0, 0, 0.25);
            }
            """
        
        # 危险按钮样式
        if self._danger:
            if self._type == "primary":
                style += """
                QPushButton {
                    background-color: #ff4d4f;
                    border-color: #ff4d4f;
                    color: #fff;
                }
                
                QPushButton:hover {
                    background-color: #ff7875;
                    border-color: #ff7875;
                    color: #fff;
                }
                
                QPushButton:pressed {
                    background-color: #d9363e;
                    border-color: #d9363e;
                    color: #fff;
                }
                
                QPushButton:disabled {
                    background-color: #f5f5f5;
                    border-color: #d9d9d9;
                    color: rgba(0, 0, 0, 0.25);
                }
                """
            else:
                style += """
                QPushButton {
                    border-color: #ff4d4f;
                    color: #ff4d4f;
                }
                
                QPushButton:hover {
                    border-color: #ff7875;
                    color: #ff7875;
                }
                
                QPushButton:pressed {
                    border-color: #d9363e;
                    color: #d9363e;
                }
                
                QPushButton:disabled {
                    border-color: #d9d9d9;
                    color: rgba(0, 0, 0, 0.25);
                }
                """
        
        # 幽灵按钮样式
        if self._ghost:
            style += """
            QPushButton {
                background-color: transparent;
            }
            """
            
            if self._type == "primary":
                style += """
                QPushButton {
                    border-color: #1890ff;
                    color: #1890ff;
                }
                
                QPushButton:hover {
                    border-color: #40a9ff;
                    color: #40a9ff;
                    background-color: transparent;
                }
                
                QPushButton:pressed {
                    border-color: #096dd9;
                    color: #096dd9;
                    background-color: transparent;
                }
                """
                
            elif self._danger:
                style += """
                QPushButton {
                    border-color: #ff4d4f;
                    color: #ff4d4f;
                }
                
                QPushButton:hover {
                    border-color: #ff7875;
                    color: #ff7875;
                    background-color: transparent;
                }
                
                QPushButton:pressed {
                    border-color: #d9363e;
                    color: #d9363e;
                    background-color: transparent;
                }
                """
        
        # 加载中状态样式
        if self._loading:
            style += """
            QPushButton {
                cursor: wait;
            }
            """
            
        self.setStyleSheet(style)
        
    def _update_size(self):
        """更新按钮尺寸"""
        if self._size == "large":
            self.setMinimumHeight(40)
            font = self.font()
            font.setPointSize(16)
            self.setFont(font)
        elif self._size == "small":
            self.setMinimumHeight(24)
            font = self.font()
            font.setPointSize(12)
            self.setFont(font)
        else:  # middle/default
            self.setMinimumHeight(32)
            
    def _update_shape(self):
        """更新按钮形状"""
        if self._shape == "circle":
            # 圆形按钮通常是正方形
            if self._size == "large":
                self.setFixedSize(40, 40)
            elif self._size == "small":
                self.setFixedSize(24, 24)
            else:
                self.setFixedSize(32, 32)
            self.setStyleSheet(self.styleSheet() + "border-radius: 50%;")
        elif self._shape == "round":
            # 椭圆形按钮
            if self._size == "large":
                self.setMinimumHeight(40)
                self.setStyleSheet(self.styleSheet() + "border-radius: 20px;")
            elif self._size == "small":
                self.setMinimumHeight(24)
                self.setStyleSheet(self.styleSheet() + "border-radius: 12px;")
            else:
                self.setMinimumHeight(32)
                self.setStyleSheet(self.styleSheet() + "border-radius: 16px;")
                
    def _on_clicked(self):
        """点击事件处理"""
        if not self._loading and not self._disabled:
            self.clicked_signal.emit()
            
    # 属性的 getter 和 setter 方法
    def get_type(self) -> str:
        """获取按钮类型"""
        return self._type
        
    def set_type(self, type: str):
        """设置按钮类型"""
        self._type = type
        self.setObjectName(f"adw-button-{type}")
        self._update_style()
        
    def get_size(self) -> str:
        """获取按钮尺寸"""
        return self._size
        
    def set_size(self, size: str):
        """设置按钮尺寸"""
        self._size = size
        self._update_size()
        # 如果是圆形按钮，需要重新设置尺寸
        if self._shape == "circle":
            self._update_shape()
            
    def get_danger(self) -> bool:
        """获取危险状态"""
        return self._danger
        
    def set_danger(self, danger: bool):
        """设置危险状态"""
        self._danger = danger
        self._update_style()
        
    def get_disabled(self) -> bool:
        """获取禁用状态"""
        return self._disabled
        
    def set_disabled(self, disabled: bool):
        """设置禁用状态"""
        self._disabled = disabled
        self.setDisabled(disabled)
        
    def get_loading(self) -> bool:
        """获取加载中状态"""
        return self._loading
        
    def set_loading(self, loading: bool):
        """设置加载中状态"""
        self._loading = loading
        self._update_style()
        # 设置加载中状态
        if loading:
            self.setCursor(Qt.WaitCursor)
        else:
            self.setCursor(Qt.ArrowCursor)
            
    def get_ghost(self) -> bool:
        """获取幽灵状态"""
        return self._ghost
        
    def set_ghost(self, ghost: bool):
        """设置幽灵状态"""
        self._ghost = ghost
        self._update_style()
        
    def get_block(self) -> bool:
        """获取块级状态"""
        return self._block
        
    def set_block(self, block: bool):
        """设置块级状态"""
        self._block = block
        if block:
            self.setMinimumWidth(200)
        else:
            self.setMinimumWidth(0)
            
    def get_shape(self) -> Optional[str]:
        """获取按钮形状"""
        return self._shape
        
    def set_shape(self, shape: Optional[str]):
        """设置按钮形状"""
        self._shape = shape
        self._update_shape()
        
    def get_text(self) -> str:
        """获取按钮文本"""
        return self.text()
        
    def set_text(self, text: str):
        """设置按钮文本"""
        # 处理中文字符间添加空格的逻辑（排除 text 和 link 类型）
        if (self._type not in ["text", "link"] and 
            len(text) == 2 and 
            all('\u4e00' <= char <= '\u9fff' for char in text)):
            text = text[0] + " " + text[1]
        self.setText(text)