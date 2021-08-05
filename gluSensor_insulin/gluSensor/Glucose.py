from Sensor import Sensor
from Cell import Cell
import random

class Glucose:
    def __init__(self, position, velocity, acceleration, mass, top_speed, maxforce, r, in_cell, lifespan):
        # some attributes have not been used(mass, in_cell)
        # in_cell = 1 means that the particle is in the cell
        self.position = position 
        self.velocity = velocity
        self.acceleration = acceleration
        self.mass = mass
        self.top_speed = top_speed
        self.maxforce = maxforce
        self.r = r
        self.in_cell = in_cell
        self.lifespan = lifespan
        self.alreadyBeFound = False
        self.status = 0
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.top_speed)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        if(self.status == 1):
            self.lifespan -= 1
        
    def display(self):
        noStroke()
        fill(64,124 + self.lifespan, 205) if self.in_cell else fill(64, 124, 205)
        ellipse(self.position.x, self.position.y, self.r, self.r)

    def displayOut(self):
        noStroke()
        fill(64, 124, 205)
        ellipse(self.position.x, self.position.y, self.r, self.r)

    def displayIn(self):
        noStroke()
        fill(64,124 + self.lifespan, 205)
        ellipse(self.position.x, self.position.y, self.r, self.r)
    
    def check_cell_edge(self, cell):
        if PVector.dist(self.position, cell.position) > cell.r:
            self.velocity.x *= random.uniform(-0.5,-2)
            self.velocity.y *= random.uniform(-0.5,-2)
            self.lifespan -= 10
    
    def check_sensor(self, sensor):
        if PVector.dist(self.position, sensor.position) < sensor.r:
            self.velocity = PVector(0,0)
            self.acceleration = PVector(0,0)
            self.status = 1
    
    def check_edge(self):
        if self.position.x < 0 or self.position.x > width - 250:
            self.velocity.x *= -1
            self.velocity.y *= 1
        elif self.position.y < 0 or self.position.y > height:
            self.velocity.y *= -1
            self.velocity.x *= 1
            
    def check_in_cell(self, cell):
        if PVector.dist(self.position, cell.position) < cell.r:
            self.in_cell = 1
            
        
    # there is sth wrong with the logic of beFound Funtion 
    def beFound(self, sensor):
        if PVector.dist(self.position, sensor.position) <= (sensor.r) and self.alreadyBeFound == False:
            self.alreadyBeFound = True
            return 1
        else:
            return 0
    
    def gluDead(self):
        if self.lifespan <= 0:
            return 1
        else:
            return 0
