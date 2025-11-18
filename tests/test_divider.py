#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Divider 组件测试
"""

import sys
import os

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_divider_basic():
    """测试分割线基本功能"""
    try:
        # 创建 QApplication
        try:
            from PySide6.QtWidgets import QApplication
        except ImportError:
            from PyQt6.QtWidgets import QApplication
            
        app = QApplication.instance() or QApplication(sys.argv)
        
        from adw.components.widgets.divider import Divider
        print("✓ 成功导入 Divider 组件")
        
        # 测试创建水平分割线
        divider = Divider()
        print(f"✓ 成功创建水平分割线: type={divider.get_type()}")
        
        # 测试创建带文本的水平分割线
        divider_with_text = Divider(text="文本")
        print(f"✓ 成功创建带文本的水平分割线: text='{divider_with_text.get_text()}'")
        
        # 测试创建垂直分割线
        vertical_divider = Divider(type="vertical")
        print(f"✓ 成功创建垂直分割线: type={vertical_divider.get_type()}")
        
        # 测试虚线分割线
        dashed_divider = Divider(dashed=True)
        print(f"✓ 成功创建虚线分割线: dashed={dashed_divider.get_dashed()}")
        
        # 测试文本位置
        left_divider = Divider(text="左对齐", orientation="left")
        print(f"✓ 成功创建左对齐文本分割线: orientation={left_divider.get_orientation()}")
        
        # 测试 setter 方法
        divider.set_text("新文本")
        divider.set_type("vertical")
        divider.set_dashed(True)
        print(f"✓ Setter 方法测试通过: text='{divider.get_text()}', type={divider.get_type()}, dashed={divider.get_dashed()}")
        
        print("所有基本测试通过！")
        return True
        
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("开始测试 Divider 组件...")
    success = test_divider_basic()
    if success:
        print("✓ 测试成功完成")
    else:
        print("✗ 测试失败")
    sys.exit(0 if success else 1)