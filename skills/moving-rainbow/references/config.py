# Moving Rainbow Configuration file
# This file contains the hardware configuration for your kit
# This file should be imported by each program

# NeoPixel LED strip configuration
NEOPIXEL_PIN = 0      # GPIO pin connected to the NeoPixel data line
NUMBER_PIXELS = 30    # Number of pixels in the LED strip

# Button configuration
BUTTON_PIN_1 = 14     # GPIO pin for button 1 (closer to the edge)
BUTTON_PIN_2 = 15     # GPIO pin for button 2 (closer to the board)

# Usage in your programs:
# import config
# strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)
