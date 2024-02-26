class TV ():
    numTV = 0
    
    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.precio = 500
        self.volumen = 1
        self.control = None
                
    def getNumTV(self):
        return self.numTV
    def getMarca(self):
        return self.marca
    def getCanal(self):
        return self.canal
    def getPrecio(self):
        return self.precio
    def getVolumen(self):
        return self.volumen
    def getControl(self):
        return self.control
    def getEstado (self):
        return self.estado
    
    def setNumTV(self,num):
        self.numTV= num
    def setMarca(self, marca ):
        self.marca = marca
    def setCanal(self,canal):
        if  1 < canal <=120  and self.estado == True:
            self.canal = canal        
    def setPrecio(self,precio):
        self.precio = precio
    def setVolumen(self,volumen):
        if  0 < volumen <=7 and self.estado == True:
            self.volumen = volumen
    def setControl(self,control):
        self.control = control

    def turnOff(self):
        self.estado = False
    def turnOn(self):
        self.estado = True

    def canalDown(self):
        if  (1 < self.canal < 120) and  self.estado == True:
            self.canal -= 1        
    def canalUp(self):
        if (self.canal < 120) and  self.estado == True:
            self.canal += 1

    def volumenUp(self):
        if (self.volumen < 7) and  self.estado == True:
            self.volumen += 1
    def volumenDown(self):
        if  (0 < self.volumen <=7) and  self.estado == True:
            self.volumen -= 1