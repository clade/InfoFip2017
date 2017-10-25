from .base import Base3D
from .vecteur3d import Vecteur3D

class Point(Base3D):
    def __init__(self, x, y=None, z=None):
        if y is None and z is None:
            if isinstance(x, Point):
                self.x = x.x
                self.y = x.y
                self.z = x.z
            elif isinstance(x, (tuple, list)):
                self.x = x[0]
                self.y = x[1]
                self.z = x[2]
            else:
                raise TypeError("Le premier argument doit être un Vecteur3D, un tuple ou une liste")
        else:
            self.x = x
            self.y = y
            self.z = z

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vecteur3D(self.x - other.x, self.y - other.y, self.z - other.z)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Vecteur3D):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented


