from Protein import Protein
from mRNA import mRNA
from miRNA import miRNA
from ReceptorSystem import ReceptorSystem
import random
class ProteinSystem:
    def __init__(self):
        self.ins_receptor = ReceptorSystem()
        self.protein_list = []
        self.mrna_list = []
        self.mirna_list = []
        
    
    def display(self):
        for pro in self.protein_list:
            pro.display()
        
        for mrna in self.mrna_list:
            mrna.display()
        
        for mirna in self.mirna_list:
            mirna.display()
            
    def update(self):
        for pro in self.protein_list:
            pro.update()
            if pro.status == 0 or pro.status == 1:
                pro.lifespan -= 0.0001
            if pro.type != "insulin" and pro.status != 2:
                continue
            pro.lifespan -= 0.005 * (20 - self.count_mrna_num())
        
        for mrna in self.mrna_list:
            mrna.update()
            
        for mirna in self.mirna_list:  # miRNA to find the mRNA and degrades it
            mirna.update()
            if mirna.mrna is None:
                mirna.find_mrna(self.mrna_list) # in some cases, there is no free mrna
            if mirna.mrna:
                if mirna.seek(PVector((mirna.mrna.start.x + mirna.mrna.end.x)/2, (mirna.mrna.start.y + mirna.mrna.end.y)/2)):
                    if frameCount % 80 == 0:   #miRNA and mRNA are combined , stay for a while and then disappear
                        self.mrna_list.remove(mirna.mrna)
                        self.mirna_list.remove(mirna)
                        
    def check_status(self, cell):
        for insulin in self.protein_list:
            if insulin.type != "insulin":
                continue
            if insulin.status == 0 and PVector.dist(insulin.position, cell.position) >=  cell.r:
                insulin.change_status()
                continue
            if insulin.status == 1 and PVector.dist(insulin.position, cell.position) >= cell.r + 0.8 * cell.thick:
                insulin.change_status()
                insulin.in_cell = 0                        
                        

            
    def check(self, cell, sensor):
        self.find(sensor.position)
        self.add_RAS(cell, num = 1)
        for pro in self.protein_list:
            pro.check_incell_edge(cell)
            pro.check_outcell_edge(cell)
            pro.check_edge()
            if pro.protein_dead():
                self.protein_list.remove(pro)

        for mrna in self.mrna_list:
            mrna.check_cell_edge(cell)
            
        for mirna in self.mirna_list:
            mirna.check_cell_edge(cell)
            
                              

    def add_mrna(self, position):
        mrna = mRNA(position)
        self.mrna_list.append(mrna)
        
    def add_mirna(self, position):
        mirna = miRNA(position)
        self.mirna_list.append(mirna)
   
        
            
    def find(self, target):
        for ras in self.protein_list:
            if ras.type != "RAS":
                continue
            ras.seek(target)    

    def add(self, position, type, status, num):
        """
        Args: 
            type: the protein type, like "Gal4", "VP16", "Complex", "insulin", "RAS"
        """
        for i in range(num):
            protein = Protein(position = position.get(), velocity = PVector(random.uniform(-2.0,1.0),random.uniform(-2.0,1.0)), 
                        acceleration = PVector(0,0), mass = 0, top_speed = 1, maxforce = 0, in_cell = 1, quadrant = 0, lifespan = 100.0, type = type, status = status)
            self.protein_list.append(protein)
    
    def add_RAS(self, cell, num):
        for ins in self.protein_list:
            if ins.type != "insulin":
                continue
            for sensor in self.ins_receptor.receptor_list:
                if ins.status == 2 and PVector.dist(sensor.position, ins.position) <= sensor.r:
                    self.add(sensor.position, type = "RAS", status = 0, num = num)
                    ins.velocity.x *= 0
                    ins.velocity.y *= 0
                    self.protein_list.remove(ins)
    
    
    def count_protein_num(self, type, status):
        num = 0
        for pro in self.protein_list:
            if pro.type == type and pro.status == status:
                num += 1
            else:
                continue
        return num 
    
    

    def count_mrna_num(self):
        num = 0
        for m in self.mrna_list:
            num +=1
        return num
       
            
    def count_mirna_num(self):
        num = 0
        for m in self.mirna_list:
            num +=1
        return num       

            
