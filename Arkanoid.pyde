import os, random
path = os.getcwd()

class Arkanoid: #game itself
     def __init__(self,dim,dim1):
         self.dim1 = dim1 
         self.dim = dim
         self.pad = Pad(0,350,725,100,49)
         self.ball = Ball(self.pad.x1+41,707,18,0,0,0,58)
         
     def display(self):
         stroke(0)
         #line(0, self.dim-100, self.dim, self.dim-100)

         self.pad.display()
         self.ball.display()




class Ball: #ball, idk yet 
    def __init__(self, x, y, r, vx, vy, flag,v):
        self.space = False
        self.x = x 
        self.y = y  
        self.r = r #r = diameter
        self.vx = vx
        self.vy = vy
        self.img = loadImage(path+'/Images/'+str(v)+'-Breakout-Tiles.png')
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
        
        if self.y+self.vy*0.3 <= 0:  #bouncing off of walls
            self.y = 0
        if self.x+self.vx*0.3 <= 0:
            self.x = 0
        if self.x+self.vx*0.3 +self.r>= 800:
            self.x = 800-self.r
        if self.y <= 0:
            self.vy = -self.vy
        if self.x <= 0:
            self.vx = -self.vx
        if self.x+self.r >= 800:
            self.vx = -self.vx
            
        if self.y + self.vy*0.3 >= 725 and self.x >= a.pad.x1-3 and self.x <= a.pad.x1+a.pad.w+3 and self.y < 725: #this works with the help of pure magic, dont even try to understand it
            self.y = 725-self.r                                                                                    # i dont rly get it either 
        if self.x >= a.pad.x1-4 and self.x <= a.pad.x1+a.pad.w+4 and self.y >= 725-self.r and self.y < 725: #bouncing off of the pad
            self.vy = -self.vy
            
    def collision(self): #just the same as update but for balls and bricks 
        pass
            
        
    def release(self):
        self.vx = random.choice([random.randint(-9,-5), random.randint(5,9)])
        self.vy = -10
    
    def display(self):
        stroke(0)
        fill(0)
        image(self.img,self.x,self.y,self.r,self.r)
        self.update()
        
        
        
        
        
        
#PAD
class Pad: #ball bounces off it the exact same way light bounces from a mirror 
    def __init__(self,vx,x1,y,w, v):
        self.keyHandler = {LEFT:False, RIGHT:False}
        self.vx = vx
        self.x1 = x1
        self.y = y
        self.w = w
        self.img = loadImage(path+'/Images/'+str(v)+'-Breakout-Tiles.png')
        
        
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
        image(self.img,self.x1,self.y,self.w,17) #rect(x1,y1,width,height, radii) #image(self.img,x1,y1,w,h)
        self.update()
        
        
        
        
        
#TILES
class Tiles: #breaking tiles on the hit 
    def __init__(self, r, c, v = 2 ):
        pass
        
    
a = Arkanoid(1000,800)


 
def setup():
    background(255)
    size(a.dim, a.dim1)

def draw():
    frameRate(90) #increasing the frameRate for a more smooth experience 
    background(0)
    fill(255)
    rect(800,-1,1000,800)
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
