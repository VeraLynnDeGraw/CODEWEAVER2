Here is your `CONTRIBUTING.md` file, fully branded and ready to paste!

---

**Command:** `nano CONTRIBUTING.md`

**Paste this:**

```markdown
# 🕸️ Contributing to CODEWEAVER2

> **Weaving insight through code — together.**

Thank you for your interest in contributing to CODEWEAVER2! Whether you're fixing a bug, adding a feature, improving documentation, or just asking a question, your help is deeply appreciated.

This document will guide you through the process of contributing to the project.

---

## 📋 Table of Contents

- [Code of Conduct](#-code-of-conduct)
- [Getting Started](#-getting-started)
- [Development Setup](#-development-setup)
- [Project Structure](#-project-structure)
- [How to Contribute](#-how-to-contribute)
- [Coding Standards](#-coding-standards)
- [Testing](#-testing)
- [Submitting Changes](#-submitting-changes)
- [Reporting Bugs](#-reporting-bugs)
- [Suggesting Features](#-suggesting-features)
- [Questions & Support](#-questions--support)

---

## 💜 Code of Conduct

We are committed to providing a welcoming and inclusive experience for everyone. Please be kind, respectful, and constructive in all interactions.

- **Be welcoming** to newcomers and experienced developers alike
- **Be respectful** of differing viewpoints and experiences
- **Be constructive** when giving and receiving feedback
- **Focus on what is best** for the community and the project

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+** (3.12 recommended)
- **Git** installed and configured
- A **GitHub account**
- **Cursor IDE** (optional, but recommended for testing the `cursor` command)

### Quick Start

```bash
# 1. Fork the repository on GitHub
#    Click the "Fork" button at: https://github.com/VeraLynnDeGraw/CODERWEAVER2

# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/CODERWEAVER2.git
cd CODERWEAVER2

# 3. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 4. Install with dev dependencies
pip install -e ".[dev]"

# 5. Verify everything works
codeweaver --help
pytest tests/ -v
```

---

## 🛠️ Development Setup

### Installing Dependencies

```bash
# Core dependencies only
pip install -e .

# Core + development tools (pytest, ruff)
pip install -e ".[dev]"
```

### Useful Commands

| Command | Purpose |
|---------|---------|
| `codeweaver` | Launch interactive menu |
| `codeweaver scan .` | Test scan command |
| `codeweaver runtime .` | Test runtime command |
| `codeweaver safety .` | Test safety command |
| `codeweaver cursor --list` | Test cursor command |
| `pytest tests/ -v` | Run all tests |
| `ruff check src/` | Lint the codebase |
| `ruff format src/` | Auto-format code |

---

## 📂 Project Structure

```
CODERWEAVER2/
├── src/codeweaver2/
│   ├── __init__.py          # Package init & version
│   ├── cli.py               # Click CLI & interactive menu
│   ├── models.py            # Pydantic V2 data models
│   └── commands/            # Command implementations
│       ├── __init__.py
│       ├── scan.py          # Code quality analysis
│       ├── runtime.py       # Runtime requirements
│       ├── safety.py        # Security auditing
│       └── cursor.py        # Cursor IDE integration
├── tests/                   # Test suite
│   ├── __init__.py
│   └── test_models.py       # Model unit tests
├── pyproject.toml           # Project configuration
├── README.md                # Project documentation
├── CONTRIBUTING.md          # You are here!
├── LICENSE                  # MIT License
└── .gitignore               # Git ignore rules
```

### Key Files to Know

| File | What It Does |
|------|-------------|
| `models.py` | All Pydantic V2 data models (FindingState, Proposal, etc.) |
| `cli.py` | Click command definitions + interactive menu |
| `commands/scan.py` | The `codeweaver scan` implementation |
| `commands/runtime.py` | The `codeweaver runtime` implementation |
| `commands/safety.py` | The `codeweaver safety` implementation |
| `commands/cursor.py` | The `codeweaver cursor` implementation |
| `pyproject.toml` | Dependencies, entry points, build config |

---

## 🤝 How to Contribute

### 1. Find Something to Work On

- Check the [Issues](https://github.com/VeraLynnDeGraw/CODERWEAVER2/issues) page for open bugs and feature requests
- Look for issues labeled `good first issue` if you're new
- Feel free to open a new issue if you have an idea

### 2. Create a Branch

```bash
# Always branch from main
git checkout main
git pull origin main

