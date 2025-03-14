# 基础

## 语法
python的缩进很重要。在其他有些语言中，缩进可能只是处于代码可读性考虑，但是在pythoon中缩进非常重要，python使用缩进来指示代码块。一般使用4个空格控制缩进。<br>
[PEP8 reference click here](https://peps.python.org/pep-0008/#code-lay-out)

## 注释
```python
# this is a comments
print("Hi") # this inline comments
"""
由于python将忽略未分配给变量的字符串文字，因此可以使用三个双引号（triple double quotes）来充当注释内容。

实际上在PEP 257文档约定中就有介绍可以使用三双引号来标记文档：
https://peps.python.org/pep-0257/
"""
```

## 变量
变量是存放数据值的容器。

与有些编程语言不通，python没有声明变量的命令；首次为其赋值时，才会创建变量。

变量也不需要使用任何特定类型声明，甚至可以在设置后更改其类型。
```python
x = 10
y = "Hi"
z = '单引号也可以表示字符串'

a, b, c = "hi", "hello", 10 # 允许在同一行中为多个变量赋值
d = e = f = "world" # 可以为多个变量分配相同的值

# 局部变量只能在函数内使用，不会覆盖具有相同名称的全局变量

#在函数内部使用global关键字可以创建一个全局变量,该关键字也可以是标记使用外部全局变量
def hi():
    global x
    x = 1
```

## 数据类型

**内置数据类型**
|    分类      |    具体类型     |
| ----------- | :--------- |
| 文本类型      | `str` |
| 数值类型      | `int` `float` `complex` |
| 序列类型      | `list` `tuple` `range` |
| 映射类型      | `dict` |
| 集合类型      | `set` `frozenset` |
| 布尔类型      | `bool` |
| 二进制类型    | `bytes` `bytearray` `memoryview` |

```python
x = 10
print(type(x)) #  获取变量数据类型

# 内置数据类型也可以使用构造函数显式定义
y = str("Hi")
```
## 数字 && 字符串 && 布尔

python没有`random()`函数，但有一个名为random的内置模块，可用于生成随机数
```python
import random
print(random.randrange(1,10)) # 前闭后开
```

字符串是数组<br>
和其他许多编程语言一样，Python中的字符串是表示unicode字符的字节数组。<br>
Python没有字符数据类型，单个字符就是长度为1的字符串。
```python
a = "Hello World!"
print(a[1])
print(a[2:5])# 前闭后开 llo

# 使用负索引从字符串末尾开始切片
print(a[-5:-2]) # orl
print(len(a)) # 获取字符串长度
print(a.strip()) # 删除头尾空白字符
print(a.lower()) # 返回小写字符串
print(a.upper()) # 返回大写字符串
print(a.replace("World", "Kitty")) # 字符串替换
print(a.split(",")) #字符串拆分
print("ina" in "China Number One")
print("a"+"b")
print("Hello {}".format("World"))
```

**布尔值**
```python
print(8>7) # True
print(8<7) # False
```
在python中如果有某种内容，则几乎所有值都将被评估为True
```python
print(bool("abc"))
print(bool(123))
print(bool(["a","b","c"]))
```
除空值((),[],{},"",0,None)外，很少有值会被评估为False。

一个值或者对象的布尔判断结果，可以通过对象的`__len__()`函数的返回结果决定。
```python
class Hi():
    def __len__(self):
        return 0

print(bool(Hi())) # False 
```

## 运算符
> 运算符用于对变量和值执行操作。

Python有以下类型运算符:
- 算数运算符
    - `+` 加 `1+2=3`
    - `-` 减 `2-1=1`
    - `*` 乘 `3*5=15`
    - `/` 除 `15/3=5.0`
    - `%` 取模 `5%2=1`
    - `**` 幂 `2**5=32`
    - `//` 取整除 `15//2=7`
- 赋值运算符
    - `=`
    - `+=`
    - `-=`
    - `*=`
    - `/=`
    - `%=`
    - `//=`
    - `**=`
    - `&=`
    - `|=`
    - `^=`
    - `>>=`
    - `<<=`
- 比较运算符
    - `==`
    - `!=`
    - `>`
    - `<`
    - `>=`
    - `<=`
- 逻辑运算符
    - `and`
    - `or`
    - `not`
- 身份运算符
    - `is`
    - `is not`
- 成员运算符
     - `in`
     - `not in`
- 位运算符
    - `&` AND
    - `|` OR
    - `^` XOR
    - `~` NOT
    - `<<` Zero fill left shift
    - `>>` Signed right shift

## Python集合

Python中有四种集合数据类型
    - 列表`List` 有序可重复可更改集合
    - 元组`Tuple` 有序可重复不可更改集合
    - 集合`Set` 无序无索引不可重复集合
    - 元组`Dictionary` 无序可变有索引不可重复集合

### 列表 List
```python
my_list = ["apple", "banana", "cherry", "orange", "Hello", "World"]
print(my_list[1]) # 索引下标从0开始
print(my_list[-1]) # -1索引表示最后一个元素 World
print(my_list[2:5]) # 前闭后开。选择索引范围(2, 5]
print(my_list[-4:-1]) # ["cherry", "orange", "Hello"]
my_list[1] = "new banana"
for item in my_list:
    print(item)
if "apple" in my_list:
    prirnt("apple is in the list")
print(len(my_list))
my_list.append("newItem")
my_list.insert(1, "kiwi") # 将 "kiwi"插入到索引1位置
my_list.remove("apple") #只删除遇到的第一个元素，如果指定元素值不存在会报错
my_list.pop(1) # 删除指定索引位置元素，不置顶则默认删除最后一项
del my_list[1] # 删除指定索引元素
del my_list # 删除整个列表
my_list.clear() # 清空整个列表
my_list_copy = my_list.copy() # 复制列表(非引用传递)
my_list_copy_new = list(my_list) # 复制列表的另一种方法(非引用传递)
list1 = ["a","b","c"]
list2 = [1,2,3]
list3 = list1+list2
print(list3) # ["a","b","c",1,2,3]
list1.extend(list2) # 将list2添加到list1的末尾
```

### 元组 Tuple
> 元组诗有序且不可更改的集合。

```python
my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(my_tuple[0])
print(my_tuple[-1]) # 最后一个元素
print(my_tuple[2:5]) # 前闭后开
print(my_tuple[-4:-1]) # 前闭后开
# 元组是不可变的，想要修改元组，可以转化为list，修改后再转换回tuple，list(my_tuple),tuple(my_list)
for item in my_tuple:
    pass
if "apple" in my_tuple:
    pass
print(len(my_tuple))
new_tuple = ("apple",) # [x] ("apple")。 必须加逗号
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3) # ("a", "b", "c", 1, 2, 3)
my_tuple.count("cherry") # cherry出现的次数
my_tuple.index("cherry") # 第一个出现的cherry所在的索引位置
```

### 集合 Set
> set是无序、无索引，不可重复的集合。

```python
my_set = {"apple","banana","cherry","cherry"}
print(my_set) # {"apple","banana","cherry"} 重复元素自动合并
# 由于set是无序集合，所以只能通过for遍历或者in查询是否存在
for item in my_set:
    pass
if "apple" in my_set:
    pass

my_set.add("kiwi") # 添加元素
my_set.update(["orange", "mango", "grapes"]) # 同时添加多个元素
print(len(my_set))
my_set.remove("banana") # 删除元素
my_set.discard("banana") # 删除元素,如果元素不存在不会 rasie exception
which_value = my_set.pop() # !!!set是无序集合，你不知道会删除什么元素，返回值就是被删掉的元素值
my_set.clear() # 清空set
del my_set # 删除集合
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) # 合并集合
print(set3) # {'c', 1, 2, 3, 'a', 'b'}
set1.update(set2) # 将set2元素插入set1中
```

### 字典 Dictionary
> 字典是无序可变有索引的集合。

```python
my_dict = {
    "id": "python3.11.6",
    "name": "python3"
    "where": "earth"
    }
name = my_dict["name"]
name = my_dict.get("name","default")
my_dict["name"] = "python3.11"
for key in my_dict:
    print(key) # 键
    print(my_dict[key]) #值
for value in my_dict.values():
    print(value)
for key,value in my_dict.items():
    print(key,value)
if "where" in my_dict:
    print("Yes,the key `where` is in the dict")
print(len(my_dict))
my_dict["new_key"] = "new_value"
my_dict.pop("where") # 删除指定项
my_dict.popitem() # 删除最后插入的项 （python3.6之前，dict删除随机项）
# python3.6之后，dict的插入有序了。
# https://mail.python.org/pipermail/python-dev/2016-September/146327.html

del my_dict("name") # 删除指定项
del my_dict # 删除整个字典
my_Dict.clear() # 清空字典
new_dict = my_dict.copy() # 复制字典（非引用传递）
new_dict_2 = dict(my_dict) # 复制字典（非引用传递）
```
## If Else

```python
a = 1
b = 20

if b > a:
    pass
elif a == b:
    pass
else:
    pass

if a > b: print("同一行简写if")
print("fit case if") if a > b else print("fit case else")
print(">") if a > b else print("=") if a == b else print("<")
if True:
    pass
if b > a or ( b >= 20 and b == 1 ):
    pass
```

## While

Python拥有两个原始的循环命令
- `while`
- `for`

```python
i = 1
while i < 7:
    print(i)
    i += 1

while True:
    i += 1
    print(i)
    if i % 3 == 0:
        continue
    if i > 100:
        break

a = 1
while a <= 100:
    print(a)
    a += 1 
else:
    # else不会在break的情况下执行，只会在while判断自然不满足时执行
    print("i is greater than 100 now")
```

## For
> `for`主要用于迭代序列(列表、元组、集合、字典、字符串等)

和其他编程语言中的`for`关键字不太相似，python中的`for`更像是其他面向对象语言中的迭代器方法。

```python
for item in ["apple", "banana", "cherry"]:
    pass
for char in "Hello World":
    pass
for item in ["apple", "banana", "cherry"]:
    if item == "apple":
        continue
    if item == "banana":
        break

for i in range(10): # range 默认从0开始,截止指定值（不包含）
    print(i) # 此处打印0到9的值

for x in range(3, 50, 6): # [3, 50) 步长为6
  print(x) # 此处打印 3，9，15，21，27，33，39，45
else:
    print("Happy Ending")

```

## 函数
> 函数是一种仅会在调用时运行的代码块。

```python
def my_func(param_1 = "p_value"):
    print("this is my_func execute. param_1={}".format(param_1))

my_func() # 调用函数
my_func("spec_value") 


from typing import Tuple
def my_func2(id: int, *args, **kwargs) -> Tuple[int,str]:
    return 0, "success"

my_fun2(1, "a","b","c",d="hello",e="world")
my_fun2(1, *("a","b","c"), **{"a":1, "b":2})

# 递归函数
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    return result
  else:
    return 0
  return result
print(tri_recursion(6))

```

## Lambda
> lambda函数是一种小的匿名函数。<br>
> lambda函数可以接受任意数量的参数，但只能有一个表达式。

`lambda arguments : expression`

```python
x = lambda a, b : a * b + 10
print(x(5, 6))

def my_func(n):
    return lambda a : a * n
print(my_func(2)(13))
print(my_func(3)(13))

```

## 数组
> python没有内置对数组的支持，但是可以使用列表`list`代替。

## 类和对象
TODO

