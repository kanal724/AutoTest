# coding=utf-8
#新增会员-手机正则
import pandas as pd
import time
from selenium import webdriver
import numpy as np
import os
df1 = pd.read_excel("F:\\AutoTest\\Python\\XZDL_SJ.xlsx")   # 把excel内容读取为DataFrame对象

df2 = pd.read_excel("F:\\AutoTest\\Python\\lambor_Inputbox_XZDL_SJ.xlsx")

driver = webdriver.Firefox()  # 创建webdriver对象，调用火狐
driver.get("http://50011.backoffice.qc.lambor.ptg/")  # 访问网站
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[2]/div/input").send_keys("sadmin4")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[4]/div/input").send_keys("123456")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[6]/div[1]/input").send_keys("94qa")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[8]/button").click()
time.sleep(3)
driver.get("http://50011.backoffice.qc.lambor.ptg/Main/Agent/AgentAdd")
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
    '''lw1 = '/html/body/div[1]/div[2]/div/div/div/form/div[1]'
    lwem = '/html/body/div[1]/div[2]/div/div/div/form/div[7]/div[2]'
    Zd = '/div[2]/a'
    Zd1 = '/span'
    Z1 = '/span[1]'
    Z2 = '/span[2]'
    Y1 = '/a[1]'
    Y2 = '/a[2]'
    cls1h = 'col-sm-4 remind_text ng-hide'
    cls2h = 'col-sm-4 remind_error ng-hide'
    cls1 = 'col-sm-4 remind_text'
    cls2 = 'col-sm-4 remind_error'  '''
    clsn = 'ng-hide'
    #S1 = '/span[1]'
    #S2 = '/span[2]'

    #elif tips_ID == '/html/body/div[1]/div[2]/div/div[1]/div/form/div[3]/div[2]/a/span' :
    #    ddSd = driver.find_element_by_xpath(tips_ID).get_attribute("class")
    #    ddS1 = driver.find_element_by_xpath(tips_ID + S1).get_attribute("class")
    #    ddS2 = driver.find_element_by_xpath(tips_ID + S2).get_attribute("class")

    for index, word in enumerate(list(df1[inputbox_ID])):   # 遍历df1中inputbox_ID下的所有值
        #print word

        result = Email_results[index]
        if word is np.nan:
            print "该栏位未输入数据"
            break
        else:
            print "该栏位已输入数据"
            driver.find_element_by_xpath(inputbox_ID).clear()  # 清空搜索框
            driver.find_element_by_xpath(inputbox_ID).send_keys(word)  # 输入关键词
            time.sleep(1)  # 等待
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div/div[1]").click()
            time.sleep(1)  # 等待
            '''if tips_ID == lw1:
                ddZd = driver.find_element_by_xpath(tips_ID + Zd).get_attribute("class")
                ddZ1 = driver.find_element_by_xpath(tips_ID + Z1).get_attribute("class")
                ddZ2 = driver.find_element_by_xpath(tips_ID + Z2).get_attribute("class")
            elif tips_ID == lwem:
                ddY1 = driver.find_element_by_xpath(tips_ID + Y1).get_attribute("class")
                ddY2 = driver.find_element_by_xpath(tips_ID + Y2).get_attribute("class")
            else:
                dd = driver.find_element_by_xpath(tips_ID).get_attribute("class")

            if tips_ID == lw1 and ddZd == '' and ddZ1 == cls1h and ddZ2 == cls2h:
                result = driver.find_element_by_xpath(tips_ID + Zd + Zd1).get_attribute("data-original-title")
                print result
            elif tips_ID == lw1 and ddZd == 'ng-hide' and ddZ1 == cls1 and ddZ2 == cls2h:
                result = driver.find_element_by_xpath(tips_ID + Z1).text
                print result
            elif tips_ID == lw1 and ddZd == 'ng-hide' and ddZ1 == cls1h and ddZ2 == cls2:
                result = driver.find_element_by_xpath(tips_ID + Z2).text
                print result
            elif tips_ID == lwem and ddY1 == '' and ddY2 == 'ng-hide':
                result = driver.find_element_by_xpath(tips_ID + Y1 + Zd1).get_attribute("data-original-title")
                print result
            elif tips_ID == lwem and ddY1 == 'ng-hide' and ddY2 == '':
                result = driver.find_element_by_xpath(tips_ID + Y2 + Zd1).get_attribute("data-original-title")
                print result
            #elif tips_ID == '/html/body/div[1]/div[2]/div/div[1]/div/form/div[3]/div[2]/a/span' and ddSd == 'alert alert-danger prompt-csss' and ddS1 == '' and ddS2 == 'ng-hide':
                #result = driver.find_element_by_xpath(tips_ID + S1).text
            #elif tips_ID == '/html/body/div[1]/div[2]/div/div[1]/div/form/div[3]/div[2]/a/span' and ddSd == 'alert alert-danger prompt-csss' and ddS1 == 'ng-hide' and ddS2 == '':
                #result = driver.find_element_by_xpath(tips_ID + S2).text
            elif tips_ID != lwem and tips_ID != lw1 and dd == '':
                result = driver.find_element_by_xpath(tips_ID + Zd1).get_attribute("data-original-title")  # 获取提示信息
                print result
            elif tips_ID != lwem and tips_ID != lw1 and dd == 'ng-hide':
                result = ""
                print result'''

            dd = driver.find_element_by_xpath(tips_ID).get_attribute("class")

            if dd == '':
                result = driver.find_element_by_xpath(tips_ID + "/span").get_attribute("data-original-title")
                print result
            elif dd == clsn:
                result = ""
                print "(无提示)"

            Email_results[index] = result  # 把搜索结果写入list

            df1[tips_ID] = Email_results  # 把list写入df1相对应的tips_ID下

df1.to_excel("F:\\AutoTest\\Python\\OUTXZDL_SJ.xlsx", index=False)  # 把df1另存为excel
time.sleep(3)
driver.quit()
# if os.system() #先判断是否有“geckodriver.exe”(暂时没有找到一个简单的方法)
os.system('taskkill /F /IM geckodriver.exe')