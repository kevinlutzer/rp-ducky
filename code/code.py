import board
import neopixel

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 30

pixels = neopixel.NeoPixel(board.GP16, num_pixels)
pixels.brightness = 0.01

while True:
    pixels.fill((255, 255, 255))

