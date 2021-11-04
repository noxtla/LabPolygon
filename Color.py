class Color():
    def __init__(self,color) -> None:
        self._color = color
    
    @property
    def color(self):
        return self.color
    
    #Aqui te falto el atributo encapsulado
    #lo pusiste normal
    @color.setter
    def color(self,color):
        self._color = color

    #No escribiste el metodo str
    #devuelve el atributo encapsulado
    def __str__(self) -> str:
        return f'El color es {self._color}'