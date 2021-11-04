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

    #Aqui le pusiste return
    @ancho.setter
    def ancho(self,ancho):
        self._ancho = ancho
    
    #overwrite str method
    #falto el atributo encapsulado
    def __str__(self) -> str:
        return f'El alto es {self._alto} El ancho es {self._ancho}'