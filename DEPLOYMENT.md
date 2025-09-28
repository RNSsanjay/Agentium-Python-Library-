# Agentium Python Library - Deployment Guide

## 🚀 Quick Start Installation

### Option 1: Local Development Installation
```bash
# Clone or extract the Agentium library
cd Agentium-Python-Library

# Install in development mode
pip install -e .

# Run tests to verify installation
python test_agentium.py
```

### Option 2: Build and Install Package
```bash
# Build the package
python setup.py sdist bdist_wheel

# Install from built package
pip install dist/agentium-1.0.0-py3-none-any.whl
```

### Option 3: Direct Installation
```bash
# Install from source directory
pip install .
```

## 📋 Prerequisites

### Required Dependencies
The core library requires these packages (automatically installed):
- `numpy>=1.21.0`
- `pandas>=1.3.0`
- `requests>=2.25.0`
- `pydantic>=1.8.0`
- `beautifulsoup4>=4.9.0`
- `nltk>=3.6`
- `networkx>=2.6`
- `jinja2>=3.0.0`

### Optional Framework Dependencies
Install these for specific framework integrations:

#### LangChain Integration
```bash
pip install agentium[langchain]
# or manually:
pip install langchain>=0.1.0
```

#### LangGraph Integration  
```bash
pip install agentium[langgraph]
# or manually:
pip install langgraph>=0.1.0
```

#### CrewAI Integration
```bash
pip install agentium[crewai]
# or manually:
pip install crewai>=0.1.0
```

#### All Integrations
```bash
pip install agentium[all]
```

## 🧪 Testing Installation

Run the comprehensive test suite:
```bash
python test_agentium.py
```

Expected output:
```
🚀 Starting Agentium Library Tests
==================================================
🧪 Testing core component imports...
✅ All core components imported successfully

🔗 Testing integration availability...
  LangChain Integration: ✅ Available / ⚠️  Not Available
  LangGraph Integration: ✅ Available / ⚠️  Not Available  
  CrewAI Integration: ✅ Available / ⚠️  Not Available

⚙️  Testing core component functionality...
✅ Agentium initialized successfully
  Testing basic workflow...
  ✅ Basic workflow completed successfully
  📊 Steps completed: 3
  📝 Final output length: 156
  Testing individual components...
  ✅ Condenser: 45.2% compression
  ✅ Optimizer: 3 improvements applied
  ✅ Summarizer: 89 character summary created
  ✅ Extractor: 127 characters of data extracted
  ✅ Memory: Data stored and retrieved

🔍 Testing integration status checking...
  Integration Status:
    langchain: ✅ Available
    langgraph: ⚠️  Not Available
    crewai: ⚠️  Not Available

📝 Testing logging functionality...
✅ Logger functionality working correctly

==================================================
🎯 Test Summary: 5/5 tests passed
🎉 All tests passed! Agentium library is ready to use.
```

## 📦 Package Structure

```
agentium/
├── __init__.py              # Main package initialization
├── core/                    # Core functionality modules
│   ├── condenser.py         # Text condensation
│   ├── optimizer.py         # Content optimization
│   ├── rearranger.py        # Content reorganization
│   ├── extractor.py         # Data extraction
│   ├── communicator.py      # Multi-channel communication
│   ├── translator.py        # Translation and localization
│   ├── insight_generator.py # AI-powered insights
│   ├── workflow_helper.py   # Workflow orchestration
│   ├── template_manager.py  # Template management
│   ├── memory_helper.py     # Context and memory storage
│   └── summarize_custom.py  # Custom summarization
├── utils/                   # Utility modules
│   └── logger_utils.py      # Advanced logging system
├── integrations/            # Framework integrations
│   ├── __init__.py
│   ├── langchain.py         # LangChain integration
│   ├── langgraph.py         # LangGraph integration
│   └── crewai.py            # CrewAI integration
setup.py                     # Package setup configuration
requirements.txt             # Dependencies list
README.md                    # Documentation
test_agentium.py            # Test suite
```

## 🎯 Basic Usage Examples

### Simple Usage
```python
from agentium import Agentium

# Initialize Agentium
agent = Agentium()

# Process content through a workflow
content = "Your text content here..."
result = agent.process_content(content, workflow="basic")
print(result['final_output'])
```

