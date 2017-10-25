import unittest
from ..vecteur3d import Vecteur3D

u = Vecteur3D(1, 2.3, 5)
v = Vecteur3D(0, -7.3, 3.5)
a = 2.5

#assert u+v == Vecteur3D(1, -5, 8.5)
#assert u-v == Vecteur3D(1, 9.6, 1.5)
#assert -u == Vecteur3D(-1, -2.3, -5)
#assert u*a == Vecteur3D(2.5, 5.75, 12.5)
#assert u*v == -2.3*7.3+5*3.5
#assert u/a == Vecteur3D(.4, 2.3/2.5, 2)
#assert v**v == Vecteur3D(0, 0, 0)
#assert Vecteur3D(1,0,0)**Vecteur3D(0,1,0) == Vecteur3D(0,0,1)
#assert a*u == u*a

class MonTest(unittest.TestCase):
    def test_somme(self):
        self.assertEqual(u+v, Vecteur3D(1, -5, 8.5))
#        self.assertEqual(1, 2)

    def test_produit(self):
        self.assertEqual(u*a, Vecteur3D(2.5, 5.75, 12.5))
        self.assertEqual(u*v, -2.3*7.3+5*3.5)

    def test_autre(self):
        self.assertTrue(True)
        self.assertLess(1, 2)
