#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ant Design 排版系统
"""

from typing import Dict, Tuple
from dataclasses import dataclass
from enum import Enum


class FontFamily:
    """字体家族"""
    DEFAULT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    MONOSPACE = "Monaco, Consolas, 'Lucida Console', 'Courier New', monospace"


@dataclass
class FontSettings:
    """字体设置"""
    size: int
    weight: int
    family: str = FontFamily.DEFAULT


class TypographyScale(Enum):
    """排版尺寸等级"""
    HEADING_1 = "heading_1"      # 超大标题
    HEADING_2 = "heading_2"      # 大标题
    HEADING_3 = "heading_3"      # 中标题
    HEADING_4 = "heading_4"      # 小标题
    BODY = "body"               # 正文
    SECONDARY = "secondary"     # 辅助文字


class Typography:
    """Ant Design 排版系统"""
    
    # 字体大小定义
    _font_sizes = {
        TypographyScale.HEADING_1: 38,
        TypographyScale.HEADING_2: 24,
        TypographyScale.HEADING_3: 18,
        TypographyScale.HEADING_4: 14,
        TypographyScale.BODY: 14,
        TypographyScale.SECONDARY: 12
    }
    
    # 字体粗细定义
    _font_weights = {
        'thin': 300,
        'regular': 400,
        'bold': 600
    }
    
    # 默认字体设置
    _default_settings = {
        TypographyScale.HEADING_1: FontSettings(38, 600),
        TypographyScale.HEADING_2: FontSettings(24, 600),
        TypographyScale.HEADING_3: FontSettings(18, 600),
        TypographyScale.HEADING_4: FontSettings(14, 600),
        TypographyScale.BODY: FontSettings(14, 400),
        TypographyScale.SECONDARY: FontSettings(12, 400)
    }
    
    @classmethod
    def get_font_size(cls, scale: TypographyScale) -> int:
        """获取指定等级的字体大小"""
        return cls._font_sizes.get(scale, 14)
    
    @classmethod
    def get_font_weight(cls, weight_name: str) -> int:
        """获取指定名称的字体粗细"""
        return cls._font_weights.get(weight_name, 400)
    
    @classmethod
    def get_font_settings(cls, scale: TypographyScale) -> FontSettings:
        """获取指定等级的完整字体设置"""
        return cls._default_settings.get(scale, FontSettings(14, 400))
    
    @classmethod
    def get_heading_1_font(cls) -> FontSettings:
        """获取超大标题字体"""
        return cls.get_font_settings(TypographyScale.HEADING_1)
    
    @classmethod
    def get_heading_2_font(cls) -> FontSettings:
        """获取大标题字体"""
        return cls.get_font_settings(TypographyScale.HEADING_2)
    
    @classmethod
    def get_heading_3_font(cls) -> FontSettings:
        """获取中标题字体"""
        return cls.get_font_settings(TypographyScale.HEADING_3)
    
    @classmethod
    def get_heading_4_font(cls) -> FontSettings:
        """获取小标题字体"""
        return cls.get_font_settings(TypographyScale.HEADING_4)
    
    @classmethod
    def get_body_font(cls) -> FontSettings:
        """获取正文字体"""
        return cls.get_font_settings(TypographyScale.BODY)
    
    @classmethod
    def get_secondary_font(cls) -> FontSettings:
        """获取辅助文字字体"""
        return cls.get_font_settings(TypographyScale.SECONDARY)
    
    @classmethod
    def get_font_family(cls, family: str = FontFamily.DEFAULT) -> str:
        """获取字体家族"""
        return family


# 便利函数
def get_heading_1_font() -> FontSettings:
    """获取超大标题字体"""
    return Typography.get_heading_1_font()

def get_heading_2_font() -> FontSettings:
    """获取大标题字体"""
    return Typography.get_heading_2_font()

def get_heading_3_font() -> FontSettings:
    """获取中标题字体"""
    return Typography.get_heading_3_font()

def get_heading_4_font() -> FontSettings:
    """获取小标题字体"""
    return Typography.get_heading_4_font()

def get_body_font() -> FontSettings:
    """获取正文字体"""
    return Typography.get_body_font()

def get_secondary_font() -> FontSettings:
    """获取辅助文字字体"""
    return Typography.get_secondary_font()