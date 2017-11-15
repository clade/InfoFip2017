# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 23:33:43 2017

@author: jaxde
"""
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

def fonction_de_transfert(omega, omega_0, zeta):
    return omega_0**2/( omega_0**2 - omega**2 + 2*1j*zeta*omega*omega_0)

f0 = 1000.0
omega_0 = 2*pi*f0
zeta = 0.1
frequence = logspace(2, 4, 100)
omega = 2*pi*frequence

gain = abs(fonction_de_transfert(omega, omega_0, zeta))
angle = angle(fonction_de_transfert(omega, omega_0, zeta))*180/pi

plt.subplot(2, 1, 1)
plt.loglog(frequence, gain)
plt.subplot(2, 1, 2)
plt.semilogx(frequence, angle, label=r"$\zeta = {zeta}$".format(zeta = zeta))


zeta = 1
frequence = logspace(2, 4, 100)
omega = 2*pi*frequence
gain = abs(fonction_de_transfert(omega, omega_0, zeta))
angle = np.angle(fonction_de_transfert(omega, omega_0, zeta))*180/pi

plt.subplot(2, 1, 1)
plt.loglog(frequence, gain)
plt.grid()
plt.ylabel("Amplitude")
plt.title(r"Oscillateur amorti ($\omega_0/2\pi$ = {omega0_sur_2pi} et $\zeta$ = {zeta})".format(omega0_sur_2pi = f0, zeta = zeta))
plt.subplot(2, 1, 2)
plt.semilogx(frequence, angle, label=r"$\zeta = {zeta}$".format(zeta = zeta))
plt.grid()
plt.ylabel("Phase[°]")
plt.xlabel("Fréquence")



plt.legend()