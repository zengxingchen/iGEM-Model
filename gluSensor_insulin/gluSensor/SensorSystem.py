from Sensor import Sensor
from Cell import Cell

class SensorSystem:
    def __init__(self,):
        self.sensor_list = []
        # add the gal4_sensor, vp16_sensor, nucleus to sensor system
        self.sensor_list.append(Sensor(r=40, position=PVector(3*Cell.sketch_Width/8, Cell.sketch_Height/3), type = 'gal4_sensor'))
        self.sensor_list.append(Sensor(r=20, position=PVector(Cell.sketch_Width/2, 5*Cell.sketch_Height/12), type = 'vp16_sensor'))
        self.sensor_list.append(Sensor(r=30, position=PVector(9*Cell.sketch_Width/16, Cell.sketch_Height/2), type = 'nucleus'))
        self.sensor_list.append(Sensor(r=30, position=PVector(5*Cell.sketch_Width/8, 7*Cell.sketch_Height/12), type = 'TRE'))
        
    def display(self):
        for sensor in self.sensor_list:
            sensor.display()

    def update(self):
        for sensor in self.sensor_list:
            sensor.update()

    
