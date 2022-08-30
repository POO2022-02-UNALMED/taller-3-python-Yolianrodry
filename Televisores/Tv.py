class TV:

    numTV = 0

    def _init_(self, marca, estado):

        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        TV.numTV += 1

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setControl(self, control):
        self.control = control

    def getControl(self):
        return self.control

    def setPrecio(self, precio):
        self.precio = precio

    def getPrecio(self):
        return self.precio

    def setVolumen(self, volumen):
        if volumen >= 0 and volumen <= 7 and self.estado:
            self.volumen = volumen

    def getVolumen(self):
        return self._volumen
 
    def setCanal(self, canal):
        if canal >= 1 and canal <= 120 and self.estado:
            self.canal = canal

    def getCanal(self):
        return self.canal

    
    @staticmethod
    def getNumTV():
        return TV.numTV
    
    @staticmethod
    def setNumTV(num):
        TV.numTV = num

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado

    def canalUp(self):
        if(self.getEstado() == True and self.canal != 120 ):
            self.canal+=1
    def canalDown(self):
        if(self.getEstado() == True and self.canal != 1 ):
            self.canal-=1

    def volumenUp(self):
        if self._estado:
            if self._volumen < 7:
                self._volumen += 1

    def volumenDown(self):
        if self._estado:
            if self._volumen > 0:
                self._volumen -= 1