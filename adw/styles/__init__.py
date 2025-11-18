#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ant Design 样式系统
"""

from .colors import (
    ColorPalette,
    ThemeType,
    set_theme,
    get_theme,
    get_primary_color,
    get_success_color,
    get_warning_color,
    get_error_color,
    get_info_color
)

from .typography import (
    Typography,
    TypographyScale,
    FontFamily,
    FontSettings,
    get_heading_1_font,
    get_heading_2_font,
    get_heading_3_font,
    get_heading_4_font,
    get_body_font,
    get_secondary_font
)

from .spacing import (
    Spacing,
    SpacingScale,
    get_spacing,
    get_xs,
    get_sm,
    get_md,
    get_lg,
    get_xl,
    get_xxl
)

from .breakpoints import (
    Breakpoint,
    BreakpointManager,
    get_breakpoint_value,
    get_media_query
)

from .theme import (
    ThemeManager,
    ThemeSettings,
    set_theme as set_global_theme,
    get_theme as get_global_theme,
    get_theme_settings,
    apply_theme_to_widget
)

__all__ = [
    # Colors
    'ColorPalette',
    'ThemeType',
    'set_theme',
    'get_theme',
    'get_primary_color',
    'get_success_color',
    'get_warning_color',
    'get_error_color',
    'get_info_color',
    
    # Typography
    'Typography',
    'TypographyScale',
    'FontFamily',
    'FontSettings',
    'get_heading_1_font',
    'get_heading_2_font',
    'get_heading_3_font',
    'get_heading_4_font',
    'get_body_font',
    'get_secondary_font',
    
    # Spacing
    'Spacing',
    'SpacingScale',
    'get_spacing',
    'get_xs',
    'get_sm',
    'get_md',
    'get_lg',
    'get_xl',
    'get_xxl',
    
    # Breakpoints
    'Breakpoint',
    'BreakpointManager',
    'get_breakpoint_value',
    'get_media_query',
    
    # Theme
    'ThemeManager',
    'ThemeSettings',
    'set_global_theme',
    'get_global_theme',
    'get_theme_settings',
    'apply_theme_to_widget'
]