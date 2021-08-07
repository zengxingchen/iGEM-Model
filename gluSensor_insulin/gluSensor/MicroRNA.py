import random
class MicroRNA:

    def __init__(self, position):
        self.position = position
        self.velocity = PVector(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0)) 
        # self.acceleration = PVector(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0))
        self.top_speed = 1
        self.r = 20
        self.status = 0
        self.spin = 100
        self.time = 200
        self.start = self.position
        self.end = None


    def set_status(self, status):
        self.status = status
        
    def update(self):
        #self.velocity.add(self.acceleration)
        self.velocity.limit(self.top_speed)
        self.position.add(self.velocity)
        # self.acceleration.mult(0) # reset the velocity
        self.time =  self.time - 1
        if(self.time == 0):
            self.velocity = PVector(0,0)

    
    
    def display(self):
        x = self.position.x 
        y = self.position.y
        stroke(0,0,0)
        for i in range(10):
            line(x, y, x + 3, y + 3)
            line(x + 3, y + 3, x + 6, y - 3)
            line(x + 6, y - 3, x + 9, y)
            x = x + 9
            y = y 
        self.end = PVector.add(self.position, PVector(90, 0))

            
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
       
