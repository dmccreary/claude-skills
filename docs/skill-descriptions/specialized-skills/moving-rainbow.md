# Moving Rainbow MicroPython Generator

## Overview

The moving-rainbow skill generates MicroPython programs for the Moving Rainbow educational project using Raspberry Pi Pico with NeoPixel LED strips and button controls. It creates programs for LED animations that are both educational and visually engaging.

## Purpose

This skill helps educators and students create MicroPython programs for LED strip animations on Raspberry Pi Pico microcontrollers, focusing on educational patterns and interactive control through physical buttons.

## Hardware Configuration

Default hardware setup:
- **Microcontroller**: Raspberry Pi Pico (RP2040)
- **LED Strip**: 30-pixel NeoPixel/WS2812B addressable LED strip connected to GPIO pin 0
- **Input Controls**: Two momentary push buttons
  - Button 1: GPIO pin 14
  - Button 2: GPIO pin 15
- **Built-in LED**: GPIO pin 25 (status indication)

Configuration values stored in `config.py` module.

## Key Features

- **Educational Code Patterns**: Clear, well-commented code for learning
- **Interactive Controls**: Button-based mode switching and parameter adjustment
- **Animation Library**: Pre-built patterns (rainbow, comet, sparkle, etc.)
- **Color Management**: Standard color wheel function for smooth transitions
- **Modular Design**: Reusable functions for common operations

## When to Use

Use this skill when users ask to:
- Create LED animations for Raspberry Pi Pico
- Work with NeoPixel/WS2812B addressable LED strips
- Build educational examples for Moving Rainbow project
- Implement button-controlled LED effects
- Generate MicroPython code for LED strip projects

## Common Animation Patterns

### Moving Dot
Single LED moving along the strip with configurable color and speed

### Rainbow Cycle
Full rainbow pattern that rotates through the strip

### Comet Tail
LED with fading tail effect simulating a comet

### Color Wipe
Progressive fill of strip with a color

### Random Effects
Random pixel positions and colors with sparkle effects

### Candle Flicker
Simulates flickering candle flame effect

## Code Structure

### Basic Program Template

```python
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# Initialize LED strip
strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

# Animation code

while True:
    # Main loop
    pass
```

### Essential Components

1. **Imports**: machine, neopixel, utime, config
2. **Strip Initialization**: NeoPixel object creation
3. **Main Loop**: while True loop for continuous animations
4. **Color Format**: RGB tuples (red, green, blue) with values 0-255

## Color Wheel Function

Standard function for smooth rainbow transitions:

```python
def wheel(pos):
    # Input 0-255 to get color value
    # Returns r-g-b transition
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)
```

## Button Integration

Interactive programs with button controls:

```python
from machine import Pin
from utime import ticks_ms
import config

button1 = Pin(config.BUTTON_PIN_1, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(config.BUTTON_PIN_2, Pin.IN, Pin.PULL_DOWN)

last_time = 0

def button_pressed_handler(pin):
    global mode, last_time
    new_time = ticks_ms()
    # Debounce: require 200ms between presses
    if (new_time - last_time) > 200:
        # Handle button action
        last_time = new_time

# Register interrupt handlers
button1.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed_handler)
button2.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed_handler)
```

## Multi-Mode Programs

Programs with multiple animation modes switchable via buttons:

```python
mode_list = ['moving rainbow', 'red dot', 'blue dot', 'candle flicker', 'random']
mode_count = len(mode_list)
mode = 0
counter = 0

while True:
    # Execute current mode
    if mode == 0:
        moving_rainbow(counter, 0.05)
    elif mode == 1:
        move_dot(counter, red, 0.05)
    # ... more modes

    counter += 1
    counter = counter % config.NUMBER_PIXELS
```

## Standard Color Definitions

Pre-defined color constants:

```python
red = (255, 0, 0)
orange = (255, 60, 0)
yellow = (255, 150, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)
white = (128, 128, 128)
off = (0, 0, 0)
```

## Educational Principles

When generating programs:

1. **Progressive Complexity**: Start simple, add features incrementally
2. **Clear Comments**: Explain what each section does
3. **Consistent Naming**: Use descriptive variable names
4. **Visible Feedback**: Use print statements to show what's happening
5. **Adjustable Parameters**: Use constants for easy experimentation

## Best Practices

1. **Always call `strip.write()`** after modifying pixels
2. **Use modulo for wrapping**: `counter % config.NUMBER_PIXELS` to loop animations
3. **Debounce buttons**: Check 200ms has passed between button presses
4. **Import config**: Always use `import config` and reference configuration constants
5. **Add delays**: Include `sleep()` calls to control animation speed
6. **Clear pixels**: Turn off pixels when moving animations to prevent trails
7. **Test boundary conditions**: Ensure animations work at pixel 0 and last pixel

## Common Functions

### Erase Strip
```python
def erase():
    for i in range(0, config.NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    strip.write()
```

### Setting Pixels
```python
strip[index] = (red_value, green_value, blue_value)
strip.write()  # Always call write() to display changes
```

### Using Counter with Modulo
```python
counter = 0
while True:
    strip[counter] = color
    strip.write()
    sleep(delay)

    counter += 1
    counter = counter % config.NUMBER_PIXELS  # Wrap around
```

## Educational Applications

- **Physical Computing**: Understanding microcontroller I/O
- **Color Theory**: RGB color mixing and perception
- **Animation Basics**: Frame-by-frame updates and timing
- **Event Handling**: Button interrupts and debouncing
- **State Machines**: Mode switching and program flow
- **Arrays and Iteration**: Working with pixel arrays
- **Modular Programming**: Breaking code into functions

## Output Format

Generated programs:
- Are complete, runnable MicroPython code
- Include necessary imports
- Use config module for hardware settings
- Include helpful comments
- Follow established code patterns
- Are educational and easy to understand

## Integration

Works well for:
- **STEM Education**: Hands-on electronics and programming
- **Maker Projects**: Interactive LED displays
- **Computer Science**: Teaching loops, arrays, and functions
- **Art/Design**: Creating visual effects and patterns
- **Project-Based Learning**: Complete working projects

## Technical Requirements

- Raspberry Pi Pico or compatible RP2040 board
- MicroPython firmware installed
- 30-pixel WS2812B/NeoPixel LED strip (5V)
- Two momentary push buttons
- Adequate power supply for LED strip (typically 2-5A)

## References

- MicroPython Documentation: https://docs.micropython.org/
- Raspberry Pi Pico: https://www.raspberrypi.com/documentation/microcontrollers/
- NeoPixel Guide: https://learn.adafruit.com/adafruit-neopixel-uberguide
- WS2812B Datasheet: Standard addressable RGB LED specifications