# Create a descriptive branch name
git checkout -b feature/add-python-ast-scanner
# or
git checkout -b fix/cursor-command-crash
# or
git checkout -b docs/update-readme
```

**Branch Naming Convention:**
- `feature/` — New features
- `fix/` — Bug fixes
- `docs/` — Documentation changes
- `test/` — Adding or fixing tests
- `refactor/` — Code refactoring

### 3. Make Your Changes

- Write clean, well-documented code
- Follow the [Coding Standards](#-coding-standards) below
- Add or update tests as needed
- Make sure all tests pass before committing

### 4. Commit Your Changes

```bash
git add .
git commit -m "feat: add Python AST scanner for type hint detection"
```

**Commit Message Convention:**
```
<type>: <short description>

<optional longer description>
```

Types:
- `feat:` — New feature
- `fix:` — Bug fix
- `docs:` — Documentation
- `test:` — Tests
- `refactor:` — Refactoring
- `style:` — Formatting (no logic change)
- `chore:` — Build/config changes

### 5. Push and Open a Pull Request

```bash
git push origin feature/add-python-ast-scanner
```

Then open a Pull Request on GitHub from your branch to `main`.

---

## 📐 Coding Standards

### Python Style

- Follow **PEP 8** guidelines
- Use **type hints** on all function signatures
- Use **docstrings** for all public functions and classes
- Maximum line length: **100 characters**

### Code Formatting

We use **Ruff** for linting and formatting:

```bash
# Check for issues
ruff check src/

# Auto-fix issues
ruff check src/ --fix

# Format code
ruff format src/
```

### Pydantic Models

All data models must:
- Inherit from `WeaverBaseModel` (which enforces `frozen=True`)
- Use `Field()` for constraints and metadata
- Use `@computed_field` for derived properties
- Include docstrings explaining the model's purpose

```python
class MyModel(WeaverBaseModel):
    """Description of what this model represents."""
    my_field: str = Field(..., description="What this field means")
    
    @computed_field
    @property
    def derived_value(self) -> bool:
        """Explain what this computes."""
        return len(self.my_field) > 0
```

### Enums

All enums with visual metadata must include:
- `icon` property (emoji)
- `color_hex` property (hex color code)
- Descriptive docstrings

### CLI Commands

- All commands must use `rich.console.Console()` for output
- Use Rich panels, tables, and progress bars for visual output
- Include the 🕸️ spiderweb branding in command headers
- Always provide a `--json` option for machine-readable output

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run a specific test file
pytest tests/test_models.py -v

# Run a specific test
pytest tests/test_models.py::test_proposal_quick_win -v

# Run with coverage
pytest tests/ --cov=codeweaver2 --cov-report=term-missing
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files `test_<module>.py`
- Name test functions `test_<what_you_are_testing>`
- Use descriptive docstrings for each test

```python
def test_finding_state_icons():
    """Test that all finding states have correct icons."""
    assert FindingState.THREAD.icon == "🧵"
    assert FindingState.CRITICAL.icon == "🔴"
```

### Test Categories

| Category | File | What to Test |
|----------|------|-------------|
| Models | `test_models.py` | Validation, defaults, computed fields |
| Enums | `test_enums.py` | Icons, colors, properties |
| Commands | `test_scan.py`, etc. | Command execution, output |
| Integration | `test_integration.py` | Full pipeline workflows |

---

## 📬 Submitting Changes

### Pull Request Checklist

Before submitting your PR, make sure:

- [ ] All tests pass (`pytest tests/ -v`)
- [ ] Code is formatted (`ruff format src/`)
- [ ] No linting errors (`ruff check src/`)
- [ ] New features have tests
- [ ] Documentation is updated (if applicable)
- [ ] Commit messages follow the convention
- [ ] Branch is up to date with `main`

### PR Description Template

```markdown
## 🕸️ Description
Brief description of what this PR does.

