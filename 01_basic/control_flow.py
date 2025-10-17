"""基础语法示例：条件与循环语句

本文件集中展示 Python 中常用的控制流写法，涵盖以下主题：

* if/elif/else 多分支语句；
* for 循环与 range 结合的枚举方式；
* while 循环与迭代器配合的用法；
* break 语句如何提前结束循环。

每个函数都通过注释解释了关键语法点，方便逐行学习。
"""

from typing import Iterable


def classify_number(number: int) -> str:
    """根据数字的正负性返回对应描述"""
    # if-elif-else 结构可以根据不同条件执行不同代码分支
    # 第一个条件判断是否大于零，满足后立即返回，不再继续执行后续条件
    if number > 0:
        return "正数"
    # Python 支持连续使用 if 语句，此处判断是否等于 0
    if number == 0:
        return "零"
    # 当上述条件均不满足时，说明是小于 0 的情况
    return "负数"


def fizz_buzz(limit: int) -> list[str]:
    """生成 FizzBuzz 序列，用于展示循环与条件组合使用"""
    results: list[str] = []
    # range 可以生成一个整数序列，常用于 for 循环
    # 通过 limit + 1 保证上限数字也会被遍历到
    for number in range(1, limit + 1):
        # 使用取余运算判断能否被 3 或 5 整除
        if number % 3 == 0 and number % 5 == 0:
            results.append("FizzBuzz")
        elif number % 3 == 0:
            results.append("Fizz")
        elif number % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(number))
    return results


def find_first_even(numbers: Iterable[int]) -> int | None:
    """演示 while 循环与 break 语句，寻找第一个偶数"""
    # iter 函数可以将任意可迭代对象转换为迭代器，配合 next 按顺序取值
    numbers_iter = iter(numbers)
    while True:
        try:
            current = next(numbers_iter)
        except StopIteration:
            # 当迭代器耗尽时，跳出循环并返回 None
            return None
        if current % 2 == 0:
            # 找到偶数后直接返回结果，等价于使用 break 再统一返回
            return current


if __name__ == "__main__":
    # 打印数字分类结果
    for sample in [3, 0, -2]:
        print(f"{sample} 是{classify_number(sample)}")

    # 展示 FizzBuzz 序列生成
    print(f"FizzBuzz(15): {fizz_buzz(15)}")

    # 演示 while 循环查找第一个偶数
    print(f"第一个偶数: {find_first_even([1, 3, 5, 6, 7])}")