from televisores.tv import TV
class Control():
    tv = None
    
    def enlazar(self, televisor):
        self.tv = TV(televisor)
    def getTv(self):
        return self.tv
    def setTv(self,televisor):
        self.tv = televisor

    def setVolumen(self,volumen):
        if  0 < volumen <=7 and TV.getEstado(self) == True:
            TV.setVolumen(volumen) 

    def setCanal(self,canal):
        if  1 < canal <=120  and TV.getEstado(self) == True:
            TV.setCanal(canal)        

    def turnOff(self):
        TV.turnOff()
    def turnOn(self):
        TV.turnOn()

    def canalDown(self):
        if  (1 < TV.getCanal() < 120) and  TV.getEstado() == True:
            TV.canalDown()        
    def canalUp(self):
        if (TV.getCanal() < 120) and  TV.getEstado() == True:
            TV.canalUp()
    def volumenUp(self):
        if (TV.getVolumen() < 7) and  TV.getEstado() == True:
            TV.volumenUp()
    def volumenDown(self):
        if  (0 < TV.getVolumen() <=7) and  TV.getEstado() == True:
            TV.volumenDown()
