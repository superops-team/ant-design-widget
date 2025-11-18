#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ant Design 间距系统
"""

from typing import Union
from enum import Enum


class SpacingScale(Enum):
    """间距等级"""
    XS = "xs"      # 微小间距 - 4px
    SM = "sm"      # 小间距 - 8px
    MD = "md"      # 中等间距 - 16px
    LG = "lg"      # 大间距 - 24px
    XL = "xl"      # 超大间距 - 32px
    XXL = "xxl"    # 巨大间距 - 48px


class Spacing:
    """Ant Design 间距系统 (基于8px网格)"""
    
    # 间距值定义 (基于8px网格系统)
    _spacing_values = {
        SpacingScale.XS: 4,      # 0.5 * 8
        SpacingScale.SM: 8,      # 1 * 8
        SpacingScale.MD: 16,     # 2 * 8
        SpacingScale.LG: 24,     # 3 * 8
        SpacingScale.XL: 32,     # 4 * 8
        SpacingScale.XXL: 48     # 6 * 8
    }
    
    # 快捷访问属性
    _shortcuts = {
        'xs': SpacingScale.XS,
        'sm': SpacingScale.SM,
        'md': SpacingScale.MD,
        'lg': SpacingScale.LG,
        'xl': SpacingScale.XL,
        'xxl': SpacingScale.XXL
    }
    
    @classmethod
    def get_spacing(cls, scale: Union[SpacingScale, str, int]) -> int:
        """
        获取间距值
        
        Args:
            scale: 间距等级或倍数
                  - SpacingScale枚举
                  - 字符串 ('xs', 'sm', 'md', 'lg', 'xl', 'xxl')
                  - 整数 (表示8px的倍数)
        
        Returns:
            int: 间距值(像素)
        """
        if isinstance(scale, SpacingScale):
            return cls._spacing_values.get(scale, 0)
        elif isinstance(scale, str):
            if scale in cls._shortcuts:
                return cls._spacing_values.get(cls._shortcuts[scale], 0)
            return 0
        elif isinstance(scale, int):
            # 按8px网格计算
            return scale * 8
        return 0
    
    @classmethod
    def get_xs(cls) -> int:
        """获取微小间距 (4px)"""
        return cls.get_spacing(SpacingScale.XS)
    
    @classmethod
    def get_sm(cls) -> int:
        """获取小间距 (8px)"""
        return cls.get_spacing(SpacingScale.SM)
    
    @classmethod
    def get_md(cls) -> int:
        """获取中等间距 (16px)"""
        return cls.get_spacing(SpacingScale.MD)
    
    @classmethod
    def get_lg(cls) -> int:
        """获取大间距 (24px)"""
        return cls.get_spacing(SpacingScale.LG)
    
    @classmethod
    def get_xl(cls) -> int:
        """获取超大间距 (32px)"""
        return cls.get_spacing(SpacingScale.XL)
    
    @classmethod
    def get_xxl(cls) -> int:
        """获取巨大间距 (48px)"""
        return cls.get_spacing(SpacingScale.XXL)
    
    @classmethod
    def get_all_spacings(cls) -> dict:
        """获取所有间距值"""
        return {scale.value: value for scale, value in cls._spacing_values.items()}


# 便利函数
def get_spacing(scale: Union[SpacingScale, str, int]) -> int:
    """获取间距值"""
    return Spacing.get_spacing(scale)

def get_xs() -> int:
    """获取微小间距 (4px)"""
    return Spacing.get_xs()

def get_sm() -> int:
    """获取小间距 (8px)"""
    return Spacing.get_sm()

def get_md() -> int:
    """获取中等间距 (16px)"""
    return Spacing.get_md()

def get_lg() -> int:
    """获取大间距 (24px)"""
    return Spacing.get_lg()

def get_xl() -> int:
    """获取超大间距 (32px)"""
    return Spacing.get_xl()

def get_xxl() -> int:
    """获取巨大间距 (48px)"""
    return Spacing.get_xxl()