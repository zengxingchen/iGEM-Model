from Sensor import Sensor
from Cell import Cell

class SensorSystem:
    def __init__(self, cell):
        self.sensor_list = []
        # add the gal4_sensor, vp16_sensor, nucleus to sensor system
        self.sensor_list.append(Sensor(r=40, position=PVector(cell.position.x - 1 * cell.r/4, cell.position.y - 2 * cell.r/3), type = 'gal4_sensor'))
        self.sensor_list.append(Sensor(r=20, position=PVector(cell.position.x, cell.position.y - 1 * cell.r/6), type = 'vp16_sensor'))
        self.sensor_list.append(Sensor(r=30, position=PVector(cell.position.x + 1 * cell.r/8, cell.position.y), type = 'nucleus'))
        self.sensor_list.append(Sensor(r=30, position=PVector(cell.position.x + 1 * cell.r/4, cell.position.y + 1*cell.r/6), type = 'TRE'))
        
    def display(self):
        for sensor in self.sensor_list:
            sensor.display()
    
    def update(self):
        for sensor in self.sensor_list:
            sensor.update()

    def displayOnly(self):
        self.sensor_list[2].display()
    
    def updateOnly(self):
        self.sensor_list[2].update()
