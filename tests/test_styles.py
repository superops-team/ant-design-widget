#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
样式系统测试
"""

import sys
import os

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def test_colors():
    """测试色彩系统"""
    try:
        from adw.styles.colors import ColorPalette, ThemeType, set_theme, get_primary_color
        print("✓ 成功导入色彩系统")
        
        # 测试获取主色
        primary_color = get_primary_color()
        print(f"✓ 默认主色: {primary_color}")
        
        # 测试获取不同色阶的颜色
        blue_1 = ColorPalette.get_color('blue', 1)
        blue_10 = ColorPalette.get_color('blue', 10)
        print(f"✓ 蓝色色阶1: {blue_1}")
        print(f"✓ 蓝色色阶10: {blue_10}")
        
        # 测试功能色
        success_color = ColorPalette.get_success_color()
        warning_color = ColorPalette.get_warning_color()
        error_color = ColorPalette.get_error_color()
        print(f"✓ 成功色: {success_color}")
        print(f"✓ 警告色: {warning_color}")
        print(f"✓ 错误色: {error_color}")
        
        # 测试主题切换
        set_theme(ThemeType.DARK)
        dark_text_color = ColorPalette.get_text_color()
        print(f"✓ 暗色主题文本色: {dark_text_color}")
        
        set_theme(ThemeType.LIGHT)
        light_text_color = ColorPalette.get_text_color()
        print(f"✓ 亮色主题文本色: {light_text_color}")
        
        return True
    except Exception as e:
        print(f"✗ 色彩系统测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_typography():
    """测试排版系统"""
    try:
        from adw.styles.typography import Typography, TypographyScale
        print("✓ 成功导入排版系统")
        
        # 测试获取字体设置
        heading_font = Typography.get_heading_1_font()
        body_font = Typography.get_body_font()
        secondary_font = Typography.get_secondary_font()
        print(f"✓ 超大标题字体: {heading_font.size}px, weight {heading_font.weight}")
        print(f"✓ 正文字体: {body_font.size}px, weight {body_font.weight}")
        print(f"✓ 辅助文字字体: {secondary_font.size}px, weight {secondary_font.weight}")
        
        return True
    except Exception as e:
        print(f"✗ 排版系统测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_spacing():
    """测试间距系统"""
    try:
        from adw.styles.spacing import Spacing, SpacingScale
        print("✓ 成功导入间距系统")
        
        # 测试获取间距值
        xs_spacing = Spacing.get_xs()
        sm_spacing = Spacing.get_sm()
        md_spacing = Spacing.get_md()
        lg_spacing = Spacing.get_lg()
        print(f"✓ 微小间距: {xs_spacing}px")
        print(f"✓ 小间距: {sm_spacing}px")
        print(f"✓ 中等间距: {md_spacing}px")
        print(f"✓ 大间距: {lg_spacing}px")
        
        # 测试通过枚举获取间距
        xl_spacing = Spacing.get_spacing(SpacingScale.XL)
        print(f"✓ 超大间距: {xl_spacing}px")
        
        # 测试通过倍数获取间距
        custom_spacing = Spacing.get_spacing(5)  # 5 * 8 = 40px
        print(f"✓ 自定义间距(5倍): {custom_spacing}px")
        
        return True
    except Exception as e:
        print(f"✗ 间距系统测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_theme():
    """测试主题管理器"""
    try:
        from adw.styles.theme import ThemeManager, ThemeType, ThemeSettings
        print("✓ 成功导入主题管理器")
        
        # 测试获取主题设置
        settings = ThemeManager.get_theme_settings()
        print(f"✓ 默认主题背景色: {settings.background_color}")
        print(f"✓ 默认主题文本色: {settings.text_color}")
        
        # 测试主题切换
        ThemeManager.set_theme(ThemeType.DARK)
        dark_settings = ThemeManager.get_theme_settings()
        print(f"✓ 暗色主题背景色: {dark_settings.background_color}")
        
        # 测试自定义设置
        ThemeManager.set_custom_setting('primary_color', '#ff0000')
        custom_settings = ThemeManager.get_theme_settings()
        print(f"✓ 自定义主色: {custom_settings.primary_color}")
        
        return True
    except Exception as e:
        print(f"✗ 主题管理器测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """主测试函数"""
    print("开始测试样式系统...")
    
    tests = [
        ("色彩系统", test_colors),
        ("排版系统", test_typography),
        ("间距系统", test_spacing),
        ("主题管理器", test_theme)
    ]
    
    passed = 0
    total = len(tests)
    
    for name, test_func in tests:
        print(f"\n测试 {name}:")
        if test_func():
            passed += 1
            print(f"✓ {name} 测试通过")
        else:
            print(f"✗ {name} 测试失败")
    
    print(f"\n测试完成: {passed}/{total} 通过")
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)