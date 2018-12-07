import os, random
path = os.getcwd()

class Arkanoid: #game itself
     def __init__(self,dim,dim1):
         self.dim1 = dim1 
         self.dim = dim
         self.pad = Pad(0,350,725,100)
         self.ball = Ball(self.pad.x1+50,725,9,0,0,0)


         
         
     def display(self):
         stroke(0)
         #line(0, self.dim-100, self.dim, self.dim-100)
         self.pad.display()
         self.ball.display()




class Ball: #ball, idk yet 
    def __init__(self, x, y, r, vx, vy, flag):
        self.space = False
        self.x = x #
        self.y = y - r  #
        self.r = r #
        self.vx = vx
        self.vy = vy
        self.flag = flag #flagfall for ball release so that the release func is not called twice
        
    def update(self): ###!!! IS IT OKAY TO HAVE 10 IF STATEMENTS IN A ROW???
        
        if self.flag == 0: #checking for space press
            self.x += a.pad.vx
        if self.space == True:
            self.flag += 1
        if self.flag == 1: #releasing the ball on space
            self.release()
        
        self.y += self.vy*0.3 #ball movement itself
        self.x += self.vx*0.3
        
        if self.y+self.vy*0.3 <= self.r:  #bouncing off of walls
            self.y = self.r
        if self.x+self.vx*0.3 <= self.r:
            self.x = self.r
        if self.x+self.vx*0.3 >= 800-self.r:
            self.x = 800-self.r
        if self.y <= self.r:
            self.vy = -self.vy
        if self.x <= self.r:
            self.vx = -self.vx
        if self.x >= 800-self.r:
            self.vx = -self.vx
            
        if self.y + self.vy*0.3 >= 725-self.r and self.x >= a.pad.x1 and self.x <= a.pad.x1+a.pad.w:
            self.y = 725-self.r+2
        if self.x >= a.pad.x1 and self.x <= a.pad.x1+a.pad.w and self.y >= 725-self.r: #bouncing off of the pad
            self.vy = -self.vy
            
    def collision(self): #just the same as update but for balls and bricks 
        pass
            
        
    def release(self):
        self.vx = random.choice([random.randint(-9,-5), random.randint(5,9)])
        self.vy = -10
    
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
        
    
a = Arkanoid(800,1000)


 
def setup():
    background(255)
    size(1100, 800)

def draw():
    frameRate(90) #increasing the frameRate for a more smooth experience 
    background(255)
    #line(0,725,800,725)
    noFill()
    stroke(0)
    rect(0,0,800,800)
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
