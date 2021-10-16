class Cell:
    # Class variable, easy to modify the size of the entire system
    sketch_Width = 1600
    sketch_Height = 1000
    r = 400
    thick = 15
    def __init__(self, r = r, thick = 15, position = PVector(sketch_Width/2, sketch_Height/2)):
        # self.Width = Width
        # self.Height = Height
        self.r = r
        self.d = r * 2
        self.thick = thick  
        self.position = position
        self.light = 0 
    
    def display(self):
        fill(239, 188, 64)
        ellipse(self.position.x, self.position.y,self.d + self.thick, self.d + self.thick)
        fill(186, 230, 235) if self.light else fill(255, 255, 255)
        ellipse(self.position.x, self.position.y, self.d, self.d)


    def switch_light(self):
        self.light = 0 if self.light else 1
    
    def update(self):
        pass
