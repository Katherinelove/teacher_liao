#交互动作
#把动作附加到交互链中

#_*_coding: utf-8_*_
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.alert import Alert
browser=webdriver.Chrome()
url="http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
browser.get(url)
#切换到目标元素所在的frame
browser.switch_to.frame("iframeResult")
#确定拖拽目标的起点
source=browser.find_element_by_id("draggable")
#确定拖拽目标的终点
target=browser.find_element_by_id("droppable")
#形成动作链
actions=ActionChains(browser)
actions.drag_and_drop(source,target)
#执行
actions.perform()
'''
1.先用switch_to_alert()方法切换到alert弹出框上
2.可以用text方法获取弹出的文本 信息
3.accept()点击确认按钮
4.dismiss()相当于点右上角x，取消弹出框
'''
t=browser.switch_to_alert()
print(t.text)
t.accept()
time.sleep(10)
browser.close()