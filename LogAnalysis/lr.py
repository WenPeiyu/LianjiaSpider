'''
Created on 2018-11-20

@author: 10200985
'''

import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder

data = pd.read_csv('h:/data2.csv') # dataset
for x in [[1], [2], [3], [4], [5], [6], [7], [8], [9]]:
    y = 10
    size1= len(x)
    x_data = data.iloc[:,x]
    y_data = data.iloc[:,y]

    # x_data = data.iloc[:,[0,1,3,4]]
    # y_data = data.iloc[:,5]
    scaler = MinMaxScaler()
    X_data = scaler.fit_transform(x_data)
    #print(X_data)
    #Y = OneHotEncoder().fit_transform(y_data).todense()
    #Y = Y.T
    Y = pd.DataFrame(y_data).values
    Y = OneHotEncoder().fit_transform(Y).todense()
    #print(Y)
    batch_size = 10
    def generatebatch(X,Y,n_examples, batch_size):
        for batch_i in range(n_examples // batch_size):
            start = batch_i*batch_size
            end = start + batch_size
            batch_xs = X[start:end, :]
            batch_ys = Y[start:end]
            yield batch_xs, batch_ys

    tf.reset_default_graph()
    tf_X = tf.placeholder(tf.float32,[None,size1])
    tf_Y = tf.placeholder(tf.float32,[None,2])

    tf_W_L1 = tf.Variable(tf.random_normal([size1,2]))
    tf_b_L1 = tf.Variable(tf.random_normal([1,2]))

    pred = tf.nn.softmax(tf.matmul(tf_X,tf_W_L1)+tf_b_L1)
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=tf_Y,logits=pred))
    train_step = tf.train.AdamOptimizer(0.001).minimize(loss)
    y_pred = tf.arg_max(pred,1)
    bool_pred = tf.equal(tf.arg_max(tf_Y,1),y_pred)

    accuracy = tf.reduce_mean(tf.cast(bool_pred,tf.float32))

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        rst_w1 = sess.run(tf_W_L1)
        print('rst_w1_init:')
        print(rst_w1)
        for epoch in range(10001):
            for batch_xs,batch_ys in generatebatch(X_data,Y,Y.shape[0],batch_size):
                sess.run(train_step,feed_dict={tf_X:batch_xs,tf_Y:batch_ys})
            if(epoch%1000==0):
                res = sess.run(accuracy,feed_dict={tf_X:X_data,tf_Y:Y})
                print (epoch,res)
        rst_w1 = sess.run(tf_W_L1)
        rst_b1 = sess.run(tf_b_L1)
        print('rst_w1:')
        print(rst_w1)
        print('rst_b1:')
        print(rst_b1)
        res_ypred = y_pred.eval(feed_dict={tf_X:X_data,tf_Y:Y}).flatten()
        print(res_ypred)
