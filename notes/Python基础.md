# Python基础

## 环境变量的调试安装

![image-20251009102316525](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251009102316525.png)

![image-20251009102343283](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251009102343283.png)

本地环境只能通过安装程序安装，在pycharm中替换解释器，可以按照以上方式更改

tips：容易遇到Error:Python packaging tool ‘setuptools‘not found

记得选择版本后点击安装

## 基本语法学习

### **rang()对象的特点**

![image-20251011085242191](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251011085242191.png)

### 注释

（注意规范Python 中的注释规范主要遵循 **PEP 8** ’常用‘和 **PEP 257** 标准）

![image-20251009102857816](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251009102857816.png)

### 数据类型

#### 数据类型分类

![image-20251011101239830](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251011101239830.png)

#### 基本数据类型的存储能力

![image-20251011095627747](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251011095627747.png)

#### 字符串

![image-20251010190846386](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251010190846386.png)![image-20251010191100644](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251010191100644.png)

![image-20251010191001498](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251010191001498.png)![image-20251010191245946](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251010191245946.png)

#### 列表

![image-20251011103523188](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251011103523188.png)

![image-20251011103610587](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251011103610587.png)

![image-20251011104048655](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251011104048655.png)

##### 浅拷贝与深拷贝！！！！

##### 列表表达式

![image-20251011113232170](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251011113232170.png)

![image-20251011105130652](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251011105130652.png)嵌套列表使用sort()按照子列的首元素进行比较

但是数据类型不同时间则无法比较

#### 序列

##### 序列包含

![image-20251011095053901](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251011095053901.png)

##### 通用操作

![image-20251011092120264](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251011092120264.png)



### ![image-20251011092155082](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251011092155082.png)

#### 是否有序

![image-20251011092446308](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251011092446308.png)

![image-20251011092459291](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251011092459291.png)

![image-20251011092745813](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251011092745813.png)

![image-20251011092758843](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251011092758843.png)

#### 是否可哈希

![image-20251011101710513](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251011101710513.png)





### 函数

**可以经常使用help函数来查看函数的传参要求**

#### 参数传递

![image-20251010115814657](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251010115814657.png)

斜杠之前必须是位置传参

![image-20251010134910663](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251010134910663.png)

![image-20251010135425261](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251010135425261.png)

**使用不定长参数时，如果右边还有其他的参数，必须要使用关键字参数**

![image-20251010143822810](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251010143822810.png)

**注意元组的打包和解包特性。**

![image-20251010150025732](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251010150025732.png)

**keywards也可以和上面一样对字典进行解包使用，但形参和字典key必须一样**

![image-20251010160639866](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251010160639866.png)

当函数名和内部函数名重合时，内部函数会被重写

![image-20251010165726846](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251010165726846.png)

![image-20251010165937034](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251010165937034.png)

![image-20251010170256292](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251010170256292.png)

![image-20251010170810520](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251010170810520.png)

![image-20251010170829963](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251010170829963.png)

**起别名**

![image-20251010171047281](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251010171047281.png)

![image-20251010171459729](C:\Users\javis\AppData\Roaming\Typora\typora-user-images\image-20251010171459729.png)