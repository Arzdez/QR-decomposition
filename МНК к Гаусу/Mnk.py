import numpy as np
import math as m
import matplotlib.pyplot as plt
def gaus(a,b):
    L = len(a)
    e = 0.001

    for k in range(0,L-1):
        if a[k][k] <= e:

            n = k+1

            while( abs( a[n][k] ) <= e ):

                n+=1
            
            a[k] , a[n] = a[n] , a[k].copy()
            temp =b[k]
            b[k]=b[n]
            b[n]=temp
            
            
        for i in range(k+1,L):
            g = a[i][k] / a[k][k]

            b[i]=b[i]-g*b[k]

            for j in range(k,L):
                a[i][j] = a[i][j] - g*a[k][j]

    print(a)
    print(b)




    X = [0 for d in range(L)]

    for i in range(len(b) - 1, -1, -1):
        X[i] = (b[i] - sum(x * j for x, j in zip(X[(i + 1):], a[i][(i + 1):])))/a[i][i]
    print("\n".join("X{0} =\t{1:10.2f}".format(i + 1, x) for i, x in
    enumerate(X)))

    return X
X = []
Y = []
LenY=len(Y)

for i in np.arange(-3,3,0.01):
    X.append(i)
    Y.append(i**3)

Aij = np.zeros((LenY,LenY))
Bi= np.zeroz(LenY)

for i in range(LenY):
    for j in range(LenY):
        Aij[i][j] = ( X[i]**3 ) * ( X[i]**3 )

for i in range(LenY):
    Bi[i] = ( X[i]**3 ) * Y[i]

C = gaus(Aij,Bi)

plt.subplot(1,2,1)
plt.plot(Y)
plt.subplot(1,2,2)
plt.plot(X)
plt.show()

