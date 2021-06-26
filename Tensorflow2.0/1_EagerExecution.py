# 1. 계산 그래프와 세션을 생성하지 않고 즉시 실행 가능한 Eager Execution 적용되었으며
# 2. 또한 사용자에게 제공되는 High-Level API 로서 Keras 만을 제공함
import tensorflow as tf
import numpy as np

# TensorFlow 1.x 에서는 계산 그래프를 선언하고 세션을 통해 텐서(Tensor)를 주고 받으며 계산하는 구조였으나.
# TensorFlow 2.x 에서는 자동으로 Eager Execution(즉시 실행 모드) 적용되기 때문에 그래프와 세션을,
# 만들지 않아도 텐서 값을 계산하고 numpy() 함수를 이용하면 파이썬의 넘파이 타입으로 변환할 수 있음

tf.__version__

a = tf.constant(10)
b = tf.constant(20)

c = a + b
d = (a+b).numpy()   # numpy()메서드는 numpy 값을 리턴

print(type(c))
print(c)
print(type(d), d)

d_numpy_to_tensor = tf.convert_to_tensor(d) # tf.convert_to_tensor() 메서드 numpy 값을 tensor 값으로 변환

print(type(d_numpy_to_tensor))
print(d_numpy_to_tensor)