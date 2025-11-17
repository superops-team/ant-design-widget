#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Button 组件测试
"""

import sys
import os

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from adw.components.widgets.button import Button
    QT_AVAILABLE = True
except ImportError as e:
    QT_AVAILABLE = False
    print(f"Qt libraries not available: {e}")

class TestButton:
    """Button 组件测试类"""
    
    def test_button_creation(self):
        """测试按钮创建"""
        if not QT_AVAILABLE:
            print("Qt libraries not available, skipping test")
            return
        button = Button("Test Button")
        assert button is not None
        assert button.text() == "Test Button"
        print("✓ test_button_creation passed")
        
    def test_button_type(self):
        """测试按钮类型"""
        if not QT_AVAILABLE:
            print("Qt libraries not available, skipping test")
            return
            
        # 测试默认类型
        button = Button("Test Button")
        assert button.get_type() == "default"
        
        # 测试主按钮类型
        primary_button = Button("Primary Button", type="primary")
        assert primary_button.get_type() == "primary"
        
        # 测试虚线按钮类型
        dashed_button = Button("Dashed Button", type="dashed")
        assert dashed_button.get_type() == "dashed"
        
        # 测试文字按钮类型
        text_button = Button("Text Button", type="text")
        assert text_button.get_type() == "text"
        
        # 测试链接按钮类型
        link_button = Button("Link Button", type="link")
        assert link_button.get_type() == "link"
        print("✓ test_button_type passed")
        
    def test_button_size(self):
        """测试按钮尺寸"""
        if not QT_AVAILABLE:
            print("Qt libraries not available, skipping test")
            return
            
        # 测试默认尺寸
        button = Button("Test Button")
        assert button.get_size() == "middle"
        
        # 测试大尺寸
        large_button = Button("Large Button", size="large")
        assert large_button.get_size() == "large"
        
        # 测试小尺寸
        small_button = Button("Small Button", size="small")
        assert small_button.get_size() == "small"
        print("✓ test_button_size passed")
        
    def test_button_danger(self):
        """测试危险按钮"""
        if not QT_AVAILABLE:
            print("Qt libraries not available, skipping test")
            return
            
        # 测试非危险按钮
        button = Button("Test Button")
        assert button.get_danger() == False
        
        # 测试危险按钮
        danger_button = Button("Danger Button", danger=True)
        assert danger_button.get_danger() == True
        print("✓ test_button_danger passed")
        
    def test_button_disabled(self):
        """测试禁用按钮"""
        if not QT_AVAILABLE:
            print("Qt libraries not available, skipping test")
            return
            
        # 测试启用按钮
        button = Button("Test Button")
        assert button.get_disabled() == False
        
        # 测试禁用按钮
        disabled_button = Button("Disabled Button", disabled=True)
        assert disabled_button.get_disabled() == True
        print("✓ test_button_disabled passed")
        
    def test_button_loading(self):
        """测试加载中按钮"""
        if not QT_AVAILABLE:
            print("Qt libraries not available, skipping test")
            return
            
        # 测试非加载中按钮
        button = Button("Test Button")
        assert button.get_loading() == False
        
        # 测试加载中按钮
        loading_button = Button("Loading Button", loading=True)
        assert loading_button.get_loading() == True
        print("✓ test_button_loading passed")
        
    def test_button_ghost(self):
        """测试幽灵按钮"""
        if not QT_AVAILABLE:
            print("Qt libraries not available, skipping test")
            return
            
        # 测试非幽灵按钮
        button = Button("Test Button")
        assert button.get_ghost() == False
        
        # 测试幽灵按钮
        ghost_button = Button("Ghost Button", ghost=True)
        assert ghost_button.get_ghost() == True
        print("✓ test_button_ghost passed")
        
    def test_button_block(self):
        """测试块级按钮"""
        if not QT_AVAILABLE:
            print("Qt libraries not available, skipping test")
            return
            
        # 测试非块级按钮
        button = Button("Test Button")
        assert button.get_block() == False
        
        # 测试块级按钮
        block_button = Button("Block Button", block=True)
        assert block_button.get_block() == True
        print("✓ test_button_block passed")
        
    def test_button_shape(self):
        """测试按钮形状"""
        if not QT_AVAILABLE:
            print("Qt libraries not available, skipping test")
            return
            
        # 测试默认形状
        button = Button("Test Button")
        assert button.get_shape() is None
        
        # 测试圆形按钮
        circle_button = Button("Circle", shape="circle")
        assert circle_button.get_shape() == "circle"
        
        # 测试圆角按钮
        round_button = Button("Round", shape="round")
        assert round_button.get_shape() == "round"
        print("✓ test_button_shape passed")
        
    def test_chinese_text_spacing(self):
        """测试中文文本间距处理"""
        if not QT_AVAILABLE:
            print("Qt libraries not available, skipping test")
            return
            
        # 测试两个中文字符的按钮（非text/link类型）
        button = Button("确定")
        # 应该自动添加空格
        assert button.text() == "确 定"
        
        # 测试text类型按钮不添加空格
        text_button = Button("确定", type="text")
        assert text_button.text() == "确定"
        
        # 测试link类型按钮不添加空格
        link_button = Button("确定", type="link")
        assert link_button.text() == "确定"
        print("✓ test_chinese_text_spacing passed")
        
    def test_setters(self):
        """测试setter方法"""
        if not QT_AVAILABLE:
            print("Qt libraries not available, skipping test")
            return
            
        button = Button("Test Button")
        
        # 测试设置类型
        button.set_type("primary")
        assert button.get_type() == "primary"
        
        # 测试设置尺寸
        button.set_size("large")
        assert button.get_size() == "large"
        
        # 测试设置危险状态
        button.set_danger(True)
        assert button.get_danger() == True
        
        # 测试设置禁用状态
        button.set_disabled(True)
        assert button.get_disabled() == True
        
        # 测试设置加载中状态
        button.set_loading(True)
        assert button.get_loading() == True
        
        # 测试设置幽灵状态
        button.set_ghost(True)
        assert button.get_ghost() == True
        
        # 测试设置块级状态
        button.set_block(True)
        assert button.get_block() == True
        
        # 测试设置形状
        button.set_shape("circle")
        assert button.get_shape() == "circle"
        
        # 测试设置文本
        button.set_text("New Text")
        assert button.text() == "New Text"
        print("✓ test_setters passed")

def run_tests():
    """运行所有测试"""
    if not QT_AVAILABLE:
        print("Qt libraries not available, cannot run tests")
        return
        
    test_instance = TestButton()
    
    # 运行所有测试方法
    test_methods = [method for method in dir(test_instance) if method.startswith('test_')]
    
    for method_name in test_methods:
        method = getattr(test_instance, method_name)
        try:
            method()
        except Exception as e:
            print(f"✗ {method_name} failed: {e}")
            return
            
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()