# py语法

## python中的序列

|                | 列表（list） | 元组（tuple） | 字典（dict） | 集合（set） |
| :------------: | ------------ | ------------- | ------------ | ----------- |
|     界定符     | []           | ()            | {}           | {}          |
|      可变      | 是           | **否**        | 是           | 是          |
|      有序      | 是           | 是            | 否           | 否          |
|      下标      | 是           | 是            | Key          | **否**      |
|      重复      | 是           | 是            | Key不行      | 否          |
|    查找速度    | 慢           | 慢            | 快           | 快          |
| 新增和删除速度 | 尾部快       | 否            | 快           | 快          |

## 列表

常用方法

```python
lst*=n#列表元素重复n次
lst.append(x)#添加元素x到lst的尾部
lst+=L#lst.extend(L) 两者都是将lst扩展
lst.insert(index,x)#在index处插入一个x
lst.remove(x)#删除首次出现的x，其他元素向前缩进
lst.pop([index])#删除并返回下标为index的元素，默认是最后一个元素
lst.count(x)#返回指定元素的出现次数
lst.reverse()#逆序
lst.sort(key=None,reverse=False)#key用来指定排序依据，reverse表示正序还是拟序
lst.copy()#返回lst的潜复制
```

列表的创建

```python
#使用[]直接创建
a=['a',1,2]
b=[]
#使用list函数将元组、range对象、字符串或者其他类型的可迭代对象类型的数据转换为列表
c=list((3,5,6,9))#转换元组 [3,5,6,9]
d=list(range(1,10,2))#转换range [1,3,5,7,9]
e=lsit('hello,world')#转换字符串['h','e','l','l','o','w','o','r','l','d']
f=list()#空列表
```

列表的删除

```python
del a #当不再有其他列表对象指向时，内存自动释放，类似智能指针
del a[1] #解除当前列表对第一个元素的引用
aList = [3,5,7,9,11]
del aList[1]
aList
#[3, 7, 9, 11]
```

> P.S.注意一个常见的错误

```python
x = [1,2,1,2,1,1,1]
for item in x:
    if item == 1:
        x.remove(item)
#注意该程序并不能删除掉x中所有的1，因为每删除一个元素都会导致当前下标元素的值发生变化
#正确的删除
x = [1,2,1,2,1,1,1]
for item in x[::]:      #切片
    if item == 1:
        x.remove(item)
x = [1,2,1,2,1,1,1]
for i in range(len(x)-1,-1,-1):         #从后往前删
    if x[i]==1:
        del x[i]
```

列表元素的增加

```python
a=a+[7]#完成两个列表的拼接
a.append(7)#直接添加一个元素
a+='1234'#将‘1’，‘2’，‘3’，‘4’加入列表
```

列表中包含的是元素值的引用

```python
>>> a = [1,2,4]
>>> b = [1,2,3]
>>> a == b
False
>>> id(a) == id(b)
False
>>> id(a[0]) == id(b[0]) #说明a和b中的第一个元素指的是同一个元素
True
>>> a = [1,2,3]
>>> id(a)
25289752
>>> a.append(4)#添加值不会改变初始地址
>>> id(a)
25289752
>>> a.remove(3)#删除值也不会改变a的地址
>>> a
[1, 2, 4]
>>> id(a)
25289752
>>> a[0] = 5
>>> a
[5, 2, 4]
>>> id(a)
25289752
#结论append、extend、remove 均属于原地操作
```

应尽量从尾部来扩展或者删除一个元素

使用乘法扩展列表的内容，结果是列表的元素重复的被添加到列表里

```python
a=[1]
a=a*3 #a=[1,1,1]
#值得注意的是，这里乘法会导致a中所有的元素是对同一块内存的引用，修改其中一个就会导致另一个的修改！
>>> x = [[None] * 2] * 3
   >>> x
    [[None, None], [None, None], [None, None]]
   >>> x[0][0] = 5
   >>> x
    [[5, None], [5, None], [5, None]]

```

列表的访问和计数

