# Agentium PyPI Deployment Commands

## Prerequisites
# 1. Create PyPI account: https://pypi.org/account/register/
# 2. Create TestPyPI account: https://test.pypi.org/account/register/
# 3. Generate API tokens from your account settings

## Build the package
python -m build

## Check the package
twine check dist/*

## Upload to TestPyPI (recommended first)
twine upload --repository testpypi dist/*

## Test install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ agentium

## Upload to Production PyPI
twine upload dist/*

## Install from PyPI
pip install agentium

## Alternative: Upload with token directly
# twine upload --repository testpypi -u __token__ -p your_testpypi_token_here dist/*
# twine upload -u __token__ -p your_pypi_token_here dist/*