#元素的交互操作
#对获取到的元素调用交互方法

#_*_coding: utf-8_*_
from selenium import webdriver
import time
browser=webdriver.Chrome()
browser.get("https://www.taobao.com")
input=browser.find_element_by_id("q")
input.send_keys("iPhone")
time.sleep(10)
input.clear()
input.send_keys("iPad")
button=browser.find_element_by_class_name("btn-search")
button.click()
time.sleep(10)
browser.close()