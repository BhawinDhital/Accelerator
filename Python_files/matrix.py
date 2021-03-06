# To test the symplectic condition
import numpy as np
M56 = A = np.array([[1.0,0.0,0.0,0.0,0.0,0.0],
[0.0,1.0,0.0,0.0,0.0,0.0],
[0.0,0.0,1.0,0.0,0.0,0.0],
[0.0,0.0,0.0,1.0,0.0,0.0],
[0.0,0.0,0.0,0.0,1.0,12.60],
[0.0,0.0,0.0,0.0,0.0,1.0]])
J = np.array([[0.0,1.0,0.0,0.0,0.0,0.0],
[-1.0,0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.0,1.0,0.0,0.0],
[0.0,0.0,-1.0,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0,1.0],
[0.0,0.0,0.0,0.0,-1.0,0.0]])

A_tra = A.transpose()
#symplectic condition: A_tra J A = J
B = np.dot(J,A)
C=np.dot(A_tra,B)
print(C)