```python
a[1]#下标访问
a.index(x)#index函数访问
```

切片

```python
ls[i]=x
ls[i:j]=l1#将指定的部分[前闭后开！)替换为一个新的列表
ls[i:j:k]=l1#将指定的部分（前闭后开步数为k，替换为一个新的列表）
del a[i:j]#删除从i到j的所有元素（前闭后开）等价于a[i:j]=[]
del a[i:j:k]#删除从i到j步数为k的所有数据

>>> aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
>>> aList[::]                            #返回包含所有元素的新列表
[3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
>>> aList[::-1]                          #逆序的所有元素
[17, 15, 13, 11, 9, 7, 6, 5, 4, 3]
>>> aList[::2]                           #偶数位置，隔一个取一个
[3, 5, 7, 11, 15]
>>> aList[1::2]                          #奇数位置，隔一个取一个
[4, 6, 9, 13, 17]
>>> aList[3::]                           #从下标3开始的所有元素
[6, 7, 9, 11, 13, 15, 17]
>>> aList[3:6]                           #下标在[3, 6)之间的所有元素
[6, 7, 9]
>>> aList[0:100:1]                       #前100个元素，自动截断
[3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
>>> aList[100:]                          #下标100之后的所有元素，自动截断
[]
>>> aList[100]                           #直接使用下标访问会发生越界

>>> aList = [3, 5, 7]
>>> aList[:2] = [1, 2]            #替换前2个元素
>>> aList
[1, 2, 7]

>>> aList = list(range(10))
>>> aList
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> aList[::2] = [0]*5            #替换偶数位置上的元素
>>> aList
[0, 1, 0, 3, 0, 5, 0, 7, 0, 9]

>>> aList = [3,5,7,9,11]
>>> del aList[1::2] 
>>> aList
[3, 7, 11]
```

- 切片返回的是列表元素的潜复制，所以修改元素是会影响到原来的列表的

深复制

```python
>>> import copy
>>> x = [1, 2, [3, 4]]
>>> y = copy.deepcopy(x) 
>>> x[2].append(5)
>>> y.append(6)
>>> y
[1, 2, [3, 4], 6]
>>> x
[1, 2, [3, 4, 5]]
#这样的h
```

用于序列操作的常用函数

sum函数

```python
sum()#对列表内元素进行求和运算，对于非数值型列表需要指定start参数
sum(range(1, 11))    #sum()函数的start参数默认为0
sum([1,2],3)	#相当于3+sum([1,2])
```

zip函数：返回可迭代的zip对象

```python
>>> aList = [1, 2, 3]
>>> bList = [4, 5, 6]
>>> cList = zip(a, b)
>>> cList
<zip object at 0x0000000003728908>
>>> list(cList)
[(1, 4), (2, 5), (3, 6)]
```

可以看出zip函数可以将打包的对象变成元组的形式储存起来

enumerate函数：可以返回对象+下标的元组形式

```python
for item in enumerate('abcdef'):
    print(item)
#(0, 'a')
#(1, 'b')
#(2, 'c')
#(3, 'd')
#(4, 'e')
#(5, 'f')
```

列表推导式

列表推导式可以使用非常简介的代码生成满足条件的列表，语法为

```python
[expression for expr1 in sequence1 if condition1
            for expr2 in sequence2 if condition2
            for expr3 in sequence3 if condition3
            ...
            for exprN in sequenceN if conditionN]
#在一个中括号当中包含一个表达式+一个for还可以嵌套if语句
#example1
[x*y for x in range(1,5) if x > 2 for y in range(1,4) if y < 3]
#相当于以下的语句
for x in range(1,5):
	if x > 2: 
		for y in range(1,4): 
			if y < 3: 
				l.append(x*y)
#[3*1,3*2,3*3,3*1...]
#example2
aList = [x*x for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#example3
vec=[[1,2,3],[1,2,3]]
[num for elem in vec for num in elem]
#或者
sum(vec,[])
#example4
aList = [-1,-4,6,7.5,-2.3,9,-11]
[i for i in aList if i>0]
[6, 7.5, 9]
#example5
>>> [(x, y) for x in range(3) for y in range(3)]
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
>>> [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
#实现矩阵转置
>>>matrix = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] 
>>> [[row[i] for row in matrix] for i in range(4)] 
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
#for语句是从后向前看的，这样看起来比较容易
#相当于
for i in range(4):
	for row in range matrix:
    	l1.append(row[i])
    l2.append(l1)
#生成0-100所有素数
[i for i in range(100) if 0 not int [for i%j in range(2,i)]]
```

