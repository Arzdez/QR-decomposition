import numpy as np
import math
from copy import deepcopy
from numpy import dot
#np.dot умножение матриц

A = np.loadtxt('1.txt')
def QR(A):
    #копирование и транспонирование матрицы
    At = A.transpose()
    Qt = deepcopy(At)
    #размеры матрицы
    Qshape0 = np.shape(Qt)[0]
    Qshape1 = np.shape(Qt)[1]
    print(np.shape(Qt))
    # объявление матрциы r
    r = np.zeros((Qshape1,Qshape1))
    #нормировка первой строки
    norm = np.dot(Qt[0],At[0])
    for i in range(Qshape1):
        Qt[0][i] = Qt[0][i]/math.sqrt(norm)

    for k in range(Qshape0):
        for j in range(Qshape1):
            if j<k:
                Vkj = np.dot(Qt[j],At[k])
                Qt[k]= Qt[k]-Vkj*Qt[j]
                norm = np.dot(Qt[0],At[0])
                for i in range(Qshape1):
                    Qt[k][i]=Qt[0][i]/math.sqrt(norm)
                
    for i in range (Qshape1):
        for j in range(Qshape1):
            if j >=i:
                r[i][j]= np.dot(At[i],Qt[j])
            else:
                r[i][j]=0
    print(Qt)
    print('\n',r)
    return 0

QR(A)

