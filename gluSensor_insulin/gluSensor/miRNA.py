import random
class miRNA:
    def __init__(self, position):
        self.position = position
        self.velocity = PVector(random.uniform(-1, 1), random.uniform(-1, 1))
        self.acceleration = PVector(0, 0) # miRNA has no initial acceleration
        self.r = 20
        self.max_speed = 1
        self.mrna = None
        self.status = 0
        self.start = self.position
        self.end = PVector.add(self.position, PVector(45, 0))

        
        
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.max_speed)
        self.position.add(self.velocity)
        self.acceleration.mult(0) # reset the velocity
        self.end = PVector.add(self.position, PVector(45, 0))
        
    def display(self):    
        x = self.position.x 
        y = self.position.y
        num = 5             # change the lenth of mRNA
        strokeWeight(2)     # Change the thickness and color of the lines
        stroke(144,238,144)
        for i in range(num):
            line(x, y, x + 3, y + 3)
            line(x + 3, y + 3, x + 6, y - 3)
            line(x + 6, y - 3, x + 9, y)
            x = x + 9
            y = y
        
        
    def apply_force(self, force):   
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)
        
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
            self.velocity = PVector(0,0)
            self.acceleration = PVector(0,0)
            self.status = 1
            return True
            
        
        
    def check(self):
        distance = PVector.sub(self.mrna.end, self.position)
        if(self.status == 1 and distance.mag() < 1):
            return True
        else:
            return False
        
        
    def find_mrna(self, mrna_list):
        for mrna in mrna_list:
            if mrna.status_mirna == 0:  # mRNA is free
                self.mrna = mrna
                self.mrna.status_mirna = 1
                break
              
        
    
    def check_cell_edge(self, cell):
        # check the cell_edge with both the start_position and end_position of the miRNA 
        if PVector.dist(self.position, cell.position) >= cell.r or PVector.dist(self.end, cell.position) >= cell.r:
            self.velocity.x *= random.uniform(-0.5,-2)
            self.velocity.y *= random.uniform(-0.5,-2)
            
            
            
            
        
        
        
