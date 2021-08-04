from Sensor import Sensor
from Cell import Cell
import random
class Glucose:
    def __init__(self, position, velocity, acceleration, mass, topSpeed, maxforce, r, inCell, quadrant,lifespan):
        # some attributes have not been used(mass, inCell, quadrant)
        # inCell = 1 means that the particle is in the cell
        self.position = position 
        self.velocity = velocity
        self.acceleration = acceleration
        self.mass = mass
        self.topSpeed = topSpeed
        self.maxforce = maxforce
        self.r = r
        self.inCell = inCell
        self.quadrant = quadrant
        self.lifespan = lifespan
        self.alreadyBeFound = False
        self.status = 0
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.topSpeed)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        if(self.status == 1):
            self.lifespan -= 1
        
    
    def displayOut(self):
        noStroke()
        fill(64,124, 205)
        ellipse(self.position.x, self.position.y, self.r, self.r)
        
    
    def displayIn(self):
        noStroke()
        fill(64,124 + self.lifespan, 205)
        ellipse(self.position.x, self.position.y, self.r, self.r)
    
    def checkCellEdges(self, cell):
        if PVector.dist(self.position, cell.position) > cell.r:
            self.velocity.x *= random.uniform(-0.5,-2)
            self.velocity.y *= random.uniform(-0.5,-2)
            self.lifespan -= 10
    
    def checkSensor(self, sensor):
        if PVector.dist(self.position, sensor.position) < sensor.r:
            self.velocity = PVector(0,0)
            self.acceleration = PVector(0,0)
            self.status = 1
    
    def checkEdges(self):
        if self.position.x < 0 or self.position.x > width - 250:
            self.velocity.x *= -1
            self.velocity.y *= 1
        elif self.position.y < 0 or self.position.y > height:
            self.velocity.y *= -1
            self.velocity.x *= 1
            
    def checkInCell(self, cell):
        if PVector.dist(self.position, cell.position) < cell.r:
            self.inCell = 1
            
        
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
