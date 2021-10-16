from Cell import Cell
class GlutProtein:
    def __init__(self, cell, theta):
        self.theta = theta
        self.position = PVector(cell.position.x + (cell.r + cell.thick / 3.5) * cos(radians(theta)), cell.position.y + (cell.r + cell.thick / 3.5) * sin(radians(theta)))
        gap = PVector(40 * cos(radians(theta)), 40 * sin(radians(theta)))
        self.start = PVector.add(self.position, gap)
        self.end = PVector.sub(self.position, gap)
        self.status = 0
        self.id = cell.id
        
    def display(self,):  # The coordinate system is transformed to facilitate the determination of its position on the cell membrane
        noStroke()
        pushMatrix()
        translate(self.position.x, self.position.y)
        rotate(radians(self.theta))
        # cover the edge of cell
        fill(248, 248, 255)
        ellipse(0, 0, 15, 15)
        fill(191,239,255)
        ellipse(0, 0 - 12,60,20)
        ellipse(0, 0 + 12,60,20)        
        popMatrix()

class InsulinRecipient(GlutProtein):
    def __init__(self, cell, theta):
        GlutProtein.__init__(self, cell, theta)
        gap = PVector(3 * cos(radians(theta)), 3 * sin(radians(theta)))
        self.start = PVector.add(self.position, gap)
        
    def display(self,):  # The coordinate system is transformed to facilitate the determination of its position on the cell membrane
        fill(1, 130, 231)
        ellipse(self.position.x, self.position.y, 20, 20)        

        
