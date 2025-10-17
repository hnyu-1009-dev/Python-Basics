"""基础语法示例：变量与数据类型

本文件聚焦在 Python 最常见的内建数据类型，通过实战示例帮助初学者了解：

* 数值类型（整数、浮点数）之间的差异与用途；
* 字符串与 f-string 的基本写法；
* 布尔与 None 在逻辑判断、空值表示中的意义；
* 类型转换的常见函数；
* bytes 与列表推导式等进阶语法。

所有示例均配有详细中文注释，方便对照理解。
"""

# 整数（int）表示没有小数部分的数字，适合用于计数或索引
integer_number: int = 42

# 浮点数（float）可以表示带小数的数值，常用于科学计算或存储分数
float_number: float = 3.14159

# 字符串（str）用于保存文本，f-string 可以在字符串中直接嵌入变量
name: str = "小明"
welcome_message: str = f"你好，{name}!"

# 布尔（bool）只有 True/False 两种值，是条件判断和循环的基础
is_active: bool = True

# None 是一个特殊值，常用来占位或表示“当前没有有效结果”
optional_value = None

# 通过内建函数进行类型转换，这里将字符串 "100" 转换为整数 100
converted_number = int("100")

# bytes 用于表示原始二进制数据，在处理网络、文件或加密信息时非常常见
binary_data: bytes = b"hello"

# 列表推导式是一种更为紧凑的写法，可从现有数据生成新的列表
squares: list[int] = [number ** 2 for number in range(5)]


def describe_variables() -> dict[str, object]:
    """返回一个字典，描述本模块中的基础变量信息"""
    return {
        "integer_number": integer_number,
        "float_number": float_number,
        "welcome_message": welcome_message,
        "is_active": is_active,
        "optional_value": optional_value,
        "converted_number": converted_number,
        "binary_data": binary_data,
        "squares": squares,
    }


if __name__ == "__main__":
    # 当直接运行本文件时，打印变量说明，方便快速查看结果
    for key, value in describe_variables().items():
        print(f"{key}: {value}")