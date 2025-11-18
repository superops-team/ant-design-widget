#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ant Design 色彩系统
"""

from typing import Dict, List, Optional, Union
from enum import Enum


class ThemeType(Enum):
    """主题类型"""
    LIGHT = "light"
    DARK = "dark"


class ColorPalette:
    """Ant Design 色彩调色板"""
    
    # Ant Design 基础色彩调色板
    # 每种颜色有10个色阶，从浅到深: 1-10
    _base_colors = {
        'blue': ['#e6f7ff', '#bae7ff', '#91d5ff', '#69c0ff', '#40a9ff', 
                 '#1890ff', '#096dd9', '#0050b3', '#003a8c', '#002766'],
        'purple': ['#f9f0ff', '#efdbff', '#d3adf7', '#b37feb', '#9254de', 
                   '#722ed1', '#531dab', '#391085', '#22075e', '#120338'],
        'cyan': ['#e6fffb', '#b5f5ec', '#87e8de', '#5cdbd3', '#36cfc9', 
                 '#13c2c2', '#08979c', '#006d75', '#00474f', '#002329'],
        'green': ['#f6ffed', '#d9f7be', '#b7eb8f', '#95de64', '#73d13d', 
                  '#52c41a', '#389e0d', '#237804', '#135200', '#092b00'],
        'magenta': ['#fff0f6', '#ffd6e7', '#ffadd2', '#ff85c0', '#f759ab', 
                    '#eb2f96', '#c41d7f', '#9e1068', '#780650', '#520339'],
        'red': ['#fff1f0', '#ffccc7', '#ffa39e', '#ff7875', '#ff4d4f', 
                '#f5222d', '#cf1322', '#a8071a', '#820014', '#5c0011'],
        'orange': ['#fff7e6', '#ffe7ba', '#ffd591', '#ffc069', '#ffa940', 
                   '#fa8c16', '#d46b08', '#ad4e00', '#873800', '#612500'],
        'yellow': ['#feffe6', '#ffffb8', '#fffb8f', '#fff566', '#ffec3d', 
                   '#fadb14', '#d4b106', '#ad8b00', '#876800', '#614700'],
        'volcano': ['#fff2e8', '#ffd8bf', '#ffbb96', '#ff9c6e', '#ff7a45', 
                    '#fa541c', '#d4380d', '#ad2102', '#871400', '#610b00'],
        'gold': ['#fffbe6', '#fff1b8', '#ffe58f', '#ffd666', '#ffc53d', 
                 '#faad14', '#d48806', '#ad6800', '#874d00', '#613400'],
        'lime': ['#fcffe6', '#f4ffb8', '#eaff8f', '#d3f261', '#bae637', 
                 '#a0d911', '#7cb305', '#5b8c00', '#3f6600', '#254000'],
        'geekblue': ['#f0f5ff', '#d6e4ff', '#adc6ff', '#85a5ff', '#597ef7', 
                     '#2f54eb', '#1d39c4', '#10239e', '#061178', '#030852']
    }
    
    # 功能色彩
    _functional_colors = {
        'success': '#52c41a',
        'warning': '#faad14',
        'error': '#ff4d4f',
        'info': '#1890ff'
    }
    
    # 中性色彩 (亮色主题)
    _light_neutral_colors = {
        'heading': 'rgba(0, 0, 0, 0.85)',
        'text': 'rgba(0, 0, 0, 0.65)',
        'secondary_text': 'rgba(0, 0, 0, 0.45)',
        'disabled_text': 'rgba(0, 0, 0, 0.25)',
        'border': '#d9d9d9',
        'divider': '#f0f0f0',
        'background': '#ffffff',
        'card_background': '#ffffff'
    }
    
    # 中性色彩 (暗色主题)
    _dark_neutral_colors = {
        'heading': 'rgba(255, 255, 255, 0.85)',
        'text': 'rgba(255, 255, 255, 0.65)',
        'secondary_text': 'rgba(255, 255, 255, 0.45)',
        'disabled_text': 'rgba(255, 255, 255, 0.25)',
        'border': '#424242',
        'divider': '#303030',
        'background': '#141414',
        'card_background': '#1f1f1f'
    }
    
    # 当前主题
    _current_theme = ThemeType.LIGHT
    
    @classmethod
    def set_theme(cls, theme: ThemeType):
        """设置主题"""
        cls._current_theme = theme
    
    @classmethod
    def get_theme(cls) -> ThemeType:
        """获取当前主题"""
        return cls._current_theme
    
    @classmethod
    def get_primary_color(cls, level: int = 6) -> str:
        """获取主色 (默认蓝色)"""
        return cls.get_color('blue', level)
    
    @classmethod
    def get_color(cls, color_name: str, level: int = 6) -> str:
        """获取指定颜色的指定色阶"""
        if color_name in cls._base_colors:
            # 确保level在有效范围内 (1-10)
            level = max(1, min(10, level))
            return cls._base_colors[color_name][level - 1]
        return '#000000'
    
    @classmethod
    def get_success_color(cls) -> str:
        """获取成功色"""
        return cls._functional_colors['success']
    
    @classmethod
    def get_warning_color(cls) -> str:
        """获取警告色"""
        return cls._functional_colors['warning']
    
    @classmethod
    def get_error_color(cls) -> str:
        """获取错误色"""
        return cls._functional_colors['error']
    
    @classmethod
    def get_info_color(cls) -> str:
        """获取信息色"""
        return cls._functional_colors['info']
    
    @classmethod
    def get_heading_color(cls) -> str:
        """获取标题文本颜色"""
        if cls._current_theme == ThemeType.DARK:
            return cls._dark_neutral_colors['heading']
        return cls._light_neutral_colors['heading']
    
    @classmethod
    def get_text_color(cls) -> str:
        """获取正文文本颜色"""
        if cls._current_theme == ThemeType.DARK:
            return cls._dark_neutral_colors['text']
        return cls._light_neutral_colors['text']
    
    @classmethod
    def get_secondary_text_color(cls) -> str:
        """获取辅助文本颜色"""
        if cls._current_theme == ThemeType.DARK:
            return cls._dark_neutral_colors['secondary_text']
        return cls._light_neutral_colors['secondary_text']
    
    @classmethod
    def get_disabled_text_color(cls) -> str:
        """获取禁用文本颜色"""
        if cls._current_theme == ThemeType.DARK:
            return cls._dark_neutral_colors['disabled_text']
        return cls._light_neutral_colors['disabled_text']
    
    @classmethod
    def get_border_color(cls) -> str:
        """获取边框颜色"""
        if cls._current_theme == ThemeType.DARK:
            return cls._dark_neutral_colors['border']
        return cls._light_neutral_colors['border']
    
    @classmethod
    def get_divider_color(cls) -> str:
        """获取分割线颜色"""
        if cls._current_theme == ThemeType.DARK:
            return cls._dark_neutral_colors['divider']
        return cls._light_neutral_colors['divider']
    
    @classmethod
    def get_background_color(cls) -> str:
        """获取背景色"""
        if cls._current_theme == ThemeType.DARK:
            return cls._dark_neutral_colors['background']
        return cls._light_neutral_colors['background']
    
    @classmethod
    def get_card_background_color(cls) -> str:
        """获取卡片背景色"""
        if cls._current_theme == ThemeType.DARK:
            return cls._dark_neutral_colors['card_background']
        return cls._light_neutral_colors['card_background']
    
    @classmethod
    def get_all_colors(cls) -> Dict[str, List[str]]:
        """获取所有颜色"""
        return cls._base_colors.copy()
    
    @classmethod
    def generate_color_palette(cls, base_color: str) -> List[str]:
        """
        根据基础颜色生成色彩调色板
        这里简化实现，实际Ant Design使用算法生成
        """
        # 这是一个简化的实现，实际项目中可以使用更复杂的算法
        # 如 ant-design-colors 库中的算法
        return [
            f"{base_color}10", f"{base_color}20", f"{base_color}30",
            f"{base_color}40", f"{base_color}50", f"{base_color}60",
            f"{base_color}70", f"{base_color}80", f"{base_color}90",
            f"{base_color}100"
        ]


# 便利函数
def set_theme(theme: ThemeType):
    """设置主题"""
    ColorPalette.set_theme(theme)

def get_theme() -> ThemeType:
    """获取当前主题"""
    return ColorPalette.get_theme()

def get_primary_color(level: int = 6) -> str:
    """获取主色"""
    return ColorPalette.get_primary_color(level)

def get_success_color() -> str:
    """获取成功色"""
    return ColorPalette.get_success_color()

def get_warning_color() -> str:
    """获取警告色"""
    return ColorPalette.get_warning_color()

def get_error_color() -> str:
    """获取错误色"""
    return ColorPalette.get_error_color()

def get_info_color() -> str:
    """获取信息色"""
    return ColorPalette.get_info_color()