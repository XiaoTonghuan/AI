# 监督学习

根据已经标记过的数据集，预测之后的结果

## 回归算法

### 线性回归

对一堆离散的数据进行曲线的拟合，称这样的问题为回归问题

-  m ：训练数据的数量
- x‘s ： 输入（**特征feature** ）
- y’s ：输出（target variable 目标变量）
- (x,y)  = 一个训练样本
- $(x^{(i)},y^{(i)})$ = 表示第i个训练样本
- h = 假设函数(hypothesis function) 
- 称所有的训练样本为数据集

如：

<img src=".assets/image-20220131140351092.png" alt="image-20220131140351092" style="zoom:80%;" />

对于假设函数是一次函数（$h(x) = \theta_0 + \theta_1 x$）的回归问题，称为**线性回归**

### 代价函数

- $\theta_i$：模型参数

- 代价函数(Cost function)：$J(\theta_0,\theta_1) = \frac{1}{2m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)})-y^{(i)})^2 \\$

  类似**方差**，计算目标变量和训练样本的偏差，为了使假设尽可能的准确，求该函数的**最小值**即可，将该操作记为${\min}_{\theta_0,\theta_1} J(\theta_0,\theta_1)\\$

  <img src=".assets/image-20220131142609473.png" alt="image-20220131142609473" style="zoom:80%;" /><img src=".assets/image-20220131142738206.png" alt="image-20220131142738206" style="zoom:80%;" />

可以将该图投影到平面上，即做该三维图像的**等高线图**。

### 梯度下降

**梯度下降**法是一种用来求代价函数**最小值**和**最小值点**的方法，即${\min}_{\theta_0,...,\theta_n} J(\theta_0,...,\theta_n)\\$

根据高等数学，**方向导数**的知识，导数指明了斜率（变化的趋势），我们只需要让参数跟随这个趋势变化，直到导函数为0即可。
$$
\theta_j := \theta_j - \alpha \frac{\part J}{\part \theta_j}
$$

- 其中$:=$表示赋值

- 值得注意的是，如果我们每做一次这个操作就赋值一次，会对原函数产生影响，所以选择对每一个自变量都求完偏导之后再进行赋值，即

  <img src=".assets/image-20220131145305922.png" alt="image-20220131145305922" style="zoom:80%;" />

- $\alpha$称为学习率，他决定了下降的速度快慢 

- 显然，使用“-”可以让我们收敛到最低点，如果使用“+”，我们就可以收敛到最高点。

### 线性回归的梯度下降

将线性的假设函数代入梯度下降算法，可以得到
$$
\theta_0 = \theta_0 - \alpha \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{i} )-y^{(i)})\\
\theta_1 = \theta_1 - \alpha \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{i} )-y^{(i)})\cdot x^{(i)}
$$

### 多元线性回归/梯度下降

当有多个特征值时
$$
h_{\theta}(x) = \theta_0+\theta_1x_1 + ...+\theta_n x_n\\
令 x = \begin{bmatrix}
x_0\\
x_1\\
\vdots\\
x_n
\end{bmatrix}
\theta=\begin{bmatrix}
\theta_0\\
\theta_1\\
\vdots\\
\theta_n
\end{bmatrix}
\\
h_{\theta}(x) = \theta^Tx
$$

- 规定$x_0 = 1$

- 代价函数可以写作

  $h_\theta(x) = \theta_j - \frac{\part J(\theta)}{\part \theta_j} =\theta_j - \alpha \frac{1}{m}\sum_{i=1}^m(h_{\theta}(x^{(i)})-y^{(i)}) x_j^{(i)}\\$

  - 其中$\theta 是向量$
  - $x_j^{(i)}$表示第i组数据的第j个特征

### 特征缩放

感觉有点像离散化的思想

对于一个特征变化范围特别大，而另一个特征变化范围比较小的情况下的梯度下降，会导致下降的速度十分的缓慢，因此可以通过特征缩放的方法，加快最小值的求解

更加一般的，常将特征收缩到**[-1,1]的范围**内，或者比较接近这个范围

**归一化**

大量的特征值似乎服从**正态分布**，所以将所有的特征值，进行变换$x_i=\frac{x_i-\mu_i}{\sigma_i}\\$

### 学习率

当迭代出现了一定的异常时，可以尝试较小的学习率

<img src=".assets/image-20220203172031536.png" alt="image-20220203172031536" style="zoom:50%;" />

直到求出的值是收敛的

### 特征和多项式回归

显然的，多项式可以拟合任意的曲线（**泰勒展开**），所以当出现线性回归无法处理的任务时，可以选择使用多项式的方式进行拟合

