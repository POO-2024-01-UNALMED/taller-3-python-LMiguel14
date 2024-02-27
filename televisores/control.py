from televisores.tv import TV
from televisores.marca import Marca
class Control:
    def __init__(self):
        self.tv = None

    def getTv(self):
        return self.tv

    def setTv(self, tv):
        self.tv = tv

    def enlazar(self, tele):
        self.tv = tele

    def turnOn(self):
        self.tv.estado = True

    def turnOff(self):
        self.tv.estado = False

    def canalUp(self):
        if self.tv.estado and self.tv.getCanal() < 120:
            self.tv.canal += 1

    def canalDown(self):
        if self.tv.estado and 1 < self.tv.getCanal() <= 120:
            self.tv.canal -= 1

    def volumenUp(self):
        if self.tv.getEstado() and self.tv.volumen < 7:
            self.tv.volumen += 1

    def volumenDown(self):
        if self.tv.getEstado() and self.tv.volumen > 0:
            self.tv.volumen -= 1

    def setCanal(self, canal):
        if 1 <= canal <= 120 and self.tv.getEstado():
            self.tv.canal = canal

    def setVolumen(self, volumen):
        if 0 <= volumen <= 7 and self.tv.getEstado():
            self.tv.volumen = volumen
