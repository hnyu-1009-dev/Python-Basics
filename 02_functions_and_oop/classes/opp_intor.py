# 导入抽象类的基类
from abc import ABC, abstractmethod


# ============================================================================================================
# Python 面向对象学习
# ============================================================================================================
# 作者：于昊男
# 目的：帮助学习oop的一系列基础操作
# 说明：每段代码都附带详细注释与命名规范建议
# ============================================================================================================
#  定义类
class ClassDefineTest:
    # 类属性
    # 如果类的所有的实例需要使用同一个数据时，就可以将该变量设置为类属性
    class_attr = "This is a class attribute"

    # 私有属性
    # 私有属性的设置： 在属性名和方法名前添加双下划线前缀
    # 不能通过类对象进行访问，只能通过类的方法进行访问
    __private_attr = "This is a private attribute"

    # 实例属性
    # 定义在__init__方法中以self.开头的就是实例属性
    def __init__(self, instance_attr):
        self.instance_attr = instance_attr
        self.test_instnce_method2 = "womeixiugai"
        self.test = "This is a test attribute"

    # 实例方法
    # 实例方法：类中的函数，第一个参数是self的就是实例方法，就是对象调用的方法
    # 只要是通过 self.xxx = ... 的方式赋值的属性，
    # 它就是实例属性 —— 不论这个赋值是在哪个方法里发生的。
    def instance_method(self):
        # 在实例方法中,可以访到在__init__中定义的实例属性
        self.test_instnce_method = "This is a test instance method"
        # 在实例方法中通过self定义的属性也是实例属性
        self.test_instnce_method2 = "This is a test instance method2"
        print("This is an instance method")
        # 访问私有属性
        # 私有属性可以被类对象访问，但是不能被实例对象访问
        print("通过 self.__class__ 访问:", self.__private_attr)
        print("通过类名访问:", ClassDefineTest.__private_attr)
        # 访问私有实例方法
        # 可以在任何类方法中调用类方法,也可以在任何实例方法中调用实例方法
        self.__private_instance_method()
        # 调用类方法
        ClassDefineTest.class_method()
        # 调用静态方法
        ClassDefineTest.static_method()

    def method_test(self):
        print("This is an instance method1")

    # 私有实例方法
    def __private_instance_method(self):
        print("This is a private instance method")
        # 访问私有实例属性
        print("通过 self.__class__ 访问:", self.__private_attr)
        print("通过类名访问:", ClassDefineTest.__private_attr)
        # 访问实例方法
        self.method_test()

    # 类方法
    # 类方法：属于类本身的方法，用来访问和修改类属性，不能访问实例属性
    @classmethod
    def class_method(cls):
        print("This is a class method")

    # 静态方法
    @staticmethod
    def static_method():
        print("This is a static method")

    def __del__(self):
        print("This is a destructor")


# 实例化类
class_define_test_obj = ClassDefineTest("This is an instance attribute")

# 访问类属性
print(ClassDefineTest.class_attr)

# 访问实例属性
print(class_define_test_obj.instance_attr)

#  调用实例方法
class_define_test_obj.instance_method()

# 调用类方法
ClassDefineTest.class_method()

# 调用静态方法
ClassDefineTest.static_method()


# ============================================================================================================
# 类的继承
# 1.属性覆盖
#   self.sound 在父类中初始为 "unknown"
#   子类 Dog 在自己的 __init__ 中重新赋值 "Woof!"
#   覆盖（shadowing）了父类同名属性
# 2.方法覆盖
#   Dog.speak() 定义与 Animal.speak() 同名，因此子类方法会覆盖父类方法。
#   调用 dog.speak() 时，执行的是子类版本。
# 3.super() 的作用
#   调用父类的构造函数或方法，保证父类部分逻辑能执行。
class Animal:
    def __init__(self, name):
        self.name = name
        self.sound = "unknown"
        print(f"[Animal.__init__] name={self.name}, sound={self.sound}")

    def speak(self):
        print(f"{self.name} makes a sound: {self.sound}")


class Dog(Animal):
    def __init__(self, name, breed):
        # 调用父类构造函数
        super().__init__(name)
        self.breed = breed
        self.sound = "Woof!"  # 覆盖父类属性
        print(f"[Dog.__init__] name={self.name}, breed={self.breed}, sound={self.sound}")

    # 覆盖父类方法
    def speak(self):
        print(f"{self.name} the {self.breed} barks: {self.sound}")


