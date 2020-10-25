# Selenium3实现网页自动化
## 1.初步工作
### 1.1 环境配置
安装Selenium

本文使用的是python3.8.4 64bit

使用pip指令安装selenium

`pip install selenium`

### 1.2 设置浏览器驱动
首先设置浏览器的地址，手动创建一个存放浏览器驱动的目录，如： E:\driver , 将下载的浏览器驱动文件（例如：chromedriver、geckodriver）丢到该目录下。

我的电脑-->属性-->系统设置-->高级-->环境变量-->系统变量-->Path，将“E:\driver”目录添加到Path的值中。

验证不同的浏览器驱动是否正常使用。

from selenium import webdriver

```python
driver = webdriver.Firefox()   # Firefox浏览器

driver = webdriver.Chrome()    # Chrome浏览器

driver = webdriver.Ie()        # Internet Explorer浏览器

driver = webdriver.Edge()      # Edge浏览器

driver = webdriver.Opera()     # Opera浏览器

driver = webdriver.PhantomJS()   # PhantomJS
```

## 2.基本操作
### 2.1 元素定位
Selenium提供了8种定位方式。

>id
>name
>class name
> name
>link text
>partial link text
>xpath
>css selector

这8种定位方式在Python selenium中所对应的方法为：

>find_element_by_id()
>find_element_by_name()
find_element_by_class_name()
find_element_by_tag_name()
find_element_by_link_text()
find_element_by_partial_link_text()
find_element_by_xpath()
find_element_by_css_selector()

定位使用的方法

假如我们有一个Web页面，通过前端工具（如，Firebug）查看到一个元素的属性是这样的。

```html
<html>
  <head>
  <body link="#0000cc">
    <a id="result_logo" href="/" onmousedown="return c({'fm':'tab','tab':'logo'})">
    <form id="form" class="fm" name="f" action="/s">
      <span class="soutu-btn"></span>
        <input id="kw" class="s_ipt" name="wd" value="" maxlength="255" autocomplete="off">输入框
```

我们的目的是要定位input标签的输入框。

- 通过id定位:

```python
dr.find_element_by_id("kw")
```

- 通过name定位:

```python
dr.find_element_by_name("wd")
```

- 通过class name定位:

```python
dr.find_element_by_class_name("s_ipt")
```

- 通过tag name定位:

```python
dr.find_element_by_tag_name("input")
```

**1、 通过xpath定位，xpath定位有多种写法，这里列几个常用写法: **
	Xpath支持ID、Class、Name定位功能，以以下三者为例：
　1）、通过ID定位
　　　　//*[@id='kw']
　2）、通过Class定位
　　　　//*[@class='class_name']
　3）、 通过Name定位
　　　　//*[@name='name']
**2、如果标签没有ID、Class、Name三总属性，Xpath还支持属性定位功能**
　　　　@ 代表以属性定位，后面可以接标签中任意属性 
　　　　//*[@other='attribute']
**3、当标签的属性重复时，Xpath提供了通过标签来进行过滤**
　　　　将 * 换位任意标签名，则可根据标签进行筛选
　　　　//input[@placeholder='用户名'] 
**4、当标签页重复时，Xpath提供了层级过滤**
	例如：找不到儿子，那么就先找他的爸爸，实在不行可以再找他的爷爷
	1）、支持通过 / 进行层级递进，找到符合层级关系的标签
　　　	//form/div/input[@placeholder="用户名"]
	2）、当层级都重复时，可以通过单个层级的属性进行定位
 　	  　//form/div[@class='login-user']/input
**5、一个元素它的兄弟元素跟它的标签一样，这时候无法通过层级定位到。因为都是一个父亲生的，多胞胎兄弟。Xpath提供了索引过滤**
　　　　通过索引，在List中定位属性，与python的索引有些差别，Xpath从1开始
　　　　//select[@name='city'][1]/option[1]
**6、上面几种如果都用上了之后还重复的话，我们就可以使用Xpath提供的终极神器，逻辑运算定位。and 或 or**　　　
　1）、通过and来缩小过滤的范围，只有条件都符合时才能定位到
 　　　　　//select[@name='city' and @size='4' and @multiple="multiple"]
