#!/usr/bin/env python3
"""
Content Processing Pipeline - Sample Project 1

This project demonstrates a complete content processing pipeline using
all major Agentium features with Gemini AI enhancement.

Features demonstrated:
- Text condensation with AI
- Content optimization  
- Data extraction
- Insight generation
- Custom summarization
- Memory management
- Template processing
- Gemini API integration

Required API Keys:
- GEMINI_API_KEY: Your Google Gemini API key for AI enhancement
  Get your key at: https://makersuite.google.com/app/apikey

Setup Instructions:
1. Get your Gemini API key from Google AI Studio
2. Set environment variable: GEMINI_API_KEY=your_api_key_here
3. Install dependencies: pip install agentium google-generativeai
4. Run: python content_pipeline.py

Example using environment variable:
Windows: set GEMINI_API_KEY=your_api_key_here
Linux/Mac: export GEMINI_API_KEY=your_api_key_here
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
    print("ERROR: Agentium not found. Install with: pip install agentium")
    print("For AI features, also install: pip install google-generativeai")
    sys.exit(1)


class ContentProcessingPipeline:
    """
    Advanced content processing pipeline with AI enhancement
    """
    
    def __init__(self, gemini_model: str = "gemini-pro"):
        """Initialize the processing pipeline"""
        # Initialize Agentium
        self.agentium = Agentium()
        
        # Setup Gemini integration
        gemini_config = GeminiConfig(
            model=GeminiModel(gemini_model),
            temperature=0.7,
            max_output_tokens=2048
        )
        self.gemini = GeminiIntegration(gemini_config)
        
        # Setup logging
        self.logger = LoggerUtils.get_logger(__name__)
        
        # Create memory context for this session
        self.memory = self.agentium.memory_helper.create_context("content_pipeline")
        
        # Processing results storage
        self.results = {}
        
        print(f"Content Processing Pipeline initialized")
        print(f"Gemini integration: {'Available' if self.gemini.is_available() else 'Not available'}")
        
    def load_sample_content(self) -> str:
        """Load sample content for processing"""
        sample_content = """
        Artificial Intelligence and Machine Learning Revolution in Business
        
        The integration of artificial intelligence (AI) and machine learning (ML) technologies 
        into business operations has fundamentally transformed how organizations operate, compete, 
        and deliver value to customers. This technological revolution represents one of the most 
        significant paradigm shifts in modern business history.
        
        Key Areas of Impact:
        
        1. Customer Experience Enhancement
        AI-powered chatbots and virtual assistants have revolutionized customer service by providing 
        24/7 support, instant responses, and personalized interactions. Companies like Amazon, 
        Netflix, and Spotify use sophisticated recommendation algorithms to deliver personalized 
        experiences that increase customer satisfaction and engagement.
        
        2. Operational Efficiency
        Machine learning algorithms optimize supply chain management, predict equipment failures, 
        and automate routine processes. Manufacturing companies report 20-30% efficiency gains 
        through predictive maintenance and quality control systems.
        
        3. Data-Driven Decision Making
        Advanced analytics and AI models enable businesses to extract actionable insights from 
        vast amounts of data. Financial institutions use ML for fraud detection, risk assessment, 
        and algorithmic trading, processing millions of transactions in real-time.
        
        4. Marketing and Sales Optimization
        AI transforms marketing through targeted advertising, customer segmentation, and sales 
        forecasting. Companies can now predict customer behavior, optimize pricing strategies, 
        and personalize marketing campaigns at scale.
        
        Challenges and Considerations:
        
        While the benefits are substantial, businesses face several challenges in AI adoption:
        - Data privacy and security concerns
        - Skills shortage in AI and ML expertise
        - Integration with existing systems
        - Ethical considerations and bias mitigation
        - Regulatory compliance requirements
        
        Future Outlook:
        
        The AI market is projected to reach $1.8 trillion by 2030, with continued growth across 
        all industries. Emerging technologies like generative AI, quantum computing, and edge 
        computing will further accelerate business transformation.
        
        Companies that successfully integrate AI into their operations will gain significant 
        competitive advantages, while those that lag behind may struggle to remain relevant 
        in an increasingly digital economy.
        
        Contact Information:
        For more information, email us at info@airevolution.com or call +1-555-AI-FUTURE.
        Visit our website at https://www.airevolution.com for detailed case studies and 
        implementation guides.
        """
        
        return sample_content.strip()
    
    def process_content(self, content: str) -> Dict[str, Any]:
        """
        Process content through the complete pipeline
        """
        print("\n Starting content processing pipeline...")
        
        results = {
            'original_content': content,
            'processing_steps': [],
            'final_summary': '',
            'extracted_data': {},
            'insights': [],
            'metadata': {
                'timestamp': datetime.now().isoformat(),
                'model_used': self.gemini.config.model.value if self.gemini.is_available() else 'local'
            }
        }
        
        # Step 1: Data Extraction
        print("Step 1: Extracting structured data...")
        extracted_data = self.extract_structured_data(content)
        results['extracted_data'] = extracted_data
        results['processing_steps'].append({
            'step': 'data_extraction',
            'description': 'Extracted emails, URLs, and key data points',
            'result': extracted_data
        })
        
        # Store in memory
        self.memory.store('extracted_data', extracted_data)
        
        # Step 2: Content Condensation
        print("Step 2: Condensing content...")
        if self.gemini.is_available():
            condensed_result = self.gemini.enhance_condenser(content, target_length=800)
            condensed_text = condensed_result.get('text', content)
        else:
            condensed_result = self.agentium.condenser.condense(content, compression_ratio=0.4)
            condensed_text = condensed_result.get('text', content)
        
        results['processing_steps'].append({
            'step': 'condensation',
            'description': 'Intelligently condensed content while preserving key information',
            'result': condensed_result
        })
        
        # Store in memory
        self.memory.store('condensed_content', condensed_text)
        
        # Step 3: Content Optimization
        print("Step 3: Optimizing content...")
        if self.gemini.is_available():
            optimized_result = self.gemini.enhance_optimizer(condensed_text, optimization_type='readability')
            optimized_text = optimized_result.get('text', condensed_text)
        else:
            optimized_result = self.agentium.optimizer.optimize(condensed_text, optimization_type='text')
            optimized_text = optimized_result.get('text', condensed_text)
        
        results['processing_steps'].append({
            'step': 'optimization',
            'description': 'Enhanced readability and structure',
            'result': optimized_result
        })
        
        # Store in memory
        self.memory.store('optimized_content', optimized_text)
        
        # Step 4: Insight Generation
        print("Step 4: Generating insights...")
        if self.gemini.is_available():
            insights_result = self.gemini.enhance_insights(optimized_text, focus_area='business')
            insights = insights_result.get('insights', [])
        else:
            insights_result = self.agentium.insight_generator.generate_insights(optimized_text)
            insights = insights_result.get('insights', [])
        
        results['insights'] = insights
        results['processing_steps'].append({
            'step': 'insight_generation',
            'description': 'Generated business insights and key takeaways',
            'result': insights_result
        })
        
        # Store in memory
        self.memory.store('insights', insights)
        
        # Step 5: Custom Summarization
        print("Step 5: Creating executive summary...")
        if self.gemini.is_available():
            summary_result = self.gemini.enhance_summarizer(optimized_text, summary_type='executive')
            final_summary = summary_result.get('summary', optimized_text)
        else:
            summary_result = self.agentium.summarizer.summarize(optimized_text, strategy='extractive')
            final_summary = summary_result.get('summary', optimized_text)
        
        results['final_summary'] = final_summary
        results['processing_steps'].append({
            'step': 'summarization',
            'description': 'Created executive summary',
            'result': summary_result
        })
        
        # Store final results in memory
        self.memory.store('final_results', results)
        
        print("Content processing pipeline completed!")
        return results
    
    def extract_structured_data(self, content: str) -> Dict[str, Any]:
        """Extract structured data from content"""
        extracted = {}
        
        # Extract emails
        email_result = self.agentium.extractor.extract(content, extraction_type='emails')
        extracted['emails'] = email_result.get('extracted_data', [])
        
        # Extract URLs
        url_result = self.agentium.extractor.extract(content, extraction_type='urls')
        extracted['urls'] = url_result.get('extracted_data', [])
        
        # Extract phone numbers
        phone_result = self.agentium.extractor.extract(content, extraction_type='phones')
        extracted['phones'] = phone_result.get('extracted_data', [])
        
        # Extract numbers and percentages
        number_result = self.agentium.extractor.extract(content, extraction_type='numbers')
        extracted['numbers'] = number_result.get('extracted_data', [])
        
        return extracted
    
    def generate_report(self, results: Dict[str, Any]) -> str:
        """Generate a comprehensive report using templates"""
        template_content = """
