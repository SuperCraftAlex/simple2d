from PIL import Image
import matrix as mx
import algo as algo
from bresenham import bresenham
import font

class color:
    def __init__(self,_r,_g,_b):
        self.r = _r
        self.g = _g
        self.b = _b
    def __lt__(self, other):
        return (self.r,self.g,self.b) < (other.r, other.g, other.b)

class vector:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class renderobject:
    def render(self):
        return []

class line():
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
            return [(m,0,0),(m2,0,0),(m3,0,0)(m4,0,0)]
        else:
            print("rect rotation not supported yet due to lazyness")
            return False

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
            return [(m,0,0),(m2,0,0),(m3,0,0)]
        else:
            return [(algo.rotate(m, self.angle),0,0),(algo.rotate(m2, self.angle),0,0),(algo.rotate(m3, self.angle),0,0)]


class text(renderobject):
    
    def __init__(self, _text: str, mixin):
        self.text = _text
        self.angle = 0
        self.mixin = mixin

    def render(self):
        rl = []
        o = 0
        for i in str(self.text):
            rl.append((font.get(i), o*12, 0))
            o += 1

        if self.angle == 0:
            if self.mixin == None:
                return rl
            else:
                nl = []
                for i in rl:
                    nl.append(self.mixin(i))
                return nl
        else:
            exit("rotation not supported for text yet bc of matrix overlay bugs")
            return False


class image(renderobject):
    def __init__(self, _path: str):
        self.im = Image.open(_path,"r")
        self.angle = 0
        self.pix = mx.tuplelist2matrix(self.im.getdata(), self.im.size)

    def render(self):
        if self.angle == 0:
            return [(self.pix,0,0)]
        else:
            return [(algo.rotate(self.pix, self.angle),0,0)]

class ab:
    def __init__(self, _a: vector, _b: vector):
        self.a = _a
        self.b = _b

class aabb:
    def __init__(self, _x1, _x2, _y1, _y2):
        self.x1 = _x1
        self.x2 = _x2
        self.y1 = _y1
        self.y1 = _y1

def trit(a, b, c):
    return (a, b, c)

def ab2aabb(i: ab):
    return aabb(i.a.x, i.b.x, i.a.y, i.b.y)

def aabb2ab(i: aabb):
    return ab(vector(i.x1, i.y1), vector(i.x2, i.y2))

def collissionPoint(c: ab, v: vector):
    if (c.a.x < v.x and v.x < c.b.x):
        if (c.a.y < v.y and v.y < c.b.y):
            return True
    return False

def ccomp(c1, c2):
    try:
        if c1 == 0:
            c1 = mty   
        if c2 == 0:
            c2 = mty   
    except: pass
    try:
        if (c1.r == c2.r) and (c1.g == c2.g) and (c1.b == c2.b):
            return True
    except: return mty
    return False

mty = color(0, 0, 0)