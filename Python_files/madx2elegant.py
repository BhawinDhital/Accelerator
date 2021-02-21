#!/usr/local/bin python2.7
from string import *
import commands
import sys
from numpy import matrix
from numpy import linalg
from numpy import matlib
from copy import deepcopy

#def factorial(n):
#    fac=1
#    for i in range(n):
#        fac=fac*(i+1)
#    return fac

#-------------------------------------------------------------
#   this program to read the magnet information into and 
#   create an elegant input files 
#-------------------------------------------------------------

print "-----------------------------------------"
print "This code convert madx output to elegant"
print "It accepts: "
print "SBEND, QUAD, SEXT, MULT, MARKER. "
print "-----------------------------------------"
print "To run the program: "
print "0) input file from MADX: parameters_input"
print "   output file         : elegant.lte" 
print "1) create parameters_input with madx: "
print "use, period=...;  "
print "select,flag=twiss,column=NAME,KEYWORD,S,L,ANGLE,E1,E2,tilt,"
print "K0L,K0SL,K1L,K1SL,K2L,K2SL,K3L,K3SL,K4L,K4SL,K5L,K5SL,K6L,K6SL," 
print "K7L,K7SL,K8L,K8SL,K9L,K9SL,K10L,K10SL,KSI,"
print "RE11,RE12,RE13,RE14,RE15,RE16,RE21,RE22,RE23,RE24,RE25,RE26,"
print "RE31,RE32,RE33,RE34,RE35,RE36,RE41,RE42,RE43,RE44,RE45,RE46,"
print "RE51,RE52,RE53,RE54,RE55,RE56,RE61,RE62,RE63,RE64,RE65,RE66;"
print "twiss,rmatrix,betx=1,bety=1,file=parameters_input; "
print "stop; "
print "------------------------------------------"

#----read into the whole file
f1name="./parameters_input"
f1=open(f1name,"r")
holder=f1.readlines()
length=len(holder)
f1.close()

#----produce the MADX file according to the type
#    now the accepted types:
#           DRIFT, HMONITOR, VMONITOR, MONITOR, MARKER
#           SBEND, QUADRUPOLE, SEXTUPOLE, QUADRUPOLE
#           MULTIPOLE, HKICKER, VKICKER

#-----the rhic element file
f2name="./elegant.lte"
f2=open(f2name,"w")
#f2.write('     \n')              
#f2.write('Q: CHARGE,TOTAL=16e-09;        \n')
#f2.write('!! ELEGANT input for MEIC \n')
#f2.write('   \n')

total_l=0.
total_ang=0
nameseq=[]      #---the element names in the beam line 
namelist=[]     #---individual different elements
rmf=matlib.eye(6)

for i in range(length-49):        # All counting starts from 0
    temp=holder[i+48]
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
    k0l=temp[8]
    k0sl=temp[9]
    k1l=temp[10]
    k1sl=temp[11]
    k2l=temp[12]
    k2sl=temp[13]
    k3l=temp[14]
    k3sl=temp[15]
    k4l=temp[16]
    k4sl=temp[17]
    k5l=temp[18]
    k5sl=temp[19]
    k6l=temp[20]
    k6sl=temp[21]
    k7l=temp[22]
    k7sl=temp[23]   
    k8l=temp[24]
    k8sl=temp[25]
    k9l=temp[26]
    k9sl=temp[27]
    k10l=temp[28]
    k10sl=temp[29]
    ksi=temp[30]
    volt=temp[31]
    lag=temp[32]
    harmon=temp[33]
    freq=temp[34]
    rmi=deepcopy(rmf)
    for i in range(6):
        for j in range(6):
            rmf[i,j]=temp[31+i*6+j]
    nameseq.append(name)
    if name not in namelist:
         namelist.append(name)
         if type=="DRIFT":
             temp_write= name+":"+"DRIFT"+",L="+l+"\n"
             f2.write(temp_write)
         elif type=="SBEND":
             temp_write=name+":"+"CSBEND"+",L="+l+", ANGLE="+str(float(angle))+",TILT="+tilt+",&\n"
             f2.write(temp_write)
             temp_write="E1="+str(float(e1))+",E2="+str(float(e2))+",K1="+str(float(k1l)/float(l))+",N_KICKS=10\n"
             f2.write(temp_write)
         elif type=="RBEND":
             temp_write=name+":"+"CSBEND"+",L="+l+", ANGLE="+str(float(angle))+",TILT="+tilt+",&\n"
             f2.write(temp_write)
             temp_write="E1="+str(float(e1))+",E2="+str(float(e2))+",K1="+str(float(k1l)/float(l))+",N_KICKS=10\n"
             f2.write(temp_write)
         elif type=="QUADRUPOLE" and float(l)!=0.:
             temp_write=name+":"+"KQUAD"+",L="+l+",K1="+str(float(k1l)/float(l))+",TILT="+tilt+",N_KICKS=10\n"
             f2.write(temp_write)
         elif type=="SEXTUPOLE" and float(l)!=0:
             temp_write=name+":"+"KSEXT"+",L="+l+",k2="+str(float(k2l)/float(l))+",TILT="+tilt+",N_KICKS=10\n"
             f2.write(temp_write)
         elif type=="MARKER" and float(l)==0.:
             temp_write= name+":"+"MARKER"+"\n"
             f2.write(temp_write)
         elif type=="MATRIX":
             rm=rmf*rmi.I
             temp_write=name+":"+"EMATRIX"+",L="+l+",ORDER=1,&\n"
             f2.write(temp_write)
             temp_write=("R11="+str(rm[0,0])+",R12="+str(rm[0,1])+",R13="+str(rm[0,2])+
                        ",R14="+str(rm[0,3])+",R15="+str(rm[0,4])+",R16="+str(rm[0,5])+",&\n")
             f2.write(temp_write)
             temp_write=("R21="+str(rm[1,0])+",R22="+str(rm[1,1])+",R23="+str(rm[1,2])+
                        ",R24="+str(rm[1,3])+",R25="+str(rm[1,4])+",R26="+str(rm[1,5])+",&\n")
             f2.write(temp_write)
             temp_write=("R31="+str(rm[2,0])+",R32="+str(rm[2,1])+",R33="+str(rm[2,2])+
                        ",R34="+str(rm[2,3])+",R35="+str(rm[2,4])+",R36="+str(rm[2,5])+",&\n")
             f2.write(temp_write)
             temp_write=("R41="+str(rm[3,0])+",R42="+str(rm[3,1])+",R43="+str(rm[3,2])+
                        ",R44="+str(rm[3,3])+",R45="+str(rm[3,4])+",R46="+str(rm[3,5])+",&\n")
             f2.write(temp_write)
             temp_write=("R51="+str(rm[4,0])+",R52="+str(rm[4,1])+",R53="+str(rm[4,2])+
                        ",R54="+str(rm[4,3])+",R55="+str(rm[4,4])+",R56="+str(rm[4,5])+",&\n")
             f2.write(temp_write)
             temp_write=("R61="+str(rm[5,0])+",R62="+str(rm[5,1])+",R63="+str(rm[5,2])+
                        ",R64="+str(rm[5,3])+",R65="+str(rm[5,4])+",R66="+str(rm[5,5])+"\n")
             f2.write(temp_write)
         elif type=="RFCAVITY" and float(volt)!=0.:
             temp_write=name+": RFCA, L="+l+", VOLT="+str(float(volt)*1E6)+\
                        ", PHASE="+str((float(lag)-0.5)*360)+", FREQ="+str(float(freq)*1E6)+\
                        ", CHANGE_T=0"+"\n"
             f2.write(temp_write)
         elif type=="SOLENOID" and float(l)!=0.:
             temp_write=name+":"+"SOLE"+",L="+l+",KS="+str(float(ksi)/float(l))+",ORDER=2\n"
             f2.write(temp_write)
