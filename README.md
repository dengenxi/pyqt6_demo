PyQt6 是基于 Python 的一系列模块。它是一个多平台的工具包，可以在包括 Unix、Windows 和 Mac OS 在内的大部分主要操作系统上运行。PyQt6 有两个许可证，开发人员可以在 GPL 和商业许可之间进行选择。

>示例大多采用[霞鹜文楷](https://github.com/lxgw/LxgwWenKai)字体，运行前请确保安装了该字体

# 使用模块
- PyQt6
- sys
- pyrcc5
- pyinstaller

# 图片转换为python文件
>转换的原因是因为pyinstaller并不会打包图片文件，所以打包成exe后图片无法加载，故需要进行处理以确保exe正常展示图片资源。

根据如下命令可以生成对应的python文件：
```bash
pyrcc5 -o 生成文件名.py .qrc文件路径 
```

# 打包exe
采用[pyinstaller](https://github.com/pyinstaller/pyinstaller)进行打包
```bash
pyinstaller --onefile --windowed python文件
```