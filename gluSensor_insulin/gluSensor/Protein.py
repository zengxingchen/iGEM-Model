import random
class Protein:
    def __init__(self, position,type):
        self.position = position 
        self.velocity = PVector(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0))
        self.acceleration = PVector(0,0)
        self.top_speed = 1
        self.r = 20
        self.in_cell = 1 if type != 'insulin' else random.randint(0,2)
        self.lifespan = 100
        self.type = type
        self.spin = 100

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
            ellipse(self.position.x, self.position.y, self.r, self.r - 5)
        elif self.type == "VP16":
            self.r = 20
            noStroke()
            fill(255, 182, 193)
            ellipse(self.position.x, self.position.y, self.r, self.r - 5)
        elif self.type == "Complex":
            self.r = 20
            noStroke()
            fill(204, 102, 0)
            ellipse(self.position.x - 5, self.position.y, self.r, self.r - 5)
            fill(255, 182, 193)
            ellipse(self.position.x + 5, self.position.y, self.r, self.r - 5)
        elif self.type == "insulin":
            self.spin -= 0.01
            self.r = 20/1.732
            noStroke()
            fill(255, 140, 0)
            x1 = self.position.x + self.r * cos(radians(100 * self.spin))
            y1 = self.position.y + self.r * sin(radians(100 * self.spin))
            x2 = self.position.x + self.r * cos(radians(120 + 100 * self.spin))
            y2 = self.position.y + self.r * sin(radians(120 + 100 * self.spin))        
            x3 = self.position.x + self.r * cos(radians(240 + 100 * self.spin))
            y3 = self.position.y + self.r * sin(radians(240 + 100 * self.spin))
            beginShape()
            vertex(x1, y1)
            vertex(x2, y2)
            vertex(x3, y3)
            endShape(CLOSE)
            fill(255,255,255)
            
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
