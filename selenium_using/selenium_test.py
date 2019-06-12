#coding:utf8
#author:katherinelove
#copyright:shuai

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()

driver.get("http://www.baidu.com")

#elem=driver.find_element_by_id("kw")
#elem.send_keys(u"网络爬虫")
#elem.clear()

#elem.send_keys(Keys.ENTER)
print(driver.page_source)

time.sleep(3)
driver.close()