#         elif type=="SEXTUPOLE":
#             temp_write= name+":"+"KSEXT"+",L="+l+",k2=0,TILT="+tilt+",N_KICKS = 10\n"
#             f2.write(temp_write)
#         elif type=="HMONITOR" and float(l)==0.:
#             temp_write= name+":"+"MARKER \n"
#             f2.write(temp_write)
#         elif type=="VMONITOR" and float(l)==0.:
#             temp_write= name+":"+"MARKER \n"
#             f2.write(temp_write)
#         elif type=="MONITOR" and float(l)==0.:
#             temp_write= name+":"+"MARKER \n"
#             f2.write(temp_write)
#         elif type=="MULTIPOLE" and k1l==0:
#             temp_write= name+":"+"MULT"+",l="+l+"," 
#             f2.write(temp_write)
#             f2.write( 'N_KICKS=1; \n')
#         elif type=="MULTIPOLE" and k1l!=0:
#             temp_write= name+":"+"MULT"+",l="+l+"," 
#             f2.write(temp_write)
#             temp_write="KNL=" +k1l+",&\n"
#             f2.write( temp_write )
#             f2.write( 'N_KICKS=1 \n')
#         elif type=="HKICKER" or type=="VKICKER":
#             temp_write= name+":"+ "KICKER" +",L="+l+ " \n"
#             f2.write(temp_write)
#         elif type=="RFCAVITY" and rf_first==1:
#             rf_first=0
#             temp_write= name+":"+ "RFCA,  FREQ = 78196.2811281, VOLT = 5e6\n"
#             f2.write(temp_write)
         else:
             temp_write= name+":"+"DRIFT"+",L="+ l+"\n" 
             f2.write(temp_write)
             
print "total length is: ",total_l
print "total number of elements =  ", len(nameseq)
print "number of different elements =  ",len(namelist)
print "total angle = ",total_ang

f2.write('SR_cooler: LINE=(& \n')

elem_per_line=10
mline=len(nameseq)/elem_per_line

for i in range(mline):
    for j in range(elem_per_line):
        f2.write(nameseq[elem_per_line*i+j]+",")
    f2.write("&\n")

for i in range(len(nameseq)-elem_per_line*mline-1):
    f2.write(nameseq[elem_per_line*mline+i]+",")
f2.write(nameseq[len(nameseq)-1]+")\n")

f2.write("USE,SR_cooler\n")
f2.write("RETURN")
f2.close()
sys.exit()


# f01=open("./rhic_elegant.lte",'r')
# holder1=f01.readlines()
# f01.close()

# nlines=len(holder1)
# f02=open("./temp",'w')
# for l in range(nlines):
#     temp1=holder1[l]
#     temp1=temp1.replace(". ",".0")
#     temp1=temp1.replace(".E",".0E")
#     f02.write(temp1)
# f02.close()

# commands.getstatusoutput("cp temp rhic_elegant.lte")

