from GlutProtein import GlutProtein

class GlutProteinSystem:
    def __init__(self):
        self.glut_list = []
        for i in range(6):
            self.glut_list.append(GlutProtein(20 + 60*i))
        
    
    def update(self):
            pass
    
    def display(self):
        for glut in self.glut_list:
            glut.display()
