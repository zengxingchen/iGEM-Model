class Cell:
    # Class variable, easy to modify the size of the entire system
    sketch_Width = 800
    sketch_Height = 500
    thick = 25
    r = 20
    def __init__(self, r = r, thick = 25, position = PVector(850, 600), id = 0):
        # self.Width = Width
        # self.Height = Height
        self.r = r
        self.d = r * 2
        self.thick = thick  
        self.position = position
        self.light = 0 
        self.id = id
    
    def display(self):
        fill(239, 188, 64)
        ellipse(self.position.x, self.position.y,self.d + self.thick, self.d + self.thick)
        fill(186, 230, 235)
        '''if self.light else fill(255, 255, 255)'''
        ellipse(self.position.x, self.position.y, self.d, self.d)


    def switch_light(self):
        self.light = 0 if self.light else 1
    
    def update(self):
        pass
    
class TissueCell(Cell):
    def __init__(self, r, thick, position, id):
        Cell.__init__(self, r, thick, position)
        self.id = id
        self.insulin_num = 0
        self.status = "InActiviated"

                
    def display(self):
        fill(246, 153, 180)
        ellipse(self.position.x, self.position.y,self.d + self.thick, self.d + self.thick)
        fill(135, 206, 250,200) if self.light else fill(255, 255, 255)
        ellipse(self.position.x, self.position.y, self.d, self.d)
    
    def check(self):
        if self.insulin_num >= 2 and self.status == "InActiviated":
            self.status = "Activiated"
        elif self.insulin_num < 2 and self.status == "Activiated":
            self.status = "InActiviated"
        self.insulin_num = 0
