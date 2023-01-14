from main import color,mty,pixel,height,width

_color = color
_mty = mty
_pixel = pixel
_width = width
_height = height

def tuplelist2matrix(_l, dim):
    l = list(_l)

    matrix = emptymatrix(dim[1], dim[0])

    ix = 0
    iy = 0
    for e in l:
        matrix[iy][ix] = tuple2color(e)
        ix += 1

        if(ix >= dim[0]):
            ix = 0
            iy += 1
    
    return matrix

def tuple2color(i):
    return color(i[0],i[1],i[2])

def emptymatrix(dx, dy):
    matrix = [[mty]*dy]*dx

    return matrix

def putpixel(_matrix, x, y, c: color):
    matrix = _matrix

    matrix[x][y] = c

    return matrix

def getdimensions(matrix):
    sx = len(list(matrix))
    sy = len(list(matrix)[0])
    return (sx,sy)

def overlaymatrix(a, b, igc: color):
    x = 0
    for ex in a:
        y = 0
        for ey in ex:
            if not ey == igc:
                b[x][y] = ey
            y+=1
        x+=1
    return b

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

def rendermatrixoff(_matrix, offx, offy):
    matrix = _matrix
    x = 0
    for ex in matrix:
        y = 0
        for ey in ex:
            pixel(y+offx,x+offy,ey)
            y+=1
        x+=1

def rendermatrix(_matrix):
    matrix = _matrix
    x = 0
    for ex in matrix:
        y = 0
        for ey in ex:
            pixel(y,x,ey)
            y+=1
        x+=1

def bresenhamtomatrix(ni, c: color):
    ml = []
    cx = 0
    for ix in range(width):
        cy = 0
        ml.append([])
        for iy in range(height):
            ml[len(ml)-1].append(mty)
            for i in list(ni):
                if i[0] == cx and i[1] == cy:
                    ml[len(ml)-1][len(ml[len(ml)-1])-1] = c
            cy += 1
        cx +=1

    return ml
