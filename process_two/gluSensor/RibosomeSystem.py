from Ribosome import Ribosome
import random
class RibosomeSystem:
    def __init__(self, cell):
        self.ribosome_list = []
        for i in range(5):
            self.ribosome_list.append(Ribosome(PVector.add(cell.position, PVector(cell.r * random.uniform(-0.5,0.5), cell.r * random.uniform(-0.5,0.5)))))


    def update(self, protein_system, insulin_system):
        for ribo in self.ribosome_list:
            ribo.update()
            if ribo.free_time <= 0:
                if ribo.mrna is None:
                    ribo.find_mrna(protein_system.mrna_list) # in some cases, there is no free mrna
                if ribo.mrna:
                    if ribo.status == 0:
                        ribo.seek(ribo.mrna.start)
                    elif ribo.status == 1:
                        ribo.seek(ribo.mrna.end)
                        ribo.translate(insulin_system)
        
        

    def display(self):
        for ribo in self.ribosome_list:
            ribo.display()

    def check(self, cell):
        for ribo in self.ribosome_list:
            ribo.check_cell_edge(cell)


    
