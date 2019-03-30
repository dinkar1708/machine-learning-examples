import numpy as np
import tensorflow as tf

# placeholder - Inserts a placeholder for a tensor that will be always fed.

# Example1-
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

adder_node = a + b
sess = tf.Session()
print(sess.run(adder_node, {a: [1, 2], b: [2, 3]}))
sess.close()

# Example2
x = tf.placeholder(tf.float32, shape=(1024, 1024))
y = tf.matmul(x, x)

with tf.Session() as sess:
    #   print(sess.run(y))  # ERROR: will fail because x was not fed.
    rand_array = np.random.rand(1024, 1024)
    print(sess.run(y, feed_dict={x: rand_array}))  # Will succeed.