dog = Dog("Buddy", "Golden Retriever")
dog.speak()


# 类的多继承
class Flyer:
    def __init__(self):
        self.can_fly = True
        print("[Flyer.__init__] can_fly=True")

    def move(self):
        print("Flying in the sky!")


class Bird(Animal, Flyer):  # 多继承
    def __init__(self, name, species):
        # 调用所有父类构造函数（注意顺序！）
        super().__init__(name)  # 只会调用第一个父类的 __init__（Animal）
        Flyer.__init__(self)  # 显式调用第二个父类的构造函数
        self.species = species
        print(f"[Bird.__init__] name={self.name}, species={self.species}")

    # 覆盖父类方法
    def speak(self):
        print(f"{self.name} chirps happily!")

    # 调用另一个父类的同名方法
    def move(self):
        print(f"{self.name} flaps wings gracefully!")


bird = Bird("Tweety", "Canary")
bird.speak()
bird.move()
print(f"Can fly: {bird.can_fly}")


# 1.多继承的调用顺序（MRO）
#   Python 使用 方法解析顺序（MRO）：
#   Bird -> Animal -> Flyer -> object
#   当多个父类存在时，super() 只会按照 MRO 顺序调用第一个父类的 __init__。
#   所以如果想让其他父类也初始化，需要手动调用（如 Flyer.__init__(self)）。
# 2.属性覆盖规则
#   子类中的属性优先级最高；
#   若属性不存在，按 MRO 顺序查找；
#   示例中：
#   Bird 没有定义 can_fly → 去 Flyer 中找到；
#   若 Bird 自己定义 can_fly = False，则会覆盖。
# 3.方法覆盖规则
#   与属性同理：子类 > 父类（按 MRO 顺序）
#   若多个父类有同名方法，Python 会按 MRO 找到第一个匹配的方法执行。
# ============================================================================================================
# 多态
class Payment:
    def pay(self, amount):
        raise NotImplementedError("子类必须实现该方法")


class WeChatPay(Payment):
    def pay(self, amount):
        print(f"使用微信支付 {amount} 元")


class Alipay(Payment):
    def pay(self, amount):
        print(f"使用支付宝支付 {amount} 元")


class BankCard(Payment):
    def pay(self, amount):
        print(f"使用银行卡支付 {amount} 元")


# 定义一个通用支付函数
# payment_method 是 参数名。
# Payment 是一个 类型提示（type hint），表示这个参数应该是一个 Payment 类型的对象（或其子类）。
# 也就是说：
# 这个函数期望传入的参数是一个 Payment 类的实例，或者是从 Payment 派生（继承）的子类对象。
def make_payment(payment_method: Payment, amount):
    payment_method.pay(amount)


# 多态调用：不同支付方式对象，执行不同逻辑
make_payment(WeChatPay(), 100)
make_payment(Alipay(), 200)
make_payment(BankCard(), 300)


# 函数 make_payment() 不需要知道具体是“支付宝”还是“微信”；
# 它只依赖统一的接口 pay()；
# 这让系统具有“可扩展性” —— 新增一种支付方式只需新建一个子类。
# ------------------------------------------------------------------------------------------------------------
# 利用多态实现“解耦”与“扩展
class Sensor:
    def read_data(self):
        raise NotImplementedError


class TemperatureSensor(Sensor):
    def read_data(self):
        print("温度传感器：采集温度数据")


class MoistureSensor(Sensor):
    def read_data(self):
        print("水分传感器：采集湿度数据")


class LightSensor(Sensor):
    def read_data(self):
        print("光照传感器：采集光强数据")


# 通用读取函数 —— 无需关心传感器类型
def collect_sensor_data(sensor: Sensor):
    sensor.read_data()


sensors = [TemperatureSensor(), MoistureSensor(), LightSensor()]
for s in sensors:
    collect_sensor_data(s)


# ------------------------------------------------------------------------------------------------------------
# 抽象类实现多态
# 使用抽象类需要导包
# Shape 是一个抽象类，要求所有子类都必须实现 area() 方法。
# 这在大型工程中尤其重要（比如接口标准化）。
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
# ============================================================================================================
