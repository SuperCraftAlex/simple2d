import PIL
import matrix as mx

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

def initfont():
    im = PIL.Image.open("Pixeloid_font.jpg","r")
    #matrix = mx.tuplelist2matrix(im.getdata(), im.size)