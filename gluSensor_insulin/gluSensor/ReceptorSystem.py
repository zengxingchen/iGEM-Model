from InsulinReceptor import InsulinReceptor

class ReceptorSystem:
    def __init__(self):
        self.receptor_list = []
        for i in  range(6):
            self.receptor_list.append(InsulinReceptor(50 + 60*i))
        
    
    
    def update(self):
        pass

    
    def display(self):
        for insR in self.receptor_list:
            insR.display()
