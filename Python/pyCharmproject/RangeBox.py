# coding=utf-8

from selenium import webdriver
import time
import os
import pandas as pd


driver = webdriver.Firefox() # 创建webdriver对象，调用火狐
driver.get("http://192.168.200.211/share/Lambo/membership_query.html") # 访问网站


driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div[4]/div/div/input[1]").send_keys("2000")
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div[4]/div/div/input[2]").send_keys("1000")
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div[4]/div").click()
tips = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div[4]/div").text
print tips

time.sleep(2)
driver.quit()

os.system('taskkill /F /IM geckodriver.exe')
