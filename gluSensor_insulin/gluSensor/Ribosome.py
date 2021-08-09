import random
class Ribosome:
    def __init__(self, position):
        """
        Args: mrna: the mRNA the Ribosome is going to translate
              target: the destination, we have two possible values {mrna.start, mrna.end}
        """
        self.position = position
        self.velocity = PVector(random.uniform(-1, 1), random.uniform(-1, 1))
        self.acceleration = PVector(0, 0) # Ribosome has no initial acceleration
        self.r = 15
        self.max_speed = 1
        self.mrna = None
        self.status = 0
        self.free_time = 0

    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.max_speed)
        self.position.add(self.velocity)
        self.acceleration.mult(0) # reset the velocity
        if(self.free_time > 0):
            self.free_time -= 1
        
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
 
    def seek(self, target):
        """
        DESCR: the core idea of the method is to use vector' subtraction to change the velocity
               every frame, so finally we can get to the destination we expected
        Hint:
        """
        desired = PVector.sub(target.get(), self.position)
        distance = desired.mag() # returns the magnitude of the vector
        if (distance == 0):
            self.status = 1
            return
        desired.normalize()
        desired.mult(self.max_speed)
        steer = PVector.sub(desired, self.velocity)
        if (distance < 20): # reduce speed to prevent shock
            steer = PVector.mult(steer, 0.1)
        self.apply_force(steer)

        if (distance < 1): # we have closely reached the start of mrna, now we changed our destination
            self.status = 1

    def translate(self, protein_system):
        if(self.check()):
            protein_system.add(position = self.mrna.end, type = "Gal4")
            self.reset()
            

    def reset(self):
        self.mrna.status = 0
        self.mrna = None
        self.status = 0
        self.velocity = PVector(random.uniform(-1, 1), random.uniform(-1, 1))
        self.free_time += 200

    def check(self):
        distance = PVector.sub(self.mrna.end, self.position)
        if(self.status == 1 and distance.mag() < 1):
            return True
        else:
            return False

    def find_mrna(self, mrna_list):
        for mrna in mrna_list:
            if mrna.status == 0: # mRNA is free
                self.mrna = mrna
                self.mrna.status = 1
                break

    def check_cell_edge(self, cell):
        if PVector.dist(self.position, cell.position) >= cell.r:
            self.velocity.x *= random.uniform(-0.5,-2)
            self.velocity.y *= random.uniform(-0.5,-2)

    
