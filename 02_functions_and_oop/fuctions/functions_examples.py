# ============================================================================================================
# Python 函数学习
# ============================================================================================================
# 作者：于昊男
# 目的：帮助学习函数定义、参数使用、返回值、作用域、lambda 等核心概念
# 说明：每段代码都附带详细注释与命名规范建议
# ============================================================================================================


# ============================================================================================================
# 一、函数的概念及自定义规则
# ============================================================================================================
# 函数（Function）是组织好的、可重复使用的代码块，
# 它可以接收输入（参数），并返回输出（结果）。
# 函数的好处：避免重复代码，提高程序结构清晰度。

# 函数命名规则（命名规范是编程基本功之一）：
# ✅ 函数名用小写字母和下划线组成（例如 calculate_sum）
# ✅ 函数名应当“见名知意”
# ✅ 代码块必须有 4 个空格缩进（不要使用 Tab 键）
# ✅ 函数定义以 def 开头，以冒号结尾
# ✅ 若函数只有一行代码，也要保持良好的缩进与结构
# ============================================================================================================
# 一、常用内置函数的使用
# pow(x, y)：需要两个参数，作用是返回x的y次幂
a = 2
b = 3
c = pow(b, a)
print(c)
print(3 ** 2)

# abs(x)：有一个参数，作用是取x的绝对值
x = -3.14
print(abs(x))

# round(x, d)：有两个参数，第一个是要操作的对象，第二个是指定要保留的位数
# 作用是返回x的四舍五入之后的值
pi = 13.1415926
print(round(pi, 3))

# 用来查看函数的原型及说明文档，内置函数几乎都有说明文档
# 自定义函数需要用户自己填写说明文档
# help函数的参数一定是函数名字且不带括号
help(pow)


# pass：就是在函数刚开始定义且没有写功能时，作为占位符
# 防止解释器报错
def test_pass():
    pass


# ============================================================================================================
# 二、自定义函数
# 函数的定义：def 函数名（参数列表）：
# 函数只有在调用的时候才会被执行
# 函数在定义的时候： Python解释器只会检查语法而不主动执行函数
def my_function(x_my, y_my):
    """
    这是第一个测试函数，用于测试自定义函数的定义与调用。
    :param x_my:
    :param y_my:
    :return: None
    """
    for i in range(x_my):
        print(i * y_my)
        print(i * x_my)


my_function(3, 4)
# ============================================================================================================
# 三、函数参数的使用
# 带有参数的函数的定义
# 参数在子代码块里如果出现某数据类型所拥有的独特标志之后
# 那么传入其他类型的数据之后，就会报错,如：传入不可变数据类型，但是惊醒了可变数据类型的操作就会报错
# ------------------------------------------------------------------------------------------------------------
# 带有参数的函数的调用
# 函数的实参除了可以直接使用数据之外
# 也可以传入变量且传入变量的使用会更多
my_function(3, 4)


# ------------------------------------------------------------------------------------------------------------
# 位置参数：参数传递时实参的顺序和个数必须和形参保持一致
def sub(x_sub, y):
    print(x_sub - y)


sub(2, 1)
# ------------------------------------------------------------------------------------------------------------
# 关键字参数：使用 形参名字=实参 的方式传递，不用考虑形参的位置
# 关键字参数使用的场景很多
sub(y=2, x_sub=1)
# Python解释器规定位置参数必须在关键字参数之前传参
# 也就是说，当调用函数时，第一个传入的参数是关键字传参时，那么后面的参数就不能使用位置传参了
# sub(y=2, 1)
# help(sum)
ls = [1, 2, 3]
# print('使用关键字传参：', sum(ls, start=1))
# print("使用位置参数传参：", sum(ls, 1))
help(dict.fromkeys)


# ------------------------------------------------------------------------------------------------------------
# 默认参数
# 定义函数时，可以给形参指定默认值，这样在调用函数时，如果不传入实参，则使用默认值
# 默认在定义时，必须放在形参的最右边
def add(x_add, y_add=1, z_add=1):
    print(x_add + y_add + z_add)


# 默认参数在调用函数时如果不需要修改默认参数的值就可以不传递
# 如果需要修改默认参数的值，可以传递实参来实现覆盖参数的默认值
add(2, y_add=1, z_add=1)


# ------------------------------------------------------------------------------------------------------------
# 位置不定长参数： 在函数定义时，使用 *args来表示
def args_test(*args):
    for i in args:
        print(f"hello{i}")

    print(len(args))
    print(type(args))  # Python 会自动把传入的所有位置参数打包成一个元组 args。
    print(args)


