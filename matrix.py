from main import color,mty,pixel,height,width, vector
import numpy as np

_color = color
_mty = mty
_pixel = pixel
_width = width
_height = height

def tuple2color(_i):
    i = _i
    return color(i[0],i[1],i[2])

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

def compactizeTop(matrix):
    offX = 0

    for c in matrix:
        if not isEmptyColum(c):
            break
        offX+=1

    return matrix[offX:], offX

def compactizeLeft(matrix):
    # TODO
    return matrix

def selection(matrix, v0: vector, v1:vector):
    nmatrix = cloneempty(matrix)

    x = 0
    for ex in matrix:
        y = 0
        for ey in ex:
            if x >= v0.x and x <= v1.x:
                if y >= v0.y and y <= v1.y:
                    nmatrix[ x - v0.x ][ y - v0.y ] = ey
            y+=1
        x+=1

    return nmatrix

def maxdimensions(a, b):
    da = getdimensions(a)
    db = getdimensions(b)

    mx = max(da[0], db[0])
    my = max(da[1], db[1])

    return [mx,my]

def overlaymatrix(a, b):
    d = maxdimensions(a,b)
    nm = emptymatrix(d[0], d[1])

    x = 0
    for ex in a:
        y = 0
        for ey in ex:
            if not (ey == mty or ey == 0):
                nm[x][y] = ey
            else:
                try:
                    nm[x][y] = b[x][y]
                except: pass
            y+=1
        x+=1

    return nm

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