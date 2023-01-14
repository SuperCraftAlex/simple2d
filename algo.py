import matrix as mx
import numpy as np
import random

def flood_recursive(matrix):
    width = len(matrix)
    height = len(matrix[0])
    def fill(x,y,start_color,color_to_update):
        #if the square is not the same color as the starting point
        if matrix[x][y] != start_color:
            return
        #if the square is not the new color
        elif matrix[x][y] == color_to_update:
            return
        else:
            #update the color of the current square to the replacement color
            matrix[x][y] = color_to_update
            neighbors = [(x-1,y),(x+1,y),(x-1,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x,y-1),(x,y+1)]
            for n in neighbors:
                if 0 <= n[0] <= width-1 and 0 <= n[1] <= height-1:
                    fill(n[0],n[1],start_color,color_to_update)
    #pick a random starting point
    start_x = random.randint(0,width-1)
    start_y = random.randint(0,height-1)
    start_color = matrix[start_x][start_y]
    fill(start_x,start_y,start_color,9)
    return matrix