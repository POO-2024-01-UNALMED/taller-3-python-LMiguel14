from tv import TV
class Control():
    tv = None
    
    def enlazar(self, televisor):
        self.tv = televisor
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
        TV.turnOff(self.tv)
    def turnOn(self):
        TV.turnOn(self.tv) 
    def canalDown(self):
        if  (1 < TV.getCanal(self.tv) < 120) and  TV.getEstado(self.tv) == True:
            TV.canalDown()        
    def canalUp(self):
        if (TV.getCanal(self.tv) < 120) and  TV.getEstado(self.tv) == True:
            TV.canalUp()
    def volumenUp(self):
        if (TV.getVolumen(self.tv) < 7) and  TV.getEstado(self.tv) == True:
            TV.volumenUp(self.tv)
    def volumenDown(self):
        if  (0 < TV.getVolumen(self.tv) <=7) and  TV.getEstado(self.tv) == True:
            TV.volumenDown(self.tv)    
televisor= TV("lg", True)
control= Control()

control.enlazar(televisor)

print(televisor.volumen)
control.volumenDown()

print(televisor.volumen)