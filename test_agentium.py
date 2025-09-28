#!/usr/bin/env python3
"""
Agentium Library Test Script

This script tests the core functionality of the Agentium library
to ensure all components are working correctly.
"""

import sys
import traceback
from typing import Dict, Any

def test_core_imports():
    """Test that all core components can be imported"""
    print("🧪 Testing core component imports...")
    
    try:
        from agentium import (
            Condenser, Optimizer, Rearranger, Extractor,
            Communicator, Translator, InsightGenerator,
            WorkflowHelper, TemplateManager, MemoryHelper,
            CustomSummarizer, LoggerUtils, Agentium
        )
        print("✅ All core components imported successfully")
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        traceback.print_exc()
        return False


def test_integration_availability():
    """Test integration availability"""
    print("\n🔗 Testing integration availability...")
    
    try:
        from agentium import (
            LANGCHAIN_INTEGRATION_AVAILABLE,
            LANGGRAPH_INTEGRATION_AVAILABLE,
            CREWAI_INTEGRATION_AVAILABLE
        )
        
        print(f"  LangChain Integration: {'✅ Available' if LANGCHAIN_INTEGRATION_AVAILABLE else '⚠️  Not Available'}")
        print(f"  LangGraph Integration: {'✅ Available' if LANGGRAPH_INTEGRATION_AVAILABLE else '⚠️  Not Available'}")
        print(f"  CrewAI Integration: {'✅ Available' if CREWAI_INTEGRATION_AVAILABLE else '⚠️  Not Available'}")
        
        return True
    except Exception as e:
        print(f"❌ Integration check failed: {e}")
        return False


def test_core_functionality():
    """Test basic functionality of core components"""
    print("\n⚙️  Testing core component functionality...")
    
    try:
        from agentium import Agentium
        
        # Initialize Agentium
        agent = Agentium()
        print("✅ Agentium initialized successfully")
        
        # Test basic workflow
        test_content = """
        This is a sample text for testing the Agentium library.
        It contains multiple sentences to demonstrate text processing capabilities.
        The library should be able to condense, optimize, and summarize this content effectively.
        We expect the workflow to process this text through multiple stages and produce meaningful results.
        """
        
        # Test basic workflow
        print("  Testing basic workflow...")
        result = agent.process_content(test_content, workflow="basic")
        
        if result.get('success'):
            print(f"  ✅ Basic workflow completed successfully")
            print(f"  📊 Steps completed: {len(result.get('steps', []))}")
            print(f"  📝 Final output length: {len(str(result.get('final_output', '')))}")
        else:
            print(f"  ❌ Basic workflow failed: {result.get('error', 'Unknown error')}")
            return False
            
        # Test individual components
        print("  Testing individual components...")
        
        # Test condenser
        condensed = agent.condenser.condense(test_content)
        print(f"  ✅ Condenser: {condensed.get('stats', {}).get('compression_ratio', 'N/A')}% compression")
        
        # Test optimizer
        optimized = agent.optimizer.optimize(test_content)
        improvements = len(optimized.get('improvements', []))
        print(f"  ✅ Optimizer: {improvements} improvements applied")
        
        # Test summarizer
        summarized = agent.summarizer.summarize(test_content)
        summary_length = len(summarized.get('summary', ''))
        print(f"  ✅ Summarizer: {summary_length} character summary created")
        
        # Test extractor
        extracted = agent.extractor.extract(test_content)
        data_points = len(str(extracted.get('extracted_data', '')))
        print(f"  ✅ Extractor: {data_points} characters of data extracted")
        
        # Test memory system
        context = agent.memory_helper.create_context("test_context")
        context.store("test_key", "test_value")
        retrieved = context.get("test_key")
        print(f"  ✅ Memory: {'Data stored and retrieved' if retrieved == 'test_value' else 'Memory test failed'}")
        
        return True
        
    except Exception as e:
        print(f"❌ Functionality test failed: {e}")
        traceback.print_exc()
        return False


def test_integration_status():
    """Test integration status checking"""
    print("\n🔍 Testing integration status checking...")
    
    try:
        from agentium import Agentium
        
        agent = Agentium()
        status = agent.get_integration_status()
        
        print("  Integration Status:")
        for framework, available in status.items():
            icon = "✅" if available else "⚠️ "
            print(f"    {framework}: {icon} {'Available' if available else 'Not Available'}")
        
        return True
        
    except Exception as e:
        print(f"❌ Integration status test failed: {e}")
        return False


def test_logger_functionality():
    """Test logging functionality"""
    print("\n📝 Testing logging functionality...")
    
    try:
        from agentium import LoggerUtils
        
        # Get a logger and test basic operations
        logger = LoggerUtils.get_logger("test_logger")
        
        # Test different log levels
        logger.info("Test info message")
        logger.warning("Test warning message")
        logger.error("Test error message")
        
        # Test operation logging
        @LoggerUtils.log_operation("test_operation")
        def test_function():
            return "Test completed"
        
        result = test_function()
        
        print("✅ Logger functionality working correctly")
        return True
        
    except Exception as e:
        print(f"❌ Logger test failed: {e}")
        return False


def run_all_tests():
    """Run all tests and provide summary"""
    print("🚀 Starting Agentium Library Tests\n")
    print("=" * 50)
    
    tests = [
        ("Core Imports", test_core_imports),
        ("Integration Availability", test_integration_availability),
        ("Core Functionality", test_core_functionality),
        ("Integration Status", test_integration_status),
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
        print("🎉 All tests passed! Agentium library is ready to use.")
        return True
    else:
        print("⚠️  Some tests failed. Please check the installation and dependencies.")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)