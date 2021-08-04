class Sensor:
    def __init__(self, r, position, type): #sensor1(GAL4):type = 0; sensor2(VP16): type = 1;nucleus:type = 2
        self.type = type
        self.gluNum = 0
        self.r = r
        self.d = r * 2
        self.position = position
   
    def addNum(self, num):
        self.gluNum += num
        
    def setNum(self, num):
        self.gluNum = num
    
 
    def getNum(self):
        return self.gluNum
            
    def display(self):
        if self.type == 0:
            def project(x):
                return x / 20.0
            fill(30+225*project(self.gluNum),144*(1-project(self.gluNum)),255*(1-project(self.gluNum)))
            ellipse(self.position.x, self.position.y, self.d, self.d)
        elif self.type == 1:
            fill(148,0,211)
            ellipse(self.position.x, self.position.y, self.d, self.d)
        elif self.type == 2:
            fill(255,69,0)
            ellipse(self.position.x, self.position.y, self.d, self.d)
        else:
            fill(255,140,140)
            beginShape()
            vertex(self.position.x - 20,self.position.y - 20)
            vertex(self.position.x + 20,self.position.y - 20)
            vertex(self.position.x + 20,self.position.y + 20)
            vertex(self.position.x - 20,self.position.y + 20)
            endShape(CLOSE)
            
            
            
    '''
    def display(self):
        def project(x):
            return (x / 20.0) * 255
        
        fill(project(self.gluNum),project(self.gluNum),project(self.gluNum))
        ellipse(self.position.x, self.position.y, self.d, self.d)
    '''
    '''
        if self.gluNum < 20 :
            fill(255,182,193)
            ellipse(self.position.x,self.position.y,self.d,self.d)
        elif self.gluNum < 50:
            fill(220,20,60)
            ellipse(self.position.x,self.position.y,self.d,self.d)
        else:
            fill(139,2,139)
            ellipse(self.position.x,self.position.y,self.d,self.d)
        '''

    def update(self):
        pass
