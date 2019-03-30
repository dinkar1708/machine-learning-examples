import tensorflow as tf

# initialize variables
W = tf.Variable([-1.0], tf.float32)
b = tf.Variable([1.0], tf.float32)
# initialize place holder
x = tf.placeholder(tf.float32)
# linear expression
linear_model = W * x + b
y = tf.placeholder(tf.float32)

squared_delta = tf.square(linear_model - y)

loss = tf.reduce_sum(squared_delta)

initializer = tf.global_variables_initializer()

sess = tf.Session()

sess.run(initializer)
# calculate loss
print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))

sess.close()