### Individual Components
```python
from agentium import Condenser, Optimizer, CustomSummarizer

# Use individual components
condenser = Condenser()
result = condenser.condense("Long text to condense...")

optimizer = Optimizer() 
result = optimizer.optimize("Content to optimize...")

summarizer = CustomSummarizer()
result = summarizer.summarize("Content to summarize...")
```

### Framework Integration Examples

#### LangChain Integration
```python
from agentium import get_agentium_langchain_integration

# Get LangChain integration
integration = get_agentium_langchain_integration()

# Get tools for LangChain agents
tools = integration.get_all_tools()
memory = integration.create_memory()
```

#### CrewAI Integration
```python
from agentium import get_agentium_crewai_integration

# Get CrewAI integration
integration = get_agentium_crewai_integration()

# Create enhanced agents
agent = integration.create_agent(
    role="Content Analyzer",
    goal="Analyze and process content",
    backstory="Expert content processor",
    tools=["condenser", "summarizer"]
)
```

## 🔧 Configuration

### Logging Configuration
```python
from agentium import LoggerUtils, LoggerConfig

# Configure logging
config = LoggerConfig(
    log_level="INFO",
    log_format="detailed",
    enable_file_logging=True,
    log_file="agentium.log"
)

LoggerUtils.configure(config)
```

### Component Configuration
```python
from agentium import Condenser, CondenserConfig

# Configure individual components
config = CondenserConfig(
    method="extractive",
    target_ratio=0.5,
    preserve_formatting=True
)

condenser = Condenser(config)
```

## 🚀 Production Deployment

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY agentium/ ./agentium/
COPY setup.py .
RUN pip install .

# Your application code
COPY your_app.py .
CMD ["python", "your_app.py"]
```

### Environment Variables
Set these environment variables for production:
```bash
# Optional API keys for enhanced functionality
export OPENAI_API_KEY="your_openai_key"
export ANTHROPIC_API_KEY="your_anthropic_key" 
export GOOGLE_TRANSLATE_API_KEY="your_translate_key"

# Email configuration for communicator
export SMTP_SERVER="smtp.gmail.com"
export SMTP_PORT="587"
export SMTP_USERNAME="your_email"
export SMTP_PASSWORD="your_password"

# Redis configuration for memory (optional)
export REDIS_HOST="localhost"
export REDIS_PORT="6379"
export REDIS_PASSWORD="your_redis_password"
```

## 🔍 Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   # Make sure package is installed
   pip list | grep agentium
   
   # Reinstall if needed
   pip uninstall agentium
   pip install -e .
   ```

2. **Integration Not Available**
   ```bash
   # Install framework-specific dependencies
   pip install agentium[langchain]
   pip install agentium[langgraph] 
   pip install agentium[crewai]
   ```

3. **NLTK Data Missing**
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

4. **Memory Storage Issues**
   ```python
   # Check memory storage backend
   from agentium import MemoryHelper
   memory = MemoryHelper()
   print(memory.get_storage_info())
   ```

### Getting Help

- Run the test suite: `python test_agentium.py`
- Check integration status programmatically:
  ```python
  from agentium import Agentium
  agent = Agentium()
  print(agent.get_integration_status())
  ```

## 📈 Performance Optimization

### For Large-Scale Deployment
1. **Use Redis for memory storage** (better performance than file-based)
2. **Configure appropriate log levels** (INFO or WARNING in production)
3. **Use workflow orchestration** for complex processing pipelines
4. **Enable caching** for frequently processed content
5. **Monitor memory usage** with built-in statistics

### Memory Configuration for Scale
```python
from agentium import MemoryHelper, MemoryConfig

config = MemoryConfig(
    storage_backend="redis",
    redis_host="your_redis_host",
    redis_port=6379,
    default_ttl=3600,  # 1 hour
    enable_cleanup=True
)

memory = MemoryHelper(config)
```

## ✅ Deployment Checklist

- [ ] Install Python 3.8+
- [ ] Install Agentium library (`pip install -e .`)
- [ ] Run test suite (`python test_agentium.py`)
- [ ] Install framework dependencies as needed
- [ ] Configure environment variables
- [ ] Set up logging configuration
- [ ] Configure memory storage backend
- [ ] Test integration status
- [ ] Verify API keys (if using external services)
- [ ] Set up monitoring/logging in production
- [ ] Configure backup for persistent memory storage
- [ ] Test workflow performance with sample data

**🎉 Your Agentium library is now ready for production use!**