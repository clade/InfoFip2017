from vecteur import Vecteur3D, Point
import numpy as np
import matplotlib.pyplot as plt

class Dioptre(object):
    diametre = 25.4
    def __init__(self, z0, R, n_1, n_2, diametre=None):
        self.z0 = z0
        self.R = float(R)
        if diametre is not None:
            self.diametre = diametre
        self.n_1 = n_1
        self.n_2 = n_2
        self.z_center = z0 + R
        self.center = Point(0, 0, self.z_center)

    def __repr__(self):
        return "Dioptre({self.z0}, {self.R}, {self.n_1}, {self.n_2})".format(self=self)

    def plot(self, N=100):
        y = np.linspace(-self.diametre/2, self.diametre/2, N+1)
        x = self.z_center - np.sign(self.R)*np.sqrt(self.R**2 - y**2)
        plt.plot(x, y)
        plt.axis('equal')

    
    def intersection(self, rayon):
        """ Trouve le point d'intersection du rayon avec le dioptre.

         On utilise la résolution de l'équation du second degré norm(p1 + t k - center)**2 = R**2
        qui est renotée a*t**2 + b*t + c """
        a = rayon.k.norm()**2
        center = self.center
        b = 2*(rayon.p0 - center)*rayon.k
        c = (rayon.p0 - center).norm()**2 - self.R**2
        if self.R > 0:
            return rayon.p0 + (-b-np.sqrt(b**2-4*a*c))/(2*a)*rayon.k
        else:
            return rayon.p0 + (-b+np.sqrt(b**2-4*a*c))/(2*a)*rayon.k

    def traversee(self, rayon):
        p2 = intersection(self, rayon)
        n = center-p2
        n = n/n.norm()
        k_ort = (n*k)*n
        k_par = k - k_ort
        alpha = np.sign(R)*np.sqrt(n_2**2 - k_par.norm()**2)

class Rayon():
    def __init__(self, p0, k, n=None):
        self.p0 = p0
        self.k = k
        if n is not None:
            self.normalize(n)

    def normalize(self, n):
        self.k = n*self.k/self.k.norm()

    def __repr__(self):
        return "Rayon(p0={self.p0}, k={self.k})".format(self=self)
