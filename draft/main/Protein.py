class Protein:
    def __init__(self, x, y):
        self.position = PVector(x, y)
        self.velocity = PVector(0, -2)
        self.acceleration = PVector(0, 0)
        self.r = 6
        self.maxspeed = 4
        self.maxforce = 0.1

    def update(self):
        self.velocity.add(acceleration)
        # Limit speed
        self.velocity.limit(maxspeed)
        self.position.add(velocity)
        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)

    def apply_force(self, force):
        self.acceleration.add(force)
    
    def seek(void, target):
        desired = PVector.sub(target, position)
        desired.setMag(maxspeed)
        steer = PVector.sub(desired,velocity)
        steer.limit(maxforce)
        self.applyForce(steer)
    
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