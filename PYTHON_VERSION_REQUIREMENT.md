# Python Version Requirement

## Required Python Version

**The pfSense Enhanced MCP Server requires Python 3.10 or higher.**

Your system currently has Python 3.9.6, but FastMCP (the MCP framework) requires Python 3.10+.

## Install Python 3.10+ on macOS

### Option 1: Homebrew (Recommended)

```bash
# Install Python 3.12 (latest stable)
brew install python@3.12

# Verify installation
python3.12 --version

# Create alias (optional)
echo 'alias python3=python3.12' >> ~/.zshrc
source ~/.zshrc
```

### Option 2: pyenv (For multiple Python versions)

```bash
# Install pyenv
brew install pyenv

# Install Python 3.12
pyenv install 3.12.0

# Set as global version
pyenv global 3.12.0

# Add to shell profile
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc
```

### Option 3: python.org Download

Download from: https://www.python.org/downloads/

## Setup After Installing Python 3.10+

Once you have Python 3.10+:

```bash
# Create virtual environment (recommended)
python3.12 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python test-http-transport.py

# Run the server
./run-http.sh
```

## Docker Alternative (No Python Installation Needed)

If you prefer not to install Python locally:

```bash
# Build and run with Docker
docker-compose up -d

# Check logs
docker-compose logs -f

# The server will be available at http://localhost:8000/mcp
```

## Why Python 3.10+?

- FastMCP requires Python 3.10+ for modern async features
- Pydantic 2.5+ (used for validation) requires Python 3.10+
- Better type hints and performance improvements
- Long-term support and security updates

## Checking Your Python Version

```bash
# Check system Python
python3 --version

# Check all installed Python versions
ls -la /usr/bin/python* /usr/local/bin/python*

# Check Homebrew Python
brew list | grep python
```
