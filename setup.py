from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="agentium",
    version="1.0.0",
    author="Sanjay N",
    author_email="2005sanjaynrs@gmail.com",
    description="A comprehensive toolkit for AI agent development and workflow orchestration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RNSsanjay/Agentium-Python-Library",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=22.0",
            "flake8>=5.0",
            "mypy>=0.991",
        ],
        "langchain": [
            "langchain>=0.1.0",
            "langchain-community>=0.0.10",
        ],
        "langgraph": [
            "langgraph>=0.0.20",
        ],
        "crewai": [
            "crewai>=0.1.0",
        ],
    },
    keywords="ai, agents, langchain, langgraph, crewai, nlp, automation, workflow",
)