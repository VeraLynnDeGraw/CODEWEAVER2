#!/bin/bash

# 🕸️ CODEWEAVER2 Installer
# One-command installation script

set -e  # Exit on error

echo "╭──────────────────────────────────────────────────────────────╮"
echo "│  🕸️  CODEWEAVER2 v2.0.0 Installer                           │"
echo "│  Weaving insight through code                                │"
echo "╰──────────────────────────────────────────────────────────────╯"
echo ""

# Check if Python 3.10+ is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.10 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
REQUIRED_VERSION="3.10"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "❌ Python $PYTHON_VERSION detected. CODEWEAVER2 requires Python $REQUIRED_VERSION or higher."
    exit 1
fi

echo "✅ Python $PYTHON_VERSION detected"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip is not installed. Please install pip."
    exit 1
fi

echo "✅ pip detected"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo ""
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
    echo "✅ Virtual environment created"
else
    echo ""
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "📦 Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip --quiet

# Install CODEWEAVER2 in editable mode
echo "📦 Installing CODEWEAVER2..."
pip install -e . --quiet

echo "✅ CODEWEAVER2 installed successfully!"
echo ""

# Ask if user wants to install dev dependencies
read -p "Would you like to install development dependencies? (y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "📦 Installing development dependencies..."
    pip install -e ".[dev]" --quiet
    echo "✅ Development dependencies installed"
fi

# Ask if user wants to install analysis dependencies
read -p "Would you like to install analysis dependencies? (y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "📦 Installing analysis dependencies..."
    pip install -e ".[analysis]" --quiet
    echo "✅ Analysis dependencies installed"
fi

echo ""
echo "╭──────────────────────────────────────────────────────────────╮"
echo "│  ✅ Installation Complete!                                   │"
echo "╰──────────────────────────────────────────────────────────────╯"
echo ""
echo "🎯 Quick Start:"
echo "  source .venv/bin/activate  # Activate virtual environment"
echo "  codeweaver                 # Launch interactive menu"
echo "  codeweaver --help          # Show help"
echo ""
echo "📚 Documentation:"
echo "  https://github.com/VeraLynnDeGraw/CODERWEAVER2#readme"
echo ""
echo "💡 Tip: Add this to your ~/.bashrc or ~/.zshrc:"
echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
echo ""
