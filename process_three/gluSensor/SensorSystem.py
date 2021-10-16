from Sensor import Sensor
from Cell import Cell

class SensorSystem:
    def __init__(self,):
        self.sensor_list = []
        # add the gal4_sensor, vp16_sensor, nucleus to sensor system
        self.sensor_list.append(Sensor(r=80, position=PVector(9*Cell.sketch_Width/16, Cell.sketch_Height/2), type = 'nucleus'))
        self.sensor_list.append(Sensor(r=20, position=PVector(9*Cell.sketch_Width/16 + 30, Cell.sketch_Height/2 + 40), type = 'gal4_sensor'))
        self.sensor_list.append(Sensor(r=20, position=PVector(9*Cell.sketch_Width/16 - 50, Cell.sketch_Height/2 -30), type = 'vp16_sensor'))
        self.sensor_list.append(Sensor(r=15, position=PVector(9*Cell.sketch_Width/16 + 20, Cell.sketch_Height/2 - 30), type = 'TRE'))
        
        
    def display(self):
        for sensor in self.sensor_list:
            sensor.display()

    def update(self):
        for sensor in self.sensor_list:
            sensor.update()

    
