from Ribosome import Ribosome
class RibosomeSystem:
    def __init__(self):
        self.ribosome_list = []
        self.ribosome_list.append(Ribosome(600, 600))

    def update(self, mrna_list):
        for ribo in self.ribosome_list:
            ribo.update()
            ribo.follow(mrna_list)

    def display(self):
        for ribo in self.ribosome_list:
            ribo.display()

    def check(self, cell):
        for ribo in self.ribosome_list:
            ribo.check_cell_edge(cell)

    def translate(self, protein_system):
        for ribo in self.ribosome_list:
                ribo.translate(protein_system)
        
