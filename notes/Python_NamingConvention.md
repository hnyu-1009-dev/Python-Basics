
# 🧱 Python 与全栈项目命名规范

## 一、命名规范总体思想

命名规范核心目标：**见名知意、一致性、可维护性**。  
良好的命名能提高代码可读性和协作效率。

---

## 二、文件与工程命名规范

### 1️⃣ 工程命名
- 使用全小写 + 下划线。
- 示例：`smart_orchard_platform`, `iot_sensor_monitor`

Java 工程可使用中划线：`smart-orchard-system`。

### 2️⃣ 文件命名
- Python 文件：小写 + 下划线，如 `user_controller.py`
- Vue 组件文件：帕斯卡命名，如 `UserDashboard.vue`
- Java 文件：与类名一致，如 `UserController.java`

---

## 三、类、函数、变量命名规范

| 类型 | 推荐命名法 | 示例 | 说明 |
|------|-------------|------|------|
| 类名 | PascalCase | `UserManager`, `DataParser` | 类、异常 |
| 函数/方法名 | snake_case | `get_user_info()` | 动词开头 |
| 变量名 | snake_case | `sensor_value` | 表示数据 |
| 常量名 | UPPER_CASE | `MAX_SPEED` | 不可变量 |
| 模块名 | snake_case | `config_loader.py` | 模块功能明确 |
| 包名 | 小写无下划线 | `models`, `controllers` | 遵循PEP8 |
| 枚举值 | UPPER_CASE | `STATUS_ACTIVE` | 枚举常量 |

---

## 四、命名禁忌与常见错误

| 错误类型 | 示例 | 原因 |
|-----------|--------|--------|
| 无意义名称 | `a`, `temp`, `data1` | 不易维护 |
| 内置函数同名 | `sum`, `id`, `input` | 会覆盖内置函数 |
| 风格混乱 | `userName` vs `user_name` | 降低可读性 |
| 拼音命名 | `jiaoyan`, `xuesheng` | 不具通用性 |
| 拼写错误 | `recieve` → `receive` | 容易误导 |

---

## 五、项目命名示例

### 📍 Python 后端结构

```
smart_orchard_backend/
├── app/
│   ├── models/
│   │   ├── user_model.py
│   │   └── sensor_model.py
│   ├── controllers/
│   │   ├── user_controller.py
│   │   └── sensor_controller.py
│   ├── services/
│   │   └── user_service.py
│   └── utils/
│       └── jwt_helper.py
└── main.py
```

### 📍 前端 Vue 结构

```
smart-orchard-frontend/
├── components/
│   ├── SensorChart.vue
│   ├── UserProfile.vue
│   └── Navbar.vue
├── views/
│   ├── Dashboard.vue
│   ├── Login.vue
│   └── Register.vue
├── store/
│   └── user.js
└── api/
    └── userApi.js
```

---

## 六、常用动词前缀表

| 功能 | 动词前缀 | 示例 |
|------|------------|------|
| 获取数据 | get_ | `get_user_info()` |
| 设置修改 | set_, update_ | `update_sensor_value()` |
| 检查验证 | check_, validate_ | `check_login_status()` |
| 计算统计 | calc_, count_ | `calc_average_temp()` |
| 创建对象 | create_, build_, generate_ | `create_user_token()` |
| 删除对象 | delete_, remove_ | `delete_task()` |
| 转换格式 | convert_, to_ | `convert_to_json()` |

---

## 七、总结口诀

> 🧠 见名知意，风格统一，动词为首，名词结尾。  
> 📁 文件小写加下划线，类名首字母大写，变量小写蛇形线。  
> 🚫 不用拼音，不拼错单词，不与内置函数重名。
