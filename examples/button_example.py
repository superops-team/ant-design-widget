#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Button 组件示例
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel
from adw.components.widgets.button import Button

class ButtonExample(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # 标题
        layout.addWidget(QLabel("Ant Design 风格按钮示例"))
        
        # 基本按钮类型
        layout.addWidget(QLabel("基本按钮类型:"))
        basic_layout = QHBoxLayout()
        basic_layout.addWidget(Button("Primary", type="primary"))
        basic_layout.addWidget(Button("Default"))
        basic_layout.addWidget(Button("Dashed", type="dashed"))
        basic_layout.addWidget(Button("Text", type="text"))
        basic_layout.addWidget(Button("Link", type="link"))
        layout.addLayout(basic_layout)
        
        # 按钮尺寸
        layout.addWidget(QLabel("按钮尺寸:"))
        size_layout = QHBoxLayout()
        size_layout.addWidget(Button("Large", size="large"))
        size_layout.addWidget(Button("Default"))
        size_layout.addWidget(Button("Small", size="small"))
        layout.addLayout(size_layout)
        
        # 危险按钮
        layout.addWidget(QLabel("危险按钮:"))
        danger_layout = QHBoxLayout()
        danger_layout.addWidget(Button("Danger Default", danger=True))
        danger_layout.addWidget(Button("Danger Primary", type="primary", danger=True))
        layout.addLayout(danger_layout)
        
        # 状态按钮
        layout.addWidget(QLabel("状态按钮:"))
        state_layout = QHBoxLayout()
        state_layout.addWidget(Button("Disabled", disabled=True))
        state_layout.addWidget(Button("Loading", loading=True))
        layout.addLayout(state_layout)
        
        # 幽灵按钮
        layout.addWidget(QLabel("幽灵按钮:"))
        ghost_layout = QHBoxLayout()
        ghost_layout.addWidget(Button("Ghost", ghost=True))
        ghost_layout.addWidget(Button("Ghost Primary", type="primary", ghost=True))
        layout.addLayout(ghost_layout)
        
        # 块级按钮
        layout.addWidget(QLabel("块级按钮:"))
        layout.addWidget(Button("Block Button", block=True))
        
        # 形状按钮
        layout.addWidget(QLabel("形状按钮:"))
        shape_layout = QHBoxLayout()
        shape_layout.addWidget(Button("Circle", shape="circle"))
        shape_layout.addWidget(Button("Round", shape="round"))
        layout.addLayout(shape_layout)
        
        # 中文文本按钮
        layout.addWidget(QLabel("中文文本按钮:"))
        chinese_layout = QHBoxLayout()
        chinese_layout.addWidget(Button("确定"))
        chinese_layout.addWidget(Button("取消"))
        chinese_layout.addWidget(Button("提交", type="primary"))
        layout.addLayout(chinese_layout)
        
        self.setLayout(layout)
        self.setWindowTitle("Ant Design Button 示例")
        self.resize(600, 400)

def main():
    app = QApplication(sys.argv)
    example = ButtonExample()
    example.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()