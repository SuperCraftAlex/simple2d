import sys, pygame
import random
import numpy as np
from bresenham import bresenham
from font import fontlist
import algo
import matrix as mx
from PIL import Image

width, height = 500, 500

if __name__ == "__main__":
    pygame.init()

    pygame.display.set_caption("Simple2D")

screen = pygame.display.set_mode((width,height))

class color:
    def __init__(self,_r,_g,_b):
        self.r = _r
        self.g = _g
        self.b = _b

mty = color(0, 0, 0)

def pixel(x, y, c: color):
    screen.set_at((x, y),(c.r, c.g, c.b))

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
                

class triangle(renderobject):
    def __init__(self, _v1: vector, _v2: vector, _v3: vector, _c: color):
        self.v1 = _v1
        self.v2 = _v2
        self.v3 = _v3

        self.l1 = line(_v1, _v2, _c)
        self.l2 = line(_v2, _v3, _c)
        self.l3 = line(_v3, _v1, _c)

        self.c = _c

    def render(self):
        m = self.l1.render()
        m2 = self.l2.render()
        m3 = self.l3.render()
        return mx.overlaymatrix(mx.overlaymatrix(m3, m2, mty), m, mty)

    def renderinstant(self):
        mx.rendermatrix(self.l1.render())
        mx.rendermatrix(self.l2.render())
        mx.rendermatrix(self.l3.render())

class text(renderobject):
    def __init__(self, _text: str):
        self.text = _text
    def renderinstant(self):
        o = 0

        for letter in self.text:
            pixellist = mx.colorize(fontlist[letter], color(255,0,0))
            mx.rendermatrixoff(pixellist,o,0)
            o += 7

class image(renderobject):
    def __init__(self, _path: str):
        self.im = Image.open(_path,"r")
        self.pix = mx.tuplelist2matrix(self.im.getdata(), self.im.size)
    def renderinstant(self):
        pass
        mx.rendermatrix(self.pix)



if __name__ == "__main__":
    elems = []

    #elems.append(text("HALLO DAS IST EIN TEST"))

    elems.append(image('image.jpg'))

    for i in elems:
        i.renderinstant()

    # a = line(vector(10,10), vector(100,100), color(255, 0, 0))
    # b = a.render()
    # rendermatrix(b)

    # elems.append(triangle(vector(10,50), vector(80,10), vector(80,100), color(255,0,0)))

    #for i in elems:
    #    mx.rendermatrix(i.render())

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        pygame.display.flip()