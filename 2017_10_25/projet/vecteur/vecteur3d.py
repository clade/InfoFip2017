from math import sqrt
from numbers import Real

from .base import Base3D

class Vecteur3D(Base3D, object):
    def __init__(self, x, y=None, z=None):
        if y is None and z is None:
            if isinstance(x, Vecteur3D):
                x, y, z = (x.x, x.y, x.z)
            elif isinstance(x, (tuple, list)):
                x, y, z = x
            else:
                raise TypeError("Le premier argument doit être un Vecteur3D, un tuple ou une liste")
        self.x = x
        self.y = y
        self.z = z


    def norm(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, other):
        if isinstance(other, Vecteur3D):
            return Vecteur3D(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vecteur3D):
            return Vecteur3D(self.x - other.x, self.y - other.y, self.z - other.z)
        return NotImplemented

    def __neg__(self):
        return Vecteur3D(-self.x, -self.y, -self.z)

    def __mul__(self, other):
        if isinstance(other, Vecteur3D):
            return self.x*other.x + self.y*other.y + self.z*other.z
        elif isinstance(other, Real):
            return Vecteur3D(other*self.x, other*self.y, other*self.z)
        return NotImplemented

    def __truediv__(self, other):
        return self*(1/other)

    def __pow__(self, other):
        if isinstance(other, Vecteur3D):
            return Vecteur3D(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y - self.y*other.x)
        return NotImplemented

    def __eq__(self, other):
        return (self-other).norm() == 0

    def __rmul__(self, other):
        return self*other

