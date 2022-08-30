class TV:
    numTV = 0
    def __init__(self, marca,estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.volumen = 1
        self.precio = 500
        TV.numTV+=1
        
    @staticmethod
    def getNumTV():
        return TV.numTV
    
    @staticmethod
    def setNumTV(num):
        TV.numTV = num

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

    def getCanal(self):
        return self.canal

    def setCanal(self, canal):
        if canal>=1 and canal<=120 and self.estado == True :
            self.canal=canal
    
    def turnOn(self):
        self.estado = True
        
    def turnOff(self):
        self.estado = False
    
    def getEstado(self):
        return self.estado
    
    def canalUp(self):
        if self.getEstado() == True and self.canal != 120 :
            self.canal+=1
    def canalDown(self):
        if self.getEstado() == True and self.canal != 1 :
            self.canal-=1
    
    def getVolumen(self):
        return self.volumen
    
    def setVolumen(self, volumen):
        if volumen>=0 and volumen<=7 and self.estado == True:
            self.volumen=volumen
        
    def volumenUp(self):
        if self.getEstado() == True and self.volumen != 7 :
            self.volumen+=1
    def volumenDown(self):
        if self.getEstado() == True and self.volumen != 0 :
            self.volumen-=1