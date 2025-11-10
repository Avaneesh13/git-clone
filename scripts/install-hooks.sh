#!/bin/bash

# Script to install git hooks

echo "Installing git hooks..."

# Copy pre-push hook
cp scripts/pre-push .git/hooks/pre-push
chmod +x .git/hooks/pre-push

echo "✅ Git hooks installed successfully!"
echo ""
echo "The following checks will run before each push:"
echo "  - Pyflakes (code errors)"
echo "  - Poetry lock file validation"
echo "  - Black formatting"
echo "  - Mypy type checking"
