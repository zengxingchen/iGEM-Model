from GlutProtein import GlutProtein
from GlutProtein import InsulinRecipient

class GlutProteinSystem:
    def __init__(self, cell):
        self.glut_list = []
        for i in range(6):
            self.glut_list.append(GlutProtein(cell, 20 + 60*i))
        
    
    def update(self):
            pass
    
    def display(self):
        for glut in self.glut_list:
            glut.display()
            
            
class InsulinRecipientSystem():
    def __init__(self, cell):
        self.IR_list = []
        for i in range(6):
            self.IR_list.append(InsulinRecipient(cell, 50 + 60*i))
        
    
    def update(self):
            pass
    
    def display(self):
        for IR in self.IR_list:
            IR.display()
