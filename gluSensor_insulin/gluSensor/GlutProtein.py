class GlutProtein:
    def __init__(self, theta,):
        self.theta = theta
        self.position = PVector(800 + (400 + 15 / 3.5) * cos(radians(theta)), 600 + (400 + 15 / 3.5) * sin(radians(theta)))
        gap = PVector(40 * cos(radians(theta)), 40 * sin(radians(theta)))
        self.start = PVector.add(self.position, gap)
        self.end = PVector.sub(self.position, gap)
        self.status = 0
        
    def display(self,):  # The coordinate system is transformed to facilitate the determination of its position on the cell membrane
        noStroke()
        pushMatrix()
        translate(self.position.x, self.position.y)
        rotate(radians(self.theta))
        # cover the edge of cell
        fill(248, 248, 255)
        ellipse(0, 0, 9, 9)
        fill(191,239,255)
        ellipse(0, 0 - 12,60,20)
        ellipse(0, 0 + 12,60,20)
        
        popMatrix()
