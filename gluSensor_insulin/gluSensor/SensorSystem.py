from Sensor import Sensor

class SensorSystem:
    def __init__(self,):
        self.sensorList = []
        self.gluNum = 0
        
    def display(self):
        for sensor in self.sensorList:
            sensor.display()
            
    def addSensor(self):
        for i in range(3):
            if i == 0:
                sensor = Sensor(r = 40, position = PVector(300,400), type = i)
                self.sensorList.append(sensor)
            elif i == 1:
                sensor = Sensor(r = 30, position = PVector(600,500), type = i)
                self.sensorList.append(sensor)
            else:
                sensor = Sensor(r = 50, position = PVector(700,600), type = i)
                self.sensorList.append(sensor)
                
    def update(self):
        for sensor in self.sensorList:
            sensor.update()
            
    # def check(self,num):
    #     self.addSensor()
    #     self.sensorList[0].addNum(num)
    #     self.proteinList.check(self.cell, self.sensorList[0])
    #     # debug
    #     # print(self.sensor.gluNum)
    #     if(self.sensorList[0].getNum()>= 20):
    #         # self.addIns(self.sensor.position)
    #         self.addGal(self.sensorList[0].position.get())
    #         self.sensorList[0].setNum(0)
            
    
