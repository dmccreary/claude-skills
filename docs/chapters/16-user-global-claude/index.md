# User Global Claude

There are specific instructions that Claude needs for ALL the
intelligent textbook projects on each computer you use.  These go in
a file in the users $HOME directory:

`$HOME/.claude/CLAUDE.md`

## Projects Directory

This tells Claude where you clone your github projects:

`PROJECTS_HOME=$HOME/projects`

You need to be in this directory when you clone a new github repository.

## Default License

When you create any new textbook, what License should you use?

- **License**: Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0)

## Claude Skill Repo

`cd ~/Documents/ws/claude-skills; git pull`


## P5.js rules

### P5.js Controls

- for p5.js MicroSims, ALWAYS use the p5.js builtin controls.  Never draw them manually.

### Button
`createButton(label)`
Used for actions: reset, start, pause, randomize

### Slider
`createSlider(min, max, value, step)`
Used for continuous parameters: speed, size, probability

### Checkbox
`createCheckbox(label, checked)`
Used for on/off options and feature toggles

### Select (Dropdown)
`createSelect()`
Used for choosing modes, algorithms, datasets

### Input (Text field)
`createInput(value, type)`
Used for numeric or short text input

## P5.js Editor Support

- for p5.js MicroSims, the deployed HTML uses the p5.js editor standard `<main></main>` (no id attribute). This allows teachers to copy and paste the JavaScript file directly into the p5.js editor without modification. In setup(), always parent the canvas with `canvas.parent(document.querySelector('main'));`.  Never add `id="main"` to the HTML `<main>` tag.

