import random
class Protein:
    def __init__(self, position, velocity, acceleration, mass, top_speed, maxforce, in_cell, quadrant,lifespan, type, status, r = 20,spin = 100):
        # some attributes have not been used(mass, in_cell, quadrant)
        self.position = position 
        self.velocity = velocity
        self.acceleration = acceleration
        self.mass = mass
        self.top_speed = top_speed
        self.maxforce = maxforce
        self.r = r
        self.in_cell = in_cell  
        self.quadrant = quadrant
        self.lifespan = lifespan
        self.type = type
        self.status = status   # status = 1:activate
        self.spin = spin
        self.target = None
        
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
            if self.status == 1:
                fill(255,178,169)
                ellipse(self.position.x, self.position.y, self.r, self.r - 5)
            else:
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
            self.r = 8
            self.spin -= 0.01
            noStroke()
            if self.status == 0 or self.status == 1:
                fill(254, 223, 112)
                ellipse(self.position.x, self.position.y, 3 * self.r, 3 * self.r)
            fill(155 + self.lifespan, 40 + + self.lifespan, 0)
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
        elif self.type == "RAS":
            self.r = 10
            fill(224, 28, 103)
            ellipse(self.position.x, self.position.y, self.r, self.r)
        
    def seek(self, target):  #The signal molecule(RAS) is directed to look for the nucleus to initiate negative feedback
        desired = PVector.sub(target, self.position)
        distance = desired.mag()
        self.dist_target = distance
        if distance == 0:
            return
        desired.normalize()
        desired.mult(self.top_speed)
        steer = PVector.sub(desired, self.velocity)
        if distance < 20:
            steer = PVector.mult(steer, 0.1)
        self.apply_force(steer)
        if distance < 1:
            self.target = self.glut.end
            self.top_speed = 0.5

    def apply_force(self, force):   
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)
            
                       
                                             
    def check_incell_edge(self, cell):
        if self.type == "insulin":
            return
        if self.in_cell == 1 and PVector.dist(self.position, cell.position) >= cell.r + 5:
            self.velocity.x *= random.uniform(-0.5,-3)
            self.velocity.y *= random.uniform(-0.5,-3)

    def check_outcell_edge(self, cell):
        if self.type != "insulin":
            return
        if self.status == 2 and PVector.dist(self.position, cell.position) <= cell.r + 10 and self.in_cell == 0:
            self.velocity.x *= random.uniform(-0.5,-4)
            self.velocity.y *= random.uniform(-0.5,-4)
            
            



    def check_edge(self):
        if self.position.x < 0 or self.position.x > width - 250: #There are icons on the right side of the canvas
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
   
    def change_status(self):
        if self.type != "insulin":
            return
        self.status += 1
        if self.status == 1:
            self.velocity = self.velocity * 0.5
        if self.status == 2:
            self.velocity = self.velocity * 2
    
