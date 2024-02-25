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

