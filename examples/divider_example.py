#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Divider 组件示例
"""

import sys
from adw.styles.theme import ThemeManager, ThemeType
from adw.components.widgets.divider import Divider

# 动态导入 PySide6 或 PyQt6
try:
    from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel
except ImportError:
    from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel

class DividerExample(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # 标题
        layout.addWidget(QLabel("Ant Design 风格分割线示例"))
        
        # 水平分割线示例
        layout.addWidget(QLabel("基本水平分割线:"))
        layout.addWidget(Divider())
        
        # 带文本的水平分割线
        layout.addWidget(QLabel("带文本的水平分割线:"))
        layout.addWidget(Divider(text="居中文本"))
        layout.addWidget(Divider(text="左对齐文本", orientation="left"))
        layout.addWidget(Divider(text="右对齐文本", orientation="right"))
        
        # 虚线分割线
        layout.addWidget(QLabel("虚线分割线:"))
        layout.addWidget(Divider(dashed=True))
        layout.addWidget(Divider(text="虚线带文本", dashed=True))
        
        # 垂直分割线示例
        layout.addWidget(QLabel("垂直分割线:"))
        h_layout = QHBoxLayout()
        h_layout.addWidget(QLabel("文本1"))
        h_layout.addWidget(Divider(type="vertical"))
        h_layout.addWidget(QLabel("文本2"))
        h_layout.addWidget(Divider(type="vertical"))
        h_layout.addWidget(QLabel("文本3"))
        layout.addLayout(h_layout)
        
        # 普通样式文本
        layout.addWidget(QLabel("普通样式文本:"))
        layout.addWidget(Divider(text="普通文本", plain=True))
        layout.addWidget(Divider(text="标题样式文本", plain=False))
        
        # 主题切换按钮
        from adw.components.widgets.button import Button
        theme_button = Button("切换到暗色主题")
        theme_button.clicked_signal.connect(self.toggle_theme)
        layout.addWidget(theme_button)
        
        self.setLayout(layout)
        self.setWindowTitle("Ant Design Divider 示例")
        self.resize(600, 400)

    def toggle_theme(self):
        """切换主题"""
        current_theme = ThemeManager.get_theme()
        sender = self.sender()
        if current_theme == ThemeType.LIGHT:
            ThemeManager.set_theme(ThemeType.DARK)
            sender.set_text("切换到亮色主题")
        else:
            ThemeManager.set_theme(ThemeType.LIGHT)
            sender.set_text("切换到暗色主题")
        # 重新应用样式
        self.setStyleSheet("")

def main():
    app = QApplication(sys.argv)
    example = DividerExample()
    example.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()