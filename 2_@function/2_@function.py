import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

# 데이터 셋을 담을 Computational Graph준비(tf.placeholder)
# 대신 tensorflow 2 에선 @tf.function으로 함수를 정의함

@tf.function
def adder(a, b):
    return a + b

#현재 constant와 Variable의 차이는 거의 없음
a = tf.constant(3)
b = tf.constant(4)

c = tf.Variable([1, 3])
d = tf.Variable([2, 4])

print(adder(a, b))
print(adder(c, d))

# 내장함수도 있다
print(tf.subtract(b, a))
print(tf.multiply(c, d))