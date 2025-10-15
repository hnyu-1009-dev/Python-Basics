
# Python 函数学习

作者：于昊男  
目的：帮助学习函数定义、参数使用、返回值、作用域、lambda、闭包、装饰器、*args/**kwargs、解包、内置函数遮蔽、作用域关键字（global/nonlocal）等核心概念，并包含常见错误、调试建议与示例。  
说明：本文档基于一个示例 .py 文件整理，逐段解释并给出运行示例与注意事项，适合初学者作为学习笔记或课堂材料。

---

## 目录

1. 函数基础与内置函数复习  
2. 自定义函数（定义、调用、文档字符串）  
3. 参数传递详解：位置参数、关键字参数、默认值  
4. 可变参数：*args、**kwargs 与解包  
5. 常见内置函数与避免覆盖（BIF）  
6. 作用域与变量生命周期：局部变量、全局变量、global、nonlocal  
7. 嵌套函数与闭包（closure）详解  
8. 匿名函数（lambda）与 PEP8 风格建议（E731）  
9. map、filter、sorted 的使用场景与区别  
10. 常见错误排查（三大类：缩进、类型、默认参数求值时机）  
11. 练习题与参考代码（完整示例）

---

## 1. 函数基础与常用内置函数复习

Python 内置很多常用函数（Built-In Functions, BIF），常用例子：

- pow(x, y) 或 x ** y：幂运算  
- abs(x)：绝对值  
- round(x, n)：四舍五入到 n 位  
- help(obj)：查看说明文档（只传名称，不带括号）

**示例：**

```python
a = 2
b = 3
print("pow(b, a) =", pow(b, a))      # 3 的 2 次方
print("3 ** 2 =", 3 ** 2)

print("abs(-3.14) =", abs(-3.14))
print("round(pi, 3) =", round(13.1415926, 3))

# 查看内置函数说明
help(pow)
```

**提示**
- help() 在脚本中会打印大量文本，交互式环境使用更方便。
- 不要使用与这些名字相同的函数或变量名（如 sum, len），以免遮蔽内置函数。

---

## 2. 自定义函数（定义、调用、文档字符串）

函数定义语法：

```python
def func_name(params):
    """文档字符串（docstring）"""
    # code...
    return value
```

**示例：**

```python
def my_function(x_my, y_my):
    """
    这是一个测试函数。
    :param x_my: 循环次数
    :param y_my: 乘数
    """
    for i in range(x_my):
        print(i * y_my)
        print(i * x_my)

my_function(3, 4)
```

**要点**
- Python 在定义函数时只检查语法，不会执行函数体。
- 使用三引号写 docstring，便于 help() 与 IDE 显示。

---

## 3. 参数传递详解

### 位置参数（positional arguments）
参数按顺序传递，位置很重要。

```python
def sub(x_sub, y):
    print(x_sub - y)

sub(2, 1)     # x_sub=2, y=1
sub(x_sub=2, y=1)  # 显式关键字也可以
```

### 关键字参数（keyword arguments）
可以通过 param=value 传参，不必按顺序。

```python
sub(y=2, x_sub=1)
```

**规则**：位置参数必须在关键字参数之前传入。

### 默认参数（default values）
默认值在函数定义时求值，只能放在参数列表的末尾。

```python
def add(x_add, y_add=1, z_add=1):
    return x_add + y_add + z_add

add(2)          # 使用默认值
add(2, z_add=4) # 覆盖默认值
```

**陷阱（重要）**：若默认参数是可变对象（如列表），会被所有调用共享。应改写为：

```python
def f(a=None):
    if a is None:
        a = []
```

---

## 4. 可变参数与解包（*args, **kwargs, 解包操作）

### *args
收集位置参数为一个元组（tuple）。

```python
def args_test(*args):
    for i in args:
        print(f"hello {i}")
    print(len(args), type(args), args)

args_test(1, 2, 3, "apple", "banana")
```

- 元组是不可变的：不能 args[0] = ...，但可以 args = list(args) 来转换。
- *args 后还能定义关键字-only 参数：

```python
def f(*args, flag=False):
    ...
# 必须通过关键字传入 flag
f(1, 2, 3, flag=True)
```

### **kwargs
收集关键字参数为字典（dict）。字典的键会被当作形参名。

```python
def kwargs_test(**kwargs):
    print(kwargs, type(kwargs))

kwargs_test(name="apple", age=18)
```

**注意**：当使用 test3(**kwargs) 解包字典时，字典中的键名必须与函数形参对应（或者函数使用 **extra 来接受剩余键）。

### 解包参数到函数
- f(*args_tuple): 将元组/列表按位置解包
- f(**kwargs_dict): 将字典按关键字解包

**示例：**

```python
def test3(x, y, m, n):
    print(x, y, m, n)

kwargs = {'x':1,'y':2,'m':3,'n':4}
test3(**kwargs)  # 等价于 test3(x=1,y=2,m=3,n=4)
```

字典键的顺序不重要；匹配是按名字完成的。

---

## 5. 常见内置函数遮蔽（不要与 BIF 同名）

不要用 sum, len, list, dict 等内置名字作为变量或函数名。例如：

```python
def sum(my_list):
    return 1
```

若不慎覆盖，可以通过 import builtins 访问原始函数：builtins.sum(...)
但最佳做法是重命名你的函数。

---

## 6. 作用域与变量生命周期（LEGB 规则）

Python 的查找顺序为：Local → Enclosing → Global → Builtins（LEGB）。

- 局部变量：函数内部定义，只在函数内部有效。
- 全局变量：模块顶层定义，可由所有函数读取（若要修改需 global）。
- global：声明在函数内部对全局变量赋值。
- nonlocal：用于嵌套函数中，声明访问外层（但非全局）作用域的变量。

**示例：**

```python
x = 0

def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
    inner()
    print(x)  # 11
```

**注意**：global 与 nonlocal 不能同时用于同一个名字；global 会指向模块级变量，而 nonlocal 指向外层函数作用域变量。

---

## 7. 嵌套函数与闭包（closure）

### 闭包定义
当内部函数引用外部函数的变量，并且外部函数返回该内部函数时，返回的函数就是闭包。闭包“记住”了创建它时的环境变量。

```python
def closure_outer_test(x):
    def closure_inner_test(y):
        return x + y
    return closure_inner_test

closure_obj1 = closure_outer_test(100)
closure_obj2 = closure_outer_test(200)
print(closure_obj1(100))  # 200
print(closure_obj2(200))  # 400

# 查看闭包中保存的变量
print(closure_obj1.__closure__[0].cell_contents)  # 100
```

### 应用场景
- 延迟计算（如 make_power(n) 生成次方函数）
- 封装状态（计数器）
- 装饰器：装饰器本质上是使用闭包封装函数行为

### 修改闭包中外层变量
要在内部函数修改外层（非全局）变量，使用 nonlocal：

```python
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
```

---

## 8. 匿名函数（lambda）与 PEP8 风格（E731）

lambda 适合用于**短小的匿名函数**，例如作为 map, filter, sorted 的 key 或临时回调。

**PEP 8（E731）建议**：不要把 lambda 赋值给变量以给它命名。若是命名函数，应使用 def，因为 def 更易读、支持注释和调试。

**不推荐：**

```python
test_lambda = lambda x: x + 1  # E731 警告
```

**推荐：**

```python
def test_fn(x):
    return x + 1
```

**注意**：函数定义时的默认参数会在定义阶段就被求值（而不是调用时）。例如：

```python
test_lambda = lambda x=int(input("请输入一个数字：")): x + 1
# 在执行这行时就会执行 input(...)
```

如果你需要交互式输入或延迟求值，请不要把 input() 放到默认参数中。

---

## 9. map, filter, sorted 的区别与示例

- map(func, iterable)：对每个元素应用 func，返回一个迭代器（可用 list() 查看）。
- filter(func, iterable)：对每个元素应用 func（返回布尔），只保留 True 的元素。
- sorted(iterable, key=func)：返回排序后的新列表，key 指定排序依据。

**示例：**

```python
print(list(map(lambda x: x+1, [1,2,3])))           # [2,3,4]
print(list(filter(lambda x: x%2==0, [1,2,3,4])))   # [2,4]
print(sorted([1,5,2,4,3], key=lambda x: x%2))     # 排序依据取模结果
```

map/filter 返回惰性迭代器，第一次消费后会为空；若需要多次使用，请转换为 list。

---

## 10. 常见错误排查

- 缩进错误（IndentationError）: 通常由混用 Tab/空格或不可见字符导致。用编辑器的“显示空白符”和“转换制表符为空格”功能排查。
- 类型错误 TypeError/AttributeError：对错误类型调用方法或做不支持的运算。检查数据类型或添加类型校验。
- 默认参数求值时机：默认值在函数定义时计算，避免把可变对象或 I/O 放到默认参数中。

---

## 11. 练习题与参考代码（完整示例）

请把下面代码保存为 `example.py`，逐行运行并观察输出：

```python
# example.py
def make_counter(start=0):
    count = start
    def inc(step=1):
        nonlocal count
        count += step
        return count
    return inc

c = make_counter(10)
print(c())    # 11
print(c(5))   # 16

def demo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

demo(1,2,3, a=10, b=20)

nums = list(range(1,11))
evens = list(filter(lambda x: x%2==0, nums))
squares = list(map(lambda x: x*x, evens))
print("evens:", evens)
print("squares:", squares)
```

---

## 附：快速参考（速查表）

- `*args` → 收集位置参数为 tuple（顺序重要）  
- `**kwargs` → 收集关键字参数为 dict（按名字匹配，顺序不重要）  
- `lambda` → 匿名函数，短小一次性使用；命名函数用 `def`  
- `global` → 修改模块级全局变量  
- `nonlocal` → 修改外层（但非全局）函数变量  
- 闭包 = 函数 + 环境（记住外层变量）  

---

如果你希望，下一步我可以：
- 将此 Markdown 保存为文件并提供下载（我已准备好），或
- 把内容转成带运行单元的 Jupyter Notebook，便于交互练习，或
- 在文档中把你的原始 `.py` 文件代码完整嵌入（按章节分割）并输出每段代码的示例运行结果（更像教案）。

请选择要生成的形式（Markdown 文件 / Jupyter Notebook / 教案式带输出的 Markdown）。
