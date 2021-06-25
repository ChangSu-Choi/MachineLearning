# 실무에서는 머신러닝 코드를 구현하기 전에
# 입력 데이터의 분포와 모양을 먼저 그래프로 그려보고, 데이터의 특성과 분포를 파악 한 후 어떤 알고리즘을 적용할지 결정하고있음
# 데이터 시각화를 위해서는 matplotlib 라이브러리를 사용함
# 일반적으로 line plot, scatter plot등을 통해 데이터의 분포와 형태를 파악함

import matplotlib.pyplot as plt
import numpy as np

# x data, y data 생성
x_data = np.random.rand(100)
y_data = np.random.rand(100)

plt.title('scatter plot')
plt.grid()
plt.scatter(x_data, y_data, color='b', marker='o')
plt.show()

X_data = [x for x in range(-5, 5)]
Y_data = [y*y for y in range(-5, 5)]

plt.title('line plot')
plt.grid()
plt.plot(X_data, Y_data, color='b')
plt.show()