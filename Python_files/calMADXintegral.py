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

#def factorial(n):
#    fac=1
#    for i in range(n):
#        fac=fac*(i+1)
#    return fac

print "-----------------------------------------"
print "This code calculates radiation integrals using the MAD-X or PTC-TWISS output"
print "-----------------------------------------"

if not os.path.isfile("./jleic_e_ring_v16.2_v2.4_detsoloff.twiss"):
#if not os.path.isfile("./jleic_e_ring_v16.2_v2.3_detsoloff.ptctwiss"):
    sys.exit() 

# read in MAD-X output file
f1name="./jleic_e_ring_v16.2_v2.4_detsoloff.twiss"
#f1name="./jleic_e_ring_v16.2_v2.3_detsoloff.ptctwiss"
f1=open(f1name,"r")
holder=f1.readlines()
length=len(holder)
f1.close()

total_l=0.
total_ang=0.
total_angx=0.
total_angy=0.
RI1=0.
RI2=0.
RI3=0.
RI4=0.
RI5x=0.
RI5y=0.
nameseq=[]      #---the element names in the beam line 
namelist=[]     #---individual different elements
rmf=matlib.eye(6)


# when read from MAD-X twiss
for i in range(length-49):        # All counting starts from 0
    temp=holder[i+48]

# when read from PTC-TWISS
#for i in range(length-56):        # All counting starts from 0
#    temp=holder[i+55]
    temp=temp.split()
    name=temp[0][1:(len(temp[0])-1)]
    type=temp[1][1:(len(temp[1])-1)]   
    s=temp[2]
    l=temp[3]
    total_l=total_l+float(l)
    angle=temp[4]
    total_ang=total_ang+float(angle)
    e1=temp[5]
    e2=temp[6]
    tilt=temp[7]
    betx=temp[8]
    bety=temp[9]
    alfx=temp[10]
    alfy=temp[11]
    dx=temp[12]
    dpx=temp[13]
    dy=temp[14]
    dpy=temp[15]

    if type=="RBEND":
       temp0=holder[i-1+48]           #  when read from MAD-X twiss
#       temp0=holder[i-1+55]           #  when read from PTC-TWISS 
       temp0=temp0.split()
       betx0=temp0[8]
       bety0=temp0[9]
       alfx0=temp0[10]
       alfy0=temp0[11]
       dx0=temp0[12]
       dpx0=temp0[13]
       dy0=temp0[14]
       dpy0=temp0[15]
       
       betxm=(float(betx0)+float(betx))/2.0
       betym=(float(bety0)+float(bety))/2.0
       alfxm=(float(alfx0)+float(alfx))/2.0
       alfym=(float(alfy0)+float(alfy))/2.0
       dxm  =(float(dx0)+float(dx))/2.0 
       dpxm =(float(dpx0)+float(dpx))/2.0
       dym  =(float(dy0)+float(dy))/2.0
       dpym =(float(dpy0)+float(dpy))/2.0 
       gamxm=(1.+alfxm**2)/betxm
       gamym=(1.+alfym**2)/betym      

       RI2=RI2+float(angle)**2/float(l)                          #  I2=integral of ds/rho^2
       RI3=RI3+abs(float(angle))**3/float(l)**2                  #  I2=integral of ds/abs(rho)^3
 
       if float(tilt)==0.0:
          total_angx=total_angx+float(angle)
          RI1=RI1+dxm*float(angle)                               #  I1=integral of ds*(Dx/rho_x+Dy/rho_y)
          Hx=betxm*dpxm**2+2.*alfxm*dxm*dpxm+gamxm*dxm**2        
          RI5x=RI5x+Hx*abs(float(angle))**3/float(l)**2

       if float(tilt)!=0.0:
          total_angy=total_angy+float(angle)
          RI1=RI1+dym*float(angle)   
          Hy=betym*dpym**2+2.*alfym*dym*dpym+gamym*dym**2        
          RI5y=RI5y+Hy*abs(float(angle))**3/float(l)**2
             
print "total angle in the horizontal plan = ",total_angx
print "total angle in the vertical plan   = ",total_angy
print "I1 =",RI1
print "I2 =",RI2
print "I3 =",RI3
print "I5x =",RI5x 
print "I5y =",RI5y

sys.exit()


