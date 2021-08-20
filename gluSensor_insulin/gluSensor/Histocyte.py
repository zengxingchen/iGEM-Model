from Cell import Cell
class Histocyte:  # It mainly includes the glucose transporter and insulin receptor
    def __init__(self,position, r = 100, thick = 10):
        self.position = position
        self.r = r
        self.thick = thick
        
        
    def display(self):
        fill(255,131,250)
        ellipse(self.position.x, self.position.y,self.d + self.thick, self.d + self.thick)
        fill(255, 255, 255)
        ellipse(self.position.x, self.position.y, self.d, self.d)
        
        
     
