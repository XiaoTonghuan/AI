import numpy as np
import pandas as pd
#data
path = "ex1data1.txt"
data = pd.read_csv(path,header=None, names=['Population', 'Profit'])
#read X,y
X = np.matrix(np.vstack((np.ones(5),np.array([[34.623660,30.286711,35.847409,60.182599,79.032736],[78.024693,43.894998,72.902198,86.308552,75.344376]]))))
y = np.matrix(np.array([0,0,0,1,1])).T
theta = np.matrix(np.array([1,1,1])).T

# sigmoid function 假设函数，返回概率
def sigmoid_func(z):
    return 1 / (1 + np.power(np.e,-z))

# cost function 损失函数
def logic_cost_function(theta,X,y):
    sigmoid_func(np.dot(theta.T,X))
    s = np.multiply(y.T ,np.log(sigmoid_func(theta.T * X))) # *在矩阵之间运算是矩阵相乘
    e = np.multiply((1-y.T) ,np.log(sigmoid_func(1-theta.T * X)))
    return - (s + e)/y.shape[0]
# 梯度下降
def gradientDescent(theta,X,y,alpha,iters):
    temp = np.matrix(np.zeros(theta.shape))
    for i in range(iters):
        outer = sigmoid_func(theta.T * X) - y.T
        for j in range(theta.shape[1]):
            temp[j] = np.sum(np.multiply(outer,X[j]))
        theta = theta - alpha * temp / y.shape[1]
    return theta



print(gradientDescent(theta,X,y,0.01,15000))