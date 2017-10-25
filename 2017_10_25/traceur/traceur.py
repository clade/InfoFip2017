import numpy as np

from matplotlib.pyplot import plot, axis

class Dioptre(object):
    diametre = 25.4
    def __init__(self, z0, R, n_1, n_2, diametre=None):
        self.z0 = z0
        self.R = float(R)
        if diametre is not None:
            self.diametre = diametre
        self.n_1 = n_1
        self.n_2 = n_2
        self.z_center = self.z0 + R

    def __repr__(self):
        return "Dioptre(z0={self.z0}, R={self.R}, n_1={self.n_1}, n_2={self.n_2})".format(self=self)

    def equation_dioptre(self, y):
        return self.z_center - np.sign(self.R)*np.sqrt(self.R**2 - y**2)

    def plot(self):
        y = np.linspace(-self.diametre/2, self.diametre/2)
        plot(self.equation_dioptre(y), y)
        axis('equal')

d = Dioptre(0, 100, 1, 1.1)
d = Dioptre(10, -100, 1, 1.1)
print(d)
d.plot()


