class Sensor:
    """
    Attributes:
        type: A flag var indicating the type of the sensor. 
              Gal4 if type is 0 or VP16 if type is 1 or nucleus if type is 2
        glu_num: An integer count of the glucose particles we have produced
        r: the radius of the sensor
        d: the diameter of the sensor
    """
    def __init__(self, r, position, type):
        self.type = type
        self.glu_num = 0
        self.r = r
        self.d = r * 2
        self.position = position

    def add_num(self, num):
        self.glu_num += num

    def set_num(self, num):
        self.glu_num = num

    def get_num(self):
        return self.glu_num

    def display(self):
        def project(x):
            return x / 20.0
        if self.type == "gal4_sensor":
            fill(30 + 225 * project(self.glu_num), 
                144 * (1 - project(self.glu_num)), 255 * (1 - project(self.glu_num)))
            ellipse(self.position.x, self.position.y, self.d, self.d)
        elif self.type == "vp16_sensor":
            fill(148, 0, 211)
            ellipse(self.position.x, self.position.y, self.d, self.d)
        elif self.type == "nucleus":
            fill(255, 69, 0)
            ellipse(self.position.x, self.position.y, self.d, self.d)
    
    

    def update(self):
        pass
