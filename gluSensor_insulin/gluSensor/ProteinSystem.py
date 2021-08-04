from Protein import Protein
import random
class ProteinSystem:
    def __init__(self):
        self.proteinList = [] # all kinds of proteins list
    
    
    def display(self):
        for pro in self.proteinList:
            pro.display()
            
    def update(self):
        for pro in self.proteinList:
            pro.update()
            
    def check(self, cell, sensor):
        for pro in self.proteinList:
            pro.checkCellEdges(cell)
            pro.checkEdges()    
            if pro.proteinDead():
                self.proteinList.remove(pro)
    
    def addGal(self, position):
        for i in range(1):
            gal = Protein(position = position.get(), velocity = PVector(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0)), 
                      acceleration = PVector(0,0), mass = 0, topSpeed = 1, maxforce = 0, r = 20, inCell = 1, quadrant = 0, lifespan = 100,type = "Gal4")
            self.proteinList.append(gal)
    
    def addVp(self, position):
        for i in range(1): 
            vp = Protein(position = position.get(), velocity = PVector(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0)), 
                      acceleration = PVector(0,0), mass = 0, topSpeed = 1, maxforce = 0, r = 20, inCell = 1, quadrant = 0, lifespan = 100,type = "VP16")
            self.proteinList.append(vp)
            
    def addComplex(self, position):
        for i in range(1):
            complex = Protein(position = position.get(), velocity = PVector(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0)), 
                      acceleration = PVector(0,0), mass = 0, topSpeed = 1, maxforce = 0, r = 30, inCell = 1, quadrant = 0, lifespan = 100,type = "Complex")
            self.proteinList.append(complex)
            
    def addInsulin(self, position):
        for i in range(1):
            insulin = Protein(position = position.get(), velocity = PVector(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0)), 
                      acceleration = PVector(0,0), mass = 0, topSpeed = 1, maxforce = 0, r = 20/1.732, inCell = random.randint(0,2), quadrant = 0, lifespan = 200,type = "insulin")
            self.proteinList.append(insulin) 
    
   
    
    def compound(self):
        for g in self.proteinList:
            if g.type == "Gal4":
                gal = g
                for v in self.proteinList:
                    if v.type == "VP16":
                        vp = v
                        if PVector.dist(gal.position, vp.position) <= gal.r + vp.r:
                            position = PVector((gal.position.x + vp.position.x)/2,(gal.position.y + vp.position.y)/2)
                            self.addComplex(position)
                            self.proteinList.remove(gal)
                            self.proteinList.remove(vp)
                            break 
    
       
            
            
