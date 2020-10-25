#-*- coding = utf-8 -*-
#@Time : 2020-10-25 15:24
#@Author : Jiancong Zhu
#@Email : 643601464@qq.com
#@File : release.py
#@Software: PyCharm

myUsername=r'' #在此输入你的学号
myPassword=r'' #在此输入你的姓名
baseUrl=r'https://selfreport.shu.edu.cn/' #默认的每日两报地址
driverUrl = r"E:\Edgedriver\msedgedriver.exe" #浏览器驱动，这里以Edge示例，不同的浏览器可以去个官网下载
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys # 或许没用上
import time
import random

def main():
    print("Hello,")
    driver = webdriver.Edge(driverUrl)
    driver.get(baseUrl)
    driver.find_element_by_id('username')
    search_username = driver.find_element_by_id('username')
    search_username.send_keys(myUsername)
    search_password = driver.find_element_by_id('password')
    search_password.send_keys(myPassword)
    driver.find_element_by_id('submit').click()

    for date in range(19,26,1):#在此修改你想实现的日期，左闭右开，如这里为[19,26)，即19至25号
        for item in ['晨报','晚报']:
            # print("Hello, world!")
            # driver = webdriver.Edge(driverUrl)
            # driver.get(baseUrl)
            # driver.find_element_by_id('username')
            # search_username = driver.find_element_by_id('username')
            # search_username.send_keys(myUsername)
            # search_password = driver.find_element_by_id('password')
            # search_password.send_keys(myPassword)
            # driver.find_element_by_id('submit').click()

            # 进入报送历史：
            driver.find_element_by_id('lbReportHistory').click()

            # 点击对应的天数：
            object = str(date) + item
            driver.find_element_by_partial_link_text(object).click()

            # 勾选承诺项：
            driver.find_element_by_id("p1_ChengNuo-inputEl-icon").click()

            # 填写体温，随机在36.0-37.0之间
            search_temperature = driver.find_element_by_id("p1_TiWen-inputEl")
            temperature = str(random.randint(360, 370) / 10)
            search_temperature.send_keys(temperature)

            # 勾选状态"良好"
            element = driver.find_element_by_id("fineui_0-inputEl")
            driver.execute_script("arguments[0].click();", element)

            # 当天随申码颜色："绿色"
            driver.find_element_by_id("fineui_7-inputEl-icon").click()
            element = driver.find_element_by_id('fineui_7-inputEl-icon')
            driver.execute_script("arguments[0].click();", element)
            # webdriver.ActionChains(driver).move_to_element(element).click(element).perform()

            # 明天是否到食堂就餐："早餐，中餐，晚餐"
            element = driver.find_element_by_id('fineui_8-inputEl-icon')
            driver.execute_script("arguments[0].click();", element)
            element = driver.find_element_by_id('fineui_9-inputEl-icon')
            driver.execute_script("arguments[0].click();", element)
            element = driver.find_element_by_id('fineui_10-inputEl-icon')
            driver.execute_script("arguments[0].click();", element)

            # 以下操作无法实现，原因应该是元素定位相互覆盖。
            # driver.find_element_by_id("fineui_8-inputEl-icon").click()
            # driver.find_element_by_id("fineui_9-inputEl-icon").click()
            # driver.find_element_bu_id("fineui_10-inputEl-icon").click()
            # driver.find_element_by_id("p1_ctl00_btnSubmit").click()

            # 点击提交
            element = driver.find_element_by_id("p1_ctl00_btnSubmit")
            driver.execute_script("arguments[0].click();", element)
            time.sleep(1)
            # 点击确认
            element = driver.find_element_by_id("fineui_14")
            driver.execute_script("arguments[0].click();", element)
            time.sleep(3)
            element = driver.find_element_by_id("fineui_19")
            # element = driver.find_element_by_class_name("f-btn-text")
            driver.execute_script("arguments[0].click();", element)
            time.sleep(1)

    driver.quit()
    print("world!") # 输出Hello,world! 完美的结束

if __name__ == "__main__": #当程序执行时
    main() #开始