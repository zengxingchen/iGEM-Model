from Cell import Cell
class InsulinReceptor:
    # global Width, Height
    # Width = 1600
    # Height = 1200
    def __init__(self, theta, r = 30):
        # self.position = position 
        self.r = r
        self.theta = theta
        self.position = PVector(Cell.sketch_Width/2 + (Cell.r + Cell.thick / 3.5) * cos(radians(theta)), Cell.sketch_Height/2 + (Cell.r + Cell.thick / 3.5) * sin(radians(theta)))
        gap = PVector(40 * cos(radians(theta)), 40 * sin(radians(theta)))
        self.start = PVector.add(self.position, gap)
        self.end = PVector.sub(self.position, gap)
        self.status = 0
        
        
    def display(self):
        noStroke()
        pushMatrix()
        translate(self.position.x, self.position.y)
        rotate(radians(self.theta))
        fill(255, 140, 140)
        ellipse(0, 0 + 12, 30, 35)
        
        popMatrix()

    def update(self):
        pass