# Content Processing Report

**Generated:** {{ metadata.timestamp }}
**AI Model:** {{ metadata.model_used }}

## Executive Summary
{{ final_summary }}

## Key Insights
{% for insight in insights %}
- {{ insight }}
{% endfor %}

## Extracted Data
{% if extracted_data.emails %}
**Emails:** {{ extracted_data.emails | join(', ') }}
{% endif %}
{% if extracted_data.urls %}
**URLs:** {{ extracted_data.urls | join(', ') }}
{% endif %}
{% if extracted_data.phones %}
**Phones:** {{ extracted_data.phones | join(', ') }}
{% endif %}

## Processing Steps
{% for step in processing_steps %}
### {{ step.step | title }}
{{ step.description }}
{% endfor %}

---
*Report generated by Agentium Content Processing Pipeline*
        """
        
        # Use template manager to render the report
        template_result = self.agentium.template_manager.process_template(
            template_content,
            results,
            template_type='markdown'
        )
        
        return template_result.get('rendered_content', 'Report generation failed')
    
    def save_results(self, results: Dict[str, Any], filename: str = None):
        """Save processing results to file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"content_processing_results_{timestamp}.json"
        
        output_dir = Path(__file__).parent / "output"
        output_dir.mkdir(exist_ok=True)
        
        output_file = output_dir / filename
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f" Results saved to: {output_file}")
        return output_file
    
    def demonstrate_memory_features(self):
        """Demonstrate memory and context management"""
        print("\nDemonstrating memory features...")
        
        # Store some sample data
        self.memory.store('user_preference', 'detailed_analysis')
        self.memory.store('processing_history', ['extraction', 'condensation', 'optimization'])
        
        # Retrieve data
        preference = self.memory.get('user_preference')
        history = self.memory.get('processing_history')
        
        print(f"Stored preference: {preference}")
        print(f"Processing history: {history}")
        
        # List all keys
        all_keys = self.memory.list_keys()
        print(f"Memory contains {len(all_keys)} items: {all_keys}")


