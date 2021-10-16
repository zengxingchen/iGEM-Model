from Cell import Cell
from Cell import TissueCell
from GlucoseSystem import GlucoseSystem
from ProteinSystem import ProteinSystem
from ProteinSystem import InsulinSystem
from SensorSystem import SensorSystem
from ReceptorSystem import ReceptorSystem
from RibosomeSystem import RibosomeSystem
from GlutProteinSystem import GlutProteinSystem
from TissueCellSystem import TissueCellSystem
import random

class TissueSystem:
    def __init__(self):
        self.tissuecell_list = []
        self.tissuecell_list.append(TissueCellSystem(position = PVector(400, 300), id = 1))
        self.tissuecell_list.append(TissueCellSystem(position = PVector(1300, 300), id = 2))    
        self.tissuecell_list.append(TissueCellSystem(position = PVector(850, 1100), id = 3))
        self.glucose_system = GlucoseSystem()
        self.insulin_system = InsulinSystem()
        self.glut_list = [self.tissuecell_list[0].glutsystem.glut_list[4], self.tissuecell_list[0].glutsystem.glut_list[3], self.tissuecell_list[0].glutsystem.glut_list[2],self.tissuecell_list[0].glutsystem.glut_list[1], self.tissuecell_list[1].glutsystem.glut_list[4], self.tissuecell_list[1].glutsystem.glut_list[5],self.tissuecell_list[1].glutsystem.glut_list[0], self.tissuecell_list[1].glutsystem.glut_list[1], self.tissuecell_list[2].glutsystem.glut_list[5], self.tissuecell_list[2].glutsystem.glut_list[3],self.tissuecell_list[2].glutsystem.glut_list[0], self.tissuecell_list[2].glutsystem.glut_list[2]]
    
    def update(self):
        for cell in self.tissuecell_list:
            cell.update()
        self.glucose_system.update()
        self.insulin_system.update()
    
    def insulin_check(self, transinsulinlist):
        self.insulin_system.protein_list += transinsulinlist
    
    
    def display(self):
        for cell in self.tissuecell_list:
            cell.display()
        self.glucose_system.display()
        self.insulin_system.display()
    
    def check(self):
        for cell in self.tissuecell_list:
            cell.cell.check()
            self.glucose_system.check(cell.cell, self.glut_list)
        self.insulin_system.checkoutside(self.tissuecell_list)
    
    def add_glu_out(self):
        self.glucose_system.add(num = 4, in_cell = 0)
                           
