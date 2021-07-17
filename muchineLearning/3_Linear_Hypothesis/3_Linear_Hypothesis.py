# cost(W, b)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

# H(x) = Wx + b
# X and Y data
x_train = [1, 2, 3]
y_train = [1, 2, 3]

# tf.Variable() 텐서에서 사용하는 변수다라고 생각하면 됨
# tf.random.normal(
#    shape, mean=0.0, stddev=1.0, dtype=tf.dtypes.float32, seed=None, name=None
# )
"""
tensorflow 2에서는 random_* 함수들이 random.*로 변경되었다.
tensorflow 2를 쓴다면 random.normal을 사용하자.
W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')
"""

W = tf.Variable(tf.random.normal([1]), name='weight')
b = tf.Variable(tf.random.normal([1]), name='bias')

# Our hyphothesis xW+b
hypothesis = x_train * W + b

# tensorflow에 있는 cost/loss function
@tf.function
def cost():
    cost = tf.reduce_mean(tf.square(hypothesis - y_train))  # tf.square = 제곱을 계산, tf.reduce_mean = 특정 차원을 제거하고 평균을 구함 -> 1/m*시그마 부분
    return cost

# Minimize
# optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01) 텐서플로 1.x
optimizer = tf.optimizers.SGD (learning_rate=0.01)
train = optimizer.minimize(cost(), var_list=None)



# 텐서플로 1.x
# outputs = session.run(f(placeholder), feed_dict={placeholder: input})
# 텐서플로 2.0
# outputs = f(input)
@tf.function
def init_var(var):
    return var.global_variables_initializer()   # Initializes global variables in the graph


# Fit the line
for step in range(2001):
    init_var(train)
    if step % 20 == 0:
        print(step, init_var(cost), init_var(W), init_var(b))