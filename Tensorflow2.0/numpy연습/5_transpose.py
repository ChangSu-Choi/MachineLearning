# transpose(전치행렬)
# 원본 행렬의 열 -> 행, 행 -> 열로 바꾼것
# 원본 행렬은 A라 하면 전치행렬은 A^T로 나타냄

import numpy as np

A = np.array([ [1, 2], [3, 4], [5, 6] ])    # 3X2 행렬
B = A.T # A의 전치행렬, 2X3 행렬

print("A.shape = ", A.shape, ", B.shape = ", B.shape)
print(A)
print(B)

# vector 전치행렬
C = np.array([1, 2, 3, 4, 5])   # vector, matrix 아님
D = C.T # C는 vector 이므로 transpose 안됨

E = C.reshape(1, 5)  # 1X5 matrix
F = E.T #E의 전치행렬

print("C.shape = ", C.shape, ", D.shape = ", D.shape)
print("E.shape = ", E.shape, ", F.shape = ", F.shape)
print(F)