import random
class mRNA:

    def __init__(self, position):   
        self.position = position
        self.velocity = PVector(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0)) 
        self.acceleration = PVector(0, 0)
        self.max_speed = 1
        self.r = 20
        self.status_mirna = 0      # Identify its status: status_mirna = 0:mRNA is free. It can be a target for miRNA; status_mirna = 1:mRNA is be find;status_mirna = 2:miRNA has combined mRNA
        self.status_ribosome = 1   # Identify its status: status_ribosome = 0:mRNA is free. It can be a target for ribosome
        self.time = 300            # motion time,When the motion time is zero, it stops
        self.start = self.position
        self.end = PVector.add(self.position, PVector(90, 0))


    def set_status(self, status):
        self.status_mirna = status
        self.status_ribosome = status
        
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.max_speed)
        self.position.add(self.velocity)
        self.acceleration.mult(0) # reset the velocity
        self.time =  self.time - 1
        if(self.time == 0):
            self.velocity = PVector(0,0)
            self.status_ribosome = 0
        self.end = PVector.add(self.position, PVector(90, 0))

    
    
    def display(self):    
        x = self.position.x 
        y = self.position.y
        num = 10            # Change the lenth of mRNA
        strokeWeight(2)     # Change the thickness and color of the lines
        if self.status_mirna == 0 or self.status_mirna == 1:
            stroke(101, 219, 205)
        if self.status_mirna == 2:
            stroke(255, 20, 147)
        for i in range(num):
            line(x, y, x + 3, y + 3)
            line(x + 3, y + 3, x + 6, y - 3)
            line(x + 6, y - 3, x + 9, y)
            x = x + 9
            y = y
                        

                                                                                                
                                        
    def check_cell_edge(self, cell):
        # check the cell_edge with both the start_position and end_position of the mRNA 
        if PVector.dist(self.position, cell.position) >= cell.r or PVector.dist(self.end, cell.position) >= cell.r:
            self.velocity.x *= random.uniform(-0.5,-2)
            self.velocity.y *= random.uniform(-0.5,-2)

    
       