　2）、or就相反了，只要这些筛选中，其中一个出现那么久匹配到了
　　　　　　//select[@name='city' or @size='4']

```python
dr.find_element_by_xpath("//*[@id='kw']")
dr.find_element_by_xpath("//*[@name='wd']")
dr.find_element_by_xpath("//input[@class='s_ipt']")
dr.find_element_by_xpath("/html/body/form/span/input")
dr.find_element_by_xpath("//span[@class='soutu-btn']/input")
dr.find_element_by_xpath("//form[@id='form']/span/input")
dr.find_element_by_xpath("//input[@id='kw' and @name='wd']")
```

- 通过css定位，css定位有多种写法，这里列几个常用写法:

```python
dr.find_element_by_css_selector("#kw")
dr.find_element_by_css_selector("[name=wd]")
dr.find_element_by_css_selector(".s_ipt")
dr.find_element_by_css_selector("html > body > form > span > input")
dr.find_element_by_css_selector("span.soutu-btn> input#kw")
dr.find_element_by_css_selector("form#form > span > input")
```

接下来，我们的页面上有一组文本链接。

```html
<a class="mnav" href="http://news.baidu.com" name="tj_trnews">新闻</a>
<a class="mnav" href="http://www.hao123.com" name="tj_trhao123">hao123</a>
```

- 通过link text定位:

```python
dr.find_element_by_link_text("新闻")
dr.find_element_by_link_text("hao123")
```

- 通过link text定位:

```python
dr.find_element_by_partial_link_text("新")
dr.find_element_by_partial_link_text("hao")
dr.find_element_by_partial_link_text("123")
```

### 2.2 浏览器控制
1. 控制浏览器大小

```python
driver.set_window_size(480, 800)
```
2. 前进，后退

```python
driver.forward()
driver.back()
```
3. 刷新页面

```python
driver.refresh()
```
### 2.3 模拟点击和输入

点击和输入
前面我们已经学习了定位元素， 定位只是第一步， 定位之后需要对这个元素进行操作， 或单击（按钮） 或输入（输入框） ， 下面就来认识 WebDriver 中最常用的几个方法：

clear()： 清除文本。

send_keys (value)： 模拟按键输入。

click()：	单击元素。
```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

driver.quit()
```

提交
submit()，
submit()方法用于提交表单。 例如， 在搜索框输入关键字之后的“回车” 操作， 就可以通过该方法模拟。

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

search_text = driver.find_element_by_id('kw')
search_text.send_keys('selenium')
search_text.submit()

driver.quit()
```
有时候 submit()可以与 click()方法互换来使用， submit()同样可以提交一个按钮， 但 submit()的应用范围远不及 click()广泛。



其他常用方法
size： 返回元素的尺寸。

text： 获取元素的文本。

get_attribute(name)： 获得属性值。

is_displayed()： 设置该元素是否用户可见。
```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 获得输入框的尺寸
size = driver.find_element_by_id('kw').size
print(size)

# 返回百度页面底部备案信息
text = driver.find_element_by_id("cp").text
print(text)

# 返回元素的属性值， 可以是 id、 name、 type 或其他任意属性
attribute = driver.find_element_by_id("kw").get_attribute('type')
print(attribute)

# 返回元素的结果是否可见， 返回结果为 True 或 False
result = driver.find_element_by_id("kw").is_displayed()
print(result)

driver.quit()
```
输出结果：

{'width': 500, 'height': 22}
©2015 Baidu 使用百度前必读 意见反馈 京 ICP 证 030173 号
text
True
执行上面的程序并查看结果： size 方法用于获取百度输入框的宽、 高， text 方法用于获得百度底部的备案信息， get_attribute()用于获得百度输入的 type 属性的值， is_displayed()用于返回一个元素是否可见， 如果可见则返回 True， 否则返回 False。

### 2.4 鼠标操作
在 WebDriver 中， 将这些关于鼠标操作的方法封装在 ActionChains 类提供。

ActionChains 类提供了鼠标操作的常用方法：

perform()： 执行所有 ActionChains 中存储的行为；

context_click()： 右击；

double_click()： 双击；

drag_and_drop()： 拖动；

move_to_element()： 鼠标悬停。



鼠标悬停操作

```python
from selenium import webdriver
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.cn")