## 元组

不可变的列表

- 可以被当作字典的键来使用

元组的创建和删除

```python
t=('a','b')
t1=('a',)#只包含一个元素，多加个，
#或者
t1='a',#也可以表示元组
x=()
t2=([1,2,3])#可以将列表转化为元组
del t2#删除元组对象
```

序列解包

```python
x,y,z = 1,2,3 #多个变量同时赋值
v_tuple = (False, 3.5, 'exp')
(x, y, z) = v_tuple
x, y, z = range(3)            #可以对range对象进行序列解包
x, y, z = iter([1, 2, 3])     #使用迭代器对象进行序列解包
x, y, z = map(str, range(3))  #使用可迭代的map对象进行序列解包
a, b = b, a                   #交换两个变量的值
x, y, z = sorted([1, 3, 2])   #sorted()函数返回排序后的列表
a, b, c = 'ABC'               #字符串也支持序列解包
x[:3] = map(str, range(5))    #切片也支持序列解包
#example 对zip,enu进行解包
for k,v in zip(key,val)
for index,v in enumerate(s)
```

生成器推导式(括号+表达式)

```python
>>> g = ((i+2)**2 for i in range(10)) #创建生成器对象
>>> g
<generator object <genexpr> at 0x0000000003095200>
>>> tuple(g)                          #转换为元组
(4, 9, 16, 25, 36, 49, 64, 81, 100, 121)
>>> list(g)
[] 
>>> g = ((i+2)**2 for i in range(10)) #重新创建生成器对象
>>> g.__next__()                      #使用生成器对象的__next__()方法获取元素
4
>>> next(g)                           #使用函数next()获取生成器对象中的元素
16
#也可以直接遍历
for i in ((i+2)**2 for i in range(10)):
	print(i)
```

## 字典

globals()：返回包含当前作用域内所有全局变量和值的字典

locals()：返回包含当前作用域内所有局部变量和值的字典

字典类型的操作

字典的创建和删除

```python
#使用{}
a_dic = {'server': 'dada'}
x = {}
#使用dict函数将元组转化为字典
>>> keys = ['a', 'b', 'c', 'd']
>>> values = [1, 2, 3, 4]
>>> dictionary = dict(zip(keys, values))
>>> dictionary
{'a': 1, 'c': 3, 'b': 2, 'd': 4}
>>> x = dict()                          #空字典
>>> x
{}
#使用键值对定义字典
d = dict{d='a',p='q'}
#{d:'a',p:'q'}
#创造值为空的键
adict=dict.fromkeys(['name','sex','age'])
#example
>>> a = dict(one=1, two=2, three=3)#直接转化为字符串
>>> b = {'one': 1, 'two': 2, 'three': 3} 
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3])) 
>>> d = dict([('two', 2), ('one', 1), ('three', 3)]) 
>>> e = dict({'three': 3, 'one': 1, 'two': 2}) 
>>> f = dict({'one': 1, 'three': 3}, two=2) 
>>> a == b == c == d == e == f 
True
del dic #删除整个字典
```

字典元素的读取

