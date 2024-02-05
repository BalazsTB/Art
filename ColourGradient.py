from dataclasses import dataclass
from PIL import Image
import random
import scipy
import numpy
import time
from itertools import chain


@dataclass
class RGB:
    Red:int
    Blue:int
    Green:int

@dataclass
class ImageSize:
    Width:int
    Height:int

class ColourGradient:

    def CreateColourGradient(self, Colour:RGB, ImageSize:ImageSize, Magnitude:int) -> numpy.array:
        start_time = time.time()

        # Create an empty image, i.e: an array of zeros.
        canvas = numpy.zeros((ImageSize.Height, ImageSize.Width, 3), dtype=numpy.uint8)

        red = 0
        blue = 0
        green = 0

        # Set the RGB values
        for y in range(canvas.shape[0]):
            if (red <= Colour.Red): 
                red = red + Magnitude
            if (green <= Colour.Green): 
                green = green + Magnitude
            if (blue <= Colour.Blue): 
                blue = blue + Magnitude

            for x in range(canvas.shape[1]):
                canvas[y][x][0] = red
                canvas[y][x][1] = green
                canvas[y][x][2] = blue

        end_time = time.time()
        print(f"""
                CreateColourGradient
                Time taken to execute: {end_time - start_time} seconds
            """)

        return canvas


col = ColourGradient
myColour = RGB(255, 0, 0)
mySize = ImageSize(255,255)

a = col.CreateColourGradient(col, myColour, mySize, 1)


image = Image.fromarray(a)
image.show()