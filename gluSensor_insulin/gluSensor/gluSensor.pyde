from CellSystem import CellSystem

cellSystem = CellSystem()
def setup(): 
    size(1600,1200)
    global f
    f = createFont("Arial",14,True)
    frameRate(40)
    
def draw():
    background(248,248,255)
    cellSystem.display()
    cellSystem.update()
    cellSystem.check()
    if frameCount % 40 == 0:  #Call one every 40 framesy
        cellSystem.addGlusOut()
    if frameCount % 240 == 0: #Call one every 240 frames
        cellSystem.addVp()
    textFont(f,14)
    fill(0,255,255)
    text("GluSensor",570,400)
    text("Nucleus",880,600)
    text("insR",790,200)
    text("insR",390,600)
    text("insR",1190,600)
    noStroke()
    fill(204, 102, 0)
    ellipse(width - 200, height/2 + 200, 20, 20)
    text("Gal4",width - 150,height/2 + 200)
    fill(255, 182, 193)
    ellipse(width - 200, height/2 + 250, 20, 20)
    text("VP16",width - 150,height/2 + 250)
    fill(255 , 20, 147)
    ellipse(width - 200, height/2 + 300, 30, 30)
    text("Complex",width - 150,height/2 + 300)
    fill(64,124, 205)
    ellipse(width - 200,height/2 + 150,10,10)
    text("Glucose",width - 150,height/2 + 150)
    fill(255, 140, 0)
    beginShape()
    vertex(width - 200,height/2 + 100 - 11.54)
    vertex(width - 200 - 10,height/2 + 100 + 5.78)
    vertex(width - 200 + 10,height/2 + 100 + 5.78)
    endShape(CLOSE)
    text("insulin",width - 150,height/2 + 100)
    fill(0,191,255)
    text("Press B or b for blue light",width - 200,height/2 + 50)

def mousePressed():
    if ((PVector.dist(PVector(mouseX, mouseY), cellSystem.cell.position) <= cellSystem.cell.r) and 
        (PVector.dist(PVector(mouseX, mouseY), cellSystem.sensorList[0].position) >= cellSystem.sensorList[0].r)):
        cellSystem.addGlusIn(PVector(mouseX, mouseY))
        
def keyPressed():
    if key == "b" or key == "B":
        cellSystem.SwitchChange()
        
        
        
        
