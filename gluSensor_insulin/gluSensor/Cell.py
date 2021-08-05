class Cell:
    def __init__(self, r = 400,thick = 15, position = PVector(800, 600)):
        self.r = r
        self.d = r * 2
        self.thick = thick
        self.position = position
        self.light = 0 
    
    def display(self):
        fill(255,131,250)
        ellipse(self.position.x, self.position.y,self.d + self.thick, self.d + self.thick)
        fill(100, 149, 237, 200) if self.light else fill(255, 255, 255)
        ellipse(self.position.x, self.position.y, self.d, self.d)

    def switch_light(self):
        self.light = 0 if self.light else 1
    
    def update(self):
        pass