args_test(1, 2, 3, "apple", "banana")


# ------------------------------------------------------------------------------------------------------------
# 为什么要打包成元组而不是别的数据类型
# 是因为元组有一个特性叫做：打包和解包
# 打包就是将多个值打包为一个元组
# 打包的用法
def Packing_test():
    return 1, 2, 3, 4


print(Packing_test())

# 解包：将一个元组的元素拆开分别赋值给对应的变量
Packing_test_x, Packing_test_y, Packing_test_z, Packing_test_m = Packing_test()
print(Packing_test_x, Packing_test_y, Packing_test_z, Packing_test_m)


# 元组解包的函数传参用法，使用 *元组名 就可以做到一次传递多个参数
def tuple_Unpacking_test(tuple_Unpacking_test_x, tuple_Unpacking_test_y, tuple_Unpacking_test_z,
                         tuple_Unpacking_test_m):
    print("这是tuple_Unpacking_test函数", tuple_Unpacking_test_x, tuple_Unpacking_test_y, tuple_Unpacking_test_z,
          tuple_Unpacking_test_m)


tuple_Unpacking = (1, 2, 3, 4)
tuple_Unpacking_test(*tuple_Unpacking)


# 字典的解包用法
def dict_Unpacking_test(dict_Unpacking_test_x, dict_Unpacking_test_y, dict_Unpacking_test_z, **kwargs):
    print("这是dict_Unpacking_test函数", dict_Unpacking_test_x, dict_Unpacking_test_y, dict_Unpacking_test_z,
          kwargs)


# 当我们用 **kwargs 这种解包字典的方式传参时，Python 会把字典的键名当作函数的参数名，所以
# 只有当字典的键名和函数形参名字完全一致时，Python 才能正确地把值传给对应的参数。
# 只需要key相同即可，对key的顺序不做要求
dict_Unpacking = {"dict_Unpacking_test_x": 1, "dict_Unpacking_test_y": 2, "dict_Unpacking_test_z": 3}
dict_Unpacking_test(**dict_Unpacking)


# ------------------------------------------------------------------------------------------------------------
# 不定长位置参数在定义时：如果右边还有其他的参数，必须要使用关键字参数
# 实现一个求最大值的函数
def max_test(*args, max_num=0):
    max_num = args[0]
    # 循环便利数组
    for i in args:
        # 如果当前元素大于max_num，则更新max_num
        if i > max_num:
            max_num = i
    return max_num


print(max_test(1, 2, 3, 4, 5))


# ------------------------------------------------------------------------------------------------------------
# 关键字不定长参数：以**kwargs 作为标志，**是必须的， kwargs是程序员约定成俗的
# 它会将输入的关键字参数中的关键字当作键值对的键，将关键字参数中的实参当作键值对的值
# 放到字典里进行存储
def kwargs_test(**kwargs):
    print(kwargs)
    print(type(kwargs))


kwargs_test(name="apple", age=18, height=1.8)


# 对传入的参数值进行相乘
def mul_kwargs_test(**kwargs):
    result = 1
    for value in kwargs.values():
        result *= value
    return result


print(mul_kwargs_test(a=2, b=3, c=4))


# ------------------------------------------------------------------------------------------------------------
# *args 与 **kwargs 同时出现在函数中
# **kwargs 必须在 *args 之后
# **kwargs 中的参数不能与其他参数同名
def args_kwargs_test(*args, **kwargs):
    print(args)
    print(kwargs)


# 注意输出数据的格式
args_kwargs_test(1, 2, 3, name="apple", age=18, height=1.8)


# ============================================================================================================
# 函数的返回值可以使得函数的功能更加灵活，可以将函数的结果保存到变量中，也可以将函数的结果作为参数传递给其他函数
# 定义函数时，使用 return 关键字来指定返回值
# 如果函数没有指定返回值，则默认返回 None
def my_function_return(x_my_return, y_my_return):
    """
    这是第二个测试函数，用于测试自定义函数的返回值。
    :param x_my_return:
    :param y_my_return:
    :return: x_my_return * y_my_return
    """
    return x_my_return * y_my_return


# 调用函数并保存返回值到变量中
result = my_function_return(3, 4)
print(result)


# 调用函数并将返回值作为参数传递给其他函数
def my_function_return_2(x_my_return_2, y_my_return_2):
    """
    这是第三个测试函数，用于测试自定义函数的返回值。
    :param x_my_return_2:
    :param y_my_return_2:
    :return: x_my_return_2 * y_my_return_2
    """
    return x_my_return_2 * y_my_return_2


