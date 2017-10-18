from vecteur import Vecteur3D, Point, Ligne

u = Vecteur3D(1, 2.3, 5)
v = Vecteur3D(0, -7.3, 3.5)
a = 2.5

assert u+v == Vecteur3D(1, -5, 8.5)
assert u-v == Vecteur3D(1, 9.6, 1.5)
assert -u == Vecteur3D(-1, -2.3, -5)
assert u*a == Vecteur3D(2.5, 5.75, 12.5)
assert u*v == -2.3*7.3+5*3.5
assert u/a == Vecteur3D(.4, 2.3/2.5, 2)
assert v**v == Vecteur3D(0, 0, 0)
assert Vecteur3D(1,0,0)**Vecteur3D(0,1,0) == Vecteur3D(0,0,1)
assert a*u == u*a

print(v.r)
print(v.theta)
print(v.phi)

A = Point(2, 3.3, 7)
B = Point(1, 1, 2)
C = Point(2, 3.3, 8)

L = Ligne(B, u)

assert A in L
assert C not in L
