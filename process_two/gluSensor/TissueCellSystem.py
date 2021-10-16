from Cell import Cell
from Cell import TissueCell
from GlucoseSystem import GlucoseSystem
from ProteinSystem import ProteinSystem
from SensorSystem import SensorSystem
from ReceptorSystem import ReceptorSystem
from RibosomeSystem import RibosomeSystem
from GlutProteinSystem import GlutProteinSystem
from GlutProteinSystem import InsulinRecipientSystem
from ProteinSystem import InsulinSystem
import random


class TissueCellSystem:
    def __init__(self, position, id, cellR=250, cell_Thick=15, sensorR=20):
        self.cell = TissueCell(cellR, cell_Thick, position, id)
        '''
        self.cell_list.append(TissueCell(cellR, cell_Thick, PVector(1100, 320)))
        self.cell_list.append(TissueCell(cellR, cell_Thick, PVector(1170, 900)))
        self.cell_list.append(TissueCell(cellR, cell_Thick, PVector(600, 850)))
        '''
        self.receptor_system = ReceptorSystem()
        self.sensor_system = SensorSystem(self.cell)
        self.protein_system = ProteinSystem()
        self.glutsystem = GlutProteinSystem(self.cell)
        self.irsystem = InsulinRecipientSystem(self.cell)
        
        
        
    def update(self):
        """
        Call each element's update function one by one.
        """
   
        self.cell.update()
        '''
        self.receptor_system.update()
        '''
        self.sensor_system.updateOnly()
        self.protein_system.update()
        self.glutsystem.update()
    
            
    
        '''
        self.ribosome_system.update(self.protein_system)
    
        if self.cell.light:
            self.protein_system.compound()
        
       '''
        

    def display(self):
        """
        Call each element's display function one by one.
        """
        self.cell.display()
        '''
        self.sensor_system.displayOnly()
        self.receptor_system.display()
        '''
        self.glutsystem.display()
        self.irsystem.display()
        self.protein_system.display()
        '''
        self.ribosome_system.display()
        '''
        

        '''
        def check(self):
        
        num = self.glucose_system.check(self.cell, self.sensor_system.sensor_list[0], self.glut_system.glut_list)
        self.sensor_system.sensor_list[0].add_num(num)
    
        self.ribosome_system.check(self.cell)
        
        self.protein_system.check(self.cell, self.sensor_system.sensor_list[3])
        self.add_insulin(self.sensor_system.sensor_list[0].position.get())
        
        if(self.sensor_system.sensor_list[0].get_num() >= 20):
            self.add_mrna(self.sensor_system.sensor_list[0].position.get())
            self.sensor_system.sensor_list[0].set_num(0)
           

        for ins in self.protein_system.protein_list:
            if ins.type == "insulin" and ins.in_cell == 1:
                for glu in self.glucose_system.gluList:
                    if glu.in_cell == 1 and PVector.dist(glu.position, ins.position) <= 30:
                        glu.lifespan -= 0.5
        
        


    def add_mrna(self, position):
        self.protein_system.add_mrna(position)

    

    def add_gal4(self, position):
        self.protein_system.add(position, type="Gal4", status = 0)

    def add_insulin(self, position):
        for complex in self.protein_system.protein_list:
            if complex.type == "Complex" and PVector.dist(self.sensor_system.sensor_list[2].position, complex.position) <= self.sensor_system.sensor_list[2].r:
            
                self.protein_system.add(position, type="insulin", status = 0)
                
                self.add_mrna(self.sensor_system.sensor_list[0].position.get())
                complex.velocity = PVector(0, 0)
                complex.acceleration = PVector(0, 0)
                complex.lifespan = complex.lifespan - 20
            
    def add_glu_in(self, position):
        self.glucose_system.add(num = 50, in_cell = 1)
    '''