def my_function_return_3(x_my_return_3, y_my_return_3):
    """
    这是第四个测试函数，用于测试自定义函数的返回值。
    :param x_my_return_3:
    :param y_my_return_3:
    :return: x_my_return_3 * y_my_return_3
    """
    result = my_function_return_2(x_my_return_3, y_my_return_3)
    return result


result = my_function_return_3(3, 4)
print(result)


# ============================================================================================================
# 五、局部变量和全局变量
# 局部变量：在函数内部定义的变量，只能在函数内部访问，外部不能访问
# 全局变量：在函数外部定义的变量，可以在整个程序范围内访问
# 局部变量的生命周期只在函数内部，函数执行完毕后，局部变量会被销毁
# 全局变量的生命周期在整个程序运行期间，直到程序结束

# ------------------------------------------------------------------------------------------------------------
# 局部变量的定义
# 局部变量的定义只在函数内部有效，函数执行完毕后，局部变量会被销毁
def localVariable_test(x_my_local, y_my_local):
    """
    这是测试函数，用于测试局部变量的定义。
    :param x_my_local:
    :param y_my_local:
    :return:
    """
    print("这是localVarble_test函数", x_my_local, y_my_local)


# -------------------------------------------------------------------------------------------------------------
# 全局变量的定义
# 全局变量：定义在函数外的变量 或 在函数内使用global关键字修饰的变量
# 在函数内部是可以访问到全局变量的，但是函数外部不可以访问到局部变量
# 当函数内部存在变量与函数外部的变量名字相同时，函数内部的变量会覆盖外部的变量
# global非必要不适用，因为global能够在函数的内部修饰全局变量的值
# 使用很对的global会导致全局变量非常危险
y_global_test = 100


def globalVariable_test(x_my_global):
    """
    这是测试函数，用于测试全局变量的定义。
    :param x_my_global:
    :return:
    """
    # global：用来将局部变量升级为全局变量
    global y_global_test
    print('这是globalVariable_test函数内部修改之前的y_global_test的id', id(y_global_test))
    y_global_test = x_my_global
    print('这是globalVariable_test函数内部修改之后的y_global_test的id', id(y_global_test))


globalVariable_test(200)


# -------------------------------------------------------------------------------------------------------------
# 函数的重写
# 函数的名字或者变量的名字一定不要跟BIF的名字相同
# 否则就调用不到BIF，BIF的全写是Build-in-Function,即内置函数
# 关于列表的sum函数和len函数
# my_list = [1, 2, 3, 'abcde', [1, 2, 3]]
#
#
# def len_list(my_list):
#     # 用来记录元素的个数
#     count = 0
#     for i in my_list:
#         count += 1
#     return count
#
#
# my_list = [1, 2, 3, 'asdasd', [1, 2, 3]]
#
#
# # ret = len_list(my_list)
# # print(ret)
# def sum(my_list):
#     # 定义一个变量，用来存储求和的结果
#     # result = 0
#     # for i in my_list:
#     #     result += i
#     return 1
# ============================================================================================================
# 六、嵌套函数
# 内部函数除了在外部函数中调用外，是无法访问到的
def outer_function_test():
    """
    这是测试函数，用于测试嵌套函数。
    :return:
    """
    print("这是outer_function_test函数")

    def inner_function_test():
        """
        这是测试函数，用于测试嵌套函数。
        :return:
        """
        print("这是inner_function_test函数")

    print("在外层函数中调用了 inner_function_test 函数", inner_function_test())


outer_function_test()

# inner_function_test 函数无法在外层被调用
# ------------------------------------------------------------------------------------------------------------
# 嵌套函数的作用域
# 嵌套函数可以访问外部函数的变量，但外部函数无法访问嵌套函数的变量
# 嵌套函数的作用域只在函数内部有效，函数执行完毕后，嵌套函数的变量会被销毁
# 因此在内部函数中： 内函数的局部变量 > 外函数的局部变量 > 全局变量
# 在内部函数中，可以使用 nonlocal 关键字来访问外层函数的变量
# 但是 nonlocal 关键字只能在 Python 3.x 版本中使用
# 对于 Python 2.x 版本，可以使用 globals() 和 locals() 函数来获取全局变量和局部变量
# 但是 globals() 和 locals() 函数只能在函数内部使用，不能在函数外部使用
# 因此，在 Python 2.x 版本中，不建议使用 nonlocal 关键字来访问外层函数的变量

