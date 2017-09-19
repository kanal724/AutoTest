# coding=utf-8
import pandas as pd
import time
from selenium import webdriver
import numpy as np
import os
df1 = pd.read_excel("F:\\AutoTest\\Python\\XZHYttt.xlsx")   # 把excel内容读取为DataFrame对象

df2 = pd.read_excel("F:\\AutoTest\\Python\\lambor_Inputbox_XZHY.xlsx")

driver = webdriver.Firefox()  # 创建webdriver对象，调用火狐
driver.get("http://backoffice.qc.lambor.ptg/")  # 访问网站
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[2]/div/input").send_keys("TK001")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[4]/div/input").send_keys("0000aaaaAAAA")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[7]/div/input").send_keys("94qa")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[9]/button").click()
time.sleep(3)
driver.get("http://backoffice.qc.lambor.ptg/Main/Member/MemberAdd")
time.sleep(5)
'''
tips_ID = '/html/body/div[1]/div[2]/div/div/div/form/div[3]/div[2]/a'
Zd = '/div[2]/a'
Zd1 = '/span'
Z1 = '/span[1]'
Z2 = '/span[2]'

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/form/div[3]/div[1]/input").clear()
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/form/div[3]/div[1]/input").send_keys("@@")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[1]").click()

time.sleep(2)
#ddZd = driver.find_element_by_xpath(tips_ID + Zd).get_attribute("class")
#ddZ1 = driver.find_element_by_xpath(tips_ID + Z1).get_attribute("class")
#ddZ2 = driver.find_element_by_xpath(tips_ID + Z2).get_attribute("class")
dd = driver.find_element_by_xpath(tips_ID).get_attribute("class")
#print ddZd
#print ddZ1
#print ddZ2
if dd == '':
    print ""
    print driver.find_element_by_xpath(tips_ID + Zd1).get_attribute("data-original-title")
else:
    print "不报错"

#print driver.find_element_by_xpath(tips_ID + Zd + Zd1).get_attribute("data-original-title")

'''
# 获取df2中的inputbox_ID的值与相对应的tips_ID的值
for a in range(0, len(df2)):
    inputbox_ID = df2.iloc[a, 0]   # df2中inputbox_ID与tips_ID相对应的取值
    #print inputbox_ID
    tips_ID = df2.iloc[a, 1]
    #print tips_ID
    Email_results = list(df1[tips_ID])  # 由df1中相对应的tips_ID创建一个列表
    lw1 = '/html/body/div[1]/div[2]/div/div/div/form/div[1]'
    Zd = '/div[2]/a'
    Zd1 = '/span'
    Z1 = '/span[1]'
    Z2 = '/span[2]'
    cls1h = 'col-sm-4 remind_text ng-hide'
    cls2h = 'col-sm-4 remind_error ng-hide'
    cls1 = 'col-sm-4 remind_text'
    cls2 = 'col-sm-4 remind_error'
    #S1 = '/span[1]'
    #S2 = '/span[2]'
    dd = driver.find_element_by_xpath(tips_ID).get_attribute("class")
    if tips_ID == lw1:
        ddZd = driver.find_element_by_xpath(tips_ID + Zd).get_attribute("class")
        ddZ1 = driver.find_element_by_xpath(tips_ID + Z1).get_attribute("class")
        ddZ2 = driver.find_element_by_xpath(tips_ID + Z2).get_attribute("class")
        print ddZd
        print ddZ1
        print ddZ2
    else:
        print "不是第一个错误提示"
    #elif tips_ID == '/html/body/div[1]/div[2]/div/div[1]/div/form/div[3]/div[2]/a/span' :
    #    ddSd = driver.find_element_by_xpath(tips_ID).get_attribute("class")
    #    ddS1 = driver.find_element_by_xpath(tips_ID + S1).get_attribute("class")
    #    ddS2 = driver.find_element_by_xpath(tips_ID + S2).get_attribute("class")

    for index, word in enumerate(list(df1[inputbox_ID])):   # 遍历df1中inputbox_ID下的所有值
        #print word

        result = Email_results[index]
        if word is np.nan:
            print "该位置为空"
            break
        else:
            print "该位置不为空"
            driver.find_element_by_xpath(inputbox_ID).clear()  # 清空搜索框
            driver.find_element_by_xpath(inputbox_ID).send_keys(word)  # 输入关键词
            time.sleep(0.5)
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[1]").click()
            time.sleep(1.5)  # 等待
            '''
            try:
                driver.find_element_by_xpath(tips_ID)
                a = True
            except:
                a = False
            if a == False:
                result = "输入符合规范"
                print result
            '''
            print tips_ID
            print ddZd
            print ddZ1
            print ddZ2

            if tips_ID == lw1 and ddZd == '' and ddZ1 == cls1h and ddZ2 == cls2h:
                result = driver.find_element_by_xpath(tips_ID + Zd + Zd1).get_attribute("data-original-title")
                print ddZd
                print ddZ1
                print ddZ2
                print result
            elif tips_ID == lw1 and ddZd == 'ng-hide' and ddZ1 == cls1 and ddZ2 == cls2h:
                result = driver.find_element_by_xpath(tips_ID + Z1).text
                print ddZd
                print ddZ1
                print ddZ2
                print result
            elif tips_ID == lw1 and ddZd == 'ng-hide' and ddZ1 == cls1h and ddZ2 == cls2:
                result = driver.find_element_by_xpath(tips_ID + Z2).text
                print ddZd
                print ddZ1
                print ddZ2
                print result
            #elif tips_ID == '/html/body/div[1]/div[2]/div/div[1]/div/form/div[3]/div[2]/a/span' and ddSd == 'alert alert-danger prompt-csss' and ddS1 == '' and ddS2 == 'ng-hide':
                #result = driver.find_element_by_xpath(tips_ID + S1).text

            #elif tips_ID == '/html/body/div[1]/div[2]/div/div[1]/div/form/div[3]/div[2]/a/span' and ddSd == 'alert alert-danger prompt-csss' and ddS1 == 'ng-hide' and ddS2 == '':
                #result = driver.find_element_by_xpath(tips_ID + S2).text

            elif dd == '':
                result = driver.find_element_by_xpath(tips_ID + Zd1).get_attribute("data-original-title")  # 获取提示信息
                print result
            elif dd == 'ng-hide':
                result = ""
                print result

            Email_results[index] = result  # 把搜索结果写入list

            df1[tips_ID] = Email_results  # 把list写入df1相对应的tips_ID下
            #print df1[tips_ID]

df1.to_excel("F:\\AutoTest\\Python\\OUTXZHY2.xlsx", index=False)  # 把df1另存为excel
time.sleep(3)
driver.quit()
# if os.system() #先判断是否有“geckodriver.exe”(暂时没有找到一个简单的方法)
os.system('taskkill /F /IM geckodriver.exe')
