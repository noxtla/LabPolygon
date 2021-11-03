class Polygon():
    def __init__(self,alto,ancho) -> None:
        self._alto = alto
        self._ancho = ancho
    
    @property
    def alto(self):
        return self.alto
    
    @property
    def ancho(self):
        return self.ancho
   
    @alto.setter
    def alto(self,alto):
        self._alto = alto

    @ancho.setter
    def ancho(self):
        return self.ancho