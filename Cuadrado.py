from Polygon import *
from Color import *

class Cuadrado(Polygon,Color):
    def __init__(self, lado, color) -> None:
        Polygon.__init__(self,lado, lado)
        Color.__init__(self,color)
    def area (self):
        return self.lado*self.lado
    def __str__(self) -> str:
        #aqui no escribiste bien el metodo
        return f'{Polygon.__str__(self)} {Color.__str__(self)}'