class Control:
    def __init__(self):
        self.tv = None
    
    def setCanal(self, canal):
        self.tv.setCanal(canal)
    
    def turnOn(self):
        self.tv.turnOn()
        
    def turnOff(self):
        self.tv.turnOff()

    def volumenUp(self):
        self.tv.volumenUp()
        
    def volumenDown(self):
        self.tv.volumenDown()

    def canalUp(self):
        self.tv.canalUp()
        
    def canalDown(self):
        self.tv.canalDown()
          
    def setTv(self, tv):
        self.tv = tv
    
    def getTv(self):
        return self.tv
    
    def enlazar(self,tv):
        self.tv = tv
        tv.setControl(self)