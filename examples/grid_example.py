#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Grid 栅格组件示例
"""

import sys
from adw.components.layout.grid import Row, Col

# 动态导入 PySide6 或 PyQt6
try:
    from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame
except ImportError:
    from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame


class GridExample(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # 标题
        title = QLabel("Ant Design 栅格系统示例")
        title.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            margin: 16px 0;
        """)
        layout.addWidget(title)
        
        # 基础栅格示例
        layout.addWidget(QLabel("基础栅格:"))
        self._add_basic_grid_examples(layout)
        
        # 区块间隔示例
        layout.addWidget(QLabel("区块间隔:"))
        self._add_gutter_examples(layout)
        
        # 左右偏移示例
        layout.addWidget(QLabel("左右偏移:"))
        self._add_offset_examples(layout)
        
        # 排版对齐示例
        layout.addWidget(QLabel("排版对齐:"))
        self._add_justify_examples(layout)
        
        # 响应式示例
        layout.addWidget(QLabel("响应式布局:"))
        self._add_responsive_examples(layout)
        
        self.setLayout(layout)
        self.setWindowTitle("Ant Design Grid 栅格示例")
        self.resize(800, 600)
        
    def _add_basic_grid_examples(self, layout):
        """添加基础栅格示例"""
        # 24格
        row1 = Row()
        row1.add_col(Col(span=24, widget=self._create_demo_box("col")))
        
        # 12格 x 2
        row2 = Row()
        row2.add_col(Col(span=12, widget=self._create_demo_box("col-12")))
        row2.add_col(Col(span=12, widget=self._create_demo_box("col-12")))
        
        # 8格 x 3
        row3 = Row()
        row3.add_col(Col(span=8, widget=self._create_demo_box("col-8")))
        row3.add_col(Col(span=8, widget=self._create_demo_box("col-8")))
        row3.add_col(Col(span=8, widget=self._create_demo_box("col-8")))
        
        # 6格 x 4
        row4 = Row()
        row4.add_col(Col(span=6, widget=self._create_demo_box("col-6")))
        row4.add_col(Col(span=6, widget=self._create_demo_box("col-6")))
        row4.add_col(Col(span=6, widget=self._create_demo_box("col-6")))
        row4.add_col(Col(span=6, widget=self._create_demo_box("col-6")))
        
        layout.addWidget(row1)
        layout.addWidget(row2)
        layout.addWidget(row3)
        layout.addWidget(row4)
        
    def _add_gutter_examples(self, layout):
        """添加区块间隔示例"""
        # 水平间隔
        gutter_row = Row(gutter=16)
        gutter_row.add_col(Col(span=6, widget=self._create_demo_box("col-6")))
        gutter_row.add_col(Col(span=6, widget=self._create_demo_box("col-6")))
        gutter_row.add_col(Col(span=6, widget=self._create_demo_box("col-6")))
        gutter_row.add_col(Col(span=6, widget=self._create_demo_box("col-6")))
        
        layout.addWidget(gutter_row)
        
    def _add_offset_examples(self, layout):
        """添加偏移示例"""
        offset_row = Row()
        offset_row.add_col(Col(span=8, widget=self._create_demo_box("col-8")))
        offset_row.add_col(Col(span=8, offset=8, widget=self._create_demo_box("col-8")))
        
        layout.addWidget(offset_row)
        
    def _add_justify_examples(self, layout):
        """添加对齐示例"""
        # 居中对齐
        center_row = Row(justify="center")
        center_row.add_col(Col(span=4, widget=self._create_demo_box("col-4")))
        center_row.add_col(Col(span=4, widget=self._create_demo_box("col-4")))
        center_row.add_col(Col(span=4, widget=self._create_demo_box("col-4")))
        center_row.add_col(Col(span=4, widget=self._create_demo_box("col-4")))
        
        layout.addWidget(center_row)
        
    def _add_responsive_examples(self, layout):
        """添加响应式示例"""
        responsive_row = Row(gutter=16)
        responsive_row.add_col(Col(
            xs=24, sm=12, md=8, lg=6,
            widget=self._create_demo_box("Responsive")
        ))
        responsive_row.add_col(Col(
            xs=24, sm=12, md=8, lg=6,
            widget=self._create_demo_box("Responsive")
        ))
        responsive_row.add_col(Col(
            xs=24, sm=12, md=8, lg=6,
            widget=self._create_demo_box("Responsive")
        ))
        responsive_row.add_col(Col(
            xs=24, sm=12, md=8, lg=6,
            widget=self._create_demo_box("Responsive")
        ))
        
        layout.addWidget(responsive_row)
        
    def _create_demo_box(self, text):
        """创建示例框"""
        label = QLabel(text)
        label.setStyleSheet("""
            background-color: #1890ff;
            color: white;
            padding: 8px 0;
            text-align: center;
            border-radius: 4px;
        """)
        label.setMinimumHeight(40)
        return label


def main():
    app = QApplication(sys.argv)
    example = GridExample()
    example.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()