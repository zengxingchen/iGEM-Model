import random
class Ribosome:
    def __init__(self, x, y):
        """
        Args: mrna: the mRNA the Ribosome is going to translate
              target: the destination, we have two possible values {mrna.start, mrna.end}
              
        """
        self.position = PVector(x, y)
        self.velocity = PVector(random.uniform(-1, 1), random.uniform(-1, 1))
        self.acceleration = PVector(0, 0) # Ribosome has no initial acceleration
        self.r = 15
        self.max_speed = 1
        self.mrna = None
        self.target = None
        self.status = 0
        self.flag = 1

    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.max_speed)
        self.position.add(self.velocity)
        self.acceleration.mult(0) # reset the velocity
        
    def display(self):
        """
        draw the mRNA
        """
        noStroke()
        fill(204,204,0)
        ellipse(self.position.x,self.position.y, self.r, self.r)
        ellipse(self.position.x,self.position.y + 0.5 * self.r, 25, 15)

    def apply_force(self, force):   
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    # def translate(self):
    #     if(self)
    #     pass

    # A method that calculates and applies a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    def seek(self, target):
        """
        DESCR: the core idea of the method is to use vector' subtraction of change the velocity
               every frame, so finally we can get to the destination we expected
        """
        desired = PVector.sub(target, self.position)
        # PVector.mag() returns the magnitude of the vector
        distance = desired.mag()
        if (distance == 0):
            return
        # Normalize desired and scale to maximum speed
        desired.normalize()
        desired.mult(self.max_speed)
        steer = PVector.sub(desired, self.velocity)
        if (distance < 20): # Reduce speed to prevent shock
            steer = PVector.mult(steer, 0.1)
        self.apply_force(steer)
        if (distance < 1): # we have closely reached the start of mrna, now we changed our destination
            self.target = self.mrna.end
            self.status = 1
            self.maxspeed = 0.5

    def translate(self, protein_system):
        if(self.check() and self.flag == 1):
            protein_system.add(position = self.mrna.end, type = "Gal4")
            self.flag = 0

    def check(self):
        if(self.target):
            distance = PVector.sub(self.target, self.position)
        if(self.status == 1 and distance.mag() < 1):
            return True

    def follow(self, mrna_list):
        if self.target is None:
            for mrna in mrna_list:
                if mrna.status == 0 and self.target is None: # mRNA is free 
                    self.mrna = mrna
                    self.target = mrna.start
                    self.seek(self.target)
                    break
        else:
            self.seek(self.target) 
                # self.produce()
  

    def check_cell_edge(self, cell):
        if PVector.dist(self.position, cell.position) >= cell.r:
            self.velocity.x *= random.uniform(-0.5,-2)
            self.velocity.y *= random.uniform(-0.5,-2)

    
