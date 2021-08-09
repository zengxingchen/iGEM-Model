from Protein import Protein
from MicroRNA import MicroRNA
import random
class ProteinSystem:
    def __init__(self):
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
        
        for mrna in self.mrna_list:
            mrna.update()
            
    def check(self, cell, sensor):
        for pro in self.protein_list:
            pro.check_cell_edge(cell)
            pro.check_edge()    
            if pro.protein_dead():
                self.protein_list.remove(pro)

        for mrna in self.mrna_list:
            mrna.check_cell_edge(cell)

    def add_mrna(self, position):
        mrna = MicroRNA(position)
        self.mrna_list.append(mrna)

    def add(self, position, type):
        """
        Args: 
            type: the protein type, like "Gal4", "VP16", "Complex", "insulin"
        """
        protein = Protein(position = position.get(), type = type)
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


    
       
            
            
