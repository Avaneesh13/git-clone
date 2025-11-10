#!/bin/bash

# Script to configure git to use custom hooks directory

echo "Configuring git hooks..."

# Set git hooks path to scripts/hooks directory
git config core.hooksPath scripts/hooks

echo "✅ Git hooks configured successfully!"
echo ""
echo "Git will now use hooks from scripts/hooks/ directory"
echo ""
echo "The following checks will run before each push:"
echo "  - Pyflakes (code errors)"
echo "  - Poetry lock file validation"
echo "  - Black formatting"
echo "  - Mypy type checking"
