from Glucose import Glucose 
import random

class GlucoseSystem:
    def __init__(self):
        self.gluList = []
    
    def display(self):
        for glu in self.gluList:
            glu.display()
            
    def update(self):
        for glu in self.gluList:
            glu.update()

    def check(self, cell, sensor):
        num = 0
        for glu in self.gluList:
            glu.check_in_cell(cell) #Check to see if it's inside the cell
            if glu.in_cell == 1:
                glu.check_cell_edge(cell)
                glu.check_sensor(sensor)
            else:
                glu.check_edge()
            num += glu.beFound(sensor)
            if glu.gluDead():
                self.gluList.remove(glu)
        return num

    def add(self, num, in_cell):
        for i in range(num):
            if in_cell:
                glu = Glucose(position = PVector(mouseX, mouseY), velocity = PVector(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0)), 
                        acceleration = PVector(0,0), mass = 0, top_speed = 1, maxforce = 0, r = 10, in_cell = 1, lifespan = 100)
            else:
                glu = Glucose(position = PVector(random.randint(0,200), random.randint(0,200)), velocity = PVector(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0)), 
                    acceleration = PVector(0,0), mass = 0, top_speed = 1, maxforce = 0, r = 10, in_cell = 0, lifespan = 100)
            self.gluList.append(glu)
            
             
               