# 定位到要悬停的元素
above = driver.find_element_by_link_text("设置")
# 对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()
```
……

from selenium.webdriver import ActionChains
导入提供鼠标操作的 ActionChains 类。

ActionChains(driver)
调用 ActionChains()类， 将浏览器驱动 driver 作为参数传入。

move_to_element(above)
context_click()方法用于模拟鼠标右键操作， 在调用时需要指定元素定位。

perform()
执行所有 ActionChains 中存储的行为， 可以理解成是对整个操作的提交动作。

### 2.5 键盘操作
Keys()类提供了键盘上几乎所有按键的方法。 前面了解到， send_keys()方法可以用来模拟键盘输入， 除此 之外， 我们还可以用它来输入键盘上的按键， 甚至是组合键， 如 Ctrl+A、 Ctrl+C 等。
```python
from selenium import webdriver
# 引入 Keys 模块
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")

# 删除多输入的一个 m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)


# 输入空格键+“教程”
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程")

# ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

# ctrl+v 粘贴内容到输入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')

# 通过回车键来代替单击操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)
driver.quit()
```
需要说明的是， 上面的脚本没有什么实际意义， 仅向我们展示模拟键盘各种按键与组合键的用法。

from selenium.webdriver.common.keys import Keys
在使用键盘按键方法前需要先导入 keys 类。

以下为常用的键盘操作：

|send_keys(Keys.BACK_SPACE) |删除键（BackSpace）|
|--|--|
|send_keys(Keys.SPACE)| 空格键(Space)|
|send_keys(Keys.TAB)| 制表键(Tab)|
|send_keys(Keys.ESCAPE)| 回退键（Esc）|
|send_keys(Keys.ENTER)| 回车键（Enter）|
|send_keys(Keys.CONTROL,'a') |全选（Ctrl+A）|
|send_keys(Keys.CONTROL,'c') |复制（Ctrl+C）|
|send_keys(Keys.CONTROL,'x') |剪切（Ctrl+X）|
|send_keys(Keys.CONTROL,'v')| 粘贴（Ctrl+V）|
|send_keys(Keys.F1) |键盘 F1|
|send_keys(Keys.F12) |键盘 F12|

## 3. 事件处理
### 3.1 断言判断
不管是在做功能测试还是自动化测试，最后一步需要拿实际结果与预期进行比较。这个比较的称之为断言。

我们通常可以通过获取title 、URL和text等信息进行断言。text方法在前面已经讲过，它用于获取标签对之间的文本信息。 下面同样以百度为例，介绍如何获取这些信息。
```python
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

print('Before search================')

# 打印当前页面title
title = driver.title
print(title)

# 打印当前页面URL
now_url = driver.current_url
print(now_url)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(1)

print('After search================')

# 再次打印当前页面title
title = driver.title
print(title)

# 打印当前页面URL
now_url = driver.current_url
print(now_url)

# 获取结果数目
user = driver.find_element_by_class_name('nums').text
print(user)

driver.quit()
```
脚本运行结果如下：

Before search================
百度一下，你就知道
https://www.baidu.com/
After search================
selenium_百度搜索
https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx...
搜索工具
百度为您找到相关结果约61,100,000个
title：用于获得当前页面的标题。

current_url：用户获得当前页面的URL。

text：获取搜索条目的文本信息。
### 3.2 元素等待

WebDriver提供了两种类型的等待：显式等待和隐式等待。

显式等待
显式等待使WebdDriver等待某个条件成立时继续执行，否则在达到最大时长时抛出超时异常（TimeoutException）。
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

element = WebDriverWait(driver, 5, 0.5).until(
                      EC.presence_of_element_located((By.ID, "kw"))
                      )
element.send_keys('selenium')
driver.quit()
```
WebDriverWait类是由WebDirver 提供的等待方法。在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常。具体格式如下：

WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
driver ：浏览器驱动。

timeout ：最长超时时间，默认以秒为单位。

poll_frequency ：检测的间隔（步长）时间，默认为0.5S。

ignored_exceptions ：超时后的异常信息，默认情况下抛NoSuchElementException异常。

WebDriverWait()一般由until()或until_not()方法配合使用，下面是until()和until_not()方法的说明。

