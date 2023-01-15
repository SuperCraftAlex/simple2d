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

def fill(matrix, x, y, color):
    start_color = matrix[x][y]
    if start_color == color:
        return matrix
    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)
        if matrix[x][y] == start_color:
            matrix[x][y] = color
            if x > 0:
                queue.append((x-1, y))
            if x < len(matrix)-1:
                queue.append((x+1, y))
            if y > 0:
                queue.append((x, y-1))
            if y < len(matrix[0])-1:
                queue.append((x, y+1))
    return matrix
