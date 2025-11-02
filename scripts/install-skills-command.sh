#!/bin/bash

# Install the /skills slash command and list-skills utility

# Get the script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Create target directories if they don't exist
mkdir -p "$HOME/.claude/commands"
mkdir -p "$HOME/bin"

# Copy the skills command to .claude/commands
cp "$PROJECT_ROOT/commands/skills.md" "$HOME/.claude/commands/"
echo "✓ Installed: ~/.claude/commands/skills.md"

# Copy list-skills.sh to ~/bin and make it executable
cp "$PROJECT_ROOT/scripts/list-skills.sh" "$HOME/bin/"
chmod +x "$HOME/bin/list-skills.sh"
echo "✓ Installed: ~/bin/list-skills.sh"

echo ""
echo "Installation complete!"
echo ""
echo "To add ~/bin to your PATH, add this line to your shell config:"
echo ""
echo "  export PATH=\"\$HOME/bin:\$PATH\""
echo ""
echo "Add it to:"
echo "  - ~/.bashrc (for Bash)"
echo "  - ~/.zshrc (for Zsh)"
echo "  - ~/.config/fish/config.fish (for Fish)"
echo ""
echo "Then run: source ~/.bashrc  (or your shell's config file)"
