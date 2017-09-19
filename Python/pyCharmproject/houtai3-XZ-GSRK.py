# coding=utf-8
# 公司入款新增
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import numpy as np
#import houtai1
from selenium.webdriver.support.ui import Select
from login import *
df1 = pd.read_excel("F:\\AutoTest\\Python\\create GSRK manager_inputbox.xlsx",sheetname='xin') # 把excel内容读取为DataFrame对象
#print (df1)

#print "执行的excel中总共有%d列数据" %len(df1.columns)
#print "执行的excel中总共有%d行数据" %len(df1)
#df2 = pd.read_excel("E:\\python test excel\\create BS manager_inputbox.xlsx",sheetname='inputbox_name')
#print (df2)
#print "ID的excel中总共有%d列数据" %len(df2.columns)
#print "ID的excel中总共有%d行数据" %len(df2)
time.sleep(3)
driver.get("http://backoffice.qc.lambor.ptg/Main/System/SystemCompanyMoneyAdd")
time.sleep(2)
m = len(df1.columns)
print m
n = len(df1)
print n
for a in range(2,m):
    for b in range(0,n):
        inputbox = df1.iloc[b,1]
        print inputbox
        word = df1.iloc[b, a]
        print word
        if word is np.nan:
            pass
        else:
            if inputbox <> '/html/body/div[1]/div[2]/div/div/div/form[1]/div[4]/div[1]/div[1]/div[1]/select' and inputbox <> '/html/body/div[1]/div[2]/div/div/div/form[1]/div[4]/div[1]/div[1]/div[2]/select' and inputbox <> '/html/body/div[1]/div[2]/div/div/div/form[1]/div[4]/div[1]/div[1]/div[3]/select':
                driver.find_element_by_xpath(inputbox).clear()  # 清空搜索框
                driver.find_element_by_xpath(inputbox).click()
                driver.find_element_by_xpath(inputbox).send_keys(word)  # 输入关键词
            elif inputbox == '/html/body/div[1]/div[2]/div/div/div/form[1]/div[4]/div[1]/div[1]/div[1]/select' :
                Select(driver.find_element_by_xpath(inputbox)).select_by_index(word)
                time.sleep(2)
            elif inputbox == '/html/body/div[1]/div[2]/div/div/div/form[1]/div[4]/div[1]/div[1]/div[2]/select' :
                Select(driver.find_element_by_xpath(inputbox)).select_by_index(word)
                time.sleep(2)
            elif inputbox == '/html/body/div[1]/div[2]/div/div/div/form[1]/div[4]/div[1]/div[1]/div[3]/select' :
                Select(driver.find_element_by_xpath(inputbox)).select_by_index(word)
                time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form[2]/div[3]/div/button').click()
    time.sleep(3)
    driver.get("http://backoffice.qc.lambor.ptg/Main/System/SystemCompanyMoneyAdd")
    time.sleep(3)
'''         elif inputbox == 'inlineRadioOptions':
                if word == u'男':
                    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/form[2]/div[1]/div/label[1]/input").click()
                elif word == u'女':
                    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/form[2]/div[1]/div/label[2]/input").click()

    driver.refresh()
    time.sleep(4)
'''
'''now_handle = driver.current_window_handle
print now_handle'''
'''time.sleep(10)
driver.find_element_by_name("Acct").send_keys("tetfe12321")
#driver.find_element_by_name("UserName").send_keys("rewwrwe")
driver.find_element_by_name("Phone").send_keys("12321343443")
time.sleep(3)'''
# 点击确定按钮
#driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form[2]/div[3]/div/button').click()
#print driver.find_element_by_xpath('//*[@id="ModelErrorInput"]/div[2]/div/div[2]').text
#time.sleep(5)
'''if driver.find_element_by_id("ModelErrorInput").is_displayed() is True:
    print "新增失败"
elif driver.find_element_by_link_text("新增管理人员").is_displayed() is True:
    print "新增成功"'''
'''aaa = driver.find_element_by_id("ModelErrorInput").is_displayed()
print aaa
if aaa == 'True':
    print "新增失败"
elif aaa == 'Flase':
    print "新增成功"'''

'''mmm = (By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/a')
try:
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located(mmm))
    print "新增成功"
finally:
    print "新增失败"
all_handle = driver.current_window_handle
for handle in all_handle:
    print handle
    if handle != now_handle:
        driver.switch_to_window(handle)
        print driver.find_element_by_xpath('//*[@id="ModelErrorInput"]/div[2]/div/div[2]').text'''



# //*[@id="ModelErrorInput"]/div[2]/div




