from Cell import Cell
from GlucoseSystem import GlucoseSystem 
from ProteinSystem import ProteinSystem 
from Sensor import Sensor
from BRaySwitch import BRaySwitch
import random
class CellSystem:
    def __init__(self, cellR = 400, cellThick = 15,cellPosition = PVector(800, 600), sensorR = 40, sensorPosition = PVector(650, 600)):
        self.cell = Cell(cellR,cellThick, cellPosition)
        self.switch = BRaySwitch(position = PVector(800,100))
        self.sensorList = []
        for i in range(4):
            if i == 0:
                sensor = Sensor(r = 40, position = PVector(600,400), type = i)
                self.sensorList.append(sensor)
            elif i == 1:
                sensor = Sensor(r = 30, position = PVector(800,500), type = i)
                self.sensorList.append(sensor)
            elif i == 2:
                sensor = Sensor(r = 50, position = PVector(900,600), type = i)
                self.sensorList.append(sensor)
            else:
                sensor = Sensor(r = 30, position = PVector(800,200), type = 3)
                self.sensorList.append(sensor)
                sensor = Sensor(r = 30, position = PVector(1200,600), type = 3)
                self.sensorList.append(sensor)
                sensor = Sensor(r = 30, position = PVector(400,600), type = 3)
                self.sensorList.append(sensor)
                
        # self.sensor1 = Sensor(r = 40, position = PVector(400,400), type = 0)
        # self.sensor2 = Sensor(r = 30, position = PVector(600,500), type = 1)
        self.glus = GlucoseSystem()
        self.proteins = ProteinSystem()
        
    def update(self):
        self.cell.update()
        for sensor in self.sensorList:
            sensor.update()
        self.glus.update()
        self.proteins.update()
        if self.switch.state == True:
            self.proteins.compound()
        
    def display(self):
        if self.switch.state == False:
            self.cell.displayWhite()
        elif self.switch.state == True:
            self.cell.displayBlue()
        for sensor in self.sensorList:
            sensor.display()
        self.glus.display()
        self.proteins.display()
        # self.switch.display()
        
    def check(self):
        num = self.glus.check(self.cell, self.sensorList[0])
        self.sensorList[0].addNum(num)
        self.proteins.check(self.cell, self.sensorList[0])
        self.addInsulin(self.sensorList[2].position.get())
        # debug
        # print(self.sensor.gluNum)
        if(self.sensorList[0].getNum()>= 20):
            # self.addIns(self.sensor.position)
            self.addGal(self.sensorList[0].position.get())
            self.sensorList[0].setNum(0)
        for ins in self.proteins.proteinList:
            if ins.type == "insulin" and ins.inCell == 1:
                    for glu in self.glus.gluList:
                        if glu.inCell == 1 and PVector.dist(glu.position,ins.position) <= 30:
                            glu.lifespan -= 1    
        
    
    def addGal(self, position):
        self.proteins.addGal(position)
        
    def addInsulin(self, position):
        for complex in self.proteins.proteinList:
            if complex.type == "Complex" and PVector.dist(self.sensorList[2].position,complex.position)<= self.sensorList[2].r:
                self.proteins.addInsulin(position)
                complex.velocity = PVector(0,0)
                complex.acceleration = PVector(0,0)
                complex.lifespan = complex.lifespan - 20
        
    def addVp(self):
        self.proteins.addVp(self.sensorList[1].position)
    
    def addGlusIn(self, position):
        self.glus.addGlusIn(position.get())
        
    def addGlusOut(self):
        self.glus.addGlusOut()
    
    def SwitchChange(self):
        self.switch.StateChange()
    
        # debug
        # print(len(self.glus.gluList))
