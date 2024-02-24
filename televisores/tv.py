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
    
    def setNumTV(self,numTv):
        self.numTV= numTv
    def setMarca(self, marca):
        self.marca = marca
    def setCanal(self,canal):
        self.canal = canal
    def setPrecio(self,precio):
        self.precio = precio
    def setVolumen(self,volumen):
        self.volumen = volumen
    def setControl(self,control):
        self.control = control


    def turnOff(self):
        self.estado = False
    def turnOn(self):
        self.estado = True