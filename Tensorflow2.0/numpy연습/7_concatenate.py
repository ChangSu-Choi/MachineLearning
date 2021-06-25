# numpy.concatenate() 행렬에 행(row) 또는 열(columm) 추가하기
# 머신러닝의 회귀(regression)코드 구현시 weight와 bias를 별도로 구분하지 않고 하나의 행렬로 취급하기 위한 프로그래밍 구현 기술

import numpy as np

# 행렬에 열과 행 추가
A = np.array([ [10, 20, 30], [40, 50, 60] ])

print(A.shape)

# A matrix에 row 추가할 행렬, 1 row 3 column로 reshape
# row을 추가하기 때문에 우선 column을 3column로 만들어야 함.
row_add = np.array([70, 80, 90]).reshape(1, 3)

# A matrix에 column 추가할 행렬, 2row 1column로 생성
# column을 추가하기 때문에 우선 row를 2row로 만들어야 함
column_add = np.array([1000, 2000]).reshape(2, 1)
print(column_add.shape)

# numpy.concatenate 에서 axis = 0 row 기준
# A 행렬에 row_add 행렬 추가
B = np.concatenate((A, row_add), axis=0)

print(B)
# numpy.concatenate에서 axis = 1 column기준
# B 행렬에 column_add 행렬 추가
C = np.concatenate((A, column_add), axis=1)

print(C)