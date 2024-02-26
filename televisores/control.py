from televisores.tv import TV
from televisores.marca import Marca
class Control():
    tv = None
    
    def enlazar(self, televisor):
        self.tv = televisor
    def getTv(self):
        return self.tv
    def setTv(self,televisor):
        self.tv = televisor
    def setCanal(self,canal):
        if  1 < canal <=120  and TV.getEstado() == True:
            self.canal = canal    
    def setVolumen(self,volumen):
        if  0 < volumen <=7 and TV.getEstado() == True:
            self.volumen = volumen
    def turnOff(self):
        TV.turnOff = False
    def turnOn(self):
        TV.turnOn = True

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
