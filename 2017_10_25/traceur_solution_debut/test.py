from rayon import Rayon, Dioptre

from vecteur import Vecteur3D, Point

u = Vecteur3D(0, 0, 1)
p = Point(0, -1, -2)
D = Dioptre(1., 100, 1.1, 1.2)
R = Rayon(p, u, 1.1)

print(D)
D.plot()
print(R)
