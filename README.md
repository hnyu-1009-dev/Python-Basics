# 🐍 Python 学习与练习仓库

欢迎来到我的 **Python 学习记录仓库**！  
这个项目用于记录我在学习 Python 基础语法、常用库和编程练习过程中的代码与笔记。  
我会在学习过程中不断完善此仓库，帮助自己巩固编程思维，并为日后查阅提供资料。

---

## 📘 学习目标
- 掌握 Python 基础语法与数据结构
- 理解函数、模块、文件操作等核心概念
- 熟悉面向对象编程（OOP）
- 掌握常用标准库（`os`, `datetime`, `re`, `json` 等）
- 通过练习与小项目提升编程能力

---
## 📂 仓库结构

```bash
Python-Learning/
│
├── 01_basic/                      # 基础语法阶段（前置）
│   ├── variables_and_types.py     # 变量与数据类型
│   ├── control_flow.py            # 条件与循环语句
│   ├── data_structures.py         # 列表、元组、字典、集合
│   └── README.md
│
├── 02_functions_and_oop/          # 函数与面向对象
│   ├── 3.1_functions/             # 函数的基本概念与使用
│   │   ├── function_examples.py
│   │   └── README.md
│   ├── 3.2_classes/               # 类的基本概念与使用
│   │   ├── oop_intro.py
│   │   └── README.md
│   └── README.md
│
├── 03_modules_and_exceptions/     # 模块与异常机制
│   ├── 3.3_modules_and_packages/  # 模块与包
│   │   ├── my_package/
│   │   │   ├── __init__.py
│   │   │   ├── math_tools.py
│   │   │   └── string_tools.py
│   │   └── use_my_package.py
│   ├── 3.4_exceptions/            # 异常处理机制
│   │   ├── try_except_finally.py
│   │   └── custom_exception.py
│   └── README.md
│
├── 04_advanced_features/          # Python 进阶特性
│   ├── 3.5_iterators_generators/  # 迭代器与生成器
│   │   ├── iterators.py
│   │   ├── generators.py
│   │   └── README.md
│   ├── 3.6_regex/                 # 正则表达式
│   │   ├── regex_examples.py
│   │   └── README.md
│   ├── 3.7_decorators/            # 装饰器
│   │   ├── decorator_demo.py
│   │   └── README.md
│   ├── 3.8_file_io/               # 文件操作
│   │   ├── read_write_files.py
│   │   └── README.md
│   └── README.md
│
├── 05_concurrency_and_network/    # 并发与网络编程
│   ├── 3.9_multiprocessing/       # 多进程
│   │   ├── multiprocessing_example.py
│   │   └── README.md
│   ├── 3.10_multithreading/       # 多线程
│   │   ├── threading_example.py
│   │   └── README.md
│   ├── 3.11_coroutines/           # 协程
│   │   ├── asyncio_demo.py
│   │   └── README.md
│   ├── 3.12_network_basics/       # 网络基础知识
│   │   ├── socket_intro.py
│   │   └── README.md
│   ├── 3.13_network_programming/  # 网络编程（选修）
│   │   ├── tcp_server_client.py
│   │   └── README.md
│   └── README.md
│
├── 06_projects/                   # 实战项目区
│   ├── file_organizer/            # 自动整理文件小工具
│   ├── todo_list_cli/             # 命令行待办事项工具
│   ├── mini_web_server/           # 简易 Web 服务器
│   └── README.md
│
├── notes/                         # 学习笔记
│   ├── functions_notes.md
│   ├── oop_notes.md
│   ├── exceptions_notes.md
│   ├── concurrency_notes.md
│   └── network_notes.md
│
├── tests/                         # 测试区
│   ├── test_functions.py
│   ├── test_oop.py
│   └── test_file_io.py
│
├── requirements.txt               # 依赖记录
├── .gitignore                     # 忽略虚拟环境和缓存文件
└── README.md                      # 仓库说明文档

