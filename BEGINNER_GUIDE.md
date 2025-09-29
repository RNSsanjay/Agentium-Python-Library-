# Agentium - Getting Started Guide for Beginners

## Table of Contents
1. [What is Agentium?](#what-is-agentium)
2. [Installation Guide](#installation-guide)
3. [API Key Setup](#api-key-setup)
4. [Your First Agentium Program](#your-first-agentium-program)
5. [Sample Projects Walkthrough](#sample-projects-walkthrough)
6. [Common Issues and Solutions](#common-issues-and-solutions)

## What is Agentium?

Agentium is a Python library that helps you build intelligent applications. Think of it as a toolkit that provides ready-to-use AI features for your programs. Whether you want to:

- Summarize long documents
- Translate text between languages
- Extract information from text
- Generate insights from data
- Optimize content for better readability

Agentium makes these tasks simple with just a few lines of code.

## Installation Guide

### Step 1: Install Python
If you don't have Python installed:
1. Go to https://python.org/downloads
2. Download Python 3.8 or newer
3. Follow the installation instructions for your operating system

### Step 2: Install Agentium
Open your command prompt or terminal and run:

```bash
# Basic installation
pip install agentium

# With AI features (recommended)
pip install agentium google-generativeai
```

### Step 3: Verify Installation
Create a test file called `test_agentium.py`:

```python
try:
    import agentium
    print("Agentium installed successfully!")
    print(f"Version: {agentium.__version__}")
except ImportError:
    print("Agentium not installed. Please run: pip install agentium")
```

Run it with: `python test_agentium.py`

## API Key Setup

To use AI-enhanced features, you need a Google Gemini API key.

### Getting Your API Key

1. **Visit Google AI Studio**
   - Go to: https://makersuite.google.com/app/apikey
   - Sign in with your Google account

2. **Create Your API Key**
   - Click the "Create API Key" button
   - Choose "Create API key in new project"
   - Copy the generated key and save it safely

### Setting Up Your API Key

Choose one of these methods:

#### Method 1: Environment Variable (Recommended)

**Windows Command Prompt:**
```cmd
set GEMINI_API_KEY=your_actual_api_key_here
```

**Windows PowerShell:**
```powershell
$env:GEMINI_API_KEY="your_actual_api_key_here"
```

**Linux/Mac:**
```bash
export GEMINI_API_KEY=your_actual_api_key_here
```

#### Method 2: In Your Python Code
```python
import os
os.environ['GEMINI_API_KEY'] = 'your_actual_api_key_here'
```

#### Method 3: Using a .env File
Create a file named `.env` in your project folder:
```
GEMINI_API_KEY=your_actual_api_key_here
```

Then in your Python code:
```python
from dotenv import load_dotenv
load_dotenv()
```

### Important Security Notes
- Never share your API key with others
- Don't commit API keys to version control (GitHub, etc.)
- Use environment variables in production applications
- Keep your API key secure and private

## Your First Agentium Program

Let's create a simple program that demonstrates basic features.

Create a file called `my_first_agentium.py`:

```python
#!/usr/bin/env python3
"""
My First Agentium Program
A simple demonstration of Agentium's basic features
"""

import os
from agentium import Agentium

def main():
    # Check if we have an API key
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("No API key found. Running with basic features only.")
        print("To enable AI features, set GEMINI_API_KEY environment variable.")
    else:
        print("API key found! AI features enabled.")
    
    # Initialize Agentium
    agentium = Agentium()
    
    # Example text to work with
    long_text = """
    Artificial Intelligence (AI) is revolutionizing the way we work, communicate, 
    and solve problems. From natural language processing to computer vision, AI 
    technologies are being integrated into various industries including healthcare, 
    finance, education, and transportation. Machine learning algorithms can now 
    analyze vast amounts of data to identify patterns and make predictions that 
    would be impossible for humans to detect manually. As AI continues to evolve, 
    it promises to bring even more innovative solutions to complex challenges 
    facing our society today.
    """
    
    print("Original text:")
    print(long_text.strip())
    print("\n" + "="*50)
    
    # 1. Condense the text
    print("\n1. CONDENSING TEXT")
    condensed = agentium.condenser.condense(long_text, compression_ratio=0.5)
    print("Condensed version:")
    print(condensed)
    
    # 2. Optimize the condensed text
    print("\n2. OPTIMIZING TEXT")
    optimized = agentium.optimizer.optimize(condensed)
    print("Optimized version:")
    print(optimized)
    
    # 3. Extract key information
    print("\n3. EXTRACTING INFORMATION")
    extracted = agentium.extractor.extract(long_text, extract_types=["keywords", "entities"])
    print("Extracted information:")
    for key, value in extracted.items():
        if value:
            print(f"  {key}: {value}")
    
    # 4. Generate insights
    print("\n4. GENERATING INSIGHTS")
    insights = agentium.insight_generator.generate_insights(long_text)
    print("Generated insights:")
    print(insights)
    
    print("\n" + "="*50)
    print("Program completed successfully!")

if __name__ == "__main__":
    main()
```

Run this program with: `python my_first_agentium.py`

## Sample Projects Walkthrough

Agentium comes with 5 comprehensive sample projects that demonstrate all features:

### 1. Content Processing Pipeline
**Location:** `sample_projects/1_content_processing_pipeline/`
**What it does:** Processes documents with AI enhancement
**Best for:** Learning document analysis and content optimization

**To run:**
```bash
cd sample_projects/1_content_processing_pipeline
python content_pipeline.py
```

### 2. Multilingual News Analyzer  
**Location:** `sample_projects/2_multilingual_news_analyzer/`
**What it does:** Analyzes news in multiple languages
**Best for:** Learning translation and sentiment analysis

### 3. Data Intelligence Dashboard
**Location:** `sample_projects/3_data_intelligence_dashboard/`
**What it does:** Creates data visualizations and insights
**Best for:** Learning data analysis and reporting

### 4. Automated Report Generator
**Location:** `sample_projects/4_automated_report_generator/`
**What it does:** Generates professional reports automatically
**Best for:** Learning report creation and templates

### 5. Smart Communication Hub
**Location:** `sample_projects/5_smart_communication_hub/`  
**What it does:** Manages multi-channel communication
**Best for:** Learning workflow orchestration

### Interactive Demo
Try the Streamlit demo for hands-on experience:
```bash
pip install streamlit plotly pandas
streamlit run sample_projects/agentium_streamlit_demo.py
```

## Common Issues and Solutions

### Issue 1: "ModuleNotFoundError: No module named 'agentium'"
**Solution:** Install Agentium
```bash
pip install agentium
```

### Issue 2: "ImportError: No module named 'google.generativeai'"
**Solution:** Install AI dependencies
```bash
pip install google-generativeai
```

### Issue 3: API key not working
**Solutions:**
1. Check if your API key is correct
2. Make sure you've enabled the Gemini API in Google Cloud
3. Verify your environment variable is set correctly:
   ```python
   import os
   print(os.getenv('GEMINI_API_KEY'))  # Should print your key
   ```

### Issue 4: "Permission denied" errors
**Solution:** Check your Python installation permissions or use:
```bash
pip install --user agentium
```

### Issue 5: Code runs but no AI enhancement
**Check these items:**
1. API key is set correctly
2. Internet connection is working
3. Google AI services are accessible in your region

### Issue 6: Slow performance
**Solutions:**
1. Use faster models like `gemini-1.5-flash` for quicker responses
2. Reduce input text size
3. Check your internet connection

## Getting Help

### Documentation
- Main documentation: https://agentium.readthedocs.io
- PyPI page: https://pypi.org/project/agentium/

### Sample Code
All sample projects include detailed comments explaining each feature.

### Community
- GitHub Issues: Report bugs or ask questions
- Stack Overflow: Tag your questions with `agentium`

### Best Practices
1. Always check if API keys are available before using AI features
2. Handle errors gracefully in your applications
3. Start with small text samples when testing
4. Use environment variables for API keys in production
5. Keep your dependencies updated

## Next Steps

1. Run the sample projects to see all features in action
2. Try the interactive Streamlit demo
3. Build your own application using Agentium features
4. Explore advanced features in the documentation
5. Join the community and share your projects

Happy coding with Agentium!