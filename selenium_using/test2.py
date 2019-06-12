#访问页面

from selenium import webdriver
browser=webdriver.Chrome()
browser.get("http://www.taobao.com")
print(browser.page_source)
browser.close()