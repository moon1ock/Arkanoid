import os, random
path = os.getcwd()

class Arkanoid: #game itself
     def __init__(self,dim):
         self.dim = dim
         self.pad = Pad(0,300,725,100)
         self.ball = Ball(350,725,9,0,0,0)

         
         
     def display(self):
         stroke(0)
         #line(0, self.dim-100, self.dim, self.dim-100)
         self.pad.display()
         self.ball.display()




class Ball: #ball, idk yet 
    def __init__(self, x, y, r, g, vx, vy):  ###!!!! wiggling movement 
        self.space = False
        self.x = x  #
        self.y = y - r  #
        self.r = r #
        self.g = g #ground 
        self.vx = 0
        self.vy = 0
        self.flag = 0
        
    def update(self):
        
        if self.space == True:
            self.flag += 1
        if self.flag == 1:
            self.release()
        self.y += self.vy
        self.x += self.vx
        if self.y <= 0:
            self.vy = -self.vy
        if self.x <= 0:
            self.vx = -self.vx
        if self.x >= 800:
            self.vx = -self.vx
            
        if self.x >= a.pad.x1 and self.x <= a.pad.x1+100 and self.y == 725:
            self.vy = -self.vy
            
            
        
    def release(self):
        self.vx = random.randint(-6,6)
        self.vy = -3
    
    def display(self):
        stroke(0)
        fill(0)
        ellipse(self.x,self.y,self.r*2,self.r*2)
        self.update()
        
        
        
        
        
        
#PAD
class Pad: #ball bounces off it the exact same way light bounces from a mirror 
    def __init__(self,vx,x1,y,w):
        self.keyHandler = {LEFT:False, RIGHT:False}
        self.vx = vx
        self.x1 = x1
        self.y = y
        self.w = w
        
        
        
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
        rect(self.x1,self.y,self.w,17,10) #rect(x1,y1,width,height, radii)
        self.update()
        
        
        
        
        
#TILES
class Tiles: #breaking tiles on the hit 
    def __init__(self, r, c, v = 2 ):
        pass
        
    
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
     if keyCode == 32:
        a.ball.space = False
