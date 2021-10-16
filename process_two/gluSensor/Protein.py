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
        self.in_cell = in_cell  #if type != 'insulin' else random.randint(0,2)
        self.quadrant = quadrant
        self.lifespan = lifespan
        self.type = type
        self.status = status   # status = 1:activate
        self.spin = spin
        
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
            fill(70, 140, 153)
            ellipse(self.position.x - 5, self.position.y, self.r, self.r - 5)
            fill(231, 118, 92)
            ellipse(self.position.x + 5, self.position.y, self.r, self.r - 5)
            
        elif self.type == "insulin":  
            noStroke()
            self.spin -= 0.01
            if self.status == 0 or self.status == 1:
                fill(254, 232, 166)
                ellipse(self.position.x, self.position.y, 3 * self.r, 3 * self.r)
            if self.status == 3:
                self.lifespan -= 0.5
                self.spin += 0.01
            fill(255, 160, 0)
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
        if self.position.x < 0 or self.position.x > width:
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

class Insulin(Protein):
    def __init__(self, position, velocity, acceleration, mass, top_speed, maxforce, in_cell, quadrant, lifespan, status, r = 8, spin = 100, type = "insulin"):
        #status: 0 represents the insulin in the engineer cell, 1 represnts it being conveyed out, 2 represents it in the internal environment, and 3 represents it attached to a tissuecell 
        Protein.__init__(self, position, velocity, acceleration, mass, top_speed, maxforce, in_cell, quadrant,lifespan, type, status, r = 8, spin = 100)
        self.type = "insulin"
        self.target = None
        self.IR = None
        self.dist_target = 10000

    def change_status(self):
        self.status += 1
        if self.status == 1:
            self.velocity = self.velocity * 0.5
        if self.status == 2:
            self.velocity = self.velocity * 2
    
    def check_outcell_edge(self, cell):
        if PVector.dist(self.position, cell.position) < cell.r:
            self.velocity.x *= random.uniform(-0.5,-2)
            self.velocity.y *= random.uniform(-0.5,-2)
    
    def seek(self, target):
        # for debug
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
            self.velocity.mult(0)
            self.change_status()
            
            
    def follow(self, IR_list, IR_threshold):
        min_dist = 10000
        if self.IR == None:
            for IR in IR_list:
                if PVector.dist(IR.position, self.position) <= IR_threshold:
                    self.IR = IR
                    self.target = IR.start
                    break
        # maybe have bot found the glut considering distance
        if self.IR != None:
            self.seek(self.target)
            
    def apply_force(self, force):
        self.acceleration.add(force)