- 多项式回归中，特征的缩放显得更加重要

### 正规方程

对于m个**样本**$(x^{(1)},y^{(1)}),...(x^{(m)},y^{(m)})$，每个x有n个**特征**
$$
x^{(i)} = \begin{bmatrix}
x_0^{(i)}\\
\vdots\\
x_n^{(i)}
\end{bmatrix} \in \R^{n+1}
 \quad X_{m\cp (n+1)} = \begin{bmatrix}
 1,(x^{(1)})^T\\
 \vdots
 \\1,(x^{(m)})^T
 \end{bmatrix} \quad y = \begin{bmatrix}
 y^{(1)}\\
 y^{(2)}\\
 \vdots
 \\
 y^{(n)}
 \end{bmatrix}
$$
 则$\theta = (X^TX)^{-1}X^Ty$即为所求

$X^TX$何时不可逆

- 两个列向量之间能线性表示
- 特征太多，甚至多余样本个数

### 正规方程法和梯度下降法的对比

梯度下降

- 需要选$\alpha$
- 需要很多次迭代
- n很大时，效果依然很好

正规方程

- 时间复杂度大，n很大时效果不好
- 不需要迭代
- 不需要选择$\alpha$

## 分类

### Logistic 回归

$$
logistic(sigmoid) \quad function\\
g(x) =  \frac{1}{e^{-x}+1}\\
令x=\theta^Tx 得到 h_{\theta}(x) = \frac{1}{e^{-\theta^T x} +1}
$$

- 这个函数的值处在0和1之间
- 表示给定x和$\theta$时y=1的估计概率，即$p(y=1|x;\theta)$
- 当$h_\theta(x) \ge 0.5$时认为y=1的概率较大
- 由于$h_\theta(0)=0.5$，且该函数为单调递增函数，所以$h_\theta(x) \ge 0.5 \Leftrightarrow x >0$
-  称$\theta^Tx=0$所确定的范围为**决策界限**

### 损失函数

训练样本
$$
\{(x^{(1)},y^{(1)}),...,(x^{(m)},y^{(m)})\}
$$
特征
$$
x\in\begin{bmatrix}
x_1\\
\vdots\\
x_n
\end{bmatrix}
x_0\in 1,y\in \{0,1\}
$$
如何确定假设函数$h_\theta(x)$中的参数$\theta$?

如果按照之前的线性的方法，得到的函数有可能会是这样

<img src=".assets/image-20220207202901935.png" alt="image-20220207202901935" style="zoom:80%;" />

由于**假设函数**不是一个线性函数，所以得到的$J(\theta)$这个函数图像有很多的局部最优解，导致梯度下降的效果不是很好，所以我们可以这样定义**代价函数**
$$
Cost(h_\theta(x),y)=\begin{cases}
-\log(h_\theta(x))\quad &y=1\\
-\log(1-h_\theta(x))\quad& y=0
\end{cases}
$$

- 首先，我们注意到这个函数对于我们描述真实值和预测值之间的差距是很准确的，当预测值和真实值没有差距时，函数的值为0，而当预测值和实际值一个为0另一个为1时，函数趋向于无穷

### 简单的代价函数和梯度下降

通过前面的定义，逻辑回归的损失函数如下
$$
J(\theta) = \frac{1}{m}\sum_{i=1}^{m}Cost(h_\theta(x^{(i)}),y^{(i)})\\
Cost(h_\theta(x),y)=\begin{cases}
-\log(h_\theta(x))\quad &y=1\\
-\log(1-h_\theta(x))\quad& y=0
\end{cases}\quad y\in\{0,1\}
$$
可以得出，这个式子等价于（通过构造的方法）
$$
Cost(h_\theta(x),y) = -y\log (h_\theta(x))-(1-y)\log(1-h_\theta(x))
$$
从而
$$
J(\theta)=-\frac{1}{m}[\sum_{i=1}^my^{(i)}\log h_\theta(x^{(i)})+(1-y^{(i)})\log( 1-h_\theta{(x^{(i)})}  )]
$$
下面考虑用梯度下降的方法求使得$J(\theta)$取得最小值时的$\theta$的值，求偏导之后惊奇的发现
$$
\theta_j = \theta_j - \alpha \sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})x_j^{(i)}
$$
这个式子和线性回归的式子是一样的，不一样的地方在于，这个式子的**假设函数**，用的不是**线性函数**，而是(**sigmoid函数**)

### 优化算法



# 无监督学习

对一个数据集进行分类

# 代码编写技巧

- 常常将一个for循环简化成为一个向量运算