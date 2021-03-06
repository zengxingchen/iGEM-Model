from Glucose import Glucose 
import random

class GlucoseSystem:
    def __init__(self, glut_threshold = 200, glu_stored = 3000):  #glut_threshold:The distance threshold of directed search for glut_protein
        self.glut_threshold = glut_threshold
        self.glu_stored = glu_stored
        self.gluList = []
                
                
    def display(self):
        for glu in self.gluList:
            glu.display()
            
    def update(self):
        for glu in self.gluList:
            glu.update()


    def check(self, cell, glut_list):
        num = self.count_num(in_cell = 1)
        for glu in self.gluList:
            glu.check_in_cell(cell, glut_list) # Check to see if it's inside the cell
            # try to find the glut
            if PVector.dist(glu.position, cell.position) >= cell.r - 30 and glu.through_glut == False:
                glu.follow(glut_list, self.glut_threshold)
                glu.check_edge()
                # not find glut or close enough to the glut yet
                if glu.dist_target >= 100:
                    glu.check_cell_out_edge(cell)
            elif glu.in_cell == 1:
                # avoid to find the glut again
                glu.through_glut = True
                if glu.change_state == False:
                    glu.velocity.x *= random.uniform(0, 5)
                    glu.velocity.y *= random.uniform(0, 5)
                    glu.change_state = True
                glu.check_cell_edge(cell)

            if glu.gluDead():
                self.gluList.remove(glu)

        return num
    
    
    def count_num(self, in_cell):
        num = 0 
        for glu in self.gluList:
            if glu.in_cell == in_cell:
                num += 1
        return num
    
    

    def add(self, num, in_cell):
        self.glu_stored -= num 
        for i in range(num):
            if in_cell:
                glu = Glucose(position = PVector(mouseX, mouseY), velocity = PVector(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0)), 
                        acceleration = PVector(0,0), mass = 0, top_speed = 1, maxforce = 0, r = 5, in_cell = 1, lifespan = 100,spin = 100)
            else:
                glu = Glucose(position = PVector(random.randint(0,250), random.randint(0,800)), velocity = PVector(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0)), 
                    acceleration = PVector(0,0), mass = 0, top_speed = 1, maxforce = 0, r = 5, in_cell = 0, lifespan = 100,spin = 100)
            self.gluList.append(glu)
            
             
               
