from math import atan2, acos


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


