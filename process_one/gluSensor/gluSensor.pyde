from CellSystem import CellSystem
cellSystem = CellSystem()

def setup(): 
    size(1600,1000)  #Modifying here you also need to change the class variable size in the Cell class
    frameRate(40)
    # create font object for print info on the screen 
    global f
    f = createFont("Arial",14,True)
    
def draw():
    background(248,248,255)
    cellSystem.display()
    cellSystem.update()
    cellSystem.check()
    if frameCount % 40 == 0 and cellSystem.glucose_system.count_num(in_cell = 0) < cellSystem.glucose_system.glu_stored / 10:  #Call one every 40 framesy
        cellSystem.add_glu_out(30)
    if frameCount % (40 * (cellSystem.protein_system.count_protein_num(type = "VP16", status = 0) / 10 + 1)) == 0 and cellSystem.protein_system.count_protein_num(type = "VP16", status = 0) <= 30: #Call one every 200 frames
            cellSystem.protein_system.add(cellSystem.sensor_system.sensor_list[2].position, type = 'VP16', status = 0)
    drawText()

    
# Add Glucose particles
def mousePressed():
    if PVector.dist(PVector(mouseX, mouseY), cellSystem.cell.position) >= cellSystem.cell.r + 100:
        cellSystem.add_glu_in(PVector(mouseX, mouseY))
        cellSystem.glucose_system.glu_stored += 1000

# Switch the blue light     
def keyPressed():
    if key == "b" or key == "B":
        cellSystem.cell.switch_light()


# Print the legend notes and the info of elements on the screen
def drawText():
    textFont(f,14)
    fill(0,255,255)
    text("GIP",9*width/16 + 15, height/2 + 40)
    text("Nucleus",9*width/16 - 25, height/2)
    
    
    #text:
    fill(255,165,0)
    text("glu_stored", width - 200, height/2 - 420)
    text("glucose_incell", width - 200, height/2 - 400)
    text("glucose_outcell", width - 200, height/2 - 380)
    text("VP16",width - 200, height/2 - 360)
    text("VP*16",width - 200, height/2 - 340)
    text("Gal4",width - 200, height/2 - 320)
    text("Complex",width - 200, height/2 - 300)
    
    #num: give a different color to display 
    fill(255,0,255)
    text(cellSystem.glucose_system.glu_stored, width - 100, height/2 - 420)
    text(cellSystem.count_glucose_num(in_cell = 1), width - 100, height/2 - 400)
    text(cellSystem.count_glucose_num(in_cell = 0), width - 100, height/2 - 380)
    text(cellSystem.count_protein_num(type = "VP16", status = 0),width - 100, height/2 - 360)
    text(cellSystem.count_protein_num(type = "VP16", status = 1),width - 100, height/2 - 340)
    text(cellSystem.count_protein_num(type = "Gal4", status = 0),width - 100, height/2 - 320)
    text(cellSystem.count_protein_num(type = "Complex", status = 0),width - 100, height/2 - 300)
    
    
    noStroke()
    fill(66, 148, 147)
    ellipse(width - 200,height/2, 15, 15)
    ellipse(width - 200,height/2 + 0.5 * 15, 25, 15)
    text("Ribosome",width - 150,height/2)
    noStroke()
    fill(231, 118, 92)
    ellipse(width - 200, height/2 + 200, 20, 15)
    text("Gal4",width - 150,height/2 + 200)
    fill(70, 140, 153)
    ellipse(width - 200, height/2 + 350, 20, 15)
    text("VP*16",width - 150,height/2 + 350)
    fill(127, 204, 212)
    ellipse(width - 200, height/2 + 250, 20, 15)
    text("VP16",width - 150,height/2 + 250)
    fill(231, 118, 92)
    ellipse(width - 200, height/2 + 300, 20, 15)
    fill(70, 140, 153)
    ellipse(width - 200 + 10, height/2 + 300, 20, 15)
    text("Complex",width - 150,height/2 + 300)
    fill(213, 105, 129)
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
    fill(255, 160, 0)
    beginShape()
    vertex(width - 200,height/2 + 100 - 11.54)
    vertex(width - 200 - 10,height/2 + 100 + 5.78)
    vertex(width - 200 + 10,height/2 + 100 + 5.78)
    endShape(CLOSE)
    text("insulin",width - 150,height/2 + 100)
    fill(62, 83, 131)
    text("Press B or b for blue light",width - 200,height/2 + 50) 
        
        
        
