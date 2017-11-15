# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:14:39 2017

@author: jaxde
"""

from numpy import *

@vectorize
def mandel(c):
    z = 0
    for n in range(100):
        z = z**2 + c
        if abs(z)>2:
            return n
    return 0


#v_mandel = vectorize(mandel)

partie_reel = linspace(-2.13,0.77, 1000)
partie_imaginaire = linspace(-1.13, 1.13, 1000)

[x, y] = meshgrid(partie_reel, partie_imaginaire)
#resultat = mandel(x + 1j*y)





imshow(resultat)