from math import sqrt, atan2, acos, sin
from numbers import Real

class Base3D:
    def __repr__(self):
        return "({self.x}, {self.y}, {self.z})".format(self=self)
    
    @property
    def r(self):
        return self.norm()

    @property
    def theta(self):
        if self.r == 0:
            return 0
        return acos(self.z/self.r)

    @property
    def phi(self):
        return atan2(self.y, self.x)


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



class Ligne:
    def __init__(self, point, vecteur):
        if isinstance(point, Point) and isinstance(vecteur, Vecteur3D):
            self.point = point
            self.vecteur = vecteur
        else:
            raise TypeError("Les arguments doivent être un Point et un Vecteur3D")

    def __contains__(self, other):
        if isinstance(other, Point):
            return ((other - self.point)**self.vecteur).norm() < 1E-15*max((other-self.point).norm(), self.vecteur.norm())
        return NotImplemented


def resolv_eq_deg2(a, b, c):
    """ Résoud l'équation a*x**2 + b*x + c du second degré en x """
    Delta = b**2 - 4*a*c
    try:
        d = sqrt(Delta)
        return ((-b+d)/(2*a), (-b-d)/(2*a))
    except ValueError:
        raise ValueError(" L'équation du second degré {a}*x**2 + {b}*x + {c} n'admet pas de solution réelle ".format(a=a, b=b, c=c))