## 🔍 Type of Change
- [ ] 🐛 Bug fix
- [ ] ✨ New feature
- [ ] 📝 Documentation
- [ ] 🧪 Tests
- [ ] ♻️ Refactoring

## 🧪 Testing
Describe how you tested your changes.

## 📸 Screenshots (if applicable)
Add terminal output screenshots here.
```

---

## 🐛 Reporting Bugs

If you find a bug, please open an issue with:

1. **A clear title** describing the bug
2. **Steps to reproduce** the issue
3. **Expected behavior** vs **actual behavior**
4. **Your environment**:
   - OS (e.g., Arch Linux, macOS, Windows)
   - Python version (`python3 --version`)
   - CODEWEAVER2 version (`codeweaver --version`)
5. **Terminal output** (copy and paste the full error)

---

## 💡 Suggesting Features

Have an idea for CODEWEAVER2? We'd love to hear it! Open an issue with:

1. **A clear title** describing the feature
2. **The problem** this feature would solve
3. **Your proposed solution**
4. **Any alternatives** you've considered

---

## ❓ Questions & Support

- **GitHub Issues**: For bugs and feature requests
- **Discord**: `veralynndegraw10011` for direct questions
- **Email**: [veralynndegraw10011@proton.me](mailto:veralynndegraw10011@proton.me)

---

## 🙏 Thank You!

Every contribution matters — whether it's a single typo fix or a major new feature. Thank you for helping make CODEWEAVER2 better for everyone!

> *"Alone we can do so little; together we can do so much."* – Helen Keller

🕸️ Happy weaving!
```

---

### 💾 Save the file:
1. Press `Ctrl + O` (letter O, not zero)
2. Press `Enter` to confirm
3. Press `Ctrl + X` to exit

---

### ✅ Verify it was created:

```bash
ls -la CONTRIBUTING.md
``
Here is your `CONTRIBUTING.md` file, fully branded and ready to paste!

---

**Command:** `nano CONTRIBUTING.md`

**Paste this:**

```markdown
# 🕸️ Contributing to CODEWEAVER2

> **Weaving insight through code — together.**

Thank you for your interest in contributing to CODEWEAVER2! Whether you're fixing a bug, adding a feature, improving documentation, or just asking a question, your help is deeply appreciated.

This document will guide you through the process of contributing to the project.

---

## 📋 Table of Contents

