import tensorflow as tf

a = tf.constant(3.0)
b = tf.constant(4.0)

c = a * b

with tf.Session() as sess:
    File_Writer = tf.summary.FileWriter("./graph", sess.graph)
    output = sess.run([c])
    print(output)

sess.close()
