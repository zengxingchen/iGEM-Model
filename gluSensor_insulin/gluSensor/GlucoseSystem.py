from Glucose import Glucose 
import random
class GlucoseSystem:
    def __init__(self):
        self.gluList = []
        '''
        for i in range(200):
            glu = Glucose(position = PVector(500,400), velocity = PVector(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0)), 
                        acceleration = PVector(0,0), mass = 0, topSpeed = 1, maxforce = 0, r = 10, inCell = 1, quadrant = 0, lifespan = 100)
            self.gluList.append(glu)
        '''
    
    def display(self):
        for glu in self.gluList:
            if glu.inCell == 1:
                glu.displayIn()
            else:
                glu.displayOut()
                
            
            
    def update(self):
        for glu in self.gluList:
            glu.update()
            
    def check(self, cell, sensor):
        num = 0
        for glu in self.gluList:
            glu.checkInCell(cell) #Check to see if it's inside the cell
            if glu.inCell == 1:
                glu.checkCellEdges(cell)
                glu.checkSensor(sensor)
            else:
                glu.checkEdges()
            num += glu.beFound(sensor)
            if glu.gluDead():
                self.gluList.remove(glu)
                # num -= glu.beFound(sensor)
        return num
    
    def addGlusIn(self, position, num = 50):
        for i in range(num):
            glu = Glucose(position = PVector(mouseX, mouseY), velocity = PVector(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0)), 
                        acceleration = PVector(0,0), mass = 0, topSpeed = 1, maxforce = 0, r = 10, inCell = 1, quadrant = 0, lifespan = 100)
            self.gluList.append(glu)
            
    def addGlusOut(self,num = 2):
        for i in range(num):
            glu = Glucose(position = PVector(random.randint(0,200), random.randint(0,200)), velocity = PVector(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0)), 
                        acceleration = PVector(0,0), mass = 0, topSpeed = 1, maxforce = 0, r = 10, inCell = 0, quadrant = 0, lifespan = 100)
            self.gluList.append(glu)
            
             
               
