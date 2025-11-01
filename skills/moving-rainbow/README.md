# Moving Rainbow MicroPython Skill

A Claude Code skill for generating MicroPython programs for the Moving Rainbow LED strip educational project.

## Overview

This skill enables Claude to generate educational MicroPython programs for the Moving Rainbow project, which uses:
- Raspberry Pi Pico (RP2040 microcontroller)
- NeoPixel/WS2812B addressable LED strips (30 pixels)
- Two momentary push buttons for interactive control

## Hardware Configuration

The default hardware setup:
- **LED Strip**: GPIO pin 0, 30 pixels
- **Button 1**: GPIO pin 14
- **Button 2**: GPIO pin 15

Configuration is managed through a `config.py` file (see `references/config.py`).

## Usage

This skill should be automatically activated when working with:
- LED strip animations for Raspberry Pi Pico
- NeoPixel/WS2812B programming in MicroPython
- Moving Rainbow educational examples
- Button-controlled LED effects

### Example Requests

- "Create a rainbow animation that cycles through colors"
- "Make a comet tail effect with a red color"
- "Generate a program with multiple modes controlled by buttons"
- "Create a candle flicker effect"
- "Build a moving dot animation"

## What This Skill Provides

### Code Patterns
- Standard MicroPython/NeoPixel setup code
- Color wheel function for rainbow effects
- Button interrupt handlers with debouncing
- Common animation patterns (moving dot, color wipe, rainbow cycle, comet tail, etc.)
- Multi-mode program structure

### Educational Guidelines
- Progressive complexity for learning
- Clear, commented code
- Consistent naming conventions
- Adjustable parameters for experimentation

### Reference Materials
- `config.py`: Standard hardware configuration template
- Complete animation function examples
- Button integration patterns
- Color definitions

## File Structure

```
moving-rainbow/
├── SKILL.md                    # Main skill definition and instructions
├── README.md                   # This file
└── references/
    └── config.py              # Hardware configuration reference
```

## Installation

To use this skill with Claude Code:

1. Place the `moving-rainbow` directory in your Claude Code skills folder
2. The skill will automatically activate when you work with Moving Rainbow projects

## Related Resources

- [Moving Rainbow Project Repository](https://github.com/dmccreary/moving-rainbow)
- [MicroPython NeoPixel Documentation](https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html)
- [Raspberry Pi Pico MicroPython Guide](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)

## License

This skill is part of the Moving Rainbow educational project. Refer to the main project repository for licensing information.
