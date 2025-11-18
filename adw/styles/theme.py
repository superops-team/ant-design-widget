#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ant Design 主题管理系统
"""

from typing import Dict, Any
from dataclasses import dataclass, asdict
from adw.styles.colors import ColorPalette, ThemeType
from adw.styles.typography import Typography, FontSettings
from adw.styles.spacing import Spacing


@dataclass
class ThemeSettings:
    """主题设置"""
    # 颜色设置
    primary_color: str = "#1890ff"
    success_color: str = "#52c41a"
    warning_color: str = "#faad14"
    error_color: str = "#ff4d4f"
    info_color: str = "#1890ff"
    
    # 文本颜色
    heading_color: str = "rgba(0, 0, 0, 0.85)"
    text_color: str = "rgba(0, 0, 0, 0.65)"
    secondary_text_color: str = "rgba(0, 0, 0, 0.45)"
    disabled_text_color: str = "rgba(0, 0, 0, 0.25)"
    
    # 背景和边框
    background_color: str = "#ffffff"
    card_background_color: str = "#ffffff"
    border_color: str = "#d9d9d9"
    divider_color: str = "#f0f0f0"
    
    # 排版设置
    font_family: str = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    
    # 间距设置
    base_spacing_unit: int = 8


class ThemeManager:
    """主题管理器"""
    
    _instance = None
    _current_theme_type = ThemeType.LIGHT
    _custom_settings = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @classmethod
    def get_instance(cls):
        """获取单例实例"""
        if cls._instance is None:
            cls._instance = ThemeManager()
        return cls._instance
    
    @classmethod
    def set_theme(cls, theme_type: ThemeType):
        """设置主题类型"""
        cls._current_theme_type = theme_type
        ColorPalette.set_theme(theme_type)
    
    @classmethod
    def get_theme(cls) -> ThemeType:
        """获取当前主题类型"""
        return cls._current_theme_type
    
    @classmethod
    def set_custom_setting(cls, key: str, value: Any):
        """设置自定义主题属性"""
        cls._custom_settings[key] = value
    
    @classmethod
    def get_custom_setting(cls, key: str, default: Any = None):
        """获取自定义主题属性"""
        return cls._custom_settings.get(key, default)
    
    @classmethod
    def get_theme_settings(cls) -> ThemeSettings:
        """获取当前主题设置"""
        settings = ThemeSettings()
        
        # 根据主题类型更新颜色设置
        if cls._current_theme_type == ThemeType.DARK:
            settings.heading_color = "rgba(255, 255, 255, 0.85)"
            settings.text_color = "rgba(255, 255, 255, 0.65)"
            settings.secondary_text_color = "rgba(255, 255, 255, 0.45)"
            settings.disabled_text_color = "rgba(255, 255, 255, 0.25)"
            settings.background_color = "#141414"
            settings.card_background_color = "#1f1f1f"
            settings.border_color = "#424242"
            settings.divider_color = "#303030"
        
        # 应用自定义设置
        for key, value in cls._custom_settings.items():
            if hasattr(settings, key):
                setattr(settings, key, value)
        
        return settings
    
    @classmethod
    def apply_theme_to_widget(cls, widget):
        """应用主题到Qt组件"""
        try:
            from PySide6.QtWidgets import QWidget
            from PySide6.QtGui import QPalette, QColor
        except ImportError:
            try:
                from PyQt6.QtWidgets import QWidget
                from PyQt6.QtGui import QPalette, QColor
            except ImportError:
                return
        
        if not isinstance(widget, QWidget):
            return
            
        settings = cls.get_theme_settings()
        
        # 创建调色板
        palette = widget.palette()
        
        # 设置背景色
        palette.setColor(QPalette.ColorRole.Window, QColor(settings.background_color))
        palette.setColor(QPalette.ColorRole.Base, QColor(settings.card_background_color))
        
        # 设置文本颜色
        palette.setColor(QPalette.ColorRole.WindowText, QColor(settings.heading_color))
        palette.setColor(QPalette.ColorRole.Text, QColor(settings.text_color))
        
        # 设置按钮颜色
        palette.setColor(QPalette.ColorRole.Button, QColor(settings.card_background_color))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(settings.text_color))
        
        # 应用调色板
        widget.setPalette(palette)
        
        # 设置样式表
        style_sheet = f"""
        QWidget {{
            background-color: {settings.background_color};
            color: {settings.text_color};
            font-family: {settings.font_family};
        }}
        """
        widget.setStyleSheet(style_sheet)


# 便利函数
def set_theme(theme_type: ThemeType):
    """设置主题"""
    ThemeManager.set_theme(theme_type)

def get_theme() -> ThemeType:
    """获取当前主题"""
    return ThemeManager.get_theme()

def get_theme_settings() -> ThemeSettings:
    """获取主题设置"""
    return ThemeManager.get_theme_settings()

def apply_theme_to_widget(widget):
    """应用主题到组件"""
    ThemeManager.get_instance().apply_theme_to_widget(widget)