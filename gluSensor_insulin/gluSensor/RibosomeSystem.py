from Ribosome import Ribosome
class RibosomeSystem:
    def __init__(self):
        self.ribosome_list = []
        self.ribosome_list.append(Ribosome(600, 600))

    def update(self, protein_system):
        for ribo in self.ribosome_list:
            ribo.update()
            if ribo.free_time <= 0:
                ribo.find_mrna(protein_system.mrna_list)
                if ribo.mrna and ribo.status == 0:
                    ribo.seek(ribo.mrna.start)
                elif ribo.mrna and ribo.status == 1:
                    ribo.seek(ribo.mrna.end)
                    ribo.translate(protein_system)

    def display(self):
        for ribo in self.ribosome_list:
            ribo.display()

    def check(self, cell):
        for ribo in self.ribosome_list:
            ribo.check_cell_edge(cell)
