class Protein:
    def __init__(self, x, y):
        self.position = PVector(x, y)
        self.velocity = PVector(0, -2)
        self.acceleration = PVector(0, 0)
        self.r = 6
        self.maxspeed = 4
        self.maxforce = 0.1

    def update(self):
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)

    def apply_force(self, force):
        self.acceleration.add(force)
    
    def seek(self, target):
        desired = PVector.sub(target, self.position)
        desired.setMag(self.maxspeed)
        steer = PVector.sub(desired, self.velocity)
        steer.limit(self.maxforce)
        self.apply_force(steer)
    
    def display(self):
        theta = self.velocity.heading2D() + PI/2
        fill(127)
        stroke(0)
        strokeWeight(1)
        pushMatrix()
        translate(self.position.x, self.position.y)
        rotate(theta)
        beginShape()
        vertex(0, -self.r*2)
        vertex(-self.r, self.r*2)
        vertex(self.r, self.r*2)
        endShape(CLOSE)
        popMatrix()
