# Keras 특징
# User Friendliness : Keras의 직관적인 API를 이용하면 일반 신경망(ANN), CNN, RNN 모델 또는 이를 조합한 다양한 딥러닝 모델을 (몇 줄의 코드만으로) 쉽게 구축 할 수 있음
# Modularity : Keras에서 제공하는 모듈은 독립적으로 설정 가능함. 즉 신경망 층, 손실함수, 활성화 함수, 최적화 알고리즘 등은 모두 독립적인 모듈이기 때문에 이러한 모듈을 서로
# 조합하기만 하면 새로운 딥러닝 모델을 쉽고 빠르게 만들어서 학습시킬 수 있음

# ///Keras의 가장 핵심적인 데이터 구조는 모델(model)////

import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.optimizers import SGD

import numpy as np
print(tf.__version__)

x_data = np.array([1, 2, 3, 4, 5, 6])
t_data = np.array([3, 4, 5, 6 ,7, 8])

model = Sequential()    # 모델

model.add(Flatten(input_shape=(1,)))    # 입력층
model.add(Dense(1, activation='linear'))    # 출력층

# model.add(Dense(1, input_shape(1,), activition='linear'))

model.compile(optimizer=SGD(learning_rate=1e-2), loss='mse')

model.summary()

hist = model.fit(x_data, t_data, epochs=2000)

result = model.predict(np.array([-3.1, 3.0, 3.5, 15.0, 20.1]))
print(result)