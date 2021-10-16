from Protein import Protein
from mRNA import mRNA
from ReceptorSystem import ReceptorSystem
import random
class ProteinSystem:
    def __init__(self):
        self.ins_receptor = ReceptorSystem()
        self.protein_list = []
        self.mrna_list = []
       
        
    
    def display(self):
        for pro in self.protein_list:
            pro.display()
        
        for mrna in self.mrna_list:
            mrna.display()
        
            
    def update(self):
        for pro in self.protein_list:
            pro.update()
            if pro.type == "Complex":
                pro.lifespan -= 0.001
        
        for mrna in self.mrna_list:
            mrna.update()
                
                        
                        

            
    def check(self, cell):
        for pro in self.protein_list:
            pro.check_cell_edge(cell)
            pro.check_edge()
            if pro.protein_dead():
                self.protein_list.remove(pro)

        for mrna in self.mrna_list:
            mrna.check_cell_edge(cell)
            
    
                              

    def add_mrna(self, position):
        mrna = mRNA(position)
        self.mrna_list.append(mrna)
        
    
    def add(self, position, type, status):
        """
        Args: 
            type: the protein type, like "Gal4", "VP16", "Complex", "insulin"
        """
        protein = Protein(position = position.get(), velocity = PVector(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0)), 
                    acceleration = PVector(0,0), mass = 0, top_speed = 1, maxforce = 0, in_cell = 1, quadrant = 0, lifespan = 100, type = type, status = status)
        self.protein_list.append(protein)
    
    def compound(self):
        """
        Make two proteins form a complex
        avoid to use the index of list for unpredictable index error in animation
        """
        for gal in self.protein_list:
            if gal.type != "Gal4": 
                continue
            for vp in self.protein_list:
                if vp.type != "VP16" or vp.status == 0:
                    continue
                if PVector.dist(gal.position, vp.position) <= gal.r + vp.r:
                    position = PVector((gal.position.x + vp.position.x) / 2, (gal.position.y + vp.position.y) / 2)
                    self.add(position, type = "Complex", status = 0)
                    self.protein_list.remove(gal)
                    self.protein_list.remove(vp)
                    break

    def activate_vp(self):  #activate VP16
        for vp in self.protein_list:
            if vp.type != "VP16":
                continue
            prob = random.randint(0,20)
            if prob <= 3 and vp.status == 1:
                vp.status = 0
            else:
                vp.status = 1
            
    def inactivate_vp(self):  #inactivate VP16
        for vp in self.protein_list:
            if vp.type != "VP16":
                continue
            prob = random.randint(0,20)
            if prob <= 2 and vp.status == 1:
                vp.status = 0
       
    def count_mrna_num(self):
        num = 0
        for m in self.mrna_list:
            num +=1
        return num
    
    
    def count_protein_num(self, type, status):
        num = 0
        for p in self.protein_list:
            if p.type == type and p.status == status:
                num += 1
            else:
                continue
        return num        
            
