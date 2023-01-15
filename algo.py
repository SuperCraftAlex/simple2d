import matrix as mx
from main import mty, vector, color
import math
import numpy as np

def avrg(values):
  return sum(values)/len(values)

def scale(matrix, scale_x, scale_y):
    # Get the dimensions of the input matrix
    rows = len(matrix)
    cols = len(matrix[0])
    # Initialize the new, scaled matrix
    new_rows = int(rows * scale_x)
    new_cols = int(cols * scale_y)
    new_matrix = [[0 for _ in range(new_cols)] for _ in range(new_rows)]
    # Iterate through the new matrix
    for i in range(new_rows):
        for j in range(new_cols):
            # Get the corresponding pixel from the original matrix
            x = int(i / scale_x)
            y = int(j / scale_y)
            if x < rows and y < cols:
                try:
                    new_matrix[i][j] = matrix[x][y]
                except:
                    pass
    return new_matrix

def rotate(testmatrix, angle):
    # Get the width and height of the matrix
    height = len(testmatrix)
    width = len(testmatrix[0])

    # Convert the angle to radians
    angle_rad = math.radians(angle)

    # Create the rotation matrix
    rotation_matrix = [
        [math.cos(angle_rad), -math.sin(angle_rad)],
        [math.sin(angle_rad), math.cos(angle_rad)],
    ]

    # Transform the matrix using the rotation matrix
    rotated_matrix = [[mty for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            new_x, new_y = rotation_matrix[0][0] * x + rotation_matrix[0][1] * y, rotation_matrix[1][0] * x + rotation_matrix[1][1] * y
            new_x, new_y = int(new_x + width / 2), int(new_y + height / 2)
            if new_x >= width or new_y >= height or new_x < 0 or new_y < 0:
                continue
            try:
                rotated_matrix[new_x][new_y] = testmatrix[x][y]
            except IndexError:
                pass
    return rotated_matrix

# B R O K E N !!!!!!!!!!!!!
def flood_fill(_matrix, x ,y, new):
    matrix = mx.convert0toMTY(_matrix)

    omatrix = mx.cloneempty(matrix)

    def rec(x, y, new):
        # we need the x and y of the start position, the old value,
        # and the new value
        # the flood fill has 4 parts
        # firstly, make sure the x and y are inbounds
        if y < 0 or y >= len(matrix[0]) or x < 0 or x >= len(matrix):
            return
        # secondly, check if the current position equals the old value
        if matrix[y][x] != mty:
            return

        # thirdly, set the current position to the new value
        omatrix[y][x] = new
        # fourthly, attempt to fill the neighboring positions
        rec(x+1, y, new)
        rec(x-1, y, new)
        rec(x, y+1, new)
        rec(x, y-1, new)

    rec(x, y, new)

    return omatrix