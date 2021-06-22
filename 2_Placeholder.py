import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

# 데이터 셋을 담을 Computational Graph준비(tf.placeholder)
a = tf.Variable(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b

print