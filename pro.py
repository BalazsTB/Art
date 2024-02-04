import numpy


import scipy.misc
import numpy as np



WHITE_PIXEL = [255, 255, 255]
BLACK_PIXEL = [0, 0, 0]

# Create a NumPy array
numpy_array_1 = numpy.array([1, 2, 3, 4, 5])
numpy_array_2 = numpy.array([1, 2, 3, 4, 5])
numpy_array_3 = numpy.array([1, 2, 3, 4, 5])

# Convert NumPy array to tuple

result_tuples = list(zip(numpy_array_1, numpy_array_2, numpy_array_3))


def generate_line(length:int) -> list:
    canvas_array = numpy.full((0, length), 255)


    return canvas_array.tolist()



arr = generate_line(10)

print(arr)