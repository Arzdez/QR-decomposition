from math import fabs
import matplotlib.pyplot as plt
import pylab
import math
def f( x ):
    return  (5*x**3)-(x**2)-20*x+4
def diff(x):
    return (15*x**2)-(2*x)-20
 
def dichotomia( a, b, eps,Xo,k,k1):
    C = ( a + b ) / 2.0

    if ( fabs( f(a) - f(b) ) <= eps ) or ( fabs( f(C) ) <= eps ):
        Xo.append(( a + b ) / 2.0 )
        k1+=1
        k.append(k1)
        return k1
    if ( f( a )*f( C ) <= 0.0 ):
        Xo.append(( a + b ) / 2.0 )
        k1+=1
        k.append(k1)
        return dichotomia( a, C, eps, Xo, k,k1)
    else:
        Xo.append(( a + b ) / 2.0 )
        k1+=1
        k.append(k1)
        return dichotomia( C, b, eps,Xo,k,k1 )

a = 1
b = 40
eps = 0.1
Xo = []
k = []
k1 = 0        

def Efaptomenos(a,b, e):
    Xi = []
    x0 = (a+b)/2
    k = []
    k1 = 0
    while(( fabs (f(x0)/diff(x0)) > e)):
        x0 = x0-(f(x0)/diff(x0))
        Xi.append(x0)
        k1+=1
        k.append(k1)
    return k1
A = []
B = []
D = []
for i in range(500):
    A.append(dichotomia( a, b, eps,Xo,k,k1))
    B.append(Efaptomenos(a,b,eps))
    D.append(eps)
    eps=eps/2

z = []
print(len(D))

for i in D:
    z.append(math.log2(i/max(D)))

print(len(A))            
    


plt.plot(z,A)
plt.plot(z,B)
plt.show()
