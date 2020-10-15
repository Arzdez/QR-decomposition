import numpy as np

a = np.loadtxt('1.txt')
print(a)
  
def det(mat):
    if len(mat) == 2:
        return mat[0,0]*mat[1,1]-mat[0,1]*mat[1,0]
    matrix_shape = mat.shape[0]-1
    arrM1 = np.eye(matrix_shape,dtype ='int')
    Deter = 0
    for j in range(len(mat)):
        arrM1[0:,:j]=mat[1:,:j]
        arrM1[0:,j:]=mat[1:,j+1:]
        Deter+=((-1)**j)*det(arrM1)*mat[0][j]
    return Deter
print(det(a))
    
