from Polygon import *
from Color import *

class Cuadrado(Polygon,Color):
    def __init__(self, lado, color) -> None:
        Polygon.__init__(lado, lado)
        Color.__init__(color)
    def area (self):
        return self.lado*self.lado
    def __str__(self) -> str:
        return f'El ancho y el largo es lo mismo {self.lado}'