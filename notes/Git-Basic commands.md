# 🧰 Git & GitHub 常用命令速查表

## 🧱 一、基本概念
- **Git**：本地版本控制工具（你电脑上的代码管理器）
- **GitHub**：远程代码托管平台（团队协作开发）

---

## 📂 二、Git 工作区结构

| 区域 | 命令 | 说明 |
|------|------|------|
| 工作区 (Working Directory) | — | 你正在修改的文件所在目录 |
| 暂存区 (Staging Area) | `git add` | 临时保存修改 |
| 本地仓库 (Local Repository) | `git commit` | 保存修改记录 |
| 远程仓库 (Remote Repository) | `git push` / `git pull` | 与 GitHub 同步代码 |

---

## 🚀 三、初始化与远程连接

```bash
git init                                 # 初始化本地仓库
git clone <url>                          # 克隆远程仓库
git remote add origin <url>              # 绑定远程仓库
git remote -v                            # 查看远程仓库地址
git remote set-url gitee <url>           # gitee修改远程仓库地址
git remote set-url origin <url>          # github修改远程仓库地址

```
## 🧩 四、查看状态与历史记录
```bash
git status                               # 查看当前修改状态
git log                                  # 查看提交记录
git log --oneline --graph --all          # 图形化查看所有分支提交
git diff                                 # 查看未暂存的修改
```
## 🧾 五、添加与提交修改
```bash
git add <file>                           # 添加单个文件到暂存区
git add .                                # 添加所有修改到暂存区
git commit -m "提交说明"                  # 提交到本地仓库
git commit -am "提交说明"                 # 添加并提交已追踪文件
```

##  ☁️ 六、推送与拉取代码
```bash
git push origin main                     # 推送 main 分支到远程
git push origin <branch>                 # 推送指定分支
git pull origin main                     # 拉取远程 main 更新
git fetch origin                         # 获取远程分支但不合并
git merge origin/main                    # 合并远程更新到当前分支
```
## 🌿 七、分支操作（Branch）
```bash
git branch                               # 查看本地分支
git branch -r                            # 查看远程分支
git branch -a                            # 查看所有分支
git branch <branch-name>                 # 创建新分支
git checkout <branch-name>               # 切换分支
git checkout -b <branch-name>            # 创建并切换分支
git switch <branch-name>                 # 切换分支（推荐）
git switch -c <branch-name>              # 创建并切换分支（推荐）
git merge <branch-name>                  # 合并指定分支到当前分支
git branch -d <branch-name>              # 删除本地分支
git push origin --delete <branch-name>   # 删除远程分支
```
## 🔄 八、标签操作（Tag）
```bash
git tag                                  # 查看标签
git tag <tag-name>                       # 创建标签
git tag -a <tag-name> -m "说明"          # 创建带说明的标签
git push origin <tag-name>               # 推送单个标签
git push origin --tags                   # 推送所有标签
git tag -d <tag-name>                    # 删除本地标签
git push origin --delete tag <tag-name>  # 删除远程标签
```
## ⚔️ 九、解决冲突（Conflict）
```bash
# 当执行 merge 或 pull 出现冲突时：
# 1. 打开冲突文件，手动修改标记内容（<<<<<<<、=======、>>>>>>）
# 2. 修改完成后执行：
git add .
git commit -m "解决合并冲突"

```

## 👥 十、团队协作推荐流程
```bash
# 1️⃣ 拉取主分支最新代码
git checkout main
git pull origin main

# 2️⃣ 创建功能分支
git checkout -b feature/login

# 3️⃣ 编码 + 提交
git add .
git commit -m "实现登录功能"

# 4️⃣ 推送到远程
git push origin feature/login

# 5️⃣ 在 GitHub 上发起 Pull Request（PR）合并到 main 或 dev

# 6️⃣ 合并后清理分支
git branch -d feature/login
git push origin --delete feature/login
```
🧼 十一、其他实用命令
## 
```bash
git restore <file>                       # 撤销未暂存的修改
git reset <file>                         # 取消暂存区的文件
git reset --hard <commit-id>             # 回退到指定提交
git stash                                # 暂存当前修改
git stash pop                            # 恢复暂存的修改
git config --global user.name "你的名字"   # 设置全局用户名
git config --global user.email "你的邮箱"  # 设置全局邮箱
```

## 💡 十二、常见分支命名规范
| 类型    | 命名示例               | 说明     |
| ----- | ------------------ | ------ |
| 主分支   | `main` / `master`  | 稳定版本   |
| 开发分支  | `dev`              | 日常开发   |
| 功能分支  | `feature/login`    | 新功能开发  |
| 修复分支  | `bugfix/api-error` | 修复缺陷   |
| 热修复分支 | `hotfix/v1.0.1`    | 线上紧急修复 |
