
class BRaySwitch:  
    def __init__(self, position, BRr = 40):

        self.r = BRr
        self.d = 2 * BRr
        self.position = position
        self.state = False


    def display(self):
        if self.state == True :
            fill(5, 9, 175) 
        else: 
            fill(0, 0, 0)
        ellipse(self.position.x, self.position.y, self.d, self.d)
    
    def StateChange(self):
        self.state = True if self.state == False else False
