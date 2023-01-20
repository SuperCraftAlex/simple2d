from main import width, height
from api import *
import matrix as mx
import algo as algo
import win32con, win32api
import string

elems = []

def start():
    pass

def loop():
    
    for i in elems:
            for o in i.render():
                try:mx.rendermatrixoff(o[0], o[1], o[2])
                except:pass

def extpreinit():
    return (start, loop)