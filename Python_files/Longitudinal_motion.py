#!/usr/local/bin python2.7
from string import *
import commands
import sys
import os.path
from numpy import matrix
from numpy import linalg
from numpy import matlib
from copy import deepcopy
from math import pi
from math import trunc
from math import sqrt
from math import cos
from math import sin
from math import atan

########  testing Geoff's formula  #######

f2name="./Longitudinal_motion.txt"
f2=open(f2name,"w")

#f2.write("deltaPhi0           deltaE0            deltaPhi2            deltaE2            deltaPhi4            detlaE4             deltaE2/E            deltaE4/E \n")
f2.write("deltaPhi2            deltaE2            deltaE2/E            deltaPhi4            detlaE4            deltaE4/E \n")

Ee  = 0.510999    # MeV

h_L = 0.000135
E_L = 155.0       # MeV
h_H = 0.0016
E_H = 1000.0      # MeV
Vol = 1690.0      # MV
phi_a = 60.0      # degree
phi_d = 240.0     # degree

gamma_L = E_L/Ee
beta_L  = sqrt(1.0-1.0/gamma_L**2)
gamma_H = E_H/Ee
beta_H  = sqrt(1.0-1.0/gamma_H**2)


deltaE0 =0.02       # MeV    20
deltaPhi0 =0.4      #        3

for i in range(10000):
    deltaPhi2  = deltaPhi0 + h_L*deltaE0/E_L
    deltaE2    = deltaE0 + Vol*(cos(phi_a*pi/180 + deltaPhi2) - cos(phi_a*pi/180))

    deltaPhi4  = deltaPhi2 + h_H*deltaE2/E_H
    deltaE4    = deltaE2 + Vol*(cos(phi_d*pi/180 + deltaPhi4) - cos(phi_d*pi/180))

    deltaE2_E  = deltaE2/beta_H**2/E_H
    deltaE4_E  = deltaE4/beta_L**2/E_L

    temp_write=str(deltaPhi2)+"      "+str(deltaE2)+"      "+str(deltaE2_E)+"      "+str(deltaPhi4)+"      "+str(deltaE4)+"      "+str(deltaE4_E)+"\n"

    f2.write(temp_write)

    deltaPhi0  = deltaPhi4
    deltaE0    = deltaE4

sys.exit()


########  testing Geoff's formula  #######

f2name="./Longitudinal_motion.txt"
f2=open(f2name,"w")

#f2.write("deltaPhi0           deltaE0            deltaPhi2            deltaE2            deltaPhi4            detlaE4             deltaE2/E            deltaE4/E \n")
f2.write("deltaPhi2            deltaE2            deltaE2/E            deltaPhi4            detlaE4            deltaE4/E \n")

Ee  = 0.510999    # MeV

h_L = 0.000135
E_L = 155.0       # MeV
h_H = 0.0016
E_H = 1000.0      # MeV
Vol = 1690.0      # MV
phi_a = 60.0      # degree
phi_d = 240.0     # degree

gamma_L = E_L/Ee
beta_L  = sqrt(1.0-1.0/gamma_L**2)
gamma_H = E_H/Ee
beta_H  = sqrt(1.0-1.0/gamma_H**2)


deltaE0 =0.02       # MeV    20
deltaPhi0 =0.4      #        3

for i in range(10000):
    deltaPhi2  = deltaPhi0 + h_L*deltaE0/E_L
    deltaE2    = deltaE0 + Vol*(cos(phi_a*pi/180 + deltaPhi2) - cos(phi_a*pi/180))

    deltaPhi4  = deltaPhi2 + h_H*deltaE2/E_H
    deltaE4    = deltaE2 + Vol*(cos(phi_d*pi/180 + deltaPhi4) - cos(phi_d*pi/180))

    deltaE2_E  = deltaE2/beta_H**2/E_H
    deltaE4_E  = deltaE4/beta_L**2/E_L

    temp_write=str(deltaPhi2)+"      "+str(deltaE2)+"      "+str(deltaE2_E)+"      "+str(deltaPhi4)+"      "+str(deltaE4)+"      "+str(deltaE4_E)+"\n"

    f2.write(temp_write)

    deltaPhi0  = deltaPhi4
    deltaE0    = deltaE4

sys.exit()


########  testing Evolution of Syn. Phase-Space Ellipse in SY's Book  #######

f2name="./Longitudinal_motion.txt"
f2=open(f2name,"w")

f2.write("Phi                 deltaE                deltaE/E \n")

Ep    = 938.272   # MeV
Ek    = 45.0      # MeV
Et0   = Ep + Ek   # MeV
gamma = Et0/Ep
beta  = sqrt(1.0-1.0/gamma**2)
alphc = 0.04340
eta   = alphc - 1.0/gamma**2
Vol   = 0.001    # MeV   0.1
phi_s = 30.0   # degree
harm  = 1

deltaE0   = -0.05     # 0.6   # MeV
phi0      = 2.1     # 3.08

for i in range(1400):

    deltaE = deltaE0 + Vol*(sin(phi0) - sin(phi_s*pi/180.0))
    Et     = Et0 + Vol*sin(phi_s*pi/180.0)
    phi    = phi0 + 2.0*pi*harm*eta/beta**2/Et*deltaE

    gamma    = Et/Ep
    beta     = sqrt(1.0-1.0/gamma**2)
    eta      = alphc - 1.0/gamma**2

    deltaE_E = deltaE/beta**2/Et

    temp_write=str(phi)+"      "+str(deltaE)+"      "+str(deltaE_E)+"   "+str(gamma)+"   "+str(beta)+"   "+str(eta)+"\n"
    f2.write(temp_write)

    deltaE0  = deltaE
    phi0     = phi
    Et0      = Et

sys.exit()
