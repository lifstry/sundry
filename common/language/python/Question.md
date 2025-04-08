# 解惑记录
> 如有错误，万望指正，感谢。[wxleolee5318@gmail.com](wxleolee5318@gmail.com)

## 经典类和新式类


> A "Classic Class" or "old-style class" is a class as it existed in Python 2.1 and before. They have been retained for backwards compatibility. This page attempts to list the differences. - [NewClass Vs classicClass](https://wiki.python.org/moin/NewClassVsClassicClass)

Python 2.2版本引入了新式类概念。

在 Python 2.x版本，默认都是经典类，只有显式继承了`object`的才是新式类。
```python
# Python2.x
# 新式类
class A(object):
    pass

# 经典类
class B:
    pass
```

在Python3.x中，取消了经典类，默认都是新式类，且不再需要显式的继承`object`。

**经典类和新式类的区别**
- 新式类都从object继承，经典类不是。
- 经典类的`MRO`(method resolution order)是`深度优先`,而新式类是`广度优先`。
- 新式类的相同父类`只执行一次构造函数`，而经典类重复执行多次。

*python2.x中的经典类采用深度优先MRO策略*
```python
class A:
    def show(self):
        print("A show")

class B(A):
    # def show(self):
    #     print("B show")

class C(A):
    def show(self):
        print("C show")

class D(B, C):
    pass

# 经典类，从左至右深度优先查找，此处D首个父类B未查到show方法，即继续深度向B的父类A去查找
D().show() # A show
```
*新式类采用广度优先MRO策略*
```python
class A(object):
    def show(self):
        print("A show")

class B(A):
    # def show(self):
    #     print("B show")

class C(A):
    def show(self):
        print("C show")

class D(B, C):
    pass

# 新式类，从左到右广度优先查找，此处D首个父类B未查到show方法，则继续向D第二个父类C查找
D().show() # C show
```
`super()`只能在新式类中使用。
```python
class A(object):
    pass
class B(A):
    def __init__(self):
        super().__init__() # Python3.x
        # super(B, self).__init__() # Python2.x
```

