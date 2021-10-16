from Protein import Protein
from Protein import Insulin
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
            pro.check_edge()
            if pro.protein_dead():
                self.protein_list.remove(pro)
            if pro.type != "insulin":
                pro.check_cell_edge(cell)
                continue
            '''
            for receptor in self.ins_receptor.receptor_list:
                if PVector.dist(pro.position,receptor.position) <= 3 * receptor.r:
                    pro.velocity = PVector(0,0)
                    pro.acceleration = PVector(0,0)
                    self.add_mirna(sensor.position.get())
                    
                    self.protein_list.remove(pro)
                    
            '''
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
                if vp.type != "VP16": #or vp.status == 0:
                    continue
                if PVector.dist(gal.position, vp.position) <= gal.r + vp.r:
                    position = PVector((gal.position.x + vp.position.x) / 2, (gal.position.y + vp.position.y) / 2)
                    self.add(position, type = "Complex", status = 0)
                    self.protein_list.remove(gal)
                    self.protein_list.remove(vp)
                    break

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




class InsulinSystem(ProteinSystem):
    def __init__(self):
        ProteinSystem.__init__(self)
        self.transinsulinlist = []
        self.IR_threshold = 150
    
    def add(self, position):
        insulin = Insulin(position = position.get(), velocity = PVector(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0)), 
                    acceleration = PVector(0,0), mass = 0, top_speed = 1, maxforce = 0, in_cell = 1, quadrant = 0, lifespan = 100, status = 0)
        self.protein_list.append(insulin)
    
    def check(self, cell, sensor):
        for insulin in self.protein_list:
            if insulin.status == 0 and PVector.dist(insulin.position, cell.position) >=  cell.r:
                insulin.change_status()
                continue
            if insulin.status == 1 and PVector.dist(insulin.position, cell.position) >= cell.r + 0.8 * cell.thick:
                insulin.change_status()
                self.transinsulinlist.append(insulin)
                self.protein_list.remove(insulin)
            if insulin.protein_dead():
                self.protein_list.remove(insulin)
    
    def checkoutside(self, celllist):
        for pro in self.protein_list:
        # try to find the IR
            for cell in celllist:
                pro.check_outcell_edge(cell.cell)
                if pro.status != 3:
                    pro.follow(cell.irsystem.IR_list, self.IR_threshold)
                    # not find glut or close enough to the glut yet
                    if pro.dist_target >= 100:
                        pro.check_outcell_edge(cell.cell)
                else:
                    cell.cell.insulin_num +=1
            if pro.protein_dead():
                self.protein_list.remove(pro)

                
    def display(self):
        for insulin in self.protein_list:
            insulin.display()
            insulin.lifespan -= 0.01
        '''
            for receptor in self.ins_receptor.receptor_list:
                if PVector.dist(pro.position,receptor.position) <= 3 * receptor.r:
                    pro.velocity = PVector(0,0)
                    pro.acceleration = PVector(0,0)
                    self.add_mirna(sensor.position.get())
                    self.protein_list.remove(pro)
        '''
                    
       
            
            