```python
#使用键作为下标可以访问值，如果值不存在则抛出异常
adic = {'name':'dong','sex':'male',age:'18'}
adic['name'] #dong
>>> aDict['tel']                     #键不存在，抛出异常
#Traceback (most recent call last):
#  File "<pyshell#53>", line 1, in <module>
#    aDict['tel']
#KeyError: 'tel'

#使用get函数可以访问到没有值的键值对
>>> print(aDict.get('address'))
#None
#可以用=的方式添加值
aDict['address']='Not Addressed'
#get函数可以用来给键添加值
>>> print(aDict.get('address', 'SDIBT'))
#SDIBT
aDict['score'] = aDict.get('score',[])#

#使用items函数，可以读取所有的键值对
>>> aDict={'name':'Dong', 'sex':'male', 'age':37}
>>> for item in aDict.items():     #输出字典中所有元素
    print(item)
#('age', 37)
#('name', 'Dong')
#('sex', 'male')

#不加特殊说明默认输出的是键
for i in dic:
	print(i)
#可以使用解包的方式
for i,j in dic:
    print(i,j)
    
#items()函数返回所有简直对的列表，每一个键值对组成一个元组
>>>aDcit.items()
dict_items([('name', 'Dong'), ('sex', 'male'), ('age', 37)])  #返回所有键：值
>>> aDict.keys()                           #返回所有键
dict_keys(['name', 'sex', 'age'])
>>> aDict.values()                         #返回所有值
dict_values(['Dong', 'male', 37])
```

字典元素的修改

```python
#= 若存在键值对修改值，不存在直接创建一个键值对
>>> aDict['age'] = 37                 #修改元素值
>>> aDict
{'age': 37, 'name': 'Li', 'sex': 'female'}
>>> aDict['address'] = 'hefei'        #增加新元素
>>> aDict
{'age': 37, 'address': 'hefei', 'name': 'Li', 'sex': 'female'}
#使用update的方式将另一个字典的所有键值对添加到这个字典
aDict.update({'a':1,'b':2})

#使用del函数删除指定键的元素，clear用来删除字典中的所有元素，pop删除并返回指定键的元素，opitem()删除并返回字典中最后一个元素
del dic #删除整个字典
dic.clear() #删除字典中所有的键值对
del dic['a']#
dic.pop('b')#返回键为'b'的值，并弹出
dic.popitem()#删除并返回字典的最后一对儿键和值
```

字典推导式

```python
#快速交换字典键值
dict2={k,v for v,k in dict1}
#字典推导式和元组推导式列表推导式并没有什么很大的差别
```

## 集合

- 集合是无序可变的序列，使用一对大括号界定，元素不可重复，同一个集合中每个元素都是唯一的
- 集合中只能包含数字、字符串、元组等可哈希的类型

创建和删除

```python
a={3,5}#集合和字典一样，用{}界定
a.add(7)#使用add而不是append向集合中添加元素
#使用set函数可以将其他类型转换成集合
a_set = set(range(8,14))
b_set = set([1,2,3,3,5])#集合可以自动去除重复的元素
#创建空集合
s = set()
s = {,}#空集合不能使用{}直接初始化，{}初始化的是字典

#删除
del a #删除整个集合
a.pop()#弹出并删除其中的一个元素
a.remove()#删除指定的元素
a.clear()#清空整个集合
```

常用函数

```python
s.copy()#返回集合的一个拷贝
s.clear()#移除S中所有的数据项
s.pop()# 随机 弹出一个元素
x in S #如果x是S中的元素，返回True 否则返回 False
x not in S #和上面的类似
s.remove('a')#删除集合中的指定元素，不在集合中报错
s.discard(x)#删除集合中的指定元素，不在集合中不报错
s.isdisjoint(T)#两个集合不相交返回true
len(s)#返回集合中元素的数量
s.difference(T)#返回在集合S但是不在集合T中的元素
S-=T#两个集合作差
s&=T#求交集
s=^T#求对称差（环和）异或
s=|T#求并集
s<=T#s是T的子集返回true
s>=T#t是s的子集返回true
```

集合推导式

```python
s = {x.strip() for x in (' he ',' she ','i')} #strip函数可以去掉空格
```

## python中的数据结构

堆

