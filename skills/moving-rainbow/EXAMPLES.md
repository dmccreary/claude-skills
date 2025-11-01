# Moving Rainbow Skill - Usage Examples

This document shows examples of how to use the Moving Rainbow skill to generate MicroPython programs.

## Example 1: Simple Moving Dot

**User Request**: "Create a simple program that moves a red dot across the LED strip"

**Generated Code**:
```python
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# Initialize the LED strip
strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

# Define colors
red = (255, 0, 0)

# Erase function
def erase():
    for i in range(0, config.NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    strip.write()

# Clear the strip at startup
erase()

# Main animation loop
counter = 0
while True:
    # Turn on the current pixel
    strip[counter] = red
    strip.write()
    sleep(0.1)

    # Turn off the current pixel
    strip[counter] = (0, 0, 0)

    # Move to next position
    counter += 1
    counter = counter % config.NUMBER_PIXELS
```

## Example 2: Rainbow Cycle

**User Request**: "Create a rainbow cycle animation"

**Generated Code**:
```python
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colors are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def rainbow_cycle(counter, delay):
    percent_color_wheel = round(255 / config.NUMBER_PIXELS)
    for i in range(0, config.NUMBER_PIXELS):
        color_index = round(i * percent_color_wheel)
        color = wheel(color_index)
        strip[(i + counter) % config.NUMBER_PIXELS] = color
        strip.write()
    sleep(delay)

counter = 0
while True:
    rainbow_cycle(counter, 0.05)
    counter += 1
    counter = counter % config.NUMBER_PIXELS
```

## Example 3: Multi-Mode Program with Buttons

**User Request**: "Create a program with three modes: red dot, blue dot, and rainbow. Use buttons to switch modes."

**Generated Code**:
```python
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

# Button setup
button1 = Pin(config.BUTTON_PIN_1, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(config.BUTTON_PIN_2, Pin.IN, Pin.PULL_DOWN)

last_time = 0
mode = 0
mode_list = ['red dot', 'blue dot', 'rainbow']
mode_count = len(mode_list)

# Colors
red = (255, 0, 0)
blue = (0, 0, 255)

def button_pressed_handler(pin):
    global mode, last_time
    new_time = ticks_ms()
    if (new_time - last_time) > 200:
        pin_num = int(str(pin)[4:6])
        if pin_num == config.BUTTON_PIN_1:
            mode += 1
        else:
            mode -= 1
        mode = mode % mode_count
        last_time = new_time
        print('Switched to mode:', mode_list[mode])

button1.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed_handler)
button2.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed_handler)

def wheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def move_dot(counter, color, delay):
    strip[counter] = color
    strip.write()
    sleep(delay)
    strip[counter] = (0, 0, 0)

def rainbow_cycle(counter, delay):
    percent_color_wheel = round(255 / config.NUMBER_PIXELS)
    for i in range(0, config.NUMBER_PIXELS):
        color_index = round(i * percent_color_wheel)
        color = wheel(color_index)
        strip[(i + counter) % config.NUMBER_PIXELS] = color
    strip.write()
    sleep(delay)

counter = 0
last_mode = -1

while True:
    if mode != last_mode:
        print('Running mode:', mode_list[mode])
        last_mode = mode

    if mode == 0:
        move_dot(counter, red, 0.05)
    elif mode == 1:
        move_dot(counter, blue, 0.05)
    elif mode == 2:
        rainbow_cycle(counter, 0.05)

    counter += 1
    counter = counter % config.NUMBER_PIXELS
```

## Example 4: Comet Tail Effect

**User Request**: "Create a comet tail effect with a green comet"

**Generated Code**:
```python
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

# Green color
green = (0, 255, 0)

# Brightness levels for the tail
levels = [255, 128, 64, 32, 16, 8, 4, 2, 1]
level_count = len(levels)

def comet_tail(counter, color, delay):
    for i in range(0, level_count):
        # Calculate position for each segment of the tail
        target = (counter - i) % config.NUMBER_PIXELS

        # Scale the color by the brightness level
        scale = levels[i] / 255
        scaled_color = (int(color[0]*scale), int(color[1]*scale), int(color[2]*scale))
        strip[target] = scaled_color

    strip.write()

    # Erase the last pixel of the tail
    erase_pos = (counter - level_count) % config.NUMBER_PIXELS
    strip[erase_pos] = (0, 0, 0)

    sleep(delay)

counter = 0
while True:
    comet_tail(counter, green, 0.02)
    counter += 1
    counter = counter % config.NUMBER_PIXELS
```

## Testing Your Programs

1. Save the generated code to a `.py` file on your Raspberry Pi Pico
2. Ensure you have a `config.py` file with the hardware configuration
3. Reset the Pico to run the program
4. Use Thonny or another IDE to monitor serial output for debugging

## Tips for Using the Skill

- Be specific about colors, speeds, and effects you want
- Mention if you want button controls
- Specify if you need multiple modes or a single animation
- Ask for explanations if you want to learn how the code works
- Request modifications to timing, colors, or patterns as needed
