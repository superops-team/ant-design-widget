#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
样式系统示例
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGroupBox
from adw.styles.colors import ColorPalette, ThemeType, set_theme
from adw.styles.typography import Typography, TypographyScale
from adw.styles.spacing import Spacing
from adw.styles.theme import ThemeManager


class StyleExample(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # 标题
        title_label = QLabel("Ant Design 样式系统示例")
        title_font = Typography.get_heading_2_font()
        title_label.setStyleSheet(f"""
            font-size: {title_font.size}px;
            font-weight: {title_font.weight};
            color: {ColorPalette.get_heading_color()};
            margin-bottom: {Spacing.get_lg()}px;
        """)
        layout.addWidget(title_label)
        
        # 颜色示例
        color_group = QGroupBox("色彩系统")
        color_layout = QVBoxLayout()
        
        # 主色示例
        primary_label = QLabel("主色 (Primary Color)")
        primary_label.setStyleSheet(f"""
            background-color: {ColorPalette.get_primary_color()};
            color: white;
            padding: {Spacing.get_sm()}px;
            margin: {Spacing.get_xs()}px 0;
            border-radius: 4px;
        """)
        color_layout.addWidget(primary_label)
        
        # 功能色示例
        status_layout = QHBoxLayout()
        
        success_label = QLabel("成功 (Success)")
        success_label.setStyleSheet(f"""
            background-color: {ColorPalette.get_success_color()};
            color: white;
            padding: {Spacing.get_sm()}px;
            margin: {Spacing.get_xs()}px;
            border-radius: 4px;
        """)
        status_layout.addWidget(success_label)
        
        warning_label = QLabel("警告 (Warning)")
        warning_label.setStyleSheet(f"""
            background-color: {ColorPalette.get_warning_color()};
            color: white;
            padding: {Spacing.get_sm()}px;
            margin: {Spacing.get_xs()}px;
            border-radius: 4px;
        """)
        status_layout.addWidget(warning_label)
        
        error_label = QLabel("错误 (Error)")
        error_label.setStyleSheet(f"""
            background-color: {ColorPalette.get_error_color()};
            color: white;
            padding: {Spacing.get_sm()}px;
            margin: {Spacing.get_xs()}px;
            border-radius: 4px;
        """)
        status_layout.addWidget(error_label)
        
        color_layout.addLayout(status_layout)
        
        # 主题切换按钮
        theme_button = QPushButton("切换到暗色主题")
        theme_button.setStyleSheet(f"""
            background-color: {ColorPalette.get_primary_color()};
            color: white;
            border: none;
            padding: {Spacing.get_sm()}px {Spacing.get_md()}px;
            border-radius: 4px;
            margin: {Spacing.get_md()}px 0;
        """)
        theme_button.clicked.connect(self.toggle_theme)
        color_layout.addWidget(theme_button)
        
        color_group.setLayout(color_layout)
        layout.addWidget(color_group)
        
        # 排版示例
        typography_group = QGroupBox("排版系统")
        typography_layout = QVBoxLayout()
        
        heading1 = QLabel("超大标题 (Heading 1)")
        h1_font = Typography.get_heading_1_font()
        heading1.setStyleSheet(f"""
            font-size: {h1_font.size}px;
            font-weight: {h1_font.weight};
            color: {ColorPalette.get_heading_color()};
            margin: {Spacing.get_xs()}px 0;
        """)
        typography_layout.addWidget(heading1)
        
        heading2 = QLabel("大标题 (Heading 2)")
        h2_font = Typography.get_heading_2_font()
        heading2.setStyleSheet(f"""
            font-size: {h2_font.size}px;
            font-weight: {h2_font.weight};
            color: {ColorPalette.get_heading_color()};
            margin: {Spacing.get_xs()}px 0;
        """)
        typography_layout.addWidget(heading2)
        
        body_text = QLabel("正文文本 (Body Text) - 这是正常的正文文本，用于显示主要内容。")
        body_font = Typography.get_body_font()
        body_text.setStyleSheet(f"""
            font-size: {body_font.size}px;
            font-weight: {body_font.weight};
            color: {ColorPalette.get_text_color()};
            margin: {Spacing.get_xs()}px 0;
        """)
        typography_layout.addWidget(body_text)
        
        secondary_text = QLabel("辅助文本 (Secondary Text) - 这是辅助文本，通常用于描述或注释。")
        secondary_font = Typography.get_secondary_font()
        secondary_text.setStyleSheet(f"""
            font-size: {secondary_font.size}px;
            font-weight: {secondary_font.weight};
            color: {ColorPalette.get_secondary_text_color()};
            margin: {Spacing.get_xs()}px 0;
        """)
        typography_layout.addWidget(secondary_text)
        
        typography_group.setLayout(typography_layout)
        layout.addWidget(typography_group)
        
        # 间距示例
        spacing_group = QGroupBox("间距系统")
        spacing_layout = QVBoxLayout()
        
        spacing_text = QLabel("不同间距示例:")
        spacing_layout.addWidget(spacing_text)
        
        # 不同间距的方块
        for i, (name, size) in enumerate([
            ("微小间距", Spacing.get_xs()),
            ("小间距", Spacing.get_sm()),
            ("中等间距", Spacing.get_md()),
            ("大间距", Spacing.get_lg())
        ]):
            spacing_box = QLabel(f"{name} ({size}px)")
            spacing_box.setStyleSheet(f"""
                background-color: {ColorPalette.get_color('blue', 2)};
                color: {ColorPalette.get_color('blue', 8)};
                padding: {Spacing.get_xs()}px;
                margin: {size}px 0;
                border-radius: 4px;
            """)
            spacing_layout.addWidget(spacing_box)
        
        spacing_group.setLayout(spacing_layout)
        layout.addWidget(spacing_group)
        
        self.setLayout(layout)
        self.setWindowTitle("Ant Design 样式系统示例")
        self.resize(600, 800)
        
        # 应用当前主题
        self.apply_current_theme()
    
    def toggle_theme(self):
        """切换主题"""
        current_theme = ThemeManager.get_theme()
        if current_theme == ThemeType.LIGHT:
            set_theme(ThemeType.DARK)
        else:
            set_theme(ThemeType.LIGHT)
        
        self.apply_current_theme()
    
    def apply_current_theme(self):
        """应用当前主题"""
        theme = ThemeManager.get_theme()
        settings = ThemeManager.get_theme_settings()
        
        # 设置窗口背景
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {settings.background_color};
                color: {settings.text_color};
            }}
            QGroupBox {{
                border: 1px solid {settings.border_color};
                margin: {Spacing.get_md()}px 0;
                padding: {Spacing.get_sm()}px;
            }}
            QGroupBox::title {{
                color: {settings.heading_color};
                subline-offset: -10px;
            }}
        """)
        
        # 更新按钮文本
        button = self.findChild(QPushButton)
        if button:
            if theme == ThemeType.LIGHT:
                button.setText("切换到暗色主题")
            else:
                button.setText("切换到亮色主题")


def main():
    app = QApplication(sys.argv)
    example = StyleExample()
    example.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()