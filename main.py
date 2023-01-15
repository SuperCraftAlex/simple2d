import sys, pygame
import random, time
import numpy as np
from bresenham import bresenham
import algo
import matrix as mx
from PIL import Image
import font

width, height = 1000, 1000

if __name__ == "__main__":
    pygame.init()

    pygame.display.set_caption("Simple2D")

screen = pygame.display.set_mode((width,height))

class color:
    def __init__(self,_r,_g,_b):
        self.r = _r
        self.g = _g
        self.b = _b
    def __lt__(self, other):
        return (self.r,self.g,self.b) < (other.r, other.g, other.b)

mty = color(0, 0, 0)

def pixel(x, y, c):
    if c == 0:
        screen.set_at((x, y),(0, 0, 0))
    else:
        screen.set_at((x, y),(c.r, c.g, c.b))

def popscreen():
    #cheaty:

    screen.fill((0, 0, 0))

    #slow:

    #x = 0
    #for dx in range(width):
    #    y = 0
    #    for dy in range(height):
    #        pixel(x,y,mty)
    #        y +=1
    #    x += 1

class vector:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class renderobject:
    def render(self):
        return []

class line(renderobject):
    def __init__(self, _v1: vector, _v2: vector, _c: color):
        self.v1 = _v1
        self.v2 = _v2
        self.c = _c
    def render(self):
        y0 = self.v1.y
        x0 = self.v1.x
        y1 = self.v2.y
        x1 = self.v2.x

        return mx.bresenhamtomatrix(bresenham(x0, y0, x1, y1), self.c)
                
class rect2point(renderobject):
    def __init__(self, _v1: vector, _v2: vector, _c: color):
        self.v1 = _v1
        self.v2 = _v2

        self.l1 = line(_v1, vector( _v2.x, _v1.y ), _c)
        self.l2 = line(vector( _v2.x, _v1.y ), _v2, _c)
        self.l3 = line(_v2, vector(_v1.x, _v2.y), _c)
        self.l4 = line(vector(_v1.x, _v2.y), _v1, _c)

        self.angle = 0

        self.c = _c

    def render(self):
        m = self.l1.render()
        m2 = self.l2.render()
        m3 = self.l3.render()
        m4 = self.l4.render()

        if self.angle == 0:
            return mx.overlaymatrix(mx.overlaymatrix(mx.overlaymatrix(m3, m4), m2), m)
        else:
            return algo.rotate(mx.overlaymatrix(mx.overlaymatrix(mx.overlaymatrix(m3, m4), m2), m), self.angle)

class triangle(renderobject):
    def __init__(self, _v1: vector, _v2: vector, _v3: vector, _c: color):
        self.v1 = _v1
        self.v2 = _v2
        self.v3 = _v3

        self.l1 = line(_v1, _v2, _c)
        self.l2 = line(_v2, _v3, _c)
        self.l3 = line(_v3, _v1, _c)

        self.angle = 0

        self.c = _c

    def render(self):
        m = self.l1.render()
        m2 = self.l2.render()
        m3 = self.l3.render()

        if self.angle == 0:
            return mx.overlaymatrix(mx.overlaymatrix(m3, m2), m)
        else:
            return algo.rotate(mx.overlaymatrix(mx.overlaymatrix(m3, m2), m), self.angle)


class text(renderobject):
    def __init__(self, _text: str):
        self.text = _text
        self.angle = 0

    def render(self):
        pass


class image(renderobject):
    def __init__(self, _path: str):
        self.im = Image.open(_path,"r")
        self.angle = 0
        self.pix = mx.tuplelist2matrix(self.im.getdata(), self.im.size)

    def render(self):
        if self.angle == 0:
            return self.pix
        else:
            return algo.rotate(self.pix, self.angle)


color_green = color(0,255,0)

if __name__ == "__main__":

    font.initfont()

    fps = 0
    
    elems = []

    #elems.append(image('image.jpg'))

    testimage = image('image.jpg')
    testimage.angle = 45

    mlX = line(vector(0, 0), vector(0,height), color_green)
    mlY = line(vector(0, 0), vector(width,0), color_green)
    
    #elems.append(triangle(vector(10,50), vector(80,10), vector(80,100), color(255,0,0)))

    while True:
        start_time = time.time()

        

        mx.rendermatrixoff(testimage.render(), 100, 100)

        for i in elems:
            mx.rendermatrix( i.render())



        x, y = pygame.mouse.get_pos()
        mlX.v1, mlX.v2 = vector(y,0), vector(y, width)
        mlY.v1, mlY.v2 = vector(0,x), vector(height,x)

        mlXt = mx.compactizeTop(mlX.render())
        mx.rendermatrixofftransparent(mlXt[0], 0, mlXt[1])
        mx.rendermatrixtransparent(mlY.render())



        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        pygame.display.flip()
        popscreen()

        try:
            fps = 1.0 / (time.time() - start_time)
        except: pass