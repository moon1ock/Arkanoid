import os
path = os.getcwd()

class Tiles: #breaking tiles on the hit 
    def __init__(self, r, c, v = 2 ):
        pass


class Pad: #ball bounces of it the exact same way light bounces from a mirror 
    def __init__(self):
        self.keyHandler = {LEFT:False, RIGHT:False}
        self.vx = 0
        self.x1 = 300
        self.w = 100
        
        
        
    def update(self):
        self.x1 += self.vx
        # self.x2 += self.vx 
        
        if self.keyHandler[LEFT]: #if LEFT KEY pressed give negative velocity 
            self.vx = -5
        elif self.keyHandler[RIGHT]: #positive self.vx if RIGHT pressed
            self.vx = 5
        else:
            self.vx = 0 #fixing the bug when a key is not pressed but the pad continues to move
   
   
        if self.x1 <= 0: # blocking the pad from going off the map
            self.x1 = 0
        elif self.x1 >= 700:
            self.x1 = 699
   
    def display(self):
        noFill()
        rect(self.x1,725,self.w,17,10) #rect(x1,y1,width,height, radii)
        self.update()
        

    

class Ball: #ball, idk yet 
    def __init__(self):
        pass

    
    
class Arkanoid: #game itself
    def __init__(self,dim):
        self.dim = dim
        self.pad = Pad()
        

    def display(self):
        stroke(0)
        #line(0, self.dim-100, self.dim, self.dim-100)
        self.pad.display()


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
         
def keyReleased():
     if keyCode == LEFT:
         a.pad.keyHandler[LEFT] = False
     elif keyCode == RIGHT:
         a.pad.keyHandler[RIGHT] = False
