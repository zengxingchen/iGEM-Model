from Cell import Cell
from GlucoseSystem import GlucoseSystem
from ProteinSystem import ProteinSystem
from SensorSystem import SensorSystem
from ReceptorSystem import ReceptorSystem
from GlutProteinSystem import GlutProteinSystem
import random


class CellSystem:
    def __init__(self, cellR=400, cell_Thick=15, sensorR=40):
        self.cell = Cell(cellR, cell_Thick)
        self.receptor_system = ReceptorSystem()
        self.sensor_system = SensorSystem()
        self.glucose_system = GlucoseSystem()
        self.protein_system = ProteinSystem()
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

    def check(self):
        num = self.glucose_system.check(self.cell, self.glut_system.glut_list)
        self.sensor_system.sensor_list[1].set_num(num)
        self.protein_system.check(self.cell, self.sensor_system.sensor_list[0])
        self.protein_system.check_status(self.cell)
        self.add_insulin(self.sensor_system.sensor_list[0].position.get())
        self.add_mirna()
        if frameCount % 2 == 0 and frameCount <= 2:     #initial mRNA
            for i in range(15):
                self.add_mrna(self.sensor_system.sensor_list[1].position.get())



    def add_mrna(self, position):
        self.protein_system.add_mrna(position)

    def add_mirna(self):
        for ras in self.protein_system.protein_list:
            if ras.type != "RAS":
                continue
            if PVector.dist(self.sensor_system.sensor_list[0].position, ras.position) <= self.sensor_system.sensor_list[0].r:
                if self.protein_system.count_mirna_num() <= 10:
                    self.protein_system.add_mirna(self.sensor_system.sensor_list[3].position.get())
                    self.protein_system.protein_list.remove(ras)
                else:
                    self.protein_system.protein_list.remove(ras)
        
    def count_protein_num(self, type, status):
        return self.protein_system.count_protein_num(type = type, status = status)
        

    def add_gal4(self, position):
        self.protein_system.add(position, type="Gal4", status = 0, num = 1)

    def add_insulin(self, position):
        if frameCount % (800 / (self.protein_system.count_mrna_num() + 1)) == 0 and self.protein_system.count_mrna_num() > 0:
            self.protein_system.add(position = position, type = "insulin", status = 0, num = 1)
        
                
    def add_glu_in(self, position):
        self.glucose_system.add(num = 50, in_cell = 1)

    def add_glu_out(self):
        self.glucose_system.add(num = 2, in_cell = 0)