- [Code of Conduct](#-code-of-conduct)
- [Getting Started](#-getting-started)
- [Development Setup](#-development-setup)
- [Project Structure](#-project-structure)
- [How to Contribute](#-how-to-contribute)
- [Coding Standards](#-coding-standards)
- [Testing](#-testing)
- [Submitting Changes](#-submitting-changes)
- [Reporting Bugs](#-reporting-bugs)
- [Suggesting Features](#-suggesting-features)
- [Questions & Support](#-questions--support)

---

## 💜 Code of Conduct

We are committed to providing a welcoming and inclusive experience for everyone. Please be kind, respectful, and constructive in all interactions.

- **Be welcoming** to newcomers and experienced developers alike
- **Be respectful** of differing viewpoints and experiences
- **Be constructive** when giving and receiving feedback
- **Focus on what is best** for the community and the project

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+** (3.12 recommended)
- **Git** installed and configured
- A **GitHub account**
- **Cursor IDE** (optional, but recommended for testing the `cursor` command)

### Quick Start

```bash
# 1. Fork the repository on GitHub
#    Click the "Fork" button at: https://github.com/VeraLynnDeGraw/CODERWEAVER2

# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/CODERWEAVER2.git
cd CODERWEAVER2

# 3. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 4. Install with dev dependencies
pip install -e ".[dev]"

# 5. Verify everything works
codeweaver --help
pytest tests/ -v
```

---

## 🛠️ Development Setup

### Installing Dependencies

```bash
# Core dependencies only
pip install -e .

# Core + development tools (pytest, ruff)
pip install -e ".[dev]"
```

### Useful Commands

| Command | Purpose |
|---------|---------|
| `codeweaver` | Launch interactive menu |
| `codeweaver scan .` | Test scan command |
| `codeweaver runtime .` | Test runtime command |
| `codeweaver safety .` | Test safety command |
| `codeweaver cursor --list` | Test cursor command |
| `pytest tests/ -v` | Run all tests |
| `ruff check src/` | Lint the codebase |
| `ruff format src/` | Auto-format code |

---

## 📂 Project Structure

```
CODERWEAVER2/
├── src/codeweaver2/
│   ├── __init__.py          # Package init & version
│   ├── cli.py               # Click CLI & interactive menu
│   ├── models.py            # Pydantic V2 data models
│   └── commands/            # Command implementations
│       ├── __init__.py
│       ├── scan.py          # Code quality analysis
│       ├── runtime.py       # Runtime requirements
│       ├── safety.py        # Security auditing
│       └── cursor.py        # Cursor IDE integration
├── tests/                   # Test suite
│   ├── __init__.py
│   └── test_models.py       # Model unit tests
├── pyproject.toml           # Project configuration
├── README.md                # Project documentation
├── CONTRIBUTING.md          # You are here!
├── LICENSE                  # MIT License
└── .gitignore               # Git ignore rules
```

### Key Files to Know

| File | What It Does |
|------|-------------|
| `models.py` | All Pydantic V2 data models (FindingState, Proposal, etc.) |
| `cli.py` | Click command definitions + interactive menu |
| `commands/scan.py` | The `codeweaver scan` implementation |
| `commands/runtime.py` | The `codeweaver runtime` implementation |
| `commands/safety.py` | The `codeweaver safety` implementation |
| `commands/cursor.py` | The `codeweaver cursor` implementation |
| `pyproject.toml` | Dependencies, entry points, build config |

---

## 🤝 How to Contribute

### 1. Find Something to Work On

- Check the [Issues](https://github.com/VeraLynnDeGraw/CODERWEAVER2/issues) page for open bugs and feature requests
- Look for issues labeled `good first issue` if you're new
- Feel free to open a new issue if you have an idea

### 2. Create a Branch

```bash
# Always branch from main
git checkout main
git pull origin main

# Create a descriptive branch name
git checkout -b feature/add-python-ast-scanner
# or
git checkout -b fix/cursor-command-crash
# or
git checkout -b docs/update-readme
```

**Branch Naming Convention:**
- `feature/` — New features
- `fix/` — Bug fixes
- `docs/` — Documentation changes
- `test/` — Adding or fixing tests
- `refactor/` — Code refactoring

### 3. Make Your Changes

- Write clean, well-documented code
- Follow the [Coding Standards](#-coding-standards) below
- Add or update tests as needed
- Make sure all tests pass before committing

### 4. Commit Your Changes

```bash
git add .
git commit -m "feat: add Python AST scanner for type hint detection"
```

**Commit Message Convention:**
```
<type>: <short description>

<optional longer description>
```

Types:
- `feat:` — New feature
- `fix:` — Bug fix
- `docs:` — Documentation
- `test:` — Tests
- `refactor:` — Refactoring
- `style:` — Formatting (no logic change)
- `chore:` — Build/config changes

### 5. Push and Open a Pull Request

```bash
git push origin feature/add-python-ast-scanner
```

Then open a Pull Request on GitHub from your branch to `main`.

---

## 📐 Coding Standards

### Python Style

- Follow **PEP 8** guidelines
- Use **type hints** on all function signatures
- Use **docstrings** for all public functions and classes
- Maximum line length: **100 characters**

### Code Formatting

We use **Ruff** for linting and formatting:

```bash
# Check for issues
ruff check src/

# Auto-fix issues
ruff check src/ --fix

# Format code
ruff format src/
```

### Pydantic Models

All data models must:
- Inherit from `WeaverBaseModel` (which enforces `frozen=True`)
- Use `Field()` for constraints and metadata
- Use `@computed_field` for derived properties
- Include docstrings explaining the model's purpose

```python
class MyModel(WeaverBaseModel):
    """Description of what this model represents."""
    my_field: str = Field(..., description="What this field means")
    
    @computed_field
    @property
    def derived_value(self) -> bool:
        """Explain what this computes."""
        return len(self.my_field) > 0
```

### Enums

All enums with visual metadata must include:
- `icon` property (emoji)
- `color_hex` property (hex color code)
- Descriptive docstrings

### CLI Commands

- All commands must use `rich.console.Console()` for output
- Use Rich panels, tables, and progress bars for visual output
- Include the 🕸️ spiderweb branding in command headers
- Always provide a `--json` option for machine-readable output

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run a specific test file
pytest tests/test_models.py -v

# Run a specific test
pytest tests/test_models.py::test_proposal_quick_win -v

# Run with coverage
pytest tests/ --cov=codeweaver2 --cov-report=term-missing
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files `test_<module>.py`
- Name test functions `test_<what_you_are_testing>`
- Use descriptive docstrings for each test

```python
def test_finding_state_icons():
    """Test that all finding states have correct icons."""
    assert FindingState.THREAD.icon == "🧵"
    assert FindingState.CRITICAL.icon == "🔴"
```

### Test Categories

| Category | File | What to Test |
|----------|------|-------------|
| Models | `test_models.py` | Validation, defaults, computed fields |
| Enums | `test_enums.py` | Icons, colors, properties |
| Commands | `test_scan.py`, etc. | Command execution, output |
| Integration | `test_integration.py` | Full pipeline workflows |

---

## 📬 Submitting Changes

### Pull Request Checklist

Before submitting your PR, make sure:

- [ ] All tests pass (`pytest tests/ -v`)
- [ ] Code is formatted (`ruff format src/`)
- [ ] No linting errors (`ruff check src/`)
- [ ] New features have tests
- [ ] Documentation is updated (if applicable)
- [ ] Commit messages follow the convention
- [ ] Branch is up to date with `main`

### PR Description Template

```markdown
## 🕸️ Description
Brief description of what this PR does.

## 🔍 Type of Change
- [ ] 🐛 Bug fix
- [ ] ✨ New feature
- [ ] 📝 Documentation
- [ ] 🧪 Tests
- [ ] ♻️ Refactoring

## 🧪 Testing
Describe how you tested your changes.

## 📸 Screenshots (if applicable)
Add terminal output screenshots here.
```

---

## 🐛 Reporting Bugs

If you find a bug, please open an issue with:

1. **A clear title** describing the bug
2. **Steps to reproduce** the issue
3. **Expected behavior** vs **actual behavior**
4. **Your environment**:
   - OS (e.g., Arch Linux, macOS, Windows)
   - Python version (`python3 --version`)
   - CODEWEAVER2 version (`codeweaver --version`)
5. **Terminal output** (copy and paste the full error)

---

## 💡 Suggesting Features

Have an idea for CODEWEAVER2? We'd love to hear it! Open an issue with:

1. **A clear title** describing the feature
2. **The problem** this feature would solve
3. **Your proposed solution**
4. **Any alternatives** you've considered

---

## ❓ Questions & Support

- **GitHub Issues**: For bugs and feature requests
- **Discord**: `veralynndegraw10011` for direct questions
- **Email**: [veralynndegraw10011@proton.me](mailto:veralynndegraw10011@proton.me)

---

## 🙏 Thank You!

Every contribution matters — whether it's a single typo fix or a major new feature. Thank you for helping make CODEWEAVER2 better for everyone!

> *"Alone we can do so little; together we can do so much."* – Helen Keller

🕸️ Happy weaving!
```

---

### 💾 Save the file:
1. Press `Ctrl + O` (letter O, not zero)
2. Press `Enter` to confirm
3. Press `Ctrl + X` to exit

---

### ✅ Verify it was created:

```bash
ls -la CONTRIBUTING.md
```
  🕸️
