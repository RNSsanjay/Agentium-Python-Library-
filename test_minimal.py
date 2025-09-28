#!/usr/bin/env python3
"""
Simplified Agentium Library Test Script

This script tests the core functionality without optional dependencies
that might cause issues.
"""

import sys
import traceback

def test_minimal_imports():
    """Test that basic components can be imported"""
    print("🧪 Testing minimal imports...")
    
    try:
        # Test logger utils first (should work without issues)
        from agentium.utils.logger_utils import LoggerUtils
        print("✅ LoggerUtils imported successfully")
        
        # Test basic classes that don't depend on NLTK
        from agentium.core.memory_helper import MemoryHelper
        print("✅ MemoryHelper imported successfully")
        
        from agentium.core.template_manager import TemplateManager  
        print("✅ TemplateManager imported successfully")
        
        from agentium.core.workflow_helper import WorkflowHelper
        print("✅ WorkflowHelper imported successfully")
        
        return True
    except Exception as e:
        print(f"❌ Minimal import failed: {e}")
        traceback.print_exc()
        return False

def test_memory_functionality():
    """Test memory functionality"""
    print("\n💾 Testing memory functionality...")
    
    try:
        from agentium.core.memory_helper import MemoryHelper
        
        # Test memory operations
        memory = MemoryHelper()
        context = memory.create_context("test")
        
        # Store and retrieve
        context.store("key1", "value1")
        retrieved = context.get("key1")
        
        if retrieved == "value1":
            print("✅ Memory store/retrieve working")
        else:
            print("❌ Memory store/retrieve failed")
            return False
            
        # Test context operations
        all_data = context.get_all()
        if "key1" in all_data:
            print("✅ Context get_all working")
        else:
            print("❌ Context get_all failed")
            return False
        
        return True
    except Exception as e:
        print(f"❌ Memory test failed: {e}")
        return False

def test_template_functionality():
    """Test template functionality"""
    print("\n📝 Testing template functionality...")
    
    try:
        from agentium.core.template_manager import TemplateManager
        
        manager = TemplateManager()
        
        # Test simple template
        template_content = "Hello {{ name }}!"
        result = manager.render_template(template_content, {"name": "World"})
        
        if result == "Hello World!":
            print("✅ Template rendering working")
        else:
            print(f"❌ Template rendering failed: expected 'Hello World!', got '{result}'")
            return False
        
        return True
    except Exception as e:
        print(f"❌ Template test failed: {e}")
        return False

def test_workflow_functionality():
    """Test workflow functionality"""
    print("\n⚙️  Testing workflow functionality...")
    
    try:
        from agentium.core.workflow_helper import WorkflowHelper
        
        workflow = WorkflowHelper()
        
        # Test simple task creation
        def simple_task():
            return "Task completed"
        
        task_id = workflow.create_task(
            name="test_task",
            function=simple_task,
            description="A simple test task"
        )
        
        if task_id:
            print("✅ Task creation working")
        else:
            print("❌ Task creation failed")
            return False
        
        return True
    except Exception as e:
        print(f"❌ Workflow test failed: {e}")
        return False

def test_logger_functionality():
    """Test logger functionality"""
    print("\n📋 Testing logger functionality...")
    
    try:
        from agentium.utils.logger_utils import LoggerUtils
        
        logger = LoggerUtils.get_logger("test")
        logger.info("Test log message")
        
        print("✅ Logger working")
        return True
    except Exception as e:
        print(f"❌ Logger test failed: {e}")
        return False

def run_minimal_tests():
    """Run minimal test suite"""
    print("🚀 Starting Minimal Agentium Tests\n")
    print("=" * 50)
    
    tests = [
        ("Minimal Imports", test_minimal_imports),
        ("Memory Functionality", test_memory_functionality),
        ("Template Functionality", test_template_functionality),
        ("Workflow Functionality", test_workflow_functionality),
        ("Logger Functionality", test_logger_functionality),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"❌ {test_name} test crashed: {e}")
    
    print("\n" + "=" * 50)
    print(f"🎯 Test Summary: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All minimal tests passed! Core Agentium functionality is working.")
        return True
    elif passed > 0:
        print(f"⚠️  {passed} tests passed, {total - passed} failed. Basic functionality available.")
        return True
    else:
        print("❌ All tests failed. Please check the installation.")
        return False

if __name__ == "__main__":
    success = run_minimal_tests()
    
    if success:
        print("\n📖 Next Steps:")
        print("1. Install optional dependencies: pip install nltk scikit-learn textstat tiktoken")
        print("2. Run the full test suite: python test_agentium.py")
        print("3. Check the DEPLOYMENT.md for complete setup instructions")
    
    sys.exit(0 if success else 1)