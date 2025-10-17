"""基础语法示例：常用数据结构

通过本文件可以快速了解 Python 内置集合类型的基本特性：

* 列表（list）的可变性与常见操作；
* 元组（tuple）的不可变特性，适合存放混合数据；
* 字典（dict）的键值映射关系；
* 集合（set）的去重能力与集合运算。

示例配合注释解释背后的用法与语法细节，帮助建立对数据结构的整体认知。
"""

from __future__ import annotations

# 列表（list）是可变序列，适合存储有序并且可能需要修改的元素集合
# 定义时可以直接使用方括号，内部元素可为任意类型
fruits: list[str] = ["苹果", "香蕉", "橙子"]

# append 方法会在列表尾部追加一个新元素，常用于动态构建列表
fruits.append("葡萄")

# 元组（tuple）是不可变序列，常用于表达一组固定的、有意义的字段
# 本例中分别存储姓名、年龄、所在城市
person: tuple[str, int, str] = ("小红", 25, "北京")

# 字典（dict）由键值对组成，可以通过键高效地查询对应的值
# 键需要保持唯一，因此适合存储映射关系或结构化数据
student_scores: dict[str, int] = {
    "语文": 92,
    "数学": 88,
    "英语": 95,
}

# dict.get 方法允许提供默认值，避免键不存在时抛出 KeyError 异常
history_score = student_scores.get("历史", 0)

# 集合（set）是无序且元素唯一的容器，常用于去重或集合运算
# 即便初始化时写入重复元素，集合也只会保留一份
unique_numbers: set[int] = {1, 2, 2, 3, 4}

# 创建一个包含所有奇数的集合，用于演示交集与并集
odd_numbers = {1, 3, 5, 7}
intersection = unique_numbers & odd_numbers
union = unique_numbers | odd_numbers


def summarize_collections() -> dict[str, object]:
    """汇总当前模块中定义的数据结构，方便演示输出"""
    return {
        "fruits": fruits,
        "person": person,
        "student_scores": student_scores,
        "history_score": history_score,
        "unique_numbers": unique_numbers,
        "intersection": intersection,
        "union": union,
    }


if __name__ == "__main__":
    # 当直接运行本文件时，逐项打印数据结构内容
    for key, value in summarize_collections().items():
        print(f"{key}: {value}")