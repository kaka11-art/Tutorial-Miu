# 01. Anaconda 入门

## 目标

- 解释 Anaconda、conda、Python、package、environment 的关系。
- 在终端或 Anaconda Prompt 中检查 conda 是否可用。
- 创建、激活、退出、删除 conda 环境。
- 在环境中安装包并运行 Python 文件。

## 节奏

| 环节 | 时间 |
| --- | ---: |
| 为什么需要 Anaconda | 15 分钟 |
| Python 环境和包的概念 | 20 分钟 |
| conda 基本命令演示 | 35 分钟 |
| 运行第一个 Python 文件 | 20 分钟 |
| 练习和答疑 | 20 分钟 |

## 1. Anaconda 是什么

Anaconda 是一个面向 Python 和数据科学的工具集合。它通常包含：

- Python 解释器。
- conda 环境和包管理工具。
- 常见数据科学包，例如 numpy、pandas、matplotlib。
- Anaconda Navigator 图形界面。
- JupyterLab / Notebook 等工具入口。

简单理解：

```text
Python        负责运行 .py 程序
package       别人写好的功能库，例如 pandas、matplotlib
conda         负责创建环境、安装包、管理包版本
environment   一个独立的 Python 工作空间
Anaconda      把这些工具打包在一起
```

## 2. 为什么需要环境

不同项目可能需要不同版本的 Python 和包。例如：

```text
项目 A：Python 3.10 + pandas 1.x
项目 B：Python 3.12 + pandas 2.x
```

如果所有项目都装在同一个 Python 里，版本冲突会越来越多。conda 环境可以把项目隔离开：

```text
base
├── py-basics       用于本课程
├── data-analysis   用于数据分析项目
└── old-project     用于旧项目
```

建议：不要长期在 `base` 环境里写项目。`base` 可以保留给 conda 自己，项目使用单独环境。

## 3. 打开命令行

Windows 推荐使用：

- Anaconda Prompt
- PowerShell

macOS 推荐使用：

- Terminal
- iTerm2

Linux 推荐使用：

- Terminal

本课程用 `$` 表示命令提示符，实际输入时不要输入 `$`。

## 4. 检查安装

运行：

```bash
conda --version
```

如果安装成功，会看到类似：

```text
conda 24.5.0
```

再检查 Python：

```bash
python --version
```

或在部分 macOS/Linux 机器上：

```bash
python3 --version
```

查看 conda 基本信息：

```bash
conda info
```

重点看：

- `active environment`：当前环境。
- `base environment`：Anaconda 安装位置。
- `platform`：系统平台。

## 5. 常用 conda 命令

### 查看所有环境

```bash
conda env list
```

或：

```bash
conda info --envs
```

当前环境前面会有 `*`。

### 创建环境

创建一个名为 `py-basics` 的环境，并指定 Python 版本：

```bash
conda create -n py-basics python=3.11
```

拆开看：

```text
conda create   创建环境
-n py-basics   环境名字
python=3.11    安装 Python 3.11
```

### 激活环境

```bash
conda activate py-basics
```

激活后，命令行前面通常会出现：

```text
(py-basics)
```

### 退出环境

```bash
conda deactivate
```

### 安装包

在 `py-basics` 环境中安装常用包：

```bash
conda install numpy pandas matplotlib jupyterlab
```

也可以指定 channel：

```bash
conda install -c conda-forge pandas
```

### 查看当前环境已安装的包

```bash
conda list
```

### 搜索包

```bash
conda search pandas
```

### 更新包

```bash
conda update pandas
```

### 删除包

```bash
conda remove pandas
```

### 删除环境

先退出环境：

```bash
conda deactivate
```

再删除：

```bash
conda env remove -n py-basics
```

## 6. 现场演示：创建课程环境

现场可以这样走一遍：

```bash
conda create -n py-basics python=3.11
conda activate py-basics
conda install numpy pandas matplotlib jupyterlab
python --version
conda list
```

然后创建一个文件 `hello_conda.py`：

```python
import sys

print("Hello from conda!")
print("Python executable:", sys.executable)
print("Python version:", sys.version)
```

运行：

```bash
python examples/hello_conda.py
```

如果不在项目根目录，需要先进入项目目录。例如：

```bash
cd path/to/PythonTutorial
python examples/hello_conda.py
```

## 7. pip 和 conda 的关系

`conda` 和 `pip` 都可以安装包，但它们不完全相同。

| 工具 | 主要用途 |
| --- | --- |
| conda | 管理 Python、环境、二进制依赖和科学计算包 |
| pip | 安装 Python Package Index 上的 Python 包 |

推荐规则：

1. 能用 conda 安装时，先用 conda。
2. conda 找不到时，再在当前 conda 环境中用 pip。
3. 不要在没有激活环境时随手运行 `pip install`。

检查 pip 属于哪个 Python：

```bash
python -m pip --version
```

安装 pip 包时优先写成：

```bash
python -m pip install package-name
```

这样能减少装错环境的概率。

## 8. 常见问题

### `conda: command not found`

可能原因：

- Anaconda 没有安装成功。
- 命令行没有加载 conda。
- Windows 没有使用 Anaconda Prompt。

解决思路：

- Windows 先用 Anaconda Prompt。
- macOS/Linux 可以尝试重启 Terminal。
- 检查 Anaconda 安装目录。

### 激活环境后还是找不到包

先确认环境：

```bash
conda env list
python -c "import sys; print(sys.executable)"
```

再确认包：

```bash
conda list package-name
```

### Jupyter 里 import 失败

常见原因是 Jupyter 选错 kernel。第二节课会重点讲。

## 9. 练习

### 练习 1：环境操作

完成以下命令：

```bash
conda create -n practice-env python=3.11
conda activate practice-env
conda install requests
conda list
conda deactivate
conda env remove -n practice-env
```

记录每一步的关键输出。

### 练习 2：确认 Python 位置

在 `py-basics` 中运行：

```bash
python -c "import sys; print(sys.executable)"
python -c "import sys; print(sys.version)"
```

解释这两行输出分别表示什么。

### 练习 3：运行文件

创建 `my_environment_check.py`：

```python
import platform
import sys

print("System:", platform.system())
print("Python:", sys.version)
print("Executable:", sys.executable)
```

在终端中运行它。

## 10. 小结

- Anaconda 是工具集合，conda 是环境和包管理工具。
- 一个项目最好使用一个独立环境。
- 常用流程是：创建环境、激活环境、安装包、运行代码。
- 排查问题时，先确认当前 Python 的位置和当前 conda 环境。
