#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Breakpoints 断点系统测试
"""

import sys
import os

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def test_breakpoints():
    """测试断点系统"""
    try:
        from adw.styles.breakpoints import Breakpoint, BreakpointManager, get_breakpoint_value, get_media_query
        print("✓ 成功导入断点系统")
        
        # 测试断点值
        xs_value = get_breakpoint_value(Breakpoint.XS)
        sm_value = get_breakpoint_value(Breakpoint.SM)
        md_value = get_breakpoint_value(Breakpoint.MD)
        lg_value = get_breakpoint_value(Breakpoint.LG)
        xl_value = get_breakpoint_value(Breakpoint.XL)
        xxl_value = get_breakpoint_value(Breakpoint.XXL)
        
        assert xs_value == 575
        assert sm_value == 576
        assert md_value == 768
        assert lg_value == 992
        assert xl_value == 1200
        assert xxl_value == 1600
        print("✓ 断点值测试通过")
        
        # 测试媒体查询
        xs_query = get_media_query(Breakpoint.XS)
        sm_query = get_media_query(Breakpoint.SM)
        md_query = get_media_query(Breakpoint.MD)
        lg_query = get_media_query(Breakpoint.LG)
        xl_query = get_media_query(Breakpoint.XL)
        xxl_query = get_media_query(Breakpoint.XXL)
        
        assert xs_query == '(max-width: 575px)'
        assert sm_query == '(min-width: 576px)'
        assert md_query == '(min-width: 768px)'
        assert lg_query == '(min-width: 992px)'
        assert xl_query == '(min-width: 1200px)'
        assert xxl_query == '(min-width: 1600px)'
        print("✓ 媒体查询测试通过")
        
        # 测试断点管理器
        xs_value_from_manager = BreakpointManager.get_breakpoint_value(Breakpoint.XS)
        sm_query_from_manager = BreakpointManager.get_media_query(Breakpoint.SM)
        
        assert xs_value_from_manager == 575
        assert sm_query_from_manager == '(min-width: 576px)'
        print("✓ 断点管理器测试通过")
        
        return True
    except Exception as e:
        print(f"✗ 断点系统测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """主测试函数"""
    print("开始测试断点系统...")
    
    tests = [
        ("断点系统", test_breakpoints)
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
    
    print(f"\n断点系统测试完成: {passed}/{total} 通过")
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)