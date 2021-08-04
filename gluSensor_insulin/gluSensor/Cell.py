class Cell:
    def __init__(self, r = 400,thick = 15, position = PVector(800, 600)):
        self.r = r
        self.d = r * 2
        self.thick = thick
        self.position = position
        
    def displayWhite(self):
        fill(255,131,250)
        ellipse(self.position.x,self.position.y,self.d + self.thick,self.d + self.thick)
        fill(255, 255, 255) # white
        ellipse(self.position.x, self.position.y, self.d, self.d)
    
    def displayBlue(self):
        fill(255,131,250)
        ellipse(self.position.x,self.position.y,self.d + self.thick,self.d + self.thick)
        fill(100, 149, 237, 200) # Blue
        ellipse(self.position.x, self.position.y, self.d, self.d)
    
    def update(self):
        pass
