from CellSystem import CellSystem
cellSystem = CellSystem()

def setup(): 
    size(1600,1000)
    frameRate(40)
    # create font object for print info on the screen 
    global f
    f = createFont("Arial",14,True)
    
def draw():
    background(248,248,255)
    cellSystem.display()
    cellSystem.update()
    cellSystem.check()
    if frameCount % 40 == 0:  #Call one every 40 framesy
        cellSystem.add_glu_out()
    if frameCount % 240 == 0: #Call one every 240 frames
        cellSystem.protein_system.add(cellSystem.sensor_system.sensor_list[1].position, type = 'VP16')
    drawText()

    
# Add Glucose particles
def mousePressed():
    if ((PVector.dist(PVector(mouseX, mouseY), cellSystem.cell.position) <= cellSystem.cell.r) and 
        (PVector.dist(PVector(mouseX, mouseY), cellSystem.sensor_system.sensor_list[0].position) >= cellSystem.sensor_system.sensor_list[0].r)):
        cellSystem.add_glu_in(PVector(mouseX, mouseY))

# Switch the blue light     
def keyPressed():
    if key == "b" or key == "B":
        cellSystem.cell.switch_light()


# Print the legend notes and the info of elements on the screen
def drawText():
    textFont(f,14)
    fill(0,255,255)
    text("GluSensor",3*width/8 - 30, height/3)
    text("Nucleus",9*width/16 - 25, height/2)
    
    
    noStroke()
    fill(204,204,0)
    ellipse(width - 200,height/2, 15, 15)
    ellipse(width - 200,height/2 + 0.5 * 15, 25, 15)
    text("Ribosome",width - 150,height/2)
    noStroke()
    fill(204, 102, 0)
    ellipse(width - 200, height/2 + 200, 20, 15)
    text("Gal4",width - 150,height/2 + 200)
    fill(255, 182, 193)
    ellipse(width - 200, height/2 + 250, 20, 15)
    text("VP16",width - 150,height/2 + 250)
    fill(204, 102, 0)
    ellipse(width - 200, height/2 + 300, 20, 15)
    fill(255, 182, 193)
    ellipse(width - 200 + 10, height/2 + 300, 20, 15)
    text("Complex",width - 150,height/2 + 300)
    fill(64,124, 205)
    ellipse(width - 200,height/2 + 150,10,10)
    # draw the glucose
    glu_r = 7
    x1 = width - 200 + glu_r * cos(radians(0))
    y1 = height/2 + 150 + glu_r * sin(radians(0))
    x2 = width - 200 + glu_r * cos(radians(60))
    y2 = height/2 + 150 + glu_r * sin(radians(60))      
    x3 = width - 200 + glu_r * cos(radians(120))
    y3 = height/2 + 150 + glu_r * sin(radians(120))
    x4 = width - 200 + glu_r * cos(radians(180))
    y4 = height/2 + 150 + glu_r * sin(radians(180))
    x5 = width - 200 + glu_r * cos(radians(240))
    y5 = height/2 + 150 + glu_r * sin(radians(240))   
    x6 = width - 200 + glu_r * cos(radians(300))
    y6 = height/2 + 150 + glu_r * sin(radians(300))
    beginShape()
    vertex(x1, y1)
    vertex(x2, y2)
    vertex(x3, y3)
    vertex(x4, y4)
    vertex(x5, y5)
    vertex(x6, y6)
    endShape(CLOSE)
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
        
        
        
        
