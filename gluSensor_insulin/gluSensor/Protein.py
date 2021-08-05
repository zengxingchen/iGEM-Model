import random
class Protein:
    def __init__(self, position, velocity, acceleration, mass, top_speed, maxforce, in_cell, quadrant,lifespan, type, r = 20):#GAL4:type = 0 VP16 type = 1 complex type = 2;insulin: type = 3
        # some attributes have not been used(mass, in_cell, quadrant)
        self.position = position 
        self.velocity = velocity
        self.acceleration = acceleration
        self.mass = mass
        self.top_speed = top_speed
        self.maxforce = maxforce
        self.r = r
        self.in_cell = in_cell if type != 'insulin' else random.randint(0,2)
        self.quadrant = quadrant
        self.lifespan = lifespan
        self.type = type
        
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.top_speed)
        self.position.add(self.velocity)
        self.acceleration.mult(0) # reset the velocity
        
    def display(self):
        if self.type == "Gal4":
            self.r = 20
            noStroke()
            fill(204, 102, 0)
            ellipse(self.position.x, self.position.y, self.r, self.r)
        elif self.type == "VP16":
            self.r = 20
            noStroke()
            fill(255, 182, 193)
            ellipse(self.position.x, self.position.y, self.r, self.r)
        elif self.type == "Complex":
            self.r = 30
            noStroke()
            fill(255 , 20, 147)
            ellipse(self.position.x, self.position.y, self.r, self.r)
        elif self.type == "insulin":
            self.r = 20/1.732
            noStroke()
            fill(255, 140, 0)
            beginShape()
            vertex(self.position.x,self.position.y - 11.54)
            vertex(self.position.x - 10,self.position.y + 5.78)
            vertex(self.position.x + 10,self.position.y + 5.78)
            endShape(CLOSE)
    
    def check_cell_edge(self, cell):
        if self.in_cell == 1 and PVector.dist(self.position, cell.position) >= cell.r:
            self.velocity.x *= random.uniform(-0.5,-2)
            self.velocity.y *= random.uniform(-0.5,-2)

    def check_edge(self):
        if self.position.x < 0 or self.position.x > width - 250:
            self.velocity.x *= -1
            self.velocity.y *= 1
        elif self.position.y < 0 or self.position.y > height:
            self.velocity.y *= -1
            self.velocity.x *= 1
    
    def protein_dead(self):
        if self.lifespan <= 0:
            return 1
        else:
            return 0       
