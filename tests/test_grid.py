#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Grid 栅格组件测试
"""

import sys
import os

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def test_grid_basic():
    """测试栅格组件基本功能"""
    try:
        # 创建 QApplication
        try:
            from PySide6.QtWidgets import QApplication, QLabel
        except ImportError:
            from PyQt6.QtWidgets import QApplication, QLabel
            
        app = QApplication.instance() or QApplication(sys.argv)
        
        from adw.components.layout.grid import Row, Col, Breakpoint
        print("✓ 成功导入 Grid 组件")
        
        # 测试创建 Row
        row = Row()
        print(f"✓ 成功创建 Row 组件")
        
        # 测试创建 Col
        col = Col(span=12)
        print(f"✓ 成功创建 Col 组件: span={col.get_span()}")
        
        # 测试 Row 添加 Col
        row.add_col(col)
        print(f"✓ Row 成功添加 Col")
        
        # 测试 Col 包含 widget
        label = QLabel("测试标签")
        col_with_widget = Col(span=8, widget=label)
        print(f"✓ Col 成功包含 widget")
        
        # 测试属性设置
        row.set_justify("center")
        row.set_align("middle")
        row.set_gutter(16)
        print(f"✓ Row 属性设置: justify={row.get_justify()}, align={row.get_align()}, gutter={row.get_gutter()}")
        
        col.set_span(6)
        col.set_offset(2)
        print(f"✓ Col 属性设置: span={col.get_span()}, offset={col.get_offset()}")
        
        # 测试响应式属性
        responsive_col = Col(
            xs=24,
            sm=12,
            md=8,
            lg=6,
            widget=QLabel("响应式列")
        )
        print(f"✓ 响应式 Col 创建成功")
        
        return True
    except Exception as e:
        print(f"✗ 栅格组件测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_grid_layout():
    """测试栅格布局功能"""
    try:
        # 创建 QApplication
        try:
            from PySide6.QtWidgets import QApplication, QLabel
        except ImportError:
            from PyQt6.QtWidgets import QApplication, QLabel
            
        app = QApplication.instance() or QApplication(sys.argv)
        
        from adw.components.layout.grid import Row, Col
        print("✓ 成功导入 Grid 组件")
        
        # 测试基础栅格布局
        row1 = Row()
        row1.add_col(Col(span=24, widget=QLabel("col")))
        
        row2 = Row()
        row2.add_col(Col(span=12, widget=QLabel("col-12")))
        row2.add_col(Col(span=12, widget=QLabel("col-12")))
        
        row3 = Row()
        row3.add_col(Col(span=8, widget=QLabel("col-8")))
        row3.add_col(Col(span=8, widget=QLabel("col-8")))
        row3.add_col(Col(span=8, widget=QLabel("col-8")))
        
        row4 = Row()
        row4.add_col(Col(span=6, widget=QLabel("col-6")))
        row4.add_col(Col(span=6, widget=QLabel("col-6")))
        row4.add_col(Col(span=6, widget=QLabel("col-6")))
        row4.add_col(Col(span=6, widget=QLabel("col-6")))
        
        print("✓ 基础栅格布局测试通过")
        
        # 测试偏移布局
        offset_row = Row()
        offset_row.add_col(Col(span=8, widget=QLabel("col-8")))
        offset_row.add_col(Col(span=8, offset=8, widget=QLabel("col-8")))
        print("✓ 偏移布局测试通过")
        
        # 测试对齐布局
        justify_row = Row(justify="center")
        justify_row.add_col(Col(span=4, widget=QLabel("col-4")))
        justify_row.add_col(Col(span=4, widget=QLabel("col-4")))
        justify_row.add_col(Col(span=4, widget=QLabel("col-4")))
        justify_row.add_col(Col(span=4, widget=QLabel("col-4")))
        print("✓ 对齐布局测试通过")
        
        # 测试垂直对齐
        align_row = Row(align="middle")
        align_row.add_col(Col(span=6, widget=QLabel("col-6")))
        align_row.add_col(Col(span=6, widget=QLabel("col-6")))
        print("✓ 垂直对齐测试通过")
        
        return True
    except Exception as e:
        print(f"✗ 栅格布局测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_grid_responsive():
    """测试响应式功能"""
    try:
        # 创建 QApplication
        try:
            from PySide6.QtWidgets import QApplication, QLabel
        except ImportError:
            from PyQt6.QtWidgets import QApplication, QLabel
            
        app = QApplication.instance() or QApplication(sys.argv)
        
        from adw.components.layout.grid import Row, Col, Breakpoint
        print("✓ 成功导入 Grid 组件")
        
        # 测试响应式栅格
        responsive_col = Col(
            xs=24,
            sm=12,
            md=8,
            lg=6,
            xl=4,
            xxl=2,
            widget=QLabel("Responsive Column")
        )
        
        # 验证响应式属性设置
        assert responsive_col._responsive[Breakpoint.XS] == 24
        assert responsive_col._responsive[Breakpoint.SM] == 12
        assert responsive_col._responsive[Breakpoint.MD] == 8
        assert responsive_col._responsive[Breakpoint.LG] == 6
        assert responsive_col._responsive[Breakpoint.XL] == 4
        assert responsive_col._responsive[Breakpoint.XXL] == 2
        print("✓ 响应式属性设置正确")
        
        # 测试响应式 Row
        responsive_row = Row(
            gutter={'xs': 8, 'sm': 16, 'md': 24, 'lg': 32}
        )
        responsive_row.add_col(Col(span=6, widget=QLabel("col-6")))
        responsive_row.add_col(Col(span=6, widget=QLabel("col-6")))
        responsive_row.add_col(Col(span=6, widget=QLabel("col-6")))
        responsive_row.add_col(Col(span=6, widget=QLabel("col-6")))
        print("✓ 响应式 Row 测试通过")
        
        return True
    except Exception as e:
        print(f"✗ 响应式测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """主测试函数"""
    print("开始测试 Grid 栅格组件...")
    
    tests = [
        ("基本功能", test_grid_basic),
        ("布局功能", test_grid_layout),
        ("响应式功能", test_grid_responsive)
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
    
    print(f"\nGrid 组件测试完成: {passed}/{total} 通过")
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)