import numpy as np
import math
from copy import deepcopy
from numpy import dot
#np.dot умножение матриц
def func():
    return(2*(x**3)+3*(x**2)+5*x+7)

A = np.loadtxt('1.txt')
x = np.loadtxt
def QR(A):
    #копирование и транспонирование матрицы
    At = A.transpose()
    shape = np.shape(At)
    Qt = np.zeros((shape[0],shape[1]))
    r = np.zeros((shape[0],shape[0]))

    for i in range(shape[0]):
        for j in range(shape[1]):
            Qt[i][j]=At[i][j]
    
    norm = np.dot(Qt[0],Qt[0])
    for i in range(shape[1]):
        Qt[0][i] = Qt[0][i]/math.sqrt(norm)
    
    for k in range(1,shape[0]):
        for j in range(shape[0]):
            if j < k:
                Vkj = np.dot(Qt[j],Qt[k])
                Qt[k]=Qt[k]-Vkj*Qt[j]
                norm2 = dot(Qt[k],Qt[k])
                for i in range(shape[1]):
                    Qt[k][i]=Qt[k][i]/math.sqrt(norm2)
                

                
    for i in range (shape[0]):
        for j in range(shape[0]):
            if j >=i:
                r[i][j]= np.dot(At[j],Qt[i])
            else:
                r[i][j]=0
    print(Qt)
    print('\n',r)
    return 0


QR(A)
Qb,rD = np.linalg.qr(A)
print('\n',Qb.T)
print('\n',rD)

def matbaz(A):
    F = []
    for i in range(3):
        for j in range(len(x))


