import random
class Ribosome:
    def __init__(self, x, y):
        self.position = PVector(x, y)
        self.velocity = PVector(random.uniform(-1, 1), random.uniform(-1, 1))
        self.acceleration = PVector(0, 0)
        self.r = 15
        self.max_speed = 4
        self.max_force = 0.1

    # def run(self):
    #     self.update()
    #     self.display()
    #     self.follow()

    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.max_speed)
        self.position.add(self.velocity)
        self.acceleration.mult(0) # reset the velocity
        

    # draw the mRNA
    def display(self):
        noStroke()
        fill(204,204,0)
        ellipse(self.position.x,self.position.y, self.r, self.r)
        ellipse(self.position.x,self.position.y + 0.5 * self.r, 25, 15)


    def apply_force(self, force):   
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    # A method that calculates and applies a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    def seek(self, target):
        desired = PVector.sub(target, self.position)
        # PVector.mag() returns the magnitude of the vector
        if (desired.mag() == 0):
            return
        # Normalize desired and scale to maximum speed
        desired.normalize()
        desired.mult(self.max_speed)

        steer = PVector.sub(desired, self.velocity)
        steer.limit(self.max_force)
        self.apply_force(steer)

    def follow(self, mrna_list):
        target = None
        for mrna in mrna_list:
            if mrna.status == 0: # mRNA is free 
                target = mrna.position
                self.seek(target)
                # self.produce()
                break
  

    # def produce():


    def check_cell_edge(self, cell):
        if PVector.dist(self.position, cell.position) >= cell.r:
            self.velocity.x *= random.uniform(-0.5,-2)
            self.velocity.y *= random.uniform(-0.5,-2)

    def check_edge(self):
        if self.position.x < 0 or self.position.x > width - 250:
            self.velocity.x *= -1
            self.velocity.y *= 1
        elif self.position.y < 0 or self.position.y > height:
            self.velocity.y *= -1
            self.velocity.x *= 1
        
    
