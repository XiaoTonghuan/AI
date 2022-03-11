import numpy as np
#sigmoid
def sigmoid_func(z):
    return 1 / (1 + np.power(np.e,-z))
#liner_func
#liner regular
#\theta_j = \theta_j - \alpha / m * [\sum_{i=1}^m ( h ^{(i)}_\theta (x) - y ^{(i)})x^{(i)}_j + \lambda \theta_j]

# 正则化的cost func
def logic_cost_func_regular(theta,X,y,lambdas):
    return (np.sum(sigmoid_func((theta.T * X) - y) ** 2) + lambdas * np.sum(theta ** 2) )/(2*y.shape[1])
#正则化梯度下降
def radientReg(theta, X, y, alpha,iters):
    y = y.T
    para = theta.shape[0]
    temp = np.matrix(np.zeros(theta.shape))
    m = y.shape[1]
    for i in range(iters):
        outer = theta.T * X - y
        for j in range(para):
            regulars = alpha* theta[j] / m if j != 0 else 0 #好像加了之后效果变差了，可能是数据太少了
            temp[j] = theta[j] - alpha * np.sum(np.multiply(outer,X[j])) / m + regulars
        theta = temp
    return theta
theta = np.matrix([1,1]).T
X = np.matrix([[1,1],[1,2]])
y = np.matrix([3,5]).T
