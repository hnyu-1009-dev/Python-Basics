# =====================================================================================================
# 📘 Python 迭代器
# -----------------------------------------------------------------------------------------------------
# 🧠 语法糖的本质
# ✅ 作用：让程序更容易被人理解和编写。
# ❌ 不改变底层逻辑：编译器或解释器最终会把语法糖转换（Desugar）成原本的底层实现。
# 语法糖写法
squares = [x ** 2 for x in range(5)]
# 等价的“去糖”写法
squares = []
for x in range(5):
    squares.append(x ** 2)
# -----------------------------------------------------------------------------------------------------
# 🧠 一、迭代器（Iterator）
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：
# __init__(self) -> Iterator对象初始化
# __next__(self) -> 返回下一个元素，如果没有下一个元素则抛出StopIteration异常
# Python 的 for、in、next()、enumerate()、解包（unpacking）等语法糖，本质上都是在调用这两个方法。

# 🕹️迭代器的流程
# 1.调用iter(obj) -> 获取迭代器对象；
# 2.循环中自动调用 next(iterator);
# 3.迭代完成会自动捕获并抛出捕获 StopIteration 异常。

# ❗可迭代对象 VS  迭代器对象
# 可迭代对象：实现了 __iter__() 方法，返回一个迭代器对象。
# 迭代器对象：实现了 __iter__() 和 __next__() 方法，可以被 next() 调用并不断返回下一个元素。
# 字符串、列表、元组、字典、文件等都是可迭代对象，但不是迭代器对象。
# ❗ 迭代器一定是可迭代对象，可迭代对象不一定是迭代器
# 用代码来实现判断
# from collections.abc 导入“抽象基类”（Abstract Base Classes, ABC）
# Iterable 与 Iterator 都是“协议（protocol）”的抽象定义，
# 用于判断一个对象是否“可迭代”或是否是“迭代器”。
from collections.abc import Iterable, Iterator

# isinstance(obj, Iterable) 用来判断 obj 是否满足“可迭代协议”
# 可迭代（Iterable）的最核心特征：实现了 __iter__ 方法，
# 调用 iter(obj) 能返回一个“迭代器”对象（Iterator）。
# 列表（list）是典型的可迭代对象，因此结果为 True。
print(isinstance([], Iterable))  # True

# isinstance(obj, Iterator) 用来判断 obj 是否本身就是“迭代器”
# 迭代器（Iterator）的核心特征：既是 Iterable（有 __iter__），
# 还实现了 __next__（在 Python 中由内置函数 next() 驱动）。
# 注意：列表不是迭代器（它没有 __next__），需要通过 iter() 产生迭代器。
print(isinstance([], Iterator))  # False

# iter(obj) 会对“可迭代对象”创建并返回一个对应的迭代器，
# 例如 iter([]) 返回 list_iterator 对象。迭代器能被 next() 逐个取值，
# 并在取尽后抛出 StopIteration 异常。
print(isinstance(iter([]), Iterator))  # True
# -----------------------------------------------------------------------------------------------------
# 🧩代码练习1
data = [1, 2, 3, 4, 5]
iter_data = iter(data)  # 创建一个可迭代对象
print(next(iter_data))  # 1
print(next(iter_data))  # 2
print(next(iter_data))  # 3
print(next(iter_data))  # 4
print(next(iter_data))  # 5
try:
    print(next(iter_data))  # StopIteration
except StopIteration:
    print("Iteration is done.")  # 迭代完成


# -----------------------------------------------------------------------------------------------------
# 🧩代码练习2
# 实现一个自定义的迭代器
# ❗ 自定义迭代器的核心是，在__init__()方法中不断初始化内置状态
class ReusableCounter:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.current = low

    def __iter__(self):  # 在多次调用时，重制属性状态。
        self.current = self.low
        return self

    def __next__(self):  # 返回下一个元素，并更新状态。  #且无法回头，之前的数据都被迭代后更新了。
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


