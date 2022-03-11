import numpy as np
import matplotlib.pyplot as plt
# 线性回归
x = np.matrix(np.array([6.1101,5.5277,8.5186,7.0032,5.8598]))
y = np.matrix(np.array([17.5920,9.1302,13.6620,11.8540,6.8233]))
theta = np.matrix(np.array([2.,2.])).T
x = np.vstack((np.ones(5),x))
# hyposis 函数 \theta_0 x + theta_1
# Cost function J(\theta) = \frac{1}{2m} \sum_{i=1}^{m}(h(x^{(i)})-y^{(i)})^2
def cost_function(x,y,theta):
    m = len(x)
    inner = np.power(np.dot(theta.T,x) - y,2)
    return np.sum(inner) / (2 * m)
# 梯度下降
# \theta_i = \theta_i - \alpha \frac{1}{m} \sum (\theta^T x - y) * x
def gradientDescent(x,y,theta,alpha,iters):
    m = len(x)
    temp = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    for i in range(iters):
        inner = (np.dot(theta.T, x) - y)
        for j in range(parameters):
            term = np.multiply(inner,x[j])
            temp[j,0] = theta[j,0] - (alpha * np.sum(term) / m)
        theta = temp
    return theta
#正规方程
#这边的数据的输入方式和上边的梯度下降的方式有些不同，这边每一个样本的所有特征构成一个列向量，X矩阵每一行代表一个样本的所有特征
#而上面的梯度下降，每一列代表，每一个样本的所有特征
#这里的y也是列向量，而上面的y是行向量
def normalEqn(X,Y):
    return np.dot(np.dot(np.linalg.pinv(np.dot(X.T,X)),X.T),Y)
print(gradientDescent(x,y,theta,0.01,15000))
print(normalEqn(x.T,y.T))

# plt.scatter(x,y)
# plt.show()