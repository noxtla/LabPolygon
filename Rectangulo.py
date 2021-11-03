from Polygon import *
from Color import *

class Rectangulo(Polygon, Color):
    def __init__(self, alto, ancho, color) -> None:
        Polygon.__init__(alto, ancho)
        Color.__init__(color)
    
    def area (ancho, alto):
        return ancho*alto
    
    def __str__(self) -> str:
        return f'El ancho es {self.ancho} El alto es {self.alto}'
