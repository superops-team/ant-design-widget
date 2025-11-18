#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ant Design 响应式断点系统
"""

from enum import Enum
from typing import Dict


class Breakpoint(str, Enum):
    """响应式断点"""
    XS = 'xs'      # <576px
    SM = 'sm'      # ≥576px
    MD = 'md'      # ≥768px
    LG = 'lg'      # ≥992px
    XL = 'xl'      # ≥1200px
    XXL = 'xxl'    # ≥1600px


# 断点值
BREAKPOINT_VALUES = {
    Breakpoint.XS: 575,
    Breakpoint.SM: 576,
    Breakpoint.MD: 768,
    Breakpoint.LG: 992,
    Breakpoint.XL: 1200,
    Breakpoint.XXL: 1600
}

# 媒体查询
MEDIA_QUERIES = {
    Breakpoint.XS: '(max-width: 575px)',
    Breakpoint.SM: '(min-width: 576px)',
    Breakpoint.MD: '(min-width: 768px)',
    Breakpoint.LG: '(min-width: 992px)',
    Breakpoint.XL: '(min-width: 1200px)',
    Breakpoint.XXL: '(min-width: 1600px)'
}


class BreakpointManager:
    """断点管理器"""
    
    @staticmethod
    def get_breakpoint_value(breakpoint: Breakpoint) -> int:
        """获取断点值"""
        return BREAKPOINT_VALUES.get(breakpoint, 0)
    
    @staticmethod
    def get_media_query(breakpoint: Breakpoint) -> str:
        """获取媒体查询"""
        return MEDIA_QUERIES.get(breakpoint, '')
    
    @staticmethod
    def is_mobile() -> bool:
        """是否为移动设备"""
        # 简化实现，实际应该检测屏幕宽度
        return False
    
    @staticmethod
    def is_tablet() -> bool:
        """是否为平板设备"""
        # 简化实现，实际应该检测屏幕宽度
        return False
    
    @staticmethod
    def is_desktop() -> bool:
        """是否为桌面设备"""
        # 简化实现，实际应该检测屏幕宽度
        return True


# 便利函数
def get_breakpoint_value(breakpoint: Breakpoint) -> int:
    """获取断点值"""
    return BreakpointManager.get_breakpoint_value(breakpoint)

def get_media_query(breakpoint: Breakpoint) -> str:
    """获取媒体查询"""
    return BreakpointManager.get_media_query(breakpoint)