.PHONY: help install install-dev install-all test lint format clean build

help:  ## Show this help message
	@echo "🕸️ CODEWEAVER2 - Available Commands"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install CODEWEAVER2 (core dependencies only)
	@echo "📦 Installing CODEWEAVER2..."
	pip install -e .
	@echo "✅ Installation complete!"

install-dev:  ## Install with development dependencies
	@echo "📦 Installing CODEWEAVER2 with dev dependencies..."
	pip install -e ".[dev]"
	@echo "✅ Installation complete!"

install-all:  ## Install with all dependencies (dev + analysis)
	@echo "📦 Installing CODEWEAVER2 with all dependencies..."
	pip install -e ".[all]"
	@echo "✅ Installation complete!"

test:  ## Run test suite
	@echo "🧪 Running tests..."
	pytest tests/ -v

test-cov:  ## Run tests with coverage report
	@echo "🧪 Running tests with coverage..."
	pytest tests/ -v --cov=codeweaver2 --cov-report=term-missing

lint:  ## Run code linter (ruff)
	@echo "🔍 Running linter..."
	ruff check src/ tests/

format:  ## Format code with ruff
	@echo "🎨 Formatting code..."
	ruff format src/ tests/

type-check:  ## Run type checker (mypy)
	@echo "🔍 Running type checker..."
	mypy src/

clean:  ## Clean up build artifacts and cache
	@echo "🧹 Cleaning up..."
	rm -rf build/ dist/ *.egg-info/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "✅ Cleaned!"

build:  ## Build distribution package
	@echo "📦 Building package..."
	python -m build
	@echo "✅ Build complete! Check dist/ directory"

run:  ## Launch CODEWEAVER2 interactive menu
	codeweaver

scan:  ## Run quick scan on current directory
	codeweaver scan . --quick

runtime:  ## Check runtime requirements
	codeweaver runtime .

safety:  ## Run safety audit
	codeweaver safety .
