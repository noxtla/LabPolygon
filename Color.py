class Color():
    def __init__(self,color) -> None:
        self._color = color
    
    @property
    def color(self):
        return self.color
    
    @color.setter
    def color(self,color):
        self.color = color