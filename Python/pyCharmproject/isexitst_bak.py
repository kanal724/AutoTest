# coding:utf-8
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

'''
一、find_elements方法判断

1.find_elements方法是查找页面上所有相同属性的方法，这个方法其实非常好用，能熟练掌握技巧的不多，小编这次就发挥它的功效

2.由于元素定位的方法很多，所以判断的时候定位方法不统一也比较麻烦，这里我选择css定位（有喜欢xpath的同学可以自己用xpath语法）

3.写一个函数判断，找到就返回Ture,没找到就返回False(或者不止一个)
'''


def is_element_exist(css):
    s = driver.find_elements_by_css_selector(css_selector=css)
    if len(s) == 0:
        print "元素未找到:%s"%css
        return False
    elif len(s) == 1:
        return True
    else:
        print "找到%s个元素：%s"%(len(s),css)
        return False

'''
二、百度输入框为例

1.判断id为kw的元素是否存在

2.判断标签为input元素是否存在

3.判断id为xxx元素是否存在
'''

# 判断页面上有无id为kw的元素
if is_element_exist("#kw"):
    driver.find_element_by_id("kw").send_keys("yoyoketang")
# 判断页面有无标签为input元素
if is_element_exist("input"):
    driver.find_element_by_tag_name("input").send_keys("yoyoketang")
# 判断页面有无id为xxx的元素
if is_element_exist("xxx"):
    driver.find_element_by_id("xxx").send_keys("yoyoketang")

'''
三、捕获异常方法

1.如果没找到元素会抛异常，返回False

2.如果找到元素就返回Ture

3.但是这个方法有个弊端，如果页面上存在多个一样元素，也会返回Ture的（也就是说只要页面上有元素就返回Ture，不管几个）
'''


def isElementExist(css):
    try:
        driver.find_element_by_css_selector(css)
        return True
    except:
        return False

print isElementExist("#xxx")