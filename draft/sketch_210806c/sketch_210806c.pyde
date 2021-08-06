from Protein import Protein



def setup():
    size(640, 360)
    global protein
    protein = Protein(width / 2, height / 2)
    
def draw():
    background(255)

    mouse = PVector(mouseX, mouseY)

    # Draw an ellipse at the mouse position
    fill(200)
    stroke(0)
    strokeWeight(2)
    ellipse(mouse.x, mouse.y, 48, 48)

    # Call the appropriate steering behaviors for our agents
    protein.seek(mouse)
    protein.update()
    protein.display()