until(method, message=‘’)
调用该方法提供的驱动程序作为一个参数，直到返回值为True。

until_not(method, message=‘’)
调用该方法提供的驱动程序作为一个参数，直到返回值为False。

在本例中，通过as关键字将expected_conditions 重命名为EC，并调用presence_of_element_located()方法判断元素是否存在。

隐式等待
WebDriver提供了implicitly_wait()方法来实现隐式等待，默认设置为0。它的用法相对来说要简单得多。
```python
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime

driver = webdriver.Firefox()

# 设置隐式等待为10秒
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

try:
    print(ctime())
    driver.find_element_by_id("kw22").send_keys('selenium')
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    driver.quit()
```
implicitly_wait() 默认参数的单位为秒，本例中设置等待时长为10秒。首先这10秒并非一个固定的等待时间，它并不影响脚本的执行速度。其次，它并不针对页面上的某一元素进行等待。当脚本执行到某个元素定位时，如果元素可以定位，则继续执行；如果元素定位不到，则它将以轮询的方式不断地判断元素是否被定位到。假设在第6秒定位到了元素则继续执行，若直到超出设置时长（10秒）还没有定位到元素，则抛出异常。

### 3.3 元素定位
WebDriver还提供了8种用于定位一组元素的方法。

find_elements_by_id()
find_elements_by_name()
find_elements_by_class_name()
find_elements_by_tag_name()
find_elements_by_link_text()
find_elements_by_partial_link_text()
find_elements_by_xpath()
find_elements_by_css_selector()
定位一组元素的方法与定位单个元素的方法类似，唯一的区别是在单词element后面多了一个s表示复数。

接下来通过例子演示定位一组元素的使用：
```python
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(1)

# 定位一组元素
texts = driver.find_elements_by_xpath('//div/h3/a')

# 循环遍历出每一条搜索结果的标题
for t in texts:
    print(t.text)

driver.quit()
```
程序运行结果：

Selenium - Web Browser Automation
官网
功能自动化测试工具——Selenium篇
selenium + python自动化测试环境搭建 - 虫师 - 博客园
selenium是什么?_百度知道
怎样开始用selenium进行自动化测试(个人总结)_百度经验
Selenium_百度百科
selenium_百度翻译
Selenium官网教程_selenium自动化测试实践_Selenium_领测软件测试网
Selenium(浏览器自动化测试框架)_百度百科
自动化基础普及之selenium是啥? - 虫师 - 博客园
python十大主流开源框架 「菜鸟必看」
### 3.4 多表单切换
在Web应用中经常会遇到frame/iframe表单嵌套页面的应用，WebDriver只能在一个页面上对元素识别与定位，对于frame/iframe表单内嵌页面上的元素无法直接定位。这时就需要通过switch_to.frame()方法将当前定位的主体切换为frame/iframe表单的内嵌页面中。
```html
<html>
  <body>
    ...
    <iframe id="x-URS-iframe" ...>
      <html>
         <body>
           ...
           <input name="email" >
```
126邮箱登录框的结构大概是这样子的，想要操作登录框必须要先切换到iframe表单。
```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.126.com")

driver.switch_to.frame('x-URS-iframe')
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("username")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()

driver.quit()
switch_to.frame() 默认可以直接取表单的id 或name属性。如果iframe没有可用的id和name属性，则可以通过下面的方式进行定位。
```
……
#先通过xpth定位到iframe
```python
xf = driver.find_element_by_xpath('//*[@id="x-URS-iframe"]')
```
#再将定位对象传给switch_to.frame()方法

```python
driver.switch_to.frame(xf)
```
……
```python
driver.switch_to.parent_frame()
```
除此之外，在进入多级表单的情况下，还可以通过switch_to.default_content()跳回最外层的页面。

### 3.5 多窗口切换

在页面操作过程中有时候点击某个链接会弹出新的窗口，这时就需要主机切换到新打开的窗口上进行操作。WebDriver提供了switch_to.window()方法，可以实现在不同的窗口之间切换。 以百度首页和百度注册页为例，在两个窗口之间的切换如下图。

