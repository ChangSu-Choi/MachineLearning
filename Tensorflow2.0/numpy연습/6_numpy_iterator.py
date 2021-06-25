# explicit(명시적) 인덱싱 / 슬라이싱 이외에, 행렬 모든 원소를 access 하는 경우에는 iterator 사용가능

import numpy as np

A = np.array([ [10, 20, 30, 40], [50, 60, 70, 80] ])

print(A, '\n')
print("A.shape = ", A.shape, "\n")

# 행렬 A의 itrator 생성
it = np.nditer(A, flags=['multi_index'], op_flags=['readwrite'])

while not it.finished:
    idx = it.multi_index
    print("current value => ", A[idx])

    it.iternext()