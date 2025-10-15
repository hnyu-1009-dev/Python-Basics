
# 🐍 Python 面向对象编程 (OOP) 学习笔记

**作者：于昊男**  
**目的：帮助学习 OOP 的基础操作**  
**说明：每段代码都附带详细注释与命名规范建议**  

---

## 一、类的定义与基本使用

### ✅ 类结构示例：
```python
class ClassDefineTest:
    class_attr = "This is a class attribute"
    __private_attr = "This is a private attribute"

    def __init__(self, instance_attr):
        self.instance_attr = instance_attr
        self.test_instnce_method2 = "womeixiugai"
        self.test = "This is a test attribute"

    def instance_method(self):
        self.test_instnce_method = "This is a test instance method"
        self.test_instnce_method2 = "This is a test instance method2"
        print("This is an instance method")
        print("通过 self.__class__ 访问:", self.__private_attr)
        print("通过类名访问:", ClassDefineTest.__private_attr)
        self.__private_instance_method()
        ClassDefineTest.class_method()
        ClassDefineTest.static_method()

    def method_test(self):
        print("This is an instance method1")

    def __private_instance_method(self):
        print("This is a private instance method")
        print("通过 self.__class__ 访问:", self.__private_attr)
        print("通过类名访问:", ClassDefineTest.__private_attr)
        self.method_test()

    @classmethod
    def class_method(cls):
        print("This is a class method")

    @staticmethod
    def static_method():
        print("This is a static method")

    def __del__(self):
        print("This is a destructor")
```

### 💡 知识点总结：
| 类型 | 说明 | 调用方式 |
|------|------|----------|
| 类属性 | 所有实例共享的属性 | `ClassName.attr` |
| 实例属性 | 每个实例独立的属性 | `self.attr` |
| 私有属性 | `__attr` 形式定义，只能类内部访问 | `ClassName._ClassName__attr` |
| 实例方法 | 第一个参数为 `self`，可访问实例属性 | `obj.method()` |
| 类方法 | 第一个参数为 `cls`，可访问类属性 | `ClassName.method()` |
| 静态方法 | 无默认参数，不依赖实例或类 | `ClassName.method()` |

---

## 二、继承与方法覆盖

```python
class Animal:
    def __init__(self, name):
        self.name = name
        self.sound = "unknown"

    def speak(self):
        print(f"{self.name} makes a sound: {self.sound}")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        self.sound = "Woof!"

    def speak(self):
        print(f"{self.name} the {self.breed} barks: {self.sound}")
```

### 🔹 知识点总结：
- 子类继承父类的属性与方法  
- 可以使用 `super()` 调用父类构造函数  
- 子类同名属性或方法会覆盖父类的  

---

## 三、多继承与 MRO（方法解析顺序）

```python
class Flyer:
    def __init__(self):
        self.can_fly = True

    def move(self):
        print("Flying in the sky!")


class Bird(Animal, Flyer):
    def __init__(self, name, species):
        super().__init__(name)
        Flyer.__init__(self)
        self.species = species

    def speak(self):
        print(f"{self.name} chirps happily!")

    def move(self):
        print(f"{self.name} flaps wings gracefully!")
```

### ⚙️ MRO 规则
Python 查找方法或属性的顺序：  
**`Bird → Animal → Flyer → object`**  
可使用 `ClassName.__mro__` 查看顺序。

---

## 四、多态与抽象类

### 🌍 普通多态示例
```python
class Payment:
    def pay(self, amount):
        raise NotImplementedError("子类必须实现该方法")


class WeChatPay(Payment):
    def pay(self, amount):
        print(f"使用微信支付 {amount} 元")


class Alipay(Payment):
    def pay(self, amount):
        print(f"使用支付宝支付 {amount} 元")
```

```python
def make_payment(payment_method: Payment, amount):
    payment_method.pay(amount)

make_payment(WeChatPay(), 100)
make_payment(Alipay(), 200)
```

### 🧠 抽象类与 `ABC` 模块
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

class Square(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2

shapes = [Circle(3), Square(4)]
for shape in shapes:
    print("面积：", shape.area())
```

### 🧩 抽象类总结：
| 元素 | 含义 |
|------|------|
| `ABC` | 抽象基类（Abstract Base Class）基类 |
| `@abstractmethod` | 定义必须由子类实现的方法 |
| 抽象类不能被实例化 | 必须通过子类实现后才能使用 |

---

## 🎯 综合总结

| 特性 | 描述 | 关键点 |
|------|------|--------|
| 封装 | 使用 `__` 实现私有属性与方法 | 隐藏内部实现 |
| 继承 | 子类继承父类功能 | 可使用 `super()` 调父类 |
| 多态 | 相同接口，不同实现 | 提升扩展性与灵活性 |
| 抽象 | 强制子类实现接口 | 提高代码规范性 |
