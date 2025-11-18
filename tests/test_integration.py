#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
组件集成测试
测试Button和Divider组件与样式系统的集成
"""

import sys
import os

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def test_button_with_styles():
    """测试Button组件与样式系统的集成"""
    try:
        # 创建 QApplication
        try:
            from PySide6.QtWidgets import QApplication
        except ImportError:
            from PyQt6.QtWidgets import QApplication
            
        app = QApplication.instance() or QApplication(sys.argv)
        
        from adw.components.widgets.button import Button
        from adw.styles.colors import ColorPalette, ThemeType
        from adw.styles.theme import ThemeManager
        
        print("✓ 成功导入Button组件和样式系统")
        
        # 测试默认主题下的Button
        button = Button("测试按钮")
        button_style = button.styleSheet()
        assert ColorPalette.get_primary_color() in button_style or ColorPalette.get_text_color() in button_style
        print("✓ Button在默认主题下正确应用样式")
        
        # 测试暗色主题下的Button
        ThemeManager.set_theme(ThemeType.DARK)
        dark_button = Button("暗色按钮")
        dark_style = dark_button.styleSheet()
        assert "rgba(255, 255, 255" in dark_style  # 暗色主题应该有白色系颜色
        print("✓ Button在暗色主题下正确应用样式")
        
        # 切换回亮色主题
        ThemeManager.set_theme(ThemeType.LIGHT)
        
        return True
    except Exception as e:
        print(f"✗ Button样式集成测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_divider_with_styles():
    """测试Divider组件与样式系统的集成"""
    try:
        # 创建 QApplication
        try:
            from PySide6.QtWidgets import QApplication
        except ImportError:
            from PyQt6.QtWidgets import QApplication
            
        app = QApplication.instance() or QApplication(sys.argv)
        
        from adw.components.widgets.divider import Divider
        from adw.styles.colors import ColorPalette, ThemeType
        from adw.styles.theme import ThemeManager
        
        print("✓ 成功导入Divider组件和样式系统")
        
        # 测试默认主题下的Divider
        divider = Divider()
        divider_style = divider.styleSheet()
        assert ColorPalette.get_border_color() in divider_style
        print("✓ Divider在默认主题下正确应用样式")
        
        # 测试暗色主题下的Divider
        ThemeManager.set_theme(ThemeType.DARK)
        dark_divider = Divider()
        dark_style = dark_divider.styleSheet()
        assert "424242" in dark_style or "303030" in dark_style  # 暗色主题的边框颜色
        print("✓ Divider在暗色主题下正确应用样式")
        
        # 切换回亮色主题
        ThemeManager.set_theme(ThemeType.LIGHT)
        
        return True
    except Exception as e:
        print(f"✗ Divider样式集成测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_theme_switching():
    """测试主题切换功能"""
    try:
        from adw.styles.colors import ColorPalette, ThemeType
        from adw.styles.theme import ThemeManager
        
        print("✓ 成功导入主题系统")
        
        # 测试默认主题
        assert ThemeManager.get_theme() == ThemeType.LIGHT
        assert "#ffffff" in ColorPalette.get_background_color()
        print("✓ 默认主题设置正确")
        
        # 切换到暗色主题
        ThemeManager.set_theme(ThemeType.DARK)
        assert ThemeManager.get_theme() == ThemeType.DARK
        assert "#141414" in ColorPalette.get_background_color()
        print("✓ 暗色主题切换正确")
        
        # 切换回亮色主题
        ThemeManager.set_theme(ThemeType.LIGHT)
        assert ThemeManager.get_theme() == ThemeType.LIGHT
        assert "#ffffff" in ColorPalette.get_background_color()
        print("✓ 主题切换功能正常")
        
        return True
    except Exception as e:
        print(f"✗ 主题切换测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """主测试函数"""
    print("开始集成测试...")
    
    tests = [
        ("Button样式集成", test_button_with_styles),
        ("Divider样式集成", test_divider_with_styles),
        ("主题切换功能", test_theme_switching)
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
    
    print(f"\n集成测试完成: {passed}/{total} 通过")
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)