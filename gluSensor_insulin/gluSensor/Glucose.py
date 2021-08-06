from Sensor import Sensor
from Cell import Cell
import random

class Glucose:
    def __init__(self, position, velocity, acceleration, mass, top_speed, maxforce, r, in_cell, lifespan,spin = 100):
        # some attributes have not been used(mass, in_cell)
        # in_cell = 1 means that the particle is in the cell
        # spin is Rotation parameters
        self.position = position 
        self.velocity = velocity
        self.acceleration = acceleration
        self.mass = mass
        self.top_speed = top_speed
        self.maxforce = maxforce
        self.r = r
        self.in_cell = in_cell
        self.lifespan = lifespan
        self.spin = spin
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
        self.spin -= 0.01
        noStroke()
        fill(64,124 + self.lifespan, 205) if self.in_cell else fill(64, 124, 205)
        x1 = self.position.x + self.r * cos(radians(100 * self.spin))
        y1 = self.position.y + self.r * sin(radians(100 * self.spin))
        x2 = self.position.x + self.r * cos(radians(60 + 100 * self.spin))
        y2 = self.position.y + self.r * sin(radians(60 + 100 * self.spin))        
        x3 = self.position.x + self.r * cos(radians(120 + 100 * self.spin))
        y3 = self.position.y + self.r * sin(radians(120 + 100 * self.spin))
        x4 = self.position.x + self.r * cos(radians(180 + 100 * self.spin))
        y4 = self.position.y + self.r * sin(radians(180 + 100 * self.spin))
        x5 = self.position.x + self.r * cos(radians(240 + 100 * self.spin))
        y5 = self.position.y + self.r * sin(radians(240 + 100 * self.spin))    
        x6 = self.position.x + self.r * cos(radians(300 + 100 * self.spin))
        y6 = self.position.y + self.r * sin(radians(300 + 100 * self.spin))
        beginShape()
        vertex(x1, y1)
        vertex(x2, y2)
        vertex(x3, y3)
        vertex(x4, y4)
        vertex(x5, y5)
        vertex(x6, y6)
        endShape(CLOSE)
    
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
