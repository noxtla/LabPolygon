from Polygon import *
from Color import *

class Rectangulo(Polygon, Color):
    def __init__(self, alto, ancho, color) -> None:
        Polygon.__init__(self,alto, ancho)
        Color.__init__(self, color)
    
    def area (ancho, alto):
        return ancho*alto
    
    def __str__(self) -> str:
        return f'{Polygon.__str__(self)} {Color.__str__(self)}'
