import tensorflow as tf

W = tf.Variable(tf.random.normal([1]))  # 가우시안 분포
print('initial W = ', W.numpy())
print('===============================')

# session 생성 없이 즉시 시행 (Eager Execution)
# numpy() 메서드 사용하면 numpy 값을 리턴해줌

for step in range(2):
    W = W + 1.0
    print('step = ', step, ', W = ', W.numpy())