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
         self.statiles = {}
         self.blink = 0
         self.frames = 0
         for j in range(80):
             self.tiles.append(Tile(j//16,j%16))
         self.hp = 3
         self.hpimg = loadImage(path+'/Images/60.png')
         self.gameover = loadImage(path+'/Images/99.png')
         
         for i in range(15):
             self.ballz.append(Ball(self.pad.x1+41,707,18,0,0,0,58))
         self.state = 0 # 0 -- menu, 1 -- gameplay

     def display(self):
         #stroke(0)
         #line(0, self.dim-100, self.dim, self.dim-100)
         if len(self.tiles) == 0:
             self.ball.vy = -self.ball.vy
             for j in range(random.randint(5,60)):
                self.tiles.append(Tile(j//16,j%16))
         self.pad.display()
         self.ball.display()
         for j in self.tiles:
             j.display()
         
     def display0(self):
         for i in self.ballz:
            i.display0()
            
     def stats(self):
        textSize(30)
        fill(255)
        text("Statistics", 835, 30)
        fill(255,224,189)
        text("Statistics", 837, 30)
        textSize(20)
        fill(220,20,60)
        text("Hp:", 817, 80)
        for i in range(self.hp):
            image(self.hpimg, 855+i*27, 67)
        for i in self.statiles:
            textSize(25)
            fill(255)
            text(':x'+str(self.statiles[i]), 873, 106+20*i)
        



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
        
    def update(self): 
        
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
        if self.x <= 0 or self.x+self.r >= 800: 
            self.vx = -self.vx
 
            
        if self.y + self.vy*0.3+self.r//2 >= 725 and self.x >= a.pad.x1-4 and self.x <= a.pad.x1+a.pad.w+4 and self.y < 725: 
            self.y = 725 - self.r
            self.vy = -self.vy +random.randint(-1,1)
            
    
        self.y += self.vy*0.3 #ball movement itself
        self.x += self.vx*0.3
        
        if self.y > 820:
            if a.hp == 0:
                a.state = 2
            else:
                a.hp -= 1
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
            
        image(self.img,self.x,self.y)
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
        '''here the order of checking is tremendously 
        important as a 'YES' after an if function breaks
        the loop and returns, yet we have to try to catch 
        the most precise collision. Based on the tests that 
        I've developped, the left bounce is the least prominent
        or possible one, while the top bounce is has the biggest 
        likelyhood, thus i placed it last'''
        for i in a.tiles:
              if self.x + self.r >= i.c*50 and self.x+self.r <=i.c*50+25 and self.y+self.r/2 >= i.r*20 and self.y + self.r/2 <= i.r*20+20: #check for the left bounce
                if i.state == 2:
                    k = random.randint(1,10)
                    if k >= 7:
                        i.state = 1
                    else:
                        a.tiles.remove(i)
                        a.statiles[i.imv]+=1
                else:
                    a.tiles.remove(i)
                    a.statiles[i.imv]+=1
                self.vx = -self.vx
                return
              elif self.x <=i.c*50+50 and self.x >= i.c*50+25 and self.y+self.r/2 >= i.r*20 and self.y + self.r/2 <= i.r*20+20: #check for the right bounce
                if i.state == 2:
                    k = random.randint(1,10)
                    if k >= 7:
                        i.state = 1
                    else:
                        a.tiles.remove(i)
                        a.statiles[i.imv]+=1
                else:
                    a.tiles.remove(i)
                    a.statiles[i.imv]+=1
                self.vx = -self.vx
                return
              elif self.x + self.r/2 >= i.c*50-3 and self.x+self.r/2 <=i.c*50+50+3 and self.y <= i.r*20+20 and self.y >= i.r*20+10: #check for the bottom bounce
                if i.state == 2:
                    k = random.randint(1,10)
                    if k >= 7:
                        i.state = 1
                    else:
                        a.tiles.remove(i)
                        a.statiles[i.imv]+=1
                else:
                    a.tiles.remove(i)
                    a.statiles[i.imv]+=1
                self.vy = -self.vy 
                return
              elif self.x + self.r/2 >= i.c*50-3 and self.x+self.r/2 <=i.c*50+50+3 and self.y+self.r >= i.r*20 and self.y + self.r <= i.r*20+10: #check for the top bounce
                if i.state == 2:
                    k = random.randint(1,10)
                    if k >= 7:
                        i.state = 1
                    else:
                        a.tiles.remove(i)
                        a.statiles[i.imv]+=1
                else:
                    a.tiles.remove(i)
                    a.statiles[i.imv]+=1
                self.vy = -self.vy 
                return

            
        
    def release(self):
        self.vx = random.choice([random.randint(-14,-8), random.randint(8,14)])
        self.vy = -14
        a.blink = 1
    
    def display(self):
        stroke(0)
        fill(0)
        image(self.img,self.x,self.y)#,self.r,self.r)
        self.update()
        self.collision()
        
        
        
        
        
        
#PAD
class Pad: #ball bounces off it the exact same way light bounces from a mirror 
    def __init__(self,vx,x1,y,w,v):
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
            self.vx = -6
        elif self.keyHandler[RIGHT]: #positive self.vx if RIGHT pressed
            self.vx = 6
        else:
            self.vx = 0 #fixing the bug when a key is not pressed but the pad continues to move
   
   
        if self.x1 <= 0: # blocking the pad from going off the map
            self.x1 = 0
        elif self.x1 >= 700:
            self.x1 = 699
   
   

    def display(self):
        noFill()
        image(self.img,self.x1,self.y) #rect(x1,y1,width,height, radii) #image(self.img,x1,y1,w,h)
        self.update()
        
        
        
        
        
#TILES
class Tile: #breaking tiles on the hit 
    def __init__(self, r, c):
        '''tiles have state (untouched or halfbroken), row and col'''
        self.r = r*2
        self.c = c
        self.state = 2
        self.imv = random.randint(0,9)*2+1 #this gives a random color to the tile
        self.img = loadImage(path+'/Images/'+str(self.imv)+'.png')
        
        
    def display(self):
        if self.imv not in a.statiles:
            a.statiles[self.imv] = 0
        if self.state == 2:
            image(self.img,self.c*50,self.r*20)
        if self.state == 1:
            self.img = loadImage(path+'/Images/'+str(self.imv+1)+'.png')
            image(self.img,self.c*50,self.r*20)

        image(self.img, 830, 90+20*self.imv)
    




def setup():
    background(255)
    #fullScreen()
    size(a.dim, a.dim1)

def draw():
    
    a.frames +=1 
    frames = a.frames//30

    frameRate(90) #increasing the frameRate for a more smooth experience 
    background(0)

    stroke(255)
    strokeWeight(6)
    line(803,0,803,800)
    #statistics
    a.stats()
    
    
    #game states
    if a.state == 0: 
        a.display0()
        if 300<= mouseX <= 520 and 350<=mouseY<=410:
            fill(0,255,0)
        else:
            fill(255)
        textSize(42)
        text("Play Game", 300, 400)
    elif a.state == 1:
        if a.blink == 0: #creating blinking text
            if frames % 2 == 1:
                fill(0)
            else:
                fill(255)
            textSize(20)
            text('PRESS SPACE',340,400)

        a.display()
        
    elif a.state == 2:
        a.display()
        image(a.gameover, 200, 330)
        fill(255)
        textSize(14)
        text('(Thank you for testing out our project, we sincerely hope you liked it!)', 310, 750)
            

        

class Star:
    def __init__(self,r,c):
        self.r = r
        self.c = c


def keyPressed():
    if a.state != 2:
        if keyCode == LEFT:
            a.pad.keyHandler[LEFT] = True
        elif keyCode == RIGHT:
            a.pad.keyHandler[RIGHT] = True
        if keyCode == 32:
            a.ball.space = True
            
            
            
a = Arkanoid(1000,800)
            
def keyReleased():
     if keyCode == LEFT:
         a.pad.keyHandler[LEFT] = False
     elif keyCode == RIGHT:
         a.pad.keyHandler[RIGHT] = False
     if keyCode == 32:
        a.ball.space = False
        
        
def mouseClicked():
    if a.state == 0:
        if 300<= mouseX <= 520 and 350<=mouseY<=410:
                a.state = 1
