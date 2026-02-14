# Claude Code Skills Tips and Tricks

## Getting Rid of Security Warnings for Git Repository Backed Work

There are two ways to use Claude Code:

1. The **safe way** of only allowing Claude Code to manipulate files within a checked out git repository.  In this case everything is versioned and you can undo even massive changes with a single git comme
2. The dangerous way of allowing Claude to work on files that are not checked into git.

If you are using safe way, you can easily disable all the annoying permission and warnings by just starting up claude like this:

```sh
cd git_hub_project
claude --dangerously-skip-permissions
```

In this mode, claude will not constantly ask for permissions to manipulate files and run commands.  However, that is a **REALLY** long and hard to remember command line option.  The solution is to create a short shell alias like `claude-dsp` so that when you type that, it expands to use the actual long option.

Add this line to your shell startup (.zshrc or .bashrc)

```sh
alias claude-dsp='claude --dangerously-skip-permissions`
```

Remember to source the file after the change:

```sh
source .zshrc
```

Then check your alias:

```sh
alias
```

```sh
claude-dsp='claude --dangerously-skip-permissions'
```

!!! Warning
    Never run `claude-dsp` when you are NOT in a git repository.

## Automatic Visual Studio Save on Change Focus

I often forget to save my editor.  One option is to have it automatically save
whenever you change focus.  To change this in Visual Studio go to the main Code menu and go to the `Settings...` option.  Search for `Auto Save`.

![](./auto-save-focus.png)

This means the file will always save.  If you change your mind you will need to use the `undo` function of your editor.  Just by moving your mouse to the MicroSim page you will get a refresh if `mkdocs serve` is running.


## Fast MicroSim Rendering with the Visual Studio Live Server Extension

After you change a microsim and you want to view it you can run `mkdocs serve` or have it running in a shell.  When you save the system will rerun `mkdocs build`.  This runs in just a second on a small book, but if you have a 500-page book, converting every chapter and all the supplementary materials can take over 10 seconds.

A better option is to have the [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension installed.  This only triggers a server for the single document you are working on, so it renders in just a fraction of a second.  To trigger it just right click over the `main.html` file in the MicroSim and click on the `Open With Live Server` option.

![](./LiveServer.png)

## Customizing p5.js Autocomplete with VSCode

Most code editors can be configured to know the rules of specific libraries.
In VSCode you can configure it to use the rules for editing p5.js code.  There are two steps:

### Load the p5.js Type Library

```sh
npm install --save-dev @types/p5
```

### Add the following to your p5.js code

```js
/// <reference types="p5/global" />
```

## README.md Generator

Although you are limited to about 30 skills, you can also run the following skill
that will create a high-quality README.md file.

`> Please generate a new README.md file by using the readme-generator skill.`

You can also explicitly add the following path if you don't install this skill.

[https://github.com/dmccreary/claude-skills/tree/main/skills/readme-generator](https://github.com/dmccreary/claude-skills/tree/main/skills/readme-generator)

## Windows Arrangement

When I am debugging MicroSims I like to have my Claude shell window on the left, my browser on the right and a small shell window running below Claude running `mkdocs serve`.  That way when I talk to claude and he make changes, I can quickly see the changes on the right side of the screen.  This arrangement also works if I use the Live Server extension, but in that case I have to open VSCode to see the MicroSim quickly.

![](./window-arrangement.png)

## Custom Status Line

```sh
/statusline Model | Directory | Percent Context Window
```                                                                    

Two pieces are needed: a shell script and a settings entry.

  1. Create ~/.claude/statusline-command.sh                      

```sh
#!/bin/bash
input=$(cat)
model=$(echo "$input" | jq -r '.model.display_name')
cwd=$(echo "$input" | jq -r '.workspace.current_dir')
parent=$(basename "$(dirname "$cwd")")
current=$(basename "$cwd")
used=$(echo "$input" | jq -r '.context_window.used_percentage // empty')

if [ -n "$used" ]; then
filled=$(echo "$used" | awk '{printf "%d", $1/5}')
empty=$((20 - filled))
RED='\033[0;31m'
GREEN='\033[0;32m'
RESET='\033[0m'
bar="${RED}"
for i in $(seq 1 $filled); do bar="${bar}░"; done
bar="${bar}${RESET}│${GREEN}"
for i in $(seq 1 $((empty - 1))); do bar="${bar}░"; done
bar="${bar}${RESET}"
printf "%s | 📁 %s/%s | [${bar}] %.0f%%\n" "$model" "$parent" "$current" "$used"
else
printf '%s | 📁 %s/%s\n' "$model" "$parent" "$current"
fi
```

### Make it executable:

```sh
chmod +x ~/.claude/statusline-command.sh
```

2. Add to ~/.claude/settings.json

Add this top-level key (or merge into your existing settings):

```json
{
"statusLine": {
    "type": "command",
    "command": "bash /Users/dan/.claude/statusline-command.sh"
}
}
```