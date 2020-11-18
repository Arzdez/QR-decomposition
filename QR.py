import numpy as np
import math
from copy import deepcopy
from numpy import dot
#np.dot умножение матриц

A = np.loadtxt('1.txt')
def QR(A):
    A = A.transpose()
    Q = deepcopy(A)

    shapes = np.shape(A)
    Vkj = 0
    norm = np.dot(Q[0],A[0])

    r = np.zeros((shapes[0],shapes(0)))

    for i in range(shapes[0]):
        Q[0][i] = Q[0][i]/math.sqrt(norm)

    for k in range(1,shapes[1]):
        for j in range(shapes[1]):
            Vkj = np.dot(Q[j],A[k])
            Q[k]= Q[k] - Vkj*Q[j]


        norm = np.dot(Q[k],Q[k])
        for i in range(shapes[0]):
            Q[k][i] = Q[k][i]/math.sqrt(norm)
    
   
    for i in range (shapes[0]):
        for j in range(shapes[0]):
            if j >=i:
                r[i][j]= np.dot(A[i],Q[j])
            else:
                r[i][j]=0
    return Q,r

Q1,r1 = QR(A)
for i in range(len(Q1)):
    print(np.linalg.norm(Q1[i]))

print('\n',Q1)
print('\n',r1)
print('\n',Q1.dot(r1))