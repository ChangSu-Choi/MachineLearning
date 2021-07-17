# Info 로그를 필터링하려면 1, Warning 로그는 2, Error 로그는 3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

#앞쪽 레이어의 노드 빌드하기
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly


# 뒷쪽 레이어의 노드(즉 node3)를 함수로 정의하기
@tf.function
def forward():
    return node1 + node2

# 그래프를 실행시키고 output을 확인해보기
out_a = forward()
print(out_a)