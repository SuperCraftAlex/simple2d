import main, algo
import matrix as mx

class PipelineObject():
    def __init__(self):
        self.object = main.renderobject
        
        self.renderpriority = 0     # higher = more priority    0 = maximal auto delay 1 tick   -1 = renders when no lag   -2 = renders async when no lag    -3 = renders async as quick as possible (priority)
        self.renderinacc = 0

        self.optimize1 = False      # uses compactize functions to optimize
        self.optimize1need = 1      # 0 = as quick as possible (async)   1 = every tick    2 = every second tick ..... -1 = only render if no lag  -2 = dont optimize at all  -3 = async if no lag
        self.optimize1needc = 0

        self.renderneed = 1         # 0 = as quick as possible (async)   1 = every tick    2 = every second tick ..... -1 = only render if no lag  -2 = dont render at all  -3 = async if no lag
        self.renderneedc = 0  

        self.x = 0
        self.y = 0
        self.angle = 0

        self.fill = []              # list ( tuple (x, y, color))

        self.antialiasingneed = 0   # 0 = as quick as possible (async)   1 = every tick    2 = every second tick ..... -1 = only render if no lag  -2 = dont antialize at all  -3 = async if no lag
        self.antialiasingneedc = 0
