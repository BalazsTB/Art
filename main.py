from PIL import Image
import random
import scipy
import numpy
import time
from itertools import chain

WHITE_PIXEL = [255, 255, 255]
BLACK_PIXEL = [0, 0, 0]


width = 640
height = 480
image_size = (width, height)

#pixel_sql = [(255,0,0), (0,255,0), (0,0,255)]



def generate_random_colours_pixel_by_pixel(image_size:list) -> list:

    start_time = time.time()

    number_of_pixels = image_size[0] * image_size[1]

    list_of_all_pixels = []
    pixel_rgb_values = []

    for x in range(number_of_pixels):
        red_val = random.randint(0, 255)
        green_val = random.randint(0, 255)
        blue_val = random.randint(0, 255)

        pixel_rgb_values = [red_val, green_val, blue_val]

        list_of_all_pixels.append(tuple(pixel_rgb_values))

    end_time = time.time()
    print(f"""
            generate_random_colours_pixel_by_pixel
            Time taken to execute: {end_time - start_time} seconds
        """)


    return list_of_all_pixels

def generate_random_colours_pixel_by_pixel_numpy(image_size:list) -> list:

    start_time = time.time()

    number_of_pixels = image_size[0] * image_size[1]

    array_of_pixels_red = numpy.random.randint(0, 255, number_of_pixels)
    array_of_pixels_blue = numpy.random.randint(0, 255, number_of_pixels)
    array_of_pixels_green = numpy.random.randint(0, 255, number_of_pixels)

    list_of_all_pixels = list(zip(array_of_pixels_red, array_of_pixels_blue, array_of_pixels_green))

    end_time = time.time()
    print(f"""
            generate_random_colours_pixel_by_pixel_numpy
            Time taken to execute: {end_time - start_time} seconds
        """)

    return list_of_all_pixels


def generate_line(length:int) -> list:
    canvas_array = numpy.full((0, length), WHITE_PIXEL)


    return


def draw_circle():
    # Image size
    width = 640
    height = 480
    channels = 3

    # Create an empty image
    img = numpy.zeros((height, width, channels), dtype=numpy.uint8)

    # Draw something (http://stackoverflow.com/a/10032271/562769)
    xx, yy = numpy.mgrid[:height, :width]
    circle = (xx - 100) ** 2 + (yy - 100) ** 2

    # Set the RGB values
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            r, g, b = circle[y][x], circle[y][x], circle[y][x]
            img[y][x][0] = r
            img[y][x][1] = g
            img[y][x][2] = b

    tuple_of_tuples = tuple(tuple(row) for row in img.tolist())
    
    flattened_list = tuple(chain.from_iterable(tuple_of_tuples))

    return img


a = draw_circle()
image = Image.fromarray(a)
image.show()



img  = Image.new( mode = "RGB", size = image_size )
pixel_sq = generate_random_colours_pixel_by_pixel_numpy(image_size)

img.putdata(pixel_sq)
img.show()