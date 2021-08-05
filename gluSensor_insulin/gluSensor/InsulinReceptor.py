class InsulinReceptor:
    def __init__(self, position):
        self.position = position
        
    def display(self):
        fill(255, 140, 140)
        beginShape()
        vertex(self.position.x - 20, self.position.y - 20)
        vertex(self.position.x + 20, self.position.y - 20)
        vertex(self.position.x + 20, self.position.y + 20)
        vertex(self.position.x - 20, self.position.y + 20)
        endShape(CLOSE)

    def update(self):
        pass