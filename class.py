import math
class Circle():
    def __init__(self, radius):
        self.radius=radius
    @property
    def radius(self):
        return self._radius
            
    @radius.setter
    def radius(self, radius):
        if radius  and (type(radius)==int or type(radius)==float):
            self._radius=radius 
        else:
            self._radius=None
            print("Incorrect radius!")
    @property
    def diametr(self):
        if self._radius:
            return self._radius*2
        else:
            return self._radius
    @property
    def length(self):
        if self._radius:
            return self._radius*2*math.pi
        else:
            return self._radius
    @property
    def square(self):
        if self._radius:
            return self._radius*math.pi**2  
        else:
            return self._radius