```python
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

# 获得百度搜索窗口句柄
sreach_windows = driver.current_window_handle

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text("立即注册").click()

# 获得当前所有打开的窗口的句柄
all_handles = driver.window_handles

# 进入注册窗口
for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to.window(handle)
        print('now register window!')
        driver.find_element_by_name("account").send_keys('username')
        driver.find_element_by_name('password').send_keys('password')
        time.sleep(2)
        # ……


driver.quit()
```

在本例中所涉及的新方法如下：

- current_window_handle：获得当前窗口句柄。
- window_handles：返回所有窗口的句柄到当前会话。
- switch_to.window()：用于切换到相应的窗口，与上一节的switch_to.frame()类似，前者用于不同窗口的切换，后者用于不同表单之间的切换。

### 3.6 警告框处理


在WebDriver中处理JavaScript所生成的alert、confirm以及prompt十分简单，具体做法是使用 switch_to.alert 方法定位到 alert/confirm/prompt，然后使用text/accept/dismiss/ send_keys等方法进行操作。

- text：返回 alert/confirm/prompt 中的文字信息。
- accept()：接受现有警告框。
- dismiss()：解散现有警告框。
- send_keys(keysToSend)：发送文本至警告框。keysToSend：将文本发送至警告框。

如下图，百度搜索设置弹出的窗口是不能通过前端工具对其进行定位的，这个时候就可以通过switch_to_alert()方法接受这个弹窗。 ![img](http://orru5lls3.bkt.clouddn.com/alert_windows.png)

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

# 鼠标悬停至“设置”链接
link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()

# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()

# 保存设置
driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(2)

# 接受警告框
driver.switch_to.alert.accept()

driver.quit()
```

通过switch_to_alert()方法获取当前页面上的警告框，并使用accept()方法接受警告框。

### 3.7 警告框处理


在WebDriver中处理JavaScript所生成的alert、confirm以及prompt十分简单，具体做法是使用 switch_to.alert 方法定位到 alert/confirm/prompt，然后使用text/accept/dismiss/ send_keys等方法进行操作。

- text：返回 alert/confirm/prompt 中的文字信息。
- accept()：接受现有警告框。
- dismiss()：解散现有警告框。
- send_keys(keysToSend)：发送文本至警告框。keysToSend：将文本发送至警告框。

如下图，百度搜索设置弹出的窗口是不能通过前端工具对其进行定位的，这个时候就可以通过switch_to_alert()方法接受这个弹窗。

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

# 鼠标悬停至“设置”链接
link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()

# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()

# 保存设置
driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(2)

# 接受警告框
driver.switch_to.alert.accept()

driver.quit()
```

通过switch_to_alert()方法获取当前页面上的警告框，并使用accept()方法接受警告框。

### 3.8 下拉框选择

有时我们会碰到下拉框，WebDriver提供了Select类来处理下拉框。 如百度搜索设置的下拉框。

```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

# 鼠标悬停至“设置”链接
driver.find_element_by_link_text('设置').click()
sleep(1)
# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()
sleep(2)

# 搜索结果显示条数
sel = driver.find_element_by_xpath("//select[@id='nr']")
Select(sel).select_by_value('50')  # 显示50条
# ……

driver.quit()
```

Select类用于定位select标签。

select_by_value() 方法用于定位下接选项中的value值。

##　4. 特殊处理
### 4.1 文件上传
对于通过input标签实现的上传功能，可以将其看作是一个输入框，即通过send_keys()指定本地文件路径的方式实现文件上传。

创建upfile.html文件，代码如下：

```html
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
<title>upload_file</title>
<link href="http://cdn.bootcss.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet" />
</head>
<body>
  <div class="row-fluid">
    <div class="span6 well">
    <h3>upload_file</h3>
      <input type="file" name="file" />
    </div>
  </div>
</body>
<script src="http://cdn.bootcss.com/bootstrap/3.3.0/css/bootstrap.min.js"></scrip>
</html>
```

通过浏览器打开upfile.html文件.

接下来通过send_keys()方法来实现文件上传。

```python
from selenium import webdriver
import os

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('upfile.html')
driver.get(file_path)

# 定位上传按钮，添加本地文件
driver.find_element_by_name("file").send_keys('D:\\upload_file.txt')

driver.quit()
```
### 4.2 cookies处理

有时候我们需要验证浏览器中cookie是否正确，因为基于真实cookie的测试是无法通过白盒和集成测试进行的。WebDriver提供了操作Cookie的相关方法，可以读取、添加和删除cookie信息。

WebDriver操作cookie的方法：

- get_cookies()： 获得所有cookie信息。
- get_cookie(name)： 返回字典的key为“name”的cookie信息。
- add_cookie(cookie_dict) ： 添加cookie。“cookie_dict”指字典对象，必须有name 和value 值。
- delete_cookie(name,optionsString)：删除cookie信息。“name”是要删除的cookie的名称，“optionsString”是该cookie的选项，目前支持的选项包括“路径”，“域”。
- delete_all_cookies()： 删除所有cookie信息。

下面通过get_cookies()来获取当前浏览器的cookie信息。

```python
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")

# 获得cookie信息
cookie= driver.get_cookies()
# 将获得cookie的信息打印
print(cookie)

driver.quit()
```

从执行结果可以看出，cookie数据是以字典的形式进行存放的。知道了cookie的存放形式，接下来我们就可以按照这种形式向浏览器中写入cookie信息。

```python
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")

# 向cookie的name 和value中添加会话信息
driver.add_cookie({'name': 'key-aaaaaaa', 'value': 'value-bbbbbb'})

# 遍历cookies中的name 和value信息并打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))

driver.quit()
```

输出结果：

======================== RESTART: =========================

```
YOUDAO_MOBILE_ACCESS_TYPE -> 1
_PREF_ANONYUSER__MYTH -> aGFzbG9nZ2VkPXRydWU=
OUTFOX_SEARCH_USER_ID -> -1046383847@218.17.158.115
JSESSIONID -> abc7qSE_SBGsVgnVLBvcu
key-aaaaaaa -> value-bbbbbb
```

从执行结果可以看到，最后一条cookie信息是在脚本执行过程中通过add_cookie()方法添加的。通过遍历得到所有的cookie信息，从而找到key为“name”和“value”的特定cookie的value。

### 4.3 js处理

虽然WebDriver提供了操作浏览器的前进和后退方法，但对于浏览器滚动条并没有提供相应的操作方法。在这种情况下，就可以借助JavaScript来控制浏览器的滚动条。WebDriver提供了execute_script()方法来执行JavaScript代码。

用于调整浏览器滚动条位置的JavaScript代码如下：

```
<!-- window.scrollTo(左边距,上边距); -->
window.scrollTo(0,450);
```

window.scrollTo()方法用于设置浏览器窗口滚动条的水平和垂直位置。方法的第一个参数表示水平的左间距，第二个参数表示垂直的上边距。其代码如下：

```python
from selenium import webdriver
from time import sleep

# 访问百度
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

# 设置浏览器窗口大小
driver.set_window_size(500, 500)

# 搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

# 通过javascript设置浏览器窗口的滚动条位置
js="window.scrollTo(100,450);"
driver.execute_script(js)
sleep(3)

driver.quit()
```

通过浏览器打开百度进行搜索，并且提前通过set_window_size()方法将浏览器窗口设置为固定宽高显示，目的是让窗口出现水平和垂直滚动条。然后通过execute_script()方法执行JavaScripts代码来移动滚动条的位置。

### 4.4 窗口截图

自动化用例是由程序去执行的，因此有时候打印的错误信息并不十分明确。如果在脚本执行出错的时候能对当前窗口截图保存，那么通过图片就可以非常直观地看出出错的原因。WebDriver提供了截图函数get_screenshot_as_file()来截取当前窗口。

```python
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(2)

# 截取当前窗口，并指定截图图片的保存位置
driver.get_screenshot_as_file("E:\\baidu_img.jpg")

driver.quit()
```

脚本运行完成后打开E盘，就可以找到baidu_img.jpg图片文件了。

### 4.5 窗口关闭

在前面的例子中我们一直使用quit()方法，其含义为退出相关的驱动程序和关闭所有窗口。除此之外，WebDriver还提供了close()方法，用来关闭当前窗口。例多窗口的处理，在用例执行的过程中打开了多个窗口，我们想要关闭其中的某个窗口，这时就要用到close()方法进行关闭了。

- close() 关闭单个窗口
- quit() 关闭所有窗口