def main():
    """Main demonstration function"""
    print("Agentium Content Processing Pipeline Demo")
    print("=" * 50)
    
    # Initialize pipeline with Gemini Pro model
    try:
        pipeline = ContentProcessingPipeline(gemini_model="gemini-pro")
    except Exception as e:
        print(f"WARNING: Using fallback model: {e}")
        pipeline = ContentProcessingPipeline()
    
    # Load sample content
    content = pipeline.load_sample_content()
    print(f"Loaded content ({len(content)} characters)")
    
    # Process content through pipeline
    results = pipeline.process_content(content)
    
    # Generate comprehensive report
    print("\nGenerating comprehensive report...")
    report = pipeline.generate_report(results)
    print("Report generated")
    
    # Save results
    output_file = pipeline.save_results(results)
    
    # Save report
    report_file = output_file.parent / f"report_{output_file.stem}.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"Report saved to: {report_file}")
    
    # Demonstrate memory features
    pipeline.demonstrate_memory_features()
    
    # Display summary
    print("\n" + "=" * 50)
    print("PROCESSING SUMMARY")
    print("=" * 50)
    print(f"Original content: {len(content)} characters")
    print(f"Final summary: {len(results['final_summary'])} characters")
    print(f"Insights generated: {len(results['insights'])}")
    print(f"Data points extracted: {sum(len(v) if isinstance(v, list) else 0 for v in results['extracted_data'].values())}")
    print(f"Processing steps: {len(results['processing_steps'])}")
    print(f" Files saved: 2 (JSON + Markdown report)")
    
    # Show key insights
    print("\nKEY INSIGHTS:")
    for i, insight in enumerate(results['insights'][:3], 1):
        print(f"{i}. {insight}")
    
    print("\nDemo completed successfully!")


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