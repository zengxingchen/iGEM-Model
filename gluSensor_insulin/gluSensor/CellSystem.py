from Cell import Cell
from GlucoseSystem import GlucoseSystem
from ProteinSystem import ProteinSystem
from SensorSystem import SensorSystem
from ReceptorSystem import ReceptorSystem
from RibosomeSystem import RibosomeSystem
from GlutProteinSystem import GlutProteinSystem
import random


class CellSystem:
    def __init__(self, cellR=400, cell_Thick=15, sensorR=40):
        self.cell = Cell(cellR, cell_Thick)
        self.receptor_system = ReceptorSystem()
        self.sensor_system = SensorSystem()
        self.glucose_system = GlucoseSystem()
        self.protein_system = ProteinSystem()
        self.ribosome_system = RibosomeSystem(self.cell)
        self.glut_system = GlutProteinSystem()
        
        
    def update(self):
        """
        Call each element's update function one by one.
        """
        self.cell.update()
        self.receptor_system.update()
        self.glucose_system.update()
        self.sensor_system.update()
        self.protein_system.update()
        self.glut_system.update()
        self.ribosome_system.update(self.protein_system)
        if self.cell.light:
            self.protein_system.compound()
        
       
        

    def display(self):
        """
        Call each element's display function one by one.
        """
        self.cell.display()
        self.sensor_system.display()
        self.receptor_system.display()
        self.glut_system.display()
        self.glucose_system.display()
        self.protein_system.display()
        self.ribosome_system.display()

    def check(self):
        num = self.glucose_system.check(self.cell, self.sensor_system.sensor_list[0], self.glut_system.glut_list)
        self.sensor_system.sensor_list[0].add_num(num)
        self.ribosome_system.check(self.cell)
        self.protein_system.check(self.cell, self.sensor_system.sensor_list[3])
        self.add_insulin(self.sensor_system.sensor_list[2].position.get())
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
        self.protein_system.add(position, type="Gal4")

    def add_insulin(self, position):
        for complex in self.protein_system.protein_list:
            if complex.type == "Complex" and PVector.dist(self.sensor_system.sensor_list[2].position, complex.position) <= self.sensor_system.sensor_list[2].r:
                self.protein_system.add(position, type="insulin")
                complex.velocity = PVector(0, 0)
                complex.acceleration = PVector(0, 0)
                complex.lifespan = complex.lifespan - 20
                
    def add_glu_in(self, position):
        self.glucose_system.add(num = 50, in_cell = 1)

    def add_glu_out(self):
        self.glucose_system.add(num = 2, in_cell = 0)
