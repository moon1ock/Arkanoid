import os, random
path = os.getcwd()

class Arkanoid: #game itself
     def __init__(self,dim,dim1):
         self.dim1 = dim1 
         self.dim = dim
         self.pad = Pad(0,350,725,100,49)
         self.ball = Ball(self.pad.x1+41,707,18,0,0,0,58)
         self.ballz = []
         self.tiles = []
         for j in range(160):
             self.tiles.append(Tile(j//16,j%16))
         
         
         for i in range(15):
             self.ballz.append(Ball(self.pad.x1+41,707,18,0,0,0,58))
         self.state = 0 # 0 -- menu, 1 -- gameplay

     def display(self):
         #stroke(0)
         #line(0, self.dim-100, self.dim, self.dim-100)

         self.pad.display()
         self.ball.display()
         for j in self.tiles:
             j.display()
         
     def display0(self):
         for i in self.ballz:
            i.display0()



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
        self.cn = 0 #used for giving a random value to the ball for menu screen once
        
    def update(self): ###!!! IS IT OKAY TO HAVE 10 IF STATEMENTS IN A ROW???
        
        if self.flag == 0: #checking for space press
            self.x += a.pad.vx
        if self.space == True:
            self.flag += 1
        if self.flag == 1: #releasing the ball on space
            self.release()
    
        
        if self.y+self.vy*0.3 <= 0:  #bouncing off of walls
            self.y = 0
        if self.x+self.vx*0.3 <= 0:
            self.x = 0
        if self.x+self.vx*0.3 +self.r>= 800:
            self.x = 800-self.r
        if self.y <= 0:
            self.vy = -self.vy
        if self.x <= 0: #COMBINE THESE |
            self.vx = -self.vx
        if self.x+self.r >= 800:
            self.vx = -self.vx #|
            
        if self.y + self.vy*0.3+self.r//2 >= 725 and self.x >= a.pad.x1-4 and self.x <= a.pad.x1+a.pad.w+4 and self.y < 725: #this works with the help of pure magic, dont even try to understand it
            self.y = 725 - self.r
            self.vy = -self.vy
            
        # if self.x >= a.pad.x1-4 and self.x <= a.pad.x1+a.pad.w+4 and self.y >= 725-self.r and self.y < 725: #bouncing off of the pad
        #     self.vy = -self.vy
            
        self.y += self.vy*0.3 #ball movement itself
        self.x += self.vx*0.3
        
        if self.y > 820:
            self.flag = 0
            self.cn = 0
            self.vx = 0
            self.vy = 0
            self.x = a.pad.x1+41
            self.y = 707

        
    def display0(self): #just random animation during the menu screen
        if not self.cn:
            self.vx = random.choice([random.randint(-25,-6), random.randint(6,25)])
            self.vy = -random.randint(5,25)
            self.cn = 1
            
        image(self.img,self.x,self.y,self.r,self.r)
        self.y += self.vy*0.3 #ball movement itself
        self.x += self.vx*0.3
        #print(self.vx,self.vy)
    

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
        if self.y+self.vy*0.3 >= 800:  #bouncing off of walls
            self.y = 800-self.r
        if self.y >= 800-self.r:
            self.vy = -self.vy
            
    def collision(self): #just the same as update but for balls and bricks 
        
        for i in a.tiles:
            
            if self.x + self.r/2 >= i.c*50 and self.x+self.r/2 <=i.c*50+50 and self.y <= i.r*20+20 and self.y >= i.r*20:
                if i.state == 2:
                    i.state = 1
                else:
                    a.tiles.remove(i)
                self.vy = -self.vy 
                return
            
        
    def release(self):
        self.vx = random.choice([random.randint(-9,-5), random.randint(5,9)])
        self.vy = -10
    
    def display(self):
        stroke(0)
        fill(0)
        image(self.img,self.x,self.y,self.r,self.r)
        self.update()
        self.collision()
        
        
        
        
        
        
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
class Tile: #breaking tiles on the hit 
    def __init__(self, r, c):
        '''tiles have state (untouched or halfbroken), row and col'''
        self.r = r
        self.c = c
        self.state = 2
        self.imv = random.randint(0,9)*2+1 #this gives a random color to the tile
        self.img = loadImage(path+'/Images/'+str(self.imv)+'.png')
        
        
    def display(self):
        if self.state == 2:
            image(self.img,self.c*50,self.r*20)
        if self.state == 1:
            self.img = loadImage(path+'/Images/'+str(self.imv+1)+'.png')
            image(self.img,self.c*50,self.r*20)

        
    
a = Arkanoid(1000,800)


 
def setup():
    background(255)
    #fullScreen()
    size(a.dim, a.dim1)

def draw():
    
    
    frameRate(90) #increasing the frameRate for a more smooth experience 
    background(0)

    stroke(255)
    strokeWeight(6)
    line(803,0,803,800)
    #statistics
    
    
    
    #game states
    if a.state == 0: 
        a.display0()
        if 300<= mouseX <= 520 and 350<=mouseY<=410:
            fill(0,255,0)
        else:
            fill(255)
        textSize(42)
        text("Play Game", 300, 400)
    else:
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
        
        
def mouseClicked():
    if 300<= mouseX <= 520 and 350<=mouseY<=410:
            a.state = 1