x_nest_function_test = 100


def outer_nested_functions_test():
    """
    通过这个函数来演示嵌套函数以及嵌套函数中变量的作用域的外部函数
    :return:
    """
    x_inner_nest_function = 200
    global x_nest_function_test
    x_nest_function_test = 10000000

    # 使用nonlocal关键字,可以在内部函数中修改外部函数的变量值
    # nonlocal 和 global 关键字不能作用于同一个变量
    def inner_nested_functions_test():
        """
        通过这个函数来演示嵌套函数以及嵌套函数中变量的作用域的内部函数
        :return:
        """
        # nonlocal x_nest_function_test # nonlocal 不可以和 globals() 同时作用在一个变量上会报错

        global x_nest_function_test  # 内部函数和外部函数都可以访问全局变量
        nonlocal x_inner_nest_function  # 内部函数可以访问外部函数的变量，但是外部函数无法访问内部函数的变量
        x_nest_function_test = 300
        x_inner_nest_function = 2000000
        print("这是inner_nested_functions_test函数内部的x_nest_function_test变量", x_nest_function_test)
        print("这是inner_nested_functions_test函数内部的变量x_inner_nest_function", x_inner_nest_function)

    print("这是outer_nested_functions_test函数内部的x_nest_function_test变量x_inner_nest_function",
          x_nest_function_test)


outer_nested_functions_test()


# ============================================================================================================
# 七、闭包函数
# 闭包函数：一个函数在其外部函数作用域已经结束后，仍然记住并能访问那个函数作用中的变量
# 简单来说：闭包 = “函数 + 环境（外层函数中的变量）”
# 也就是说，即使外层函数执行完毕，其局部变量按理应该销毁，但是只要这个变量被内层函数引用了，他就会被记住并形成闭包
# 闭包的基本构成
def closure_outer_test(x_my_closure):  # 外部函数
    def closure_inner_test(y_my_closure):  # 内部函数(嵌套函数)
        return x_my_closure + y_my_closure  # 内部函数使用了外部函数的变量

    return closure_inner_test  # 返回内部函数（不是调用）


# 在上面这个例子中 变量 x_my_closure 被 内部函数 closure_inner_test
# 闭包过程演示
# 创建闭包对象
closure_obj1 = closure_outer_test(100)
closure_obj2 = closure_outer_test(200)
# 调用闭包
print("这是闭包对象1", closure_obj1(100))
print("这是闭包对象2", closure_obj2(200))
print(closure_outer_test(123))  # 注意这里返回的是一个函数体
# 可以通过.__closure__ 属性来查看闭包保存了那些外部变量
print("这里在查看闭包对象中存储了哪些外部变量", closure_obj1.__closure__[0].cell_contents)
print("这里在查看闭包对象中存储了哪些外部变量", closure_obj2.__closure__[0].cell_contents)
# 闭包函数的常用场景
# 1.实现延迟计算（保存数据状态）
# 2. 代替全局变量，封装状态
# 3. 实现装饰器
# ============================================================================================================
# 八、匿名函数 lambda
# 匿名函数：没有名字的函数，可以直接使用 lambda 关键字来定义
# 匿名函数的基本语法：lambda 参数列表: 表达式
# 匿名函数的作用：
# 1. 快速定义简单的函数
# 2. 简化代码，减少代码量
# 3. 作为函数参数传递
# 4. 作为函数的返回值
# 匿名函数的注意事项：
# 匿名函数只能有一个表达式，不能有 return 语句
# 变量定义
# lambda函数会先执行默认参数表达式。

test_lambda = lambda x_lambda=int(input("请输入一个数字：")): x_lambda + 1
# test_lambda被警告是因为，规范不推荐这么使用lambda函数。
print("匿名函数的返回值", test_lambda)  # 这里只是返回了一个函数体
print("匿名函数的返回值", test_lambda())  # 这里输出的才是运算后的值，需要调用！
# lambda 的设计初衷是写简单的、一次性的小函数，比如在 map、filter 或 sorted 中用。
map_test = map(lambda x: x + 1, [1, 2, 3, 4, 5])  # map函数会修改原数据
print("匿名函数作为map函数的使用", list(map_test))
filter_test = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])  # filter函数不会修改原数据
print("匿名函数作为filter函数的使用", list(filter_test))
sorted_test = sorted([1, 5, 2, 4, 3], key=lambda x: x % 2)
print("匿名函数作为sorted函数的使用", sorted_test)
# ============================================================================================================
