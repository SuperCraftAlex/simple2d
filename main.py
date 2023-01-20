import sys, pygame
import random, time
import numpy as np
import algo
import matrix as mx
from PIL import Image
import font
from api import *
import const
import win32gui



# MASTER CONFIG (BUILDSIDE)
cfg_usewin32api = False      # use win32gui instaead of pygame. not recommented due to slowness!

if cfg_usewin32api:
    import win32api
    import win32con
    width, height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
else:
    width, height = 1000, 1000

if cfg_usewin32api:
    hwnd = win32gui.WindowFromPoint((0,0))
    monitor = (0, 0, win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1))

if cfg_usewin32api:
    import win32gui
    import win32api

if __name__ == "__main__":
    if not cfg_usewin32api:
        pygame.init()

        pygame.display.set_caption("Simple2D")

if not cfg_usewin32api:
    screen = pygame.display.set_mode((width,height))

mty = color(0, 0, 0)
if cfg_usewin32api:
    dc = win32gui.GetDC(0)

def pixel(x, y, c):
    if mx.isblank(c):
        return
    if (cfg_usewin32api):
        try:
            win32gui.SetPixel(dc, x, y, win32api.RGB(c.r, c.g, c.b))
        except:
            pass
    else:
        screen.set_at((x, y),(c.r, c.g, c.b))

def popscreen():
    if cfg_usewin32api:
        win32gui.InvalidateRect(0, monitor, True)
    else:
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

def mousepos():
    if cfg_usewin32api:
        return win32api.GetCursorPos()
    else:
        return pygame.mouse.get_pos()

apps = []


if __name__ == "__main__":

    import test_pixelmousebrowser
    apps.append(test_pixelmousebrowser.extpreinit())

    font.initfont()

    fps = 0
    
    elems = []


    for i in apps:
            i[0]()

    frame = -1

    elems.append((10 , lambda a: text("Hallo! Der Text funktioniert ENDLICH!", (lambda i: trit(algo.scale(i[0], a, a), i[1]*a, i[2]*a)))))

    while True:
        frame += 1
        start_time = time.time()
        
        for i in apps:
            i[1]()


        for i in elems:
            x = i[1](i[0])
            for o in x.render():
                try:mx.rendermatrixoff(o[0], o[1], o[2])
                except:pass


        if not cfg_usewin32api:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            
            pygame.display.flip()

        popscreen()

        try:
            fps = 1.0 / (time.time() - start_time)
        except: pass