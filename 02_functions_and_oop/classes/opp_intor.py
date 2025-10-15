# ============================================================================================================
# Python 函数学习
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

    # 私有实例方法
    def __private_instance_method(self):
        print("This is a private instance method")
        # 访问私有实例属性
        print("通过 self.__class__ 访问:", self.__private_attr)
        print("通过类名访问:", ClassDefineTest.__private_attr)
        # 访问实例方法
        self.instance_method()

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


# ============================================================================================================
# 类的继承
class ParentClass:
    pass


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
