X# 🕸️ CODEWEAVER2

> **Weaving insight through code.**

CODEWEAVER2 is a powerful, human-centered CLI tool designed to analyze your codebase, assess runtime requirements, audit security, and seamlessly hand off actionable fixes directly to your IDE (Cursor). 

It answers the four most important questions about any codebase:
- 🔍 **How good is this code?** (`scan`)
- 📦 **Can I run this?** (`runtime`)
- 🛡️ **Should I trust this?** (`safety`)
- 🖱️ **How do I fix this?** (`cursor`)

---

## ✨ Features

- **🧵 Smart State Machine**: Uses a unique "spiderweb" taxonomy (Thread → Node → Pattern → Repair) to track code health.
- **⚡ Blazing Fast**: Get a full project health check in under a second with `--quick` mode.
- **🛡️ Safety First**: Built-in heuristics to detect obfuscated code, credential harvesting, and malicious patterns in downloaded programs.
- **🖱️ Cursor Integration**: One-click handoff of proposed fixes directly into Cursor IDE with full diff previews.
- **📊 Beautiful Terminal UI**: Powered by `Rich` for a professional, colorful, and easy-to-read dashboard experience.
- **🔒 Type-Safe Core**: Built entirely on **Pydantic V2** with strict immutability (`frozen=True`) to guarantee data integrity.

---

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/VeraLynnDeGraw/CODERWEAVER2.git
cd CODERWEAVER2
```

### 2. Create a Virtual Environment (Recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

### 3. Install the Package
```bash
pip install -e .
```
*(The `-e` flag installs it in "editable" mode, so the `codeweaver` command becomes available globally in your environment).*

---

## 🎯 Quick Start

### The Interactive Menu
Simply run the tool without arguments to launch the beautiful interactive TUI:
```bash
codeweaver
```

### Direct CLI Commands
Prefer the command line? Use these directly:

```bash
# 🔍 Quick health check of the current directory
codeweaver scan . --quick

# 📦 Check what dependencies are needed to run a downloaded project
codeweaver runtime ./downloaded-app

# 🛡️ Audit a suspicious or untrusted directory for security risks
codeweaver safety ~/Downloads/mystery-script

# 🖱️ List available fixes and open one in Cursor
codeweaver cursor --list
codeweaver cursor prop-001
```

---

## 📖 Command Reference

| Command | Description | Key Options |
| :--- | :--- | :--- |
| **`scan`** | Analyze code quality & generate proposals | `--quick`, `--deep`, `--export markdown` |
| **`runtime`** | Check dependencies & environment setup | `--install` (auto-install missing deps) |
| **`safety`** | Security audit for untrusted code | `--sandbox` (run in isolated mode) |
| **`cursor`** | View and apply proposals in Cursor IDE | `--list`, `--apply`, `--dry-run` |

---

## 📂 Project Structure

```text
CODERWEAVER2/
├── src/codeweaver2/
│   ├── __init__.py          # Package initialization
│   ├── cli.py               # Main Click entry point & interactive menu
│   ├── models.py            # Pydantic V2 data models (Immutable & Typed)
│   └── commands/            # Core command implementations
│       ├── scan.py
│       ├── runtime.py
│       ├── safety.py
│       └── cursor.py
├── tests/                   # Unit and integration tests
├── pyproject.toml           # Modern Python packaging configuration
├── README.md                # You are here!
└── .gitignore               # Git ignore rules
```

---

## 🛠️ Development & Testing

To run the test suite (once tests are added):
```bash
pytest tests/ -v
```

To check code formatting and linting:
```bash
ruff check src/
ruff format src/
```

---

## 👩‍💻 Author & Contact

Built with ❤️ by **Vera Lynn DeGraw**

- 🐙 **GitHub**: [VeraLynnDeGraw](https://github.com/VeraLynnDeGraw)
- 📧 **Email**: [veralynndegraw10011@proton.me](mailto:veralynndegraw10011@proton.me)
- 💬 **Discord**: `veralynndegraw10011`

---

## 📝 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

> *"Code is like humor. When you have to explain it, it’s bad."* – Cory House
```

