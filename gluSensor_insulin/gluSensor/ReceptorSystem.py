from InsulinReceptor import InsulinReceptor

class ReceptorSystem:
    def __init__(self):
        self.receptor_list = []
        self.receptor_list.append(InsulinReceptor(position=PVector(800, 200)))
        self.receptor_list.append(InsulinReceptor(position=PVector(1200, 600)))
        self.receptor_list.append(InsulinReceptor(position=PVector(400, 600)))
    def update(self):
        pass

    def display(self):
        for ins in self.receptor_list:
            ins.display()