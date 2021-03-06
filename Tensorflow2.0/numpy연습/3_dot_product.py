# 행렬 곱(dot product)
# A 행렬과 B 행렬의 행렬 곱(doc product)는 np.dot(A, B)로 나타내며, 행렬 A의 열 벡터와 B 행렬의 행 벡터가 같아야함.
# 만약 같지 않다면, reshape 또는 전치행렬(transpose)등을 사용하여 형 변환을 한 후에 행렬 곱을 실행 하여야 함
# 행렬 곱의 계산은 왼쪽에 있는 행렬에서 행 하나를 가져오고 오른쪽에 있는 행렬에서 열 하나를 가져와서 계산하면 된다.

import numpy as np

A = np.array([ [1, 2, 3], [4, 5, 6] ])          # 2x3 행렬
B = np.array([ [-1, -2], [-3, -4], [-5, -6] ])  # 3x2 행렬

# (2x3) dot product (3x2) == (2x2) 행렬
C = np.dot(A, B)    # 행렬 곱 수행

# matrix A, B 형상 출력 => shape
print("A.shpae = ", A, "B.shape =", B.shape)
print("C.shape = ", C.shape)
print(C)

# 행렬 곱은, 행렬의 원소 개수가 같아야만 계산할 수 있는 사칙연산의 한계를 벗어나
# 1. 행렬  곱 조건을 만족하는 다양한 크기의 행렬을 연속으로 만들고
# 2. 행렬 곱을 연속적으로 계산하면서
# 3. 결과값을 만들수 있기 때문에 머신러닝과 이미지 프로세싱 분야에서 자주 사용됨