```python
import heapq #堆
heap=[]#先建立一个列表
for i in data:#通过heappush将元素放进去
	heapq.heappush(heap,i)
heapq.heappop(heap)#弹出堆顶的元素
#将列表堆化
h = [1,2,3,4,5,6,7,8]
heapq.heapify(h)
heapq.heapreplace(h,6)#弹出最小的元素，并向堆中插入一个新的元素6
heapq.nlargest(3,h)#返回堆中前3个最大的元素
heapq.nsmallest(3,h)#返回堆中前三个最小的元素
```

队列

```python
import queue #队列
q = queue.Queue() #初始化一个队列
#入队
q.put(0)
q.put(1)
q.queue
#[0,1]
q.get()#返回队首元素，并出队
```

优先队列

```python
from queue import PriorityQueue #导入优先级队列
q = PriorityQueue() #创建优先级队列对象
#插入元素
q.put(3)
q.put(8)
#返回并删除队列中优先级最低的元素
q.get()
```

双端队列

```python
#collections 提供了双端队列
form collections import deque
q = deque(maxlen=5) #创建双端队列
q.append(3)#向队列尾部添加元素，如果超出了maxlen那么就自动溢出掉左侧的元素
q.appendleft(3)#向队列的头部添加元素，元素从从右侧溢出
```

## 关键字

- 关键字：as
  - 对导入的包起一个别名，如 ``import numpy as np``
  
- 关键字 assert
  - 条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况。
  
- **zip()** 

  用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

  如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

  ```python
  >>>a = [1,2,3]
  >>> b = [4,5,6]
  >>> c = [4,5,6,7,8]
  >>> zipped = zip(a,b)     # 打包为元组的列表
  [(1, 4), (2, 5), (3, 6)]
  >>> zip(a,c)              # 元素个数与最短的列表一致
  [(1, 4), (2, 5), (3, 6)]
  >>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
  [(1, 2, 3), (4, 5, 6)]
  ```

- *的用法

  - 用作乘法

  - 用作乘方

  - 用于解包

    ```python
    def d(x,y,z):
        return (x,y,z)
    a=[1,2,3]
    d(*a)#将一个列表转化为实参
  
- **的作用
  
    - 用于函数参数，将传入的参数打包为字典

    	```python
    	def demo(**p):
        	for i in p.items():
            	print(i)
    	demo(x=1,y=2)
    	#('x',1)
    	#('y',2)
    	```
    	
    - 用于解包字典
    
      ```python
      dic={'a':1,'b':2,'c':}
      str='{a},{b},{c}'.format(**dic)
      ```
    
- 

# numpy

## array

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



array的对象属性

<img src=".assets/image-20220202104029564.png" alt="image-20220202104029564" style="zoom:80%;" />

## 切片和索引

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
```

二维数组中切片和索引的使用

```python
#索引
a = np.array([[1,2],[1,3,2]])
a[2] #获取第三行
a[2][1] #获取第3行的第2个元素
#切片
[对行进行切片,对列进行切片]
a[:,:]#获取所有行所有列
a[:,2]#获取所有行第3列p
a[:,0:2]#获取所有行第1，2列
a[1::2,::2]#获取偶数行奇数列
#使用坐标获取元素
a[1,2] #获取第2行第3列的元素a[1][2]相同
a[(1,2),(3,4)] #获取多个元素第2行第4个和第3行第5个
a[::-1]#行倒叙
a[::-1,::-1]#列倒叙
```

三个点

```python
a[:,:,None] 和a[…, None] 等价
```

省略前面两维的数据

# cv,torch

- ``vc = VedioCapture(0)``

  - 参数是0，表示打开摄像头，参数是路径，表示打开文件

- ``ret,frame = vc.read()``

  vc.read()按帧读取视频，ret,frame是获cap.read()方法的两个返回值。其中ret是布尔值，如果读取帧是正确的则返回True，如果文件读取到结尾，它的返回值就为False。frame就是每一帧的图像，是个**三维矩阵**（m，n，3）m表示高，n表示宽，3表示RGB。

- ``letterbox(img,new_shape=(a,b))``