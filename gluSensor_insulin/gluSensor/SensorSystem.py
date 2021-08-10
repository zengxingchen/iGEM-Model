from Sensor import Sensor

class SensorSystem:
    def __init__(self,):
        self.sensor_list = []
        # add the gal4_sensor, vp16_sensor, nucleus to sensor system
        self.sensor_list.append(Sensor(r=40, position=PVector(600, 400), type = 'gal4_sensor'))
        self.sensor_list.append(Sensor(r=20, position=PVector(800, 500), type = 'vp16_sensor'))
        self.sensor_list.append(Sensor(r=30, position=PVector(900, 600), type = 'nucleus'))
        self.sensor_list.append(Sensor(r=30, position=PVector(1000, 700), type = 'TRE'))
        
    def display(self):
        for sensor in self.sensor_list:
            sensor.display()

    def update(self):
        for sensor in self.sensor_list:
            sensor.update()

    
