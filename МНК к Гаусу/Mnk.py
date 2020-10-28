import numpy as np
import math as m
import matplotlib.pyplot as plt
def gaus(a,b):
    L = len(a)
    e = 0.001
    Perestan = []
    for i in range(L):
        Perestan.append(i)

    for k in range(0,L-1):
        if a[k][k] <= e:

            n = k+1

            while( abs( a[n][k] ) <= e ):

                n+=1
            
            a[k] , a[n] = a[n] , a[k].copy()
            temp = Perestan[k]
            Perestan[k]=Perestan[n]
            Perestan[n]=temp
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
z = []
g = []
for i in np.arange(-3,3,0.001):
    g.append(i)
    z.append(i**3)



def koef(xn,y):
    A = [ [0 for j in range(10)] for i in range(10)]
    b = []
    L = len(xn)
    aij = 0
    bi = 0
    for i in range(10):
        for j in range(10):
            for n in range(400):
                aij+=(xn[n]**3)*(xn[n]**3)
            A[i][j]=aij
            
    for i in range(10):
        for n in range(400):
            bi += xn[n]*y[n]
        b.append(bi)
    return(A,b)

K = koef(g,z)
print(K[0])
I = gaus(K[0],K[1])

plt.subplot(1,2,1)
plt.plot(g,z)
plt.subplot(1,2,2)
plt.plot(g,I)