import random
class Protein:
    def __init__(self, position, velocity, acceleration, mass, topSpeed, maxforce, r, inCell, quadrant,lifespan,type):#GAL4:type = 0 VP16 type = 1 complex type = 2;insulin: type = 3
        # some attributes have not been used(mass, inCell, quadrant)
        self.position = position 
        self.velocity = velocity
        self.acceleration = acceleration
        self.mass = mass
        self.topSpeed = topSpeed
        self.maxforce = maxforce
        self.r = r
        self.inCell = inCell
        self.quadrant = quadrant
        self.lifespan = lifespan
        self.type = type
    
    def getDirection(self):
        direct_x = 1 if self.velocity.x >= 0 else -1
        direct_y = 1 if self.velocity.y >= 0 else -1
        
        return direct_x, direct_y
        
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.topSpeed)
        self.position.add(self.velocity)
        self.acceleration.mult(0) # reset the velocity
        
    def display(self):
        if self.type == "Gal4":
            noStroke()
            fill(204, 102, 0)
            ellipse(self.position.x, self.position.y, self.r, self.r)
        elif self.type == "VP16":
            noStroke()
            fill(255, 182, 193)
            ellipse(self.position.x, self.position.y, self.r, self.r)
        elif self.type == "Complex":
            noStroke()
            fill(255 , 20, 147)
            ellipse(self.position.x, self.position.y, self.r, self.r)
        elif self.type == "insulin":
            noStroke()
            fill(255, 140, 0)
            # ellipse(self.position.x, self.position.y, self.r, self.r+5)
            beginShape()
            vertex(self.position.x,self.position.y - 11.54)
            vertex(self.position.x - 10,self.position.y + 5.78)
            vertex(self.position.x + 10,self.position.y + 5.78)
            endShape(CLOSE)
    
    def checkCellEdges(self, cell):
        if self.inCell == 1 and PVector.dist(self.position, cell.position) >= cell.r:
            self.velocity.x *= random.uniform(-0.5,-2)
            self.velocity.y *= random.uniform(-0.5,-2)

    def checkEdges(self):
        if self.position.x < 0 or self.position.x > width - 250:
            self.velocity.x *= -1
            self.velocity.y *= 1
        elif self.position.y < 0 or self.position.y > height:
            self.velocity.y *= -1
            self.velocity.x *= 1
    
    def proteinDead(self):
        if self.lifespan <= 0:
            return 1
        else:
            return 0       
