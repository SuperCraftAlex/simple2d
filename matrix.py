from main import mty,pixel,height,width, vector
from api import *
import numpy as np

_color = color
_mty = mty
_pixel = pixel
_width = width
_height = height

def tuple2color(_i):
    i = _i
    try:
        return color(i[0],i[1],i[2])
    except:
        if i > 120:
            return mty
        if i < 120:
            return color(255,255,255)

def convert0toMTY(matrix):
    x = 0
    for ex in matrix:
        y = 0
        for ey in ex:
            if ey == 0:
                matrix[x][y] = mty
            y+=1
        x+=1

    return matrix

def tuplelist2matrix(_l, dim):
    l = list(_l)

    matrix = [[]]
    #matrix = emptymatrix(dim[1], dim[0])

    ix = 0
    iy = 0

    for e in l:
        matrix[-1].append(tuple2color(e))
        ix += 1
        if(ix >= dim[0]):
            ix = 0
            iy += 1
            matrix.append([])
    
    return matrix

def putpixel(_matrix, x, y, c: color):
    matrix = _matrix

    matrix[x][y] = c

    return matrix

def getdimensions(matrix):
    sx = len(list(matrix))
    sy = len(list(matrix)[0])
    return (sx,sy)

def isEmptyColum(c):
    if mty in c or 0 in c:
        return True
    return False

def compactize(matrix):
    offX = 0
    offY = 0
    width = len(matrix[0])
    height = len(matrix)

    # Find the offset for empty columns
    for i in range(width):
        empty = True
        for j in range(height):
            if matrix[j][i] != mty:
                empty = False
                break
        if empty:
            offX += 1
        else:
            break
    
    # Find the offset for empty rows
    for i in range(height):
        empty = True
        for j in range(width):
            if matrix[i][j] != mty:
                empty = False
                break
        if empty:
            offY += 1
        else:
            break
    
    # Cut the matrix
    matrix = [row[offX:] for row in matrix[offY:]]

    return matrix, offX, offY

#def compactizeTop(matrix):
#    offX = 0
#
#    for c in matrix:
#        if not isEmptyColum(c):
#            break
#        offX+=1
#
#    return matrix[offX:], offX
#
#def compactizeLeftSlow(matrix):
#    m = rot90(matrix)
#    m,o = compactizeTop(m)
#    m = rot90(m)
#    m = rot90(m)
#    m = rot90(m)
#    return m,o

def rot90(matrix):
    d = getdimensions(matrix)
    nmatrix = emptymatrix(d[1], d[0])

    x = 0
    for ex in matrix:
        y = 0
        for ey in ex:
            nmatrix[y][x] = ey
            y+=1
        x+=1
    
    return nmatrix

def selection(matrix, v0: vector, v1:vector):
    return [row[v0.y:v1.y] for row in matrix[v0.x:v1.x]]

def maxdimensions(a, b):
    da = getdimensions(a)
    db = getdimensions(b)

    mx = max(da[0], db[0])
    my = max(da[1], db[1])

    return [mx,my]

def maxdimensionsoff(a, aoffx, aoffy, b, boffx, boffy):
    da = getdimensions(a)
    db = getdimensions(b)

    mx = max(da[0]+aoffx, db[0]+boffx)
    my = max(da[1]+boffy, db[1]+aoffy)

    return [mx,my]

def overlaymatrix(matrix2, matrix1): # lays matrix2 over matrix1
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    if rows1 < rows2 or cols1 < cols2:
        matrix1 = [[0 for _ in range(cols2)] for _ in range(rows2)]
    
    for i in range(rows2):
        for j in range(cols2):
            matrix1[i][j] = matrix2[i][j]
    
    return matrix1

def isblank(p):
    if p == mty or p == 0:
        return True
    try:
        if p.r == 0 and p.g == 0 and p.b == 0:
            return True
    except: pass
    return False

def internal_looptrough(matrix, funct):
    a,b = getdimensions(matrix)

    for row in range(a):
        for col in range(b):
            funct(row, col)

def overlaymatrixoff(matrix1, matrix2, offx, offy):
    d = maxdimensionsoff(matrix1, offx, offy, matrix2, 0, 0)
    m = emptymatrix(d[0], d[1])

    def l(row,col):
        try:
                m[row][col] = matrix2[row][col]
        except: pass
        try:
            if not isblank(matrix1[row][col]):
                m[row+offx][col+offy] = matrix1[row][col]
        except: pass

    internal_looptrough(m, l)

    return m

def cloneempty(matrix):
    d = getdimensions(matrix)
    return emptymatrix(d[0], d[1])

def colorize(_matrix, to):
    matrix = _matrix

    cx = 0
    for i in matrix:
        cy = 0
        for j in i:
            if matrix[cx][cy] == 1:
                matrix[cx][cy] = to
            else:
                try:
                    matrix[cx][cy].r
                except:
                    matrix[cx][cy] = mty
            cy += 1
        cx += 1
    return matrix

def renderline(l, ox, oy):
    x = 0
    for e in l:
        pixel(x+ox,oy,e)
        x+=1

def renderlinetransp(l, ox, oy):
    x = 0
    for e in l:
        if (not e == mty )and (not e == 0):
            pixel(x+ox,oy,e)
        x+=1

def rendermatrixoff(matrix, offx, offy):
    y = 0
    for l in matrix:
        renderline(l, offx, y+offy)
        y += 1

def rendermatrixofftransparent(matrix, offx, offy):
    y = 0
    for l in matrix:
        renderlinetransp(l, offx, y+offy)
        y += 1

def rendermatrix(matrix):
    y = 0
    for l in matrix:
        renderline(l, 0, y)
        y += 1

def rendermatrixtransparent(matrix):
    y = 0
    for l in matrix:
        renderlinetransp(l, 0, y)
        y += 1

def tuplemax(arr, index):
    max = 0
    for i in arr:
        e = i[index]
        if e > max:
            max = e
    return max

def emptymatrix(dx, dy):
    matrix = []

    for x in range(dx):
        matrix.append([])
        for y in range(dy):
            matrix[-1].append(0)

    return matrix

def bresenhamtomatrix(_ni, c: color):
    ni = list(_ni)

    ml = emptymatrix(tuplemax(ni, 0)+1, tuplemax(ni, 1)+1)

    for i in ni:
        ml = putpixel(ml, i[0], i[1], c)

    return ml