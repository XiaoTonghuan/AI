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

## 字符串

nPython 3.x完全支持中文字符，默认使用UTF8编码格式，无论是一个数字、英文字母，还是一个汉字，在统计字符串长度时都按一个字符对待和处理

字符串的创建

```python
s = "he"
s = 'he'
s = str(1/7)#将一个浮点转换成一个字符串类型
```

Python字符串驻留机制：对于**短字符串**，将其赋值给多个不同的对象时，内存中只有一个副本，多个对象共享该副本。长字符串不遵守驻留机制。  

字符串格式化

``"%?" % str``

| **格式字符** | **说明**                                      |
| ------------ | --------------------------------------------- |
| %s           | 字符串  (采用str()的显示)                     |
| %r           | 字符串  (采用repr()的显示)详细 见倒数第2页PPT |
| %c           | 单个字符                                      |
| %d           | 十进制整数                                    |
| %i           | 十进制整数                                    |
| %o           | 八进制整数                                    |
| %x           | 十六进制整数                                  |
| %e           | 指数  (基底写为e)                             |
| %E           | 指数  (基底写为E)                             |
| %f、%F       | 浮点数                                        |
| %g           | 指数(e)或浮点数  (根据显示长度)               |
| %G           | 指数(E)或浮点数  (根据显示长度)               |
| %%           | 一个字符"%"                                   |

```python
>>> x = 1235
>>> so = "%o" % x
>>> so
"2323"
>>> sh = "%x" % x
>>> sh
"4d3"
>>> se = "%e" % x
>>> se
"1.235000e+03"
>>> int('555')
555
>>> '%s'%[1, 2, 3]        #直接把对象转换成字符串
'[1, 2, 3]'
>>> str((1,2,3))          #直接把对象转换成字符串
'(1, 2, 3)'
>>> str([1,2,3])
'[1, 2, 3]'
>>> list(str([1, 2, 3]))  #字符串中的每个字符都成为列表的元素（特别注意空格哦，英文规范）
['[', '1', ',', ' ', '2', ',', ' ', '3', ']']
```

eval()

```python
eval() #该函数用来执行一个字符串表达式的值
>>>x = 7 
>>> eval('3 * x')
21 
>>> eval('pow(2,2)') 
4 
>>> eval('2 + 2') 4 
>>> n=81 
>>> eval("n + 4") 
85
```

format()方法

```python
#{}是占位符
>>>"{} {}".format("hello", "world") # 不设置指定位置，按默认顺序 
'hello world’ 
>>> "{0} {1}".format("hello", "world") # 设置指定位置 
'hello world’ 
>>> "{1} {0} {1}".format("hello", "world") # 设置指定位置 
'world hello world’
#数字格式调整
{:.2f}#保留两位小数
{:+.2f}#带符号暴力小数点后两位
{:.0f}#不带小数
{:0>2d}#左边补零 直到总位数为2
{:0<2d}#右边补零 直到总位数为4
{:,}#以，的形式划分数字 如 1,000,000
{:.2%}#化成百分数，小数点后保留两位
{:>10d}#右对齐
{:<10d}#左对齐
{:^10d}#居中
{:b}#2
{:d}#10
{:o}#8
{:x}#16进制
{:#x}0x16进制，字母小写
{:#X}0X 16进制，字母大写
 
#example
>>> print("The number {0:,} in hex is: {0:#x}, the number {1} in oct is {1:#o}".format(5555,55))
The number 5,555 in hex is: 0x15b3, the number 55 in oct is 0o67
>>> print("The number {1:,} in hex is: {1:#x}, the number {0} in oct is {0:o}".format(5555,55))
The number 55 in hex is: 0x37, the number 5555 in oct is 12663
>>> position = (5, 8, 13)
>>> print("X:{0[0]};Y:{0[1]};Z:{0[2]}".format(position))
X:5;Y:8;Z:13
>>> '{0:<8d},{0:^8d},{0:>8d}'.format(65) #设置对齐方式
'65      ,   65   ,      65'
 
 #example2
weather = [("Monday","rainy"),("Tuesday","sunny"),
           ("Wednesday", "sunny"),("Thursday","rainy"),
           ("Friday","cloudy")]
formatter = "Weather of '{0[0]}' is '{0[1]}'".format
for item in map(formatter,weather):
    print(item)
```

Formatted String Literals

```python
#用法如下
name = 'xiao'
f'{name} is smell '
```

字符串常用操作方法

| **操作**                                                     | **含义**                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **+**                                                        | **连接**                                                     |
| *****                                                        | **重复**                                                     |
| <string>[  ]，index(), rindex()                              | **索引**                                                     |
| <string>[  : ]                                               | **剪切**                                                     |
| len(<string>)                                                | **长度**                                                     |
| **upper(),  lower()**                                        | 字符串中字母大/小写                                          |
| **capitalize()、title()、swapcase()**                        | **首字母大写，每个单词首字母大写，大小写交换**               |
| **strip()**                                                  | **去两边空格及去指定字符**                                   |
| **split(),**  **rsplit****(),** **lstrip****()**             | **按指定字符分割字符串为数组**                               |
| **join()**                                                   | **连接两个字符串序列**                                       |
| **find(),**  **rfind****()**                                 | **搜索指定字符串**                                           |
| **replace()**                                                | **字符串替换**                                               |
| for  <var> in <string>                                       | **字符串迭代**                                               |
| startswith()endswith()center()、ljust()、rjust()zfill() isalnum() 等 | **字符串是否以指定字符串开始或结束**  **居中、左对齐或右对齐**  **返回指定宽度的字符串，在左侧以字符0进行填充**  **字符串是否为数字、字母** |

```python
```

## 函数

- 函数形参不需要声明类型，也不需要指定函数返回值类型

- 即使该函数不需要接收任何参数，也必须保留一对空的圆括号
- 括号后面的冒号必不可少
- 函数体相对于def关键字必须保持一定的空格缩进
- Python允许嵌套定义函数
- 函数调用时向其传递实参，将**实参引用**传递给形参。
- 对于绝大多数情况下，在函数内部直接修改形参的值**不会影响实参**，而是**创建一个新变量**。

```python
def func_name():
    '''注释'''
    #<函数体>
    #return <返回值列表>
```

函数的对象特性

```python
>>> def func():
    print(func.x) 
>>> func() 
AttributeError: 'function' object has no attribute 'x'
>>> func.x = 3                    #动态为函数增加新成员
>>> func()
3
>>> func.x                        #在外部也可以直接访问函数的成员
3
>>> del func.x                    #删除函数成员
>>> func()
AttributeError: 'function' object has no attribute 'x'
#可以函数是函数对象，有成员对象
```

函数传递实参引用，在函数内部改变形参，新建一个变量

```python
>>> def addOne(a):
    print(id(a), ':', a)
    a += 1
    print(id(a), ':', a)
	
>>> v = 3
>>> id(v)
1599055008
>>> addOne(v)
1599055008 : 3
1599055040 : 4 #得到修改的时候新建变量，因此id发生了变化
>>> v
3
>>> id(v)
1599055008
#注意！如果传递给函数的实参是可变序列，并且在函数内部使用“下标”或“可变序列自身的方法增加、删除元素或修改元素时”，实参也得到相应的修改。
>>> def modify(d):         
    d['age'] = 38
>>> a = {'name':‘zhang', 'age':46, 'sex':'Male'}
>>> a
{'age': 46, 'name': ‘zhang', 'sex': 'Male'}
>>> modify(a)
>>> a
{'age': 38, 'name': ‘zhang', 'sex': 'Male'}
```

函数的参数类型

- 参数允许默认值（注意：默认值参数必须出现在函数参数列表的最右端，任何一个默认值参数右边不能有非默认值参数。）
- 参数可以指定类型

```python
def demo(newitem,old_list=[]):
    old_list.append(newitem)
    return old_list

print(demo('5',[1,2,3,4]))
print(demo('aaa',['a','b']))
print(demo('a'))#当使用默认参数的时候，他一直是可改变的，会改变多次哦
print(demo('b'))
#解决方案
def demo(newitem,old_list=None):
    if old_list is None:
        old_list=[]
    new_list = old_list[:] #直接返回新建的，而不在原来的基础上改变
    new_list.append(newitem)
    return new_list

print(demo('5',[1,2,3,4]))
print(demo('aaa',['a','b']))
print(demo('a'))
print(demo('b'))
```

关键参数，防止用户忘记参数的顺序时出现麻烦

```python
#在调用时指定参数名就可以将实参传给指定给定形参
>>> def demo(a,b,c=5):
    print(a,b,c)

>>> demo(3,7)
3 7 5
>>> demo(a=7,b=3,c=6)
7 3 6
>>> demo(c=8,a=9,b=0)#
9 0 8
```

可变长度参数

n可变长度参数主要有两种形式：在参数名前加1个*或2个**

- *parameter用来接收多个位置实参并将其**放在一个元组**中

- \**parameter接收多个**关键参数**并存放到**字典**中

```python
#传任意参数
>>> def demo(*p):
    print(p)
>>> demo(1,2,3)
(1, 2, 3)
>>> demo(1,2)
(1, 2)
>>> demo(1,2,3,4,5,6,7)
(1, 2, 3, 4, 5, 6, 7)
#传关键参数给**
>>> def demo(**p): #p是一个字典
    for item in p.items():
        print(item)
>>> demo(x=1,y=2,z=3)
('y', 2)
('x', 1)
('z', 3)
```

参数传递的序列解包

```python
#序列加*就是解包
#** 关键参数解包
#* 序列解包
>>> def demo(a, b, c):
    print(a+b+c)
>>> seq = [1, 2, 3]
>>> demo(*seq)
6
>>> tup = (1, 2, 3)
>>> demo(*tup)
6
>>> dic = {1:'a', 2:'b', 3:'c'}
>>> demo(*dic)#默认是key值的传递
6
>>> Set = {1, 2, 3}
>>> demo(*Set)
6
>>> demo(*dic.values())#这样是val值的传递
abc
>>> def demo(a, b, c):
    print(a, b, c)	

>>> demo(*(1, 2, 3))                  #调用，序列解包
1 2 3
>>> demo(1, *(2, 3))                  #位置参数和序列解包同时使用
1 2 3
>>> demo(1, *(2,), 3)#创建元组要，
1 2 3
#序列解包相当于位置参数，优先处理
>>> demo(a=1, *(2, 3)) 
#相当于demo(a=1,a=2,b=3)所以会报错
#序列解包会在关键参数解包之前进行解包，序列解包不能放在关键参数解包之后
>>> def demo(a, b, c):
    print(a, b, c)
>>> demo(**{'a':1, 'b':2}, *(3,)) #**不能放在*之前
#SyntaxError: iterable argument unpacking follows keyword argument unpacking

>>> demo(*(3,), **{'a':1, 'b':2}) #这个是重复的参数
#Traceback (most recent call last):
 # File "<pyshell#30>", line 1, in <module>
   # demo(*(3,), **{'a':1, 'b':2})
#TypeError: demo() got multiple values for argument 'a'
>>> demo(*(3,), **{'c':1, 'b':2})
3 2 1
```

变量和作用域

- 一个变量已在函数外定义，如果在函数内需要为这个变量赋值，并要将这个赋值结果反映到函数外，可以在**函数内使用global将其声明为全局变量**。
- 如果一个变量在函数外没有定义，在函数内部也可以直接将一个变量定义为全局变量，该函数执行后，将增加一个新的全局变量。

```python
global x = 3 #定义一个全局变量
#example
>>> def demo(): #函数定义
    global x
    x = 3 #将x转变为全局变量（如果x之前被定义过）
    y = 4
    print(x,y)
>>> x = 5
>>> demo()
3  4
>>> x
3
```

- 如果在局部使用了赋值操作（**任意位置**），并且没有显式的使用global进行定义，那么该变量就是局部变量，和使用的先后顺序无关！

  ```python
  >>> x = 3
  >>> def f():
      print(x) #按理来说是先输出全局变量的值，但是后面使用了x = 5 ，所以x是局部变量此时x还没有定义，因此报错
      x = 5
      print(x)
  
  >>> f()
  #Traceback (most recent call last):
  #  File "<pyshell#10>", line 1, in <module>
  #    f()
  #  File "<pyshell#9>", line 2, in f
  #    print(x)
  #UnboundLocalError: local variable 'x' referenced before assignment
  
  ```

- 如果出现局部变量和全局变量重名的情况，局部变量不会影响全局变量的值、

  ```python
  >>> def demo():
      x = 3         	#这里的x和外边的x=5的x不是一个x
  >>> x = 5
  >>> x
  5
  >>> demo()
  >>> x             
  5
  ```

- nonlocal关键字定义一种介于二者之间的变量。关键字nonlocal声明的变量会引用距离最近的非全局作用域的变量，要求声明的变量已经存在，关键字nonlocal不会创建新变量。

  ```python
  def scope_test():
      def do_local():
          spam = "我是局部变量"
  
      def do_nonlocal():
          nonlocal spam           #这时要求spam必须是已存在的变量
          spam = "我不是局部变量，也不是全局变量"
  
      def do_global():
          global spam             #如果全局作用域内没有spam，就自动新建一个
          spam = "我是全局变量"
          
      spam = "原来的值"
      do_local()
      print("局部变量赋值后：", spam)
      do_nonlocal()
      print("nonlocal变量赋值后：", spam) #可以看出spam是在local和nonlocal之间定义的量
      do_global()
      print("全局变量赋值后：", spam) #这里对全局变量进行赋值不会影响到里面的spam，也就是说全局变量的spam和前两个函数操作的spam不是一个spam
  scope_test()
  print("全局变量：", spam)
  ```

lambda

```python
<函数名>=lambda<参数列表>:<表达式>
#example1
>>> f = lambda x, y, z: x+y+z        #可以给lambda表达式起名字
>>> f(1,2,3)                         #像函数一样调用
6
>>> g = lambda x, y=2, z=3: x+y+z    #参数默认值
>>> g(1)
6
>>> g(2, z=4, y=5)                   #关键参数
11
#example2
>>> L = [(lambda x: x**2),
         (lambda x: x**3),
         (lambda x: x**4)] #用()括起来
>>> print(L[0](2),L[1](2),L[2](2))#调用的时候返回的仅仅是函数名，还要加上参数列表
4 8 16
>>> D = {'f1':(lambda:2+3),
         'f2':(lambda:2*3),         
         'f3':(lambda:2**3)}
>>> print(D['f1'](), D['f2'](), D['f3']())
5 6 8
>>> L = [1,2,3,4,5]
>>> print(list(map(lambda x: x+10, L))) 
[11, 12, 13, 14, 15]
>>> L
[1, 2, 3, 4, 5]
```



map函数：将一个函数的操作作用到一个序列上

```python
#语法：map(func_name,lis)

>>> def add5(v):
    return v+5

>>> list(map(add5,range(10))) #第一个参数是函数名，第二个参数是list
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

#同样可以作用于多个参数的函数
>>> def add(x, y):return x+y
>>> list(map(add, range(5), range(5)))
[0, 2, 4, 6, 8]
```

filter函数：返回符合函数条件的序列

```python
>>> seq=['foo','x41','?!','***']
>>> def func(x):
    return x.isalnum()
>>> list(filter(func,seq))
['foo', 'x41']

>>> list(filter(lambda x:x.isalnum(),seq))
['foo', 'x41']
```

reduce函数：n标准库functools中的reduce()函数可以将一个接受2个参数的函数以迭代的方式从左到右依次作用到一个序列或迭代器对象的所有元素上。

```python
>>> from functools import reduce
>>> seq=[1,2,3,4,5,6,7,8,9]
>>> reduce(lambda x,y:x+y, seq) #先对前两个进行运算，生成的结果再和第三个进行运算，以此类推
45
>>> def add(x, y):
    return x + y
>>> reduce(add,range(10))
45
>>> reduce(add,map(str,range(10)))
'0123456789'
```

yield函数：生成器对象，执行到yield程序挂起，直到执行到next()函数恢复执行

```python
>>> def f():
    a, b = 1, 1            #序列解包，同时为多个元素赋值
    while True:
        yield a            #暂停执行，需要时再产生一个新元素
        a, b = b, a+b      #序列解包，继续生成新元素

>>> a = f()                #创建生成器对象
>>> for i in range(10):    #斐波那契数列中前10个元素
    print(a.__next__(), end=' ')

1 1 2 3 5 8 13 21 34 55 
```

## 面向对象

## 文件操作

## 关键字

- 关键字：as
  - 对导入的包起一个别名，如 ``import numpy as np``
  
- 关键字 assert
  - 条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况。
  
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