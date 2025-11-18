#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Button 组件测试
"""

import sys
import os

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_button_basic():
    """测试按钮基本功能"""
    try:
        # 创建 QApplication
        try:
            from PySide6.QtWidgets import QApplication
        except ImportError:
            from PyQt6.QtWidgets import QApplication
            
        app = QApplication.instance() or QApplication(sys.argv)
        
        from adw.components.widgets.button import Button
        print("✓ 成功导入 Button 组件")
        
        # 测试创建按钮
        button = Button("测试按钮")
        print(f"✓ 成功创建按钮: {button.text()}")
        
        # 测试按钮类型
        primary_button = Button("主要按钮", type="primary")
        print(f"✓ 主要按钮类型: {primary_button.get_type()}")
        
        # 测试按钮尺寸
        large_button = Button("大按钮", size="large")
        print(f"✓ 大按钮尺寸: {large_button.get_size()}")
        
        # 测试危险按钮
        danger_button = Button("危险按钮", danger=True)
        print(f"✓ 危险按钮状态: {danger_button.get_danger()}")
        
        # 测试中文文本间距
        chinese_button = Button("确定")
        print(f"✓ 中文文本间距处理: '{chinese_button.text()}'")
        
        # 测试 setter 方法
        button.set_type("primary")
        button.set_size("small")
        button.set_danger(True)
        print(f"✓ Setter 方法测试通过: type={button.get_type()}, size={button.get_size()}, danger={button.get_danger()}")
        
        print("所有基本测试通过！")
        return True
        
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_button_basic()
    sys.exit(0 if success else 1)
