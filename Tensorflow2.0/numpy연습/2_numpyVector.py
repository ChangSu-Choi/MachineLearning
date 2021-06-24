# vertor는 np.array([....])를 사용하여 생성함 (import numpy as np)
# 머신러닝 코드 구현시, 연산을 위해서 vector, matrix 등의 형상(shape), 차원(demension)을 확인하는 것이 필요함
import numpy as np

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# vector A, B 출력
print("A == ", A, ", B == ", B)

# vector A, B 형상 출력 => shape
print("A.shape == ", A.shape, ", B.shape == ", B.shape)

# vector A, B 차원 출력 => ndim
print("A.ndim == ", A.ndim, ", B.ndim == ", B.ndim)

# vector 산술 연산
# vector간 산술연산은 벡터의 각각의 원소에 대해서 행해짐
print("A + B ==", A+B)
print("A - B ==", A-B)
print("A * B ==", A*B)
print("A / B ==", A/B)



# 행렬(matrix) 생성 => matrix는 vector과 마찬가지로 np.array([ [...], [...], [...] ])를 사용하여 생성함(import numpy as np)

A = np.array([ [1, 2, 3], [4, 5, 6] ])
B = np.array([ [-1, -2, -3], [-4, -5, -6] ])

# vector A, B 형상 출력 => shape
print("A.shape == ", A.shape, ", B.shape == ", B.shape)

# vector A, B 차원 출력 => ndim
print("A.ndim == ", A.ndim, ", B.ndim == ", B.ndim)


# 형 변환 (reshape)
# => vector를 matrix로 변경하거나 matrix를 다른 형상의 matrix로 변경하기 위해서는 reshape() 사용하여 행렬의 shape을 변경하여야 함

# vector생성
C = np.array([1, 2, 3])

# vector C형상 출력 => shape
print(C)
print("C.shape ==", C.shape)

# vector를 (1, 3) 행렬로 형 변환
C = C.reshape(3, 1)

print(C)
print("C.shape == ", C.shape)