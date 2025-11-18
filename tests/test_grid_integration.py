#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Grid 组件集成测试
测试Grid组件与样式系统的集成
"""

import sys
import os

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def test_grid_with_styles():
    """测试Grid组件与样式系统的集成"""
    try:
        # 创建 QApplication
        try:
            from PySide6.QtWidgets import QApplication, QLabel
        except ImportError:
            from PyQt6.QtWidgets import QApplication, QLabel
            
        app = QApplication.instance() or QApplication(sys.argv)
        
        from adw.components.layout.grid import Row, Col
        from adw.styles.colors import ColorPalette, ThemeType
        from adw.styles.theme import ThemeManager
        
        print("✓ 成功导入Grid组件和样式系统")
        
        # 测试默认主题下的Grid
        row = Row()
        col = Col(span=12, widget=QLabel("测试"))
        row.add_col(col)
        
        # 检查样式是否正确应用
        row_style = row.styleSheet()
        col_style = col.styleSheet()
        assert "adw-row" in row_style or "background-color: transparent" in row_style
        assert "adw-col" in col_style or "background-color: transparent" in col_style
        print("✓ Grid在默认主题下正确应用样式")
        
        # 测试暗色主题下的Grid
        ThemeManager.set_theme(ThemeType.DARK)
        dark_row = Row()
        dark_col = Col(span=12, widget=QLabel("暗色测试"))
        dark_row.add_col(dark_col)
        
        # 检查暗色主题样式
        dark_row_style = dark_row.styleSheet()
        dark_col_style = dark_col.styleSheet()
        assert "adw-row" in dark_row_style
        assert "adw-col" in dark_col_style
        print("✓ Grid在暗色主题下正确应用样式")
        
        # 切换回亮色主题
        ThemeManager.set_theme(ThemeType.LIGHT)
        
        return True
    except Exception as e:
        print(f"✗ Grid样式集成测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_grid_responsive_behavior():
    """测试Grid响应式行为"""
    try:
        # 创建 QApplication
        try:
            from PySide6.QtWidgets import QApplication, QLabel
        except ImportError:
            from PyQt6.QtWidgets import QApplication, QLabel
            
        app = QApplication.instance() or QApplication(sys.argv)
        
        from adw.components.layout.grid import Row, Col, Breakpoint
        
        print("✓ 成功导入Grid组件")
        
        # 测试响应式属性
        responsive_col = Col(
            xs=24,
            sm=12,
            md=8,
            lg=6,
            widget=QLabel("Responsive")
        )
        
        # 验证响应式属性存储
        assert responsive_col._responsive[Breakpoint.XS] == 24
        assert responsive_col._responsive[Breakpoint.SM] == 12
        assert responsive_col._responsive[Breakpoint.MD] == 8
        assert responsive_col._responsive[Breakpoint.LG] == 6
        print("✓ 响应式属性正确存储")
        
        # 测试响应式 Row
        gutter_dict = {'xs': 8, 'sm': 16, 'md': 24, 'lg': 32}
        responsive_row = Row(
            gutter=gutter_dict,
            justify="center",
            align="middle"
        )
        
        # 验证属性
        assert responsive_row.get_gutter() == gutter_dict
        assert responsive_row.get_justify() == "center"
        assert responsive_row.get_align() == "middle"
        print("✓ 响应式Row属性正确")
        
        return True
    except Exception as e:
        print(f"✗ Grid响应式测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_grid_layout_features():
    """测试Grid布局特性"""
    try:
        # 创建 QApplication
        try:
            from PySide6.QtWidgets import QApplication, QLabel
        except ImportError:
            from PyQt6.QtWidgets import QApplication, QLabel
            
        app = QApplication.instance() or QApplication(sys.argv)
        
        from adw.components.layout.grid import Row, Col
        
        print("✓ 成功导入Grid组件")
        
        # 测试各种布局特性
        # 1. 基础栅格
        row1 = Row()
        col1 = Col(span=12)
        row1.add_col(col1)
        assert col1.get_span() == 12
        print("✓ 基础栅格功能正常")
        
        # 2. 偏移功能
        col2 = Col(span=8, offset=8)
        assert col2.get_span() == 8
        assert col2.get_offset() == 8
        print("✓ 偏移功能正常")
        
        # 3. 对齐功能
        row2 = Row(justify="space-between", align="middle")
        assert row2.get_justify() == "space-between"
        assert row2.get_align() == "middle"
        print("✓ 对齐功能正常")
        
        # 4. 间隔功能
        row3 = Row(gutter=16)
        assert row3.get_gutter() == 16
        print("✓ 间隔功能正常")
        
        # 5. 包含widget功能
        label = QLabel("测试标签")
        col3 = Col(span=6, widget=label)
        assert col3.get_widget() == label
        print("✓ 包含widget功能正常")
        
        return True
    except Exception as e:
        print(f"✗ Grid布局特性测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """主测试函数"""
    print("开始Grid组件集成测试...")
    
    tests = [
        ("样式集成", test_grid_with_styles),
        ("响应式行为", test_grid_responsive_behavior),
        ("布局特性", test_grid_layout_features)
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
    
    print(f"\nGrid组件集成测试完成: {passed}/{total} 通过")
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)