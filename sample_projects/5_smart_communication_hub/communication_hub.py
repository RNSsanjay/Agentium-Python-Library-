#!/usr/bin/env python3
"""
Smart Communication Hub - Sample Project 5

Advanced communication system demonstrating workflow orchestration,
multi-channel messaging, and AI-enhanced content processing.
"""

import os
import sys
from pathlib import Path
from typing import Dict, Any, List
import json
from datetime import datetime

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

try:
    from agentium import (
        Agentium, 
        GeminiIntegration, 
        GeminiConfig, 
        GeminiModel,
        LoggerUtils
    )
except ImportError:
    print("Agentium not found. Install with: pip install agentium")
    sys.exit(1)


class SmartCommunicationHub:
    """Smart communication system with AI enhancement"""
    
    def __init__(self, gemini_model: str = "gemini-pro"):
        self.agentium = Agentium()
        gemini_config = GeminiConfig(model=GeminiModel(gemini_model), temperature=0.6)
        self.gemini = GeminiIntegration(gemini_config)
        self.logger = LoggerUtils.get_logger(__name__)
        self.memory = self.agentium.memory_helper.create_context("communication_hub")
        
        print(f"Smart Communication Hub initialized")
        print(f"Gemini integration: {'Available' if self.gemini.is_available() else 'Not available'}")
    
    def process_and_distribute_message(self, message_content: str, channels: List[str]) -> Dict[str, Any]:
        """Process message and distribute to multiple channels"""
        print(f"\n Processing message for {len(channels)} channels...")
        
        # Step 1: Optimize message content
        print("  Optimizing message...")
        if self.gemini.is_available():
            optimized = self.gemini.enhance_optimizer(message_content, optimization_type='professional')
            optimized_content = optimized.get('text', message_content)
        else:
            optimized = self.agentium.optimizer.optimize(message_content)
            optimized_content = optimized.get('text', message_content)
        
        # Step 2: Create different versions for different channels
        print("  Creating channel-specific versions...")
        channel_messages = {}
        
        for channel in channels:
            if channel == 'email':
                # Formal version for email
                if self.gemini.is_available():
                    email_version = self.gemini.enhance_optimizer(optimized_content, optimization_type='professional')
                    channel_messages[channel] = email_version.get('text', optimized_content)
                else:
                    channel_messages[channel] = optimized_content
            
            elif channel == 'slack':
                # Condensed version for Slack
                if self.gemini.is_available():
                    slack_version = self.gemini.enhance_condenser(optimized_content, target_length=500)
                    channel_messages[channel] = slack_version.get('text', optimized_content)
                else:
                    condensed = self.agentium.condenser.condense(optimized_content, compression_ratio=0.5)
                    channel_messages[channel] = condensed.get('text', optimized_content)
            
            else:  # console, file, etc.
                channel_messages[channel] = optimized_content
        
        # Step 3: Extract key information for tracking
        print("  Extracting key information...")
        extracted = self.agentium.extractor.extract(message_content, extraction_type='emails')
        
        # Step 4: Send to channels
        print("   Distributing messages...")
        distribution_results = {}
        
        for channel, content in channel_messages.items():
            try:
                result = self.agentium.communicator.send_notification(
                    message=content,
                    channel=channel,
                    title="Smart Hub Notification"
                )
                distribution_results[channel] = {'success': True, 'result': result}
                print(f"    Sent to {channel}")
            except Exception as e:
                distribution_results[channel] = {'success': False, 'error': str(e)}
                print(f"    Failed to send to {channel}: {e}")
        
        # Step 5: Store communication history
        communication_record = {
            'original_message': message_content,
            'optimized_message': optimized_content,
            'channel_messages': channel_messages,
            'distribution_results': distribution_results,
            'extracted_data': extracted.get('extracted_data', []),
            'timestamp': datetime.now().isoformat(),
            'channels_targeted': channels,
            'success_count': sum(1 for r in distribution_results.values() if r['success'])
        }
        
        self.memory.store(f"communication_{datetime.now().strftime('%H%M%S')}", communication_record)
        
        return communication_record
    
    def create_workflow_notification(self, workflow_name: str, status: str, details: Dict[str, Any]) -> str:
        """Create workflow status notification"""
        print(f"   Creating {workflow_name} notification...")
        
        # Generate insights about the workflow
        if self.gemini.is_available():
            insights_prompt = f"""
            Create a professional status update for workflow: {workflow_name}
            Status: {status}
            Details: {json.dumps(details, indent=2)}
            
            Make it informative and actionable.
            """
            
            result = self.gemini.generate_text(insights_prompt)
            if result['success']:
                return result['text']
        
        # Fallback template
        return f"""
        Workflow Update: {workflow_name}
        Status: {status}
        
        Details:
        {json.dumps(details, indent=2)}
        
        Timestamp: {datetime.now().isoformat()}
        """
    
    def demonstrate_full_workflow(self):
        """Demonstrate complete communication workflow"""
        print("\n Demonstrating complete communication workflow...")
        
        # Simulate a business process completion
        workflow_details = {
            'process': 'Monthly Report Generation',
            'completion_time': '45 minutes',
            'reports_generated': 12,
            'data_sources': 4,
            'insights_created': 23,
            'recipients_notified': 15
        }
        
        # Create workflow notification
        notification_content = self.create_workflow_notification(
            "Monthly Business Analytics",
            "Completed Successfully",
            workflow_details
        )
        
        # Process and distribute
        channels = ['console', 'file']  # Add more channels as configured
        
        result = self.process_and_distribute_message(notification_content, channels)
        
        return result


