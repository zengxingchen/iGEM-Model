from ProteinSystem import ProteinSystem 

class Switch:  
    def __init__(self, position, r = 40):
        self.r = r
        self.d = 2 * r
        self.position = position
        self.state = False

    def display(self):
        if self.state == True :
            fill(5, 9, 175) 
        else: 
            fill(0, 0, 0)
        ellipse(self.position.x, self.position.y, self.d, self.d)
    
    def stateChange(self):
        self.state = True if self.state == False else False
