import PIL
import matrix as mx
from api import *
import algo

charlist0=[]
charlist1=[]
charlist2=[]

row0 = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z"
]

row1 = []
for i in row0:
    row1.append(i.upper())

row2 = [
    "0","1","2","3","4","5","6","7","8","9",
    ".", ":", ",", ";", "(", "*", "!", "?", "}", "^", ")",
    "#","$","{","%","^","&","-","+","@"
]

white = color(255,255,255)

def initfont():
    im = PIL.Image.open("Pixeloid_font.png","r")
    matrix = mx.tuplelist2matrix(im.getdata(), im.size)
    matrix = mx.selection(matrix, vector(6,10), vector(67,367))

    mr0 = mx.selection(matrix, vector(0,0), vector(18,367))
    mr1 = mx.selection(matrix, vector(22,0), vector(18+22,367))
    mr2 = mx.selection(matrix, vector(0+43,0), vector(18+43,367))

    for i in range(len(row0)):
        s = mx.selection(mr0, vector(0, i*12), vector(18, i*12+11))
        charlist0.append(s)

    for i in range(len(row1)):
        s = mx.selection(mr1, vector(0, i*12), vector(18, i*12+11))
        charlist1.append(s)

    for i in range(len(row2)):
        s = mx.selection(mr2, vector(0, i*12), vector(18, i*12+11))
        charlist2.append(s)

def get(s):
    if s == " ":
        return mx.emptymatrix(1,1)
    s = str(s)
    if s in row0:
        return charlist0[row0.index(s)]
    if s in row1:
        return charlist1[row1.index(s)]
    if s in row2:
        return charlist2[row2.index(s)]
    print("error: character "+s+" not in string list")
    exit()