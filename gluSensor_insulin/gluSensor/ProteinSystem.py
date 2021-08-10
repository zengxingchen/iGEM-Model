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
        
        for mrna in self.mrna_list:
            mrna.update()
            
        for mirna in self.mirna_list:  # miRNA to find the mRNA and degrades it
            mirna.update()
            if mirna.mrna is None:
                mirna.find_mrna(self.mrna_list) # in some cases, there is no free mrna
            if mirna.mrna:
                if mirna.status == 0:
                    if mirna.seek(PVector((mirna.mrna.start.x + mirna.mrna.end.x)/2, (mirna.mrna.start.y + mirna.mrna.end.y)/2)):
                        self.mrna_list.remove(mirna.mrna)
                        self.mirna_list.remove(mirna)
                        
                                
                        

            
    def check(self, cell, sensor):
        for pro in self.protein_list:
            pro.check_cell_edge(cell)
            pro.check_edge()
            if pro.protein_dead():
                self.protein_list.remove(pro)
            if pro.type != "insulin":
                continue     
            for receptor in self.ins_receptor.receptor_list:
                if PVector.dist(pro.position,receptor.position) <= receptor.r:
                    pro.velocity = PVector(0,0)
                    pro.acceleration = PVector(0,0)
                    self.add_mirna(sensor.position.get())
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

    def add(self, position, type):
        """
        Args: 
            type: the protein type, like "Gal4", "VP16", "Complex", "insulin"
        """
        protein = Protein(position = position.get(), velocity = PVector(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0)), 
                    acceleration = PVector(0,0), mass = 0, top_speed = 1, maxforce = 0, in_cell = 1, quadrant = 0, lifespan = 100, type = type)
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
                if vp.type != "VP16":
                    continue
                if PVector.dist(gal.position, vp.position) <= gal.r + vp.r:
                    position = PVector((gal.position.x + vp.position.x) / 2, (gal.position.y + vp.position.y) / 2)
                    self.add(position, type = "Complex")
                    self.protein_list.remove(gal)
                    self.protein_list.remove(vp)
                    break


    
       
            
            
