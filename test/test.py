import sys
import os

# sys.path 默认内容：
# ┌─────────────────────────────────────────────────────────────--─┐
# │ 1️⃣ 当前脚本所在目录               → ./                            │
# │ 2️⃣ Python 标准库路径              → C:\Python312\Lib             │
# │ 3️⃣ 第三方库路径（pip安装）        → C:\Python312\Lib\site-packages │
# └────────────────────────────────────────────────────────────--──┘
#
# 你手动添加：
# sys.path.append("D:/WorkSystem/.../modules_and_packages")
# 导入搜索顺序变成：
# 1. 当前脚本目录 # 当前脚本目录 是指你正在运行的 Python 文件（脚本）所在的文件夹。
# 2. 你手动添加的目录 ✅
# 3. 标准库目录
# 4. 第三方库目录


my_package_path = os.path.abspath("../03_modules_and_exceptions/modules_and_packages")
print("🧭 my_package_path =", my_package_path)

# 检查路径是否存在
print("📁 exists:", os.path.exists(os.path.join(my_package_path, "my_packages")))

sys.path.append(my_package_path)
print("✅ sys.path 最后一个路径:", sys.path[-1])

# 尝试导入
import my_packages

print("✅ 导入成功")
# 可以直接使用 __init__.py 中导入的内容
my_packages.func1()  # ✅ 输出：This is func1 in module1
my_packages.func2()  # ✅ 输出：This is func2 in module2
# # 2️⃣ 使用 “from 包 import *”
# from my_packages import *
#
# # 只会导入 __all__ 中定义的内容：func1 和 func2
# func1()  # ✅
# func2()  # ✅
# # 3️⃣ 如果在 __init__.py 中不导入 module1、module2
# #    那么要用完整路径：
# # import mypackage.module1
# # mypackage.module1.func1()
