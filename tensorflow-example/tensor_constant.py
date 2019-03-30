import tensorflow as tf

# create constant nodes
node_a = tf.constant(3.0, tf.float32)
node_b = tf.constant(4.0)

# Method1
# sess = tf.Session()
# print(sess.run([node1, node2]))
# sess.close()

# Method2
with tf.Session() as sess:
    output = sess.run([node_a, node_b])
    print(output)
