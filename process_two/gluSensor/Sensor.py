class Sensor:


    """
    Attributes:
        type: A flag var indicating the type of the sensor. 
        it has 4 certain values {"gal4_sensor", "vp16_sensor", "nucleus","TRE":generate miRNA}
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
            fill(80, 183, 62)
            arc(self.position.x, self.position.y, 30, 30, HALF_PI, PI + HALF_PI)
            arc(self.position.x, self.position.y + 15, 60, 60, PI + HALF_PI, 2 * PI)
            arc(self.position.x + 15, self.position.y + 15, 30, 30, 0, PI)
        elif self.type == "nucleus":
            fill(153, 200, 193)
            ellipse(self.position.x, self.position.y, self.d, self.d)
            fill(141, 188, 182)
            ellipse(self.position.x, self.position.y, 0.2 * self.d, 0.2 * self.d )
            ellipse(self.position.x + 0.35 * self.d, self.position.y, 0.2 * self.d, 0.2 * self.d )
            ellipse(self.position.x - 0.35 * self.d, self.position.y, 0.2 * self.d, 0.2 * self.d )
            ellipse(self.position.x + 0.2 * self.d, self.position.y + 0.35 * self.d, 0.2 * self.d, 0.2 * self.d )
            ellipse(self.position.x + 0.2 * self.d, self.position.y - 0.35 * self.d, 0.2 * self.d, 0.2 * self.d )
            ellipse(self.position.x - 0.2 * self.d, self.position.y + 0.35 * self.d, 0.2 * self.d, 0.2 * self.d )
            ellipse(self.position.x - 0.2 * self.d, self.position.y - 0.35 * self.d, 0.2 * self.d, 0.2 * self.d )
        elif self.type == "TRE":
            fill(186, 35, 114)
            ellipse(self.position.x, self.position.y, self.d / 0.618, self.d)

    def update(self):
        pass