def main():
    """Main demonstration"""
    print("Agentium Smart Communication Hub Demo")
    print("=" * 50)
    
    hub = SmartCommunicationHub()
    
    # Sample message for distribution
    sample_message = """
    Important Update: System Maintenance Completed
    
    We have successfully completed the scheduled system maintenance that began at 2:00 AM EST. 
    All services are now fully operational and performing optimally. During the maintenance window, 
    we implemented several critical security updates, performance optimizations, and new feature 
    enhancements that will improve your user experience.
    
    Key improvements include:
    - Enhanced security protocols
    - 25% faster response times
    - New dashboard features
    - Improved mobile compatibility
    - Advanced reporting capabilities
    
    If you experience any issues or have questions, please contact our support team at 
    support@company.com or call +1-555-SUPPORT (555-787-7678). 
    
    Thank you for your patience during the maintenance window.
    """
    
    # Process and distribute message
    channels = ['console', 'file']  # Add email, slack if configured
    result = hub.process_and_distribute_message(sample_message, channels)
    
    # Demonstrate workflow integration
    workflow_result = hub.demonstrate_full_workflow()
    
    # Show memory contents
    print("\nCommunication history:")
    all_keys = hub.memory.list_keys()
    print(f"Stored {len(all_keys)} communication records")
    
    print(f"\nDistribution Summary:")
    print(f"  Successful: {result['success_count']}/{len(result['channels_targeted'])}")
    print(f"   Channels: {', '.join(result['channels_targeted'])}")
    
    print("\nSmart Communication Hub demo completed!")


if __name__ == "__main__":
    # Check for API key and provide setup instructions
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("WARNING: No Gemini API key found!")
        print("To enable AI enhancement, please set your API key:")
        print("\nWindows Command Prompt:")
        print("  set GEMINI_API_KEY=your_api_key_here")
        print("\nWindows PowerShell:")
        print("  $env:GEMINI_API_KEY=\"your_api_key_here\"")
        print("\nLinux/Mac:")
        print("  export GEMINI_API_KEY=your_api_key_here")
        print("\nGet your API key at: https://makersuite.google.com/app/apikey")
        print("\nContinuing with standard processing...\n")
    
    main()