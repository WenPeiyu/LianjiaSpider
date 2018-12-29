# import os
# from os.path import getsize
#
# def getsize1(path):
#     return getsize(path)/1024/1024/1024
#
#
# size = 0
# with open(r"C:\Users\wenpeiyu\Desktop\filelist.txt", "r",encoding="utf-8") as f:
#     for i in f.readlines():
#         size += getsize1(i.strip())
# print(size)
#
#
#
# import shutil
# import os
# from xml.dom.minidom import parse
# import xml.dom.minidom
# from utils import dir_list
# import sys

# 使用minidom解析器打开 XML 文档
# DOMTree = xml.dom.minidom.parse(r"C:\Users\wenpeiyu\Desktop\FileZilla.xml")
# collection = DOMTree.documentElement
# for i in collection.getElementsByTagName("LocalFile"):
#     shutil.copyfile(i.childNodes[0].data, r"f:/1/"+os.path.split(i.childNodes[0].data)[1])


# print(os.path.split(sys.argv[0])[0])
# with open(os.path.split(sys.argv[0])[0] + "/rawdata/enodeb.txt", "w") as wf:
#     for i in dir_list(os.path.split(sys.argv[0])[0] + "/rawdata/",filter_="BPN"):
#         with open(i, "r") as rf:
#             wf.writelines(rf.readlines())




import tensorflow as tf

# Import MINST data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

# Parameters
learning_rate = 0.01
training_epochs = 25
batch_size = 100
display_step = 1

# tf Graph Input
x = tf.placeholder(tf.float32, [None, 784]) # mnist data image of shape 28*28=784
y = tf.placeholder(tf.float32, [None, 10]) # 0-9 digits recognition => 10 classes

# Set model weights
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# Construct model
pred = tf.nn.softmax(tf.matmul(x, W) + b) # Softmax

# Minimize error using cross entropy
cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), reduction_indices=1))
# Gradient Descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    # Training cycle
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples/batch_size)
        # Loop over all batches
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            # Fit training using batch data
            _, c = sess.run([optimizer, cost], feed_dict={x: batch_xs,
                                                          y: batch_ys})
            # Compute average loss
            avg_cost += c / total_batch
        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            print ("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(avg_cost))

    print ("Optimization Finished!")

    # Test model
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    # Calculate accuracy for 3000 examples
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print( "Accuracy:", accuracy.eval({x: mnist.test.images[:3000], y: mnist.test.labels[:3000]}))