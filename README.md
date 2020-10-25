# SHU每日两报脚本
## 1. 实现结果
本程序利用python中的Selenium库，并结合浏览器驱动，来自动完成指定日期内（如从1号至30号）的每日两报的操作，最后测试结果将每天的体温设置区间为36度至37度之间（含小数点后一位）。
## 2. 使用步骤
1、首先，此程序基于python 3.8.5版本运行，使用的浏览器为Edge，版本号86.0.622.51 (Official build) (64-bit)，IDE为PyCharm 2020.1.3 (Professional Edition)

2、打开命令行，使用pip指令安装selenium
`pip install selenium`
3、通过浏览器官网下载相应的浏览器启动插件，将其设置为系统环境变量(可选)，也可以在程序中自行设置浏览器启动驱动位置，如在E盘的E:\Edgedriver目录，就更改默认的地址 driverUrl = r"E:\Edgedriver\msedgedriver.exe"
4、运行程序时，请关闭其他任何可能影响浏览器运行的插件或者软件，如果网络信号不佳，则需要将time.sleep(1)中的数值调大，以等待网页的元素彻底加载成功

## 3. 写在最后
本着测试web自动化的初衷，加之校园的日填写网页结构较为简单，无复杂的html结构或者css样式，是个十分适合练习的网站。当然，为了实现最终结果也是走了不少弯路，这里感谢网站`http://www.testclass.net/`的免费教程，为此工程完成提供了不少帮助。此项目在GitHub完全开源，仅供学习使用，请不要为了省却时间，选择欺报或者瞒报，而放松了对疫情的警惕。
```python
#-*- coding = utf-8 -*-
#@Time : 2020-10-24 20:08
#@Author : Jiancong Zhu
#@Email : 643601464@qq.com
#@File : test.py
#@Software: PyCharm
def main():
    print("Hello, world!")#人生苦短，我用python

if __name__ == "__main__":
    main()
```