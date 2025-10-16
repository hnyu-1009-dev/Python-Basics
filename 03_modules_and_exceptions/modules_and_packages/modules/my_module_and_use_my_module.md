# 📘 Python 模块与内置变量学习笔记

---

## 一、模块（Module）的概念与定义

### 1. 模块的基本概念
- 模块是程序设计中的一个独立功能单位。
- 将程序划分为具有特定功能、相对独立的部分，每个模块通常对应一个文件或逻辑组件。
- **模块化（Modularization）**：将大型系统拆分为若干小模块，降低系统复杂性，提高可维护性与可复用性。

### 2. 模块主要特征
1. **独立性（Independence）**：模块能独立完成特定功能，对外透明。  
2. **接口性（Interface）**：通过函数、类、API 与其他模块通信。  
3. **封装性（Encapsulation）**：隐藏内部实现，只暴露必要接口。  
4. **可复用性（Reusability）**：可在其他程序中重复使用。  
5. **可维护性（Maintainability）**：修改或扩展某模块不会影响整体系统。

### 3. 模块的作用与优势
- 降低程序复杂度  
- 提高代码复用率  
- 方便团队协作开发  
- 支持分层架构与功能扩展  
- 有利于测试与调试

### 4. 模块与其他概念的关系
| 概念 | 区别 |
|------|------|
| 模块 vs 类（Class） | 模块是结构单元，类是对象定义单元 |
| 模块 vs 包（Package） | 包是多个模块集合，模块是包的组成部分 |
| 模块 vs 函数（Function） | 模块由函数组成，是函数的上层组织单位 |

### 5. 不同语言的模块实现
- Python：每个 `.py` 文件即为模块，可通过 `import` 导入。  
- Java：模块由包和类组成，Java 9 引入 `module-info.java`。  
- JS / Vue：使用 ES Module（`import/export`）管理模块。  
- C/C++：由 `.h`（头文件）和 `.cpp`（实现文件）组成。  
- Spring Boot：按功能划分为 controller、service、repository 等。

### 6. 模块设计原则
- **高内聚（High Cohesion）**：内部功能紧密相关，形成完整逻辑单元。  
- **低耦合（Low Coupling）**：模块间依赖少，修改一个模块不影响其他模块。

### 7. 模块划分方法
- 按功能划分（功能模块）  
- 按层次划分（表现层 / 业务层 / 数据层）  
- 按数据流划分（输入处理 / 分析 / 输出）  
- 按职责划分（用户管理 / 日志 / 传感器等）

---

## 二、模块导入方式及底层逻辑

### 1. import 机制
执行 `import my_module`：
1. Python 在 `sys.path` 查找 `my_module.py` 文件  
2. 创建模块对象并执行模块顶层代码  
3. 将模块对象加入 `sys.modules` 缓存，并在当前命名空间创建 `my_module` 名称  

> ⚡ 注意：import 不仅仅是“引入名字”，它会运行模块代码。

### 2. 模块导入方式示例

```python
# 第一种方式：import
import my_module
my_module.test_function1(10, 20)

# 第二种方式：from ... import
from my_module import test_function1, test_function2
test_function1(10, 20)
test_function2(10, 20)

# 第三种方式：import ... as
import my_module as mm
mm.test_function1(10, 20)

# 第四种方式：动态导入
import sys
sys.path.append('/03_modules_and_exceptions')
import my_module as mm
mm.test_function1(10, 20)
```
## 三、内置模块 builtins
### 1. 模块概述

- 每个 `Python` 文件创建时默认导入 `builtins`（Python 内置函数与类型集合）。

- 常用类型：`int, float, str, bool, list, tuple, set, dict`

- 常用函数：`print(), input(), len(), sum(), max(), min(), abs(), round(), pow()`

- 异常类：`BaseException, Exception, TypeError, ValueError` 等

### 2. 示例
```python
import builtins

# 查看内置对象
print(dir(builtins))

# 获取内置函数对象
print(builtins.print)
print(builtins.len)
print(builtins.str)

# ⚠️ 可以扩展 builtins（不建议）
# builtins.greet = lambda name: print(f"Hello, {name}!")
# greet("World")

```
## 四、__name__ 和 __main__ 模块
- __name__：模块被导入时为模块名，直接运行时为 "__main__"

- 判断主模块用法： 
```python
- if __name__ == "__main__":
    print("当前模块是主模块")
```
- __all__：控制模块被 from ... import * 导入的成员
### 其他内置变量
| 变量                | 作用                 |
| ----------------- | ------------------ |
| `__file__`        | 当前文件路径             |
| `__doc__`         | 模块/函数的文档字符串        |
| `__dict__`        | 对象或类的属性字典          |
| `__module__`      | 类或函数所在模块名          |
| `__class__`       | 查看实例所属的类           |
| `__bases__`       | 查看类的父类             |
| `__annotations__` | 存储函数的类型注解          |
| `__builtins__`    | 内置模块（所有内置函数/类型/异常） |
| `__package__`     | 当前模块所属包名           |

```python
def add(a, b):
    """返回两个数的和"""
    return a + b

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 22)
print(p.__dict__)        # 实例属性字典
print(Person.__dict__)   # 类属性字典
print(p.__class__)       # 实例类型

```
### 六、自定义模块示例
```python
__all__ = ["test_function1", "test_function2"]

def test_function1(x, y):
    print(x, y)
    print("This is test_function1")

def test_function2(x, y):
    print(x, y)
    print("This is test_function2")

def test_function3(x, y):
    print(x, y)
    print("This is test_function3 (测试 __all__)")

if __name__ == '__main__':
    print("调用了主函数")

```
### 总结
- 模块是软件系统中的功能单元，具备独立性、可复用性与可维护性。

- 模块化设计是现代软件工程的重要思想，贯穿前后端开发全过程。

- 内置变量与模块导入机制是 Python 高效开发的重要基础。