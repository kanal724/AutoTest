# coding=utf-8
import time
from selenium import webdriver
driver = webdriver.Firefox()  # 创建webdriver对象，调用火狐
driver.get("http://backoffice.qc.lambor.ptg/")  # 访问网站
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[2]/div/input").send_keys("yingzi1-1")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[4]/div/input").send_keys("123456")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[7]/div/input").send_keys("94qa")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[9]/button").click()
time.sleep(5)