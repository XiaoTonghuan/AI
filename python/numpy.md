# numpy简介

numpy是科学计算库，常用来代替matlab进行向量、矩阵的运算，可以用作数据分析和机器学习

# array

这个库是科学计算基础库

创建数组，可以将一个列表作类型传入，得到一个array

```python
a = np.array([1,2,3,4])
print(a)
print(type(a)) #type可以返回类型,ndarray

#二维数组
b = np.array([[1,2],[1,2]]) #
#有多个参数
np.array([1,2,3],dtype=float,ndmin=3) #数据类型和维数
```

可以通过arange的方式创建array

```python
a=list(range(1,9,2)) #[),step,默认步长是1
a=np.arange(1,11,2)#返回一个array类型
np.arange(1,22,2,dtype=float)
```

其他的创建数组的方式

```python
#zeros
np.zeros(shape,dtype=float,order='C')#创建全是0的数组,第三个参数是type
#如
np.zero(5)
np.zero((2,3))
#ones
a=np.ones(1)#数据初始化为1
np.empty(1)#数据初始化为任意
```

数组操作

```python
#reshape numpy.reshape(arr, newshape, order')
a = np.array(range(10)).reshape((5,2))
#flat 一维迭代器
a.flat[5] #结果为5
#flatten 返回一维副本
print(a.flatten()) #[0 1 2 3 4 5 6 7 8 9]
#ravel 返回连续的展开数组
#同上
```

# 切片和索引

一维数组中切片和索引的使用

```python
a=np.arange(1,9,2)#先创建一个数组
#索引
y = a[-1] #倒数第一个
y = a[-3] #倒数第三个
#切片
y = a[:]#从开始到结尾
y = a[1:3]#从索引1到3同样是左闭右开
y = a[1:6:2]#步长为2
y = a[::-1]#从开始到结尾，步长为-1，即反向输出
y = a[-5:-2]#从-5到-2
y = a[-5:]#倒数前5个数字
```

二维数组中切片、索引、高级索引

```python
#索引
a = np.array([[1,2],[1,3,2]])
a[2] #获取第三行
a[2][1] #获取第3行的第2个元素
#切片
#[对行进行切片,对列进行切片]
a[:,:]#获取所有行所有列
a[:,2]#获取所有行第3列p
a[:,0:2]#获取所有行第1，2列
a[1::2,::2]#获取偶数行奇数列
#使用坐标获取元素
a[1,2] #获取第2行第3列的元素a[1][2]相同，被称为高级索引
#高级索引也可以被用在多维数组当中
a[(1,2),(3,4)] #获取多个元素第2行第4个和第4行5个
a[[1,3],[2,5]] #第2行的第3个和第4行第6个
a[[1,2,3],[3,5,6]] #返回a[1][3]、a[2][5]、a[3][6]元素组成的列表
#可以通过下标的访问方式调整返回的方式，如
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
# y = [[ 0  2] [ 9 11]]
#可见对于索引进行处理，可以使返回的array也按照索引的方式处理
#可以组合使用
a[[1,3],2:4] #第一行和第三行，第2到四列
a[::-1]#行倒叙
a[::-1,::-1]#列倒叙
```

三个点

```python
a[:,:,None] 和a[..., None] 等价
a[...,1]#表示第二列的所有元素
a[...,1:]#表示第二列及剩余的所有列的元素
```

布尔索引（有点类似函数式编程的filter函数）

```python
x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
y = x[x > 5] #会打印x中>5的元素
#[ 6  7  8  9 10 11]
a = np.array([np.nan,  1,2,np.nan,3,4,5])  
b = a[~np.isnan(a)]
#b: [1. 2. 3. 4. 5.]
```

# 广播

可以使对数组的算术运算在数组中的每个元素上执行

```python
a = np.array([1,2,3,4]) 
b = np.array([10,20,30,40]) 
c = a * b
#c:[10 40 90 160]
```

当维数不同时，会对维数低的那一个数组进行拓展，使得两者能够进行运算

如果两个array可广播，那么满足下面三个条件之一

- shape相同
- 维数相同，shape不同，不同的维度长度为1
- 维度不同，但是可以在**前面**追加若干长度为1的维度，使上述条件成立

