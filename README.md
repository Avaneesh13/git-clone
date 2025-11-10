# Git Clone Implementation

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An educational implementation of Git's core functionality in Python. This project helps developers understand version control system internals by building a simplified Git clone from scratch.

## Features

- 📦 Repository initialization and management
- 📝 File staging and commit creation
- 📊 Repository status tracking
- 📜 Commit history viewing
- 💾 Stash functionality for temporary changes
- ⏮️ Soft and hard reset operations
- 🔐 SHA-256 content-addressable storage
- 🗜️ Object compression with zlib

## Why This Project?

Understanding how Git works under the hood makes you a better developer. This implementation:
- Demonstrates core version control concepts
- Shows how content-addressable storage works
- Explains the DAG (Directed Acyclic Graph) structure of commits
- Provides a learning resource for Git internals

## Prerequisites

- Python 3.9 or higher
- Poetry package manager

## Installation

### For Users

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/gitclone.git
cd gitclone

# Install with Poetry
poetry install

# Run the CLI
poetry run gitclone --help
```

### For Development

```bash
# Clone and install with dev dependencies
git clone https://github.com/YOUR_USERNAME/gitclone.git
cd gitclone
poetry install

# Configure git to use version-controlled hooks
bash scripts/install-hooks.sh
```

## Usage

```bash
# Initialize a repository
gitclone init

# Add files to staging
gitclone add <files>

# Create a commit
gitclone commit -m "message"

# View status
gitclone status

# View commit history
gitclone log

# Stash changes
gitclone stash save -m "message"
gitclone stash apply
gitclone stash list

# Reset repository
gitclone reset <commit> --soft
gitclone reset <commit> --hard
```

## Development Tools

### Git Hooks
The project uses version-controlled git hooks in `scripts/hooks/` that automatically check code quality before pushing:
- **Pyflakes**: Checks for code errors
- **Poetry lock**: Validates poetry.lock is up to date
- **Black**: Ensures code formatting
- **Mypy**: Runs type checking

Configure git to use these hooks:
```bash
bash scripts/install-hooks.sh
```

This sets `core.hooksPath` to `scripts/hooks/`, so hooks are version-controlled and automatically updated.

### Code Formatting
```bash
# Format code with Black
poetry run black src/ tests/

# Check formatting without changes
poetry run black --check src/ tests/
```

### Linting
```bash
# Check for code errors
poetry run pyflakes src/ tests/
```

### Testing
```bash
poetry run pytest
```

### Type Checking
```bash
poetry run mypy src/
```

## Project Structure

```
gitclone/
├── src/
│   └── gitclone/
│       ├── __init__.py
│       ├── cli.py           # Command-line interface
│       ├── interfaces.py    # Abstract base classes
│       └── errors.py        # Error handling
├── tests/                   # Test suite
├── scripts/
│   ├── hooks/              # Version-controlled git hooks
│   │   └── pre-push        # Pre-push quality checks
│   └── install-hooks.sh    # Configure git hooks path
├── pyproject.toml          # Project configuration
└── README.md
```

## How It Works

This implementation follows Git's core architecture:

1. **Content-Addressable Storage**: Files are stored as objects identified by SHA-256 hashes
2. **Three Object Types**: Blobs (file content), Trees (directory structure), Commits (snapshots)
3. **Staging Area**: An index that tracks files ready for commit
4. **DAG Structure**: Commits form a directed acyclic graph through parent references

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Learning Resources

- [Git Internals - Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)
- [Git from the Bottom Up](https://jwiegley.github.io/git-from-the-bottom-up/)
- [Understanding Git Conceptually](https://www.sbf5.com/~cduan/technical/git/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the original Git implementation by Linus Torvalds
- Built as an educational project to understand version control internals

## Author

**Avaneesh Singh**
- GitHub: [@YOUR_GITHUB_USERNAME](https://github.com/YOUR_GITHUB_USERNAME)
- Email: avaneeshsingh242@gmail.com
