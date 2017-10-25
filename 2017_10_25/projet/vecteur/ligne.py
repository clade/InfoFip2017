from .vecteur3d import Vecteur3D
from .point3d import Point

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

