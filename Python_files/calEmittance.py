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

print "-----------------------------------------"
print "This code calculates the emittance"
print "-----------------------------------------"

if not os.path.isfile("./Elegant_Run_twoDBA_2conds_100p.www3"):
    sys.exit()

# read in MAD-X output file
f1name="./Elegant_Run_twoDBA_2conds_100p.www3"
f1=open(f1name,"r")
holder=f1.readlines()
length=len(holder)
f1.close()

x0=0.
xp0=0.
y0=0.
yp0=0.
p0=0.

x20=0.
xp20=0.
y20=0.
yp20=0.
p20=0.

num=0.

betx0=35.0
bety0=10.0

for i in range(length-6):        # All counting starts from 0
    temp=holder[i+5]
    temp=temp.split()
    pID=temp[0]
    x=temp[1]
    xp=temp[2]
    y=temp[3]
    yp=temp[4]
    t=temp[5]
    p=temp[6]
    dt=temp[7]

    xt =x0 +float(x)
    xpt=xp0+float(xp)
    yt =y0 +float(y)
    ypt=yp0+float(yp)
    pt =p0 +float(p)

    x2t =x20 +float(x)**2
    xp2t=xp20+float(xp)**2
    y2t =y20 +float(y)**2
    yp2t=yp20+float(yp)**2
    p2t =p20 +float(p)**2

    x0  = xt
    xp0 = xpt
    y0  = yt
    yp0 = ypt
    p0  = pt

    x20 = x2t
    xp20= xp2t
    y20 = y2t
    yp20= yp2t
    p20 = p2t

    num = num + 1.

x2t_ave =x2t/num
xp2t_ave=xp2t/num
y2t_ave =y2t/num
yp2t_ave=yp2t/num
p2t_ave =p2t/num

xt_ave  =xt/num
xpt_ave =xpt/num
yt_ave  =yt/num
ypt_ave =ypt/num
pt_ave  =pt/num

sigma_x=sqrt(x2t_ave-2.0*xt_ave*xt_ave+xt_ave**2)

sigma_y=sqrt(y2t_ave-2.0*yt_ave*yt_ave+yt_ave**2)

sigma_p =sqrt(p2t_ave-2.0*pt_ave*pt_ave+pt_ave**2)

emit_x  =sigma_x**2/betx0
emit_y  =sigma_y**2/bety0

print "num = ",num
print "x2t_ave   = ",x2t_ave
print "y2t_ave   = ",y2t_ave
print "p2t_ave   = ",p2t_ave
print "xt_ave    = ",xt_ave
print "yt_ave    = ",yt_ave
print "pt_ave    = ",pt_ave

print "sigma_x  = ",sigma_x
print "sigma_y  = ",sigma_y

print "emit_x    = ",emit_x
print "emit_y    = ",emit_y
print "sigma_p   = ",sigma_p

sys.exit()
