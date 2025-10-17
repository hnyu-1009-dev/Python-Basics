# KeyboardInterrupt: 用户主动结束程序去触发
import time

# 抛出你所写的语句
# for i in range(10):
#     try:
#         print(i)
#         time.sleep(1)
#     except KeyboardInterrupt:
#         print("Program interrupted by user")
#         break

# 控制台抛出异常
# for i in range(1000):
#     print(i)
#     time.sleep(1)
# Traceback (most recent call last):
#   File "D:\WorkSystem\Python-Basics\03_modules_and_exceptions\exceptions\common_exceptions.py", line 16, in <module>
#     time.sleep(1)
# KeyboardInterrupt

# AttributeError：尝试访问对象没有的属性时出发异常
# my_str = "Hello World"
# my_str.abc()
# Traceback (most recent call last):
#   File "D:\WorkSystem\Python-Basics\03_modules_and_exceptions\exceptions\common_exceptions.py", line 24, in <module>
#     my_str.abc()
#     ^^^^^^^^^^
# AttributeError: 'str' object has no attribute 'abc'

# IndexError：访问不存在的索引时会触发
# my_list = [1, 2, 3, 4, 5]
# print(my_list[10])
# Traceback (most recent call last):
#   File "D:\WorkSystem\Python-Basics\03_modules_and_exceptions\exceptions\common_exceptions.py", line 33, in <module>
#     print(my_list[10])
#           ~~~~~~~^^^^
# IndexError: list index out of range


# 捕获单个异常
x = 10
y = 0
try:
    result = x / y
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result is:", result)
finally:
    print("This code will always run")

# 捕获多个异常
try:
    x = 10
    y = 0
    result = x / y
    print(result)
except (ZeroDivisionError, TypeError):
    print("Cannot divide by zero or type error")
else:
    print("未发生异常Result is:", result)
finally:
    print("This code will always run")

# 捕获所有异常
try:
    x = 10
    y = 0
    result = x / y
    print(result)
except Exception as e:
    print(e)
    print("An error occurred")
else:
    print("Result is:", result)
# 通过 raise 手动抛出异常
try:
    print("Before raise")
    raise ValueError("手动抛出异常")
    print("After raise")
except ValueError as e:
    print(e)
finally:
    print("This code will always run")


# raise ValueError("手动抛出异常")
# # Traceback (most recent call last):
# #   File "D:\WorkSystem\Python-Basics\03_modules_and_exceptions\exceptions\common_exceptions.py", line 89, in <module>
# #     raise ValueError("手动抛出异常")
# # ValueError: 手动抛出异常
# print("不会执行")

# 引入自定义变量
# from custom_exceptions import CustomException
#
# raise CustomException("Something went wrong", 123, "Traceback")


# 异常传递
# 当某个函数或代码块中发生异常，而该处没有被捕获（没有 except 块处理）时，
# 异常会自动向外层调用者传递，直到：
# 找到能够捕获该异常的 try...except；
# 或者一直传到最顶层（解释器），程序终止并打印异常信息。
def funcB():
    print("进入 funcB")
    1 / 0  # 这里抛出 ZeroDivisionError
    print("funcB 执行结束")


def funcA():
    print("进入 funcA")
    funcB()
    print("funcA 执行结束")


def main():
    try:
        funcA()
    except ZeroDivisionError as e:
        print("在 main 中捕获到异常:", e)


# main()
# funcB() 抛出异常；
#
# funcA() 没有处理；
#
# 异常传递到 main()；
#
# main() 捕获后，程序不再中断。
# 当前函数 → 调用它的函数 → 更外层函数 → 解释器
# 若异常全都未被捕获则会打印traceback
# Traceback (most recent call last):
#   File "D:\WorkSystem\Python-Basics\03_modules_and_exceptions\exceptions\common_exceptions.py", line 125, in <module>
#     main()
#   File "D:\WorkSystem\Python-Basics\03_modules_and_exceptions\exceptions\common_exceptions.py", line 120, in main
#     funcA()
#   File "D:\WorkSystem\Python-Basics\03_modules_and_exceptions\exceptions\common_exceptions.py", line 114, in funcA
#     funcB()
#   File "D:\WorkSystem\Python-Basics\03_modules_and_exceptions\exceptions\common_exceptions.py", line 108, in funcB
#     1 / 0  # 这里抛出 ZeroDivisionError
#     ~~^~~
# ZeroDivisionError: division by zero