for x in ReusableCounter(1, 5):
    print(x, end=' ')  # 1 2 3 4 5


# 🕹️for 每次都会通过 iter() 调用 __iter__()于是每次迭代都会自动重置 current 到起点，从而能“重复使用”。
#   但是对于这个for循环中，ReusableCounter(1, 5)本身就会返回一个迭代器对象，for循环首先对这个
#   迭代器对象使用iter(),返回的还是这个迭代器对象本身。
# ┌─────────────────────────────────────────────┐
# │                for 循环开始
# │           for x in <可迭代对象>:
# │                 <循环体>
# └─────────────────────────────────────────────┘
#                     │
#                     ▼
#         ┌────────────────────────┐
#         │ 调用 iter(<可迭代对象>)
#         │ → 触发对象的 __iter__()
#         └────────────────────────┘
#                     │
#                     ▼
#         ┌────────────────────────┐
#         │ 返回一个 迭代器 (Iterator)
#         │ 注意：如果对象本身是迭代器
#         │ iter(obj) 直接返回自己
#         └────────────────────────┘
#                     │
#                     ▼
#         ┌────────────────────────┐
#         │ 开始循环调用 next()
#         │ → 调用 迭代器.__next__()
#         └────────────────────────┘
#                     │
#         ┌────────────────────────┐
#         │ __next__() 返回一个值
#         │  → 赋给变量 x
#         │  → 执行循环体
#         └────────────────────────┘
#                     │
#                     ▼
#         ┌────────────────────────┐
#         │ 再次调用 next()
#         │ 重复上一步
#         └────────────────────────┘
#                     │
#                     ▼
#         ┌────────────────────────┐
#         │ 当没有更多数据时
#         │ __next__() 抛出 StopIteration
#         └────────────────────────┘
#                     │
#                     ▼
#         ┌────────────────────────┐
#         │ for 捕获 StopIteration
#         │ → 自动结束循环
#         └────────────────────────┘
# -----------------------------------------------------------------------------------------------------
# 🧩代码练习3:双状态迭代器（模拟数据缓冲区）
# ❗重点理解为什么peek不会消费
# ❗消费的真正含义是，指针向后移动，这个代码中的peek虽然也让指针后移，但是他将值暂存到了buffer缓冲区中
#   下次next直接从缓冲区中取走数据就行。
class BufferedIterator:
    def __init__(self, source):
        self.source = iter(source)
        print("这里是init中的source", self.source)
        self._buffer = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._buffer is not None:
            result, self._buffer = self._buffer, None
            return result
        return next(self.source)

    def peek(self):
        if self._buffer is None:
            self._buffer = next(self.source)  # 注意这里的 next
            print("这里是peek中的_source", self.source)
        return self._buffer


# 使用
it = BufferedIterator(range(5))
print("这里是实例化后的BufferedIterator的对象it", it)

print(it.peek())  # 0（查看下一个值但不消费）
print("这里是peek后的_source", it.source)
print(next(it))  # 0
print("这里是next后的_source", it.source)
print(next(it))  # 1
print(it.peek())
print(it.peek())


# ==================================
# ===================================================================
# 📘 Python 生成器
# 🧠 生成器是实现迭代器协议的函数对象，是一种特殊的迭代器，它不存储所有数据，而是生成数据。
#    调用生成器的函数不会执行函数体，而是返回一个可迭代的generator对象
def gen():
    yield 1
    yield 2


g = gen()
print(next(g))  # 1
print(next(g))  # 2


# yield 会暂停函数执行，保存局部变量与执行栈。
# 下次 next() 调用从上次中断点恢复执行。
# 当执行完所有代码后，会自动抛出 StopIteration 异常（for 循环自动捕获它）。
def simple_gen():
    yield 1
    yield 2
    yield 3


g = simple_gen()
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
try:
    print(next(g))  # StopIteration
except StopIteration:
    print("生成器结束")