```python
#维数相同
a = np.array(range(6)).reshape((3,2))
b = np.array(range(6,12)).reshape((3,2))
a*b
#维数相同，不同长度，其中长度有为1的
a = np.array(range(120)).reshape((3,2,5,4))
b = np.array(range(15)).reshape((3,1,5,1))
a*b
## 在这个例子中，维数相同，但是，某些维数的长度不同，不同的有1
#低维的
a = np.array(range(120)).reshape((3,2,5,4))
b = np.array(range(20)).reshape((5,4))
a*b
## 注意，一定是在低维的array前面添加，也就是说，从后向前是一样的
```

# 迭代

可以使用nditer进行迭代

```python
a = np.array(range(10)).reshape((2,5))
for i in np.nditer(a):
    print(i,end=' ')
# 结果 0 1 2 3 4 5 6 7 8 9 
```

迭代顺序在定义时就已经确定好了，转置操作不会影响，迭代的顺序

```python
a = np.array(range(10)).reshape((2,5))
a.T
for i in np.nditer(a):
    print(i,end=' ')
#结果和上一个一样
```

可以指定nditer的迭代顺序

```python
a = np.array(range(10)).reshape((2,5))

for i in np.nditer(a,order='F'):
    print(i,end=' ')
print()
for i in np.nditer(a,order='C'):
    print(i,end=' ')
#0 5 1 6 2 7 3 8 4 9 
#0 1 2 3 4 5 6 7 8 9 
#F---二维中按列
#C---二维中按行
```

默认状态下不允许修改array中的值，可以指定参数op_flags修改

```python
for i in np.nditer(a,op_flags=['readwrite']):
    i = i ** 2
    print(i,end=' ')
#0 1 4 9 16 25 36 49 64 81 
```

可以调整参数，遍历外层数组，该方法**只对F生效**

```python
a = np.array(range(10)).reshape((5,2))
print(a)
for i in np.nditer(a,flags=['external_loop'],order='F'):
    print(i,end=' ')
#a
#[[0 1]
# [2 3]
# [4 5]
# [6 7]
# [8 9]]
#i
#[0 2 4 6 8] [1 3 5 7 9] 
```

广播迭代

```python
a = np.array(range(10)).reshape((5,2))
b = np.array(range(10,20)).reshape(5,2)
for i,j in np.nditer([a,b]): #注意，必须要[]括起来
    print(i,j,end=' ')
#0 10 1 11 2 12 3 13 4 14 5 15 6 16 7 17 8 18 9 19 
```

# 数组操作

反转

堆叠

分割

修改维度

添加和删除元素

# 位操作

# 字符串函数

# 算术函数

这些函数的优越性在于可以对向量进行处理

三角函数

```python
#返回弧度的三角函数
np.sin(np.pi/3)
np.cos(np.pi/3)
np.tan(np.pi/3)
# np.csc(np.pi/3)
# np.sec(np.pi/3)
#没有正割和余割的函数
a = np.array([0,30,45,60,90])
sin = np.sin(a*np.pi/180)
inv = np.arcsin(sin) #可以求反三角函数
np.degrees(inv) #将弧度转化成角度
```

舍入函数

```python
# round 四舍五入
# floor 向下取整
# ceil 向上取整
a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])
np.ceil(a)
np.floor(a)
np.round(a)
```

四则运算

```python
# add
# subtract
# multiply
# divide
#shape不同的类似广播的处理
a = np.arange(9, dtype = np.float_).reshape(3,3)#
b = np.array([10,10,10]) #(1,3)
np.add(a,b)
np.subtract(a,b)
np.multiply(a,b)
np.divide(a,b)
```

倒数、乘方、取模、复数

```python
#reciprocal
#power
#mod
#real imag conj angle 实部 虚部 共轭复数 辐角
a = np.array([0.25,  1.33,  1,  0,  100])    
print (np.reciprocal(a))  
#[ 4.  0.7518797  1.  inf  0.01     ]
b = np.array([100], dtype =  int) 
print (np.reciprocal(b))
#[0]
#power
b = np.power(a,2) #a^2
#mod
a = array([10,20,30])
b = np.mod(a,3)#a mod 3
```

# 统计函数

# 排序搜索和计数

# 字节交换

# 副本和视图

# 矩阵库

# 线代库





