import os
from Pad import Pad
from Ball import Ball 
from Tiles import Tiles
path = os.getcwd()

class Arkanoid: #game itself
     def __init__(self,dim):
         self.dim = dim
         self.pad = Pad()
         self.ball = Ball()
         
         
         
     def display(self):
         stroke(0)
         #line(0, self.dim-100, self.dim, self.dim-100)
         self.pad.display()
         self.ball.display()

    
a = Arkanoid(800)


def setup():
    background(0)
    size(a.dim, a.dim)

def draw():
    background(255)
    a.display()


def keyPressed():
    if keyCode == LEFT:
         a.pad.keyHandler[LEFT] = True
    elif keyCode == RIGHT:
         a.pad.keyHandler[RIGHT] = True
    if keyCode == 32:
        a.ball.space = True
         
         
def keyReleased():
     if keyCode == LEFT:
         a.pad.keyHandler[LEFT] = False
     elif keyCode == RIGHT:
         a.pad.keyHandler[RIGHT] = False
