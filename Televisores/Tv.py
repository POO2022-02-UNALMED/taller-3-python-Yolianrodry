class TV:
    numTV=0
    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.control = None
        self.precio=500
        self.volumen=1
        self.canal=1
        TV.numTV += 1 
        
    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca=marca

    def getControl(self):
        return self.control

    def setControl(self, control):
        self.control=control

    def getPrecio(self):
        return self.precio

    def setPrecio(self, precio):
        self.precio=precio

    def getVolumen(self):
        return self.volumen

    def setVolumen(self, volumen):
        if ((self.estado == True) and (volumen <8 and volumen >0)):
            self.volumen=volumen

    def getCanal(self):
        return self.canal

    def setCanal(self, canal):
        if  (canal > 0 and canal < 121) and (self.estado == True):
            self.canal=canal

    @classmethod
    def setNumTV(self, numTV):
        self.numTV=numTV

    @classmethod
    def getNumTV(self):
        return self.numTV

    def turnOn(self):
        if self.estado ==False:
            self.estado = True

    def turnOff(self):
        if self.estado ==True:
            self.estado = False

    def canalUp(self):
        if (self.canal > 0 and self.canal < 120)and(self.estado==True):
            self.canal+=1

    def canalDown(self):
        if (self.canal > 1 and self.canal <= 120)and(self.estado==True):
            self.canal-=1

    def volumenUp(self):
        if (self.volumen >=0 and self.volumen <7)and(self.estado==True):
            self.volumen+=1

    def volumenDown(self):
        if (self.volumen < 8 and self.volumen >0)and(self.estado == True):
            self.volumen-=1

    def getEstado(self):
        return self.estado