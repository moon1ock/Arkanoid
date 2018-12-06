class Pad: #ball bounces off it the exact same way light bounces from a mirror 
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
