# coding=utf-8
import pandas as pd
import time
from selenium import webdriver
import numpy as np
import os
from selenium.webdriver.support.ui import Select
df1 = pd.read_excel("F:\\AutoTest\\Python\\GSRK.xlsx") # 把excel内容读取为DataFrame对象
#print (df1)
#print "执行的excel中总共有%d列数据" %len(df1.columns)
#print "执行的excel中总共有%d行数据" %len(df1)
df2 = pd.read_excel("F:\\AutoTest\\Python\\lambor_Inputbox_GSRK.xlsx")
#print (df2)
#print "ID的excel中总共有%d列数据" %len(df2.columns)
#print "ID的excel中总共有%d行数据" %len(df2)
driver = webdriver.Firefox()  # 创建webdriver对象，调用火狐
driver.get("http://bkweb.qc.lambor.ptg/")  # 访问网站
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[2]/div/input").send_keys("MasterTester24")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[4]/div/input").send_keys("123456")
time.sleep(8)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[9]/button").click()
time.sleep(3)
driver.get("http://bkweb.qc.lambor.ptg/Main/System/SystemCompanyMoneyAdd")
time.sleep(8)





Select(driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/form[1]/div[4]/div[1]/div[1]/div[1]/select')).select_by_index('1') #省下拉框切换成value=1的值
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form[1]/div[4]/div[1]/div[1]/div[2]/select').click() #点击城市的下拉框


driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[1]").click() #点击空白处

dd = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form[1]/div[4]/div[1]/div[2]/a').get_attribute("class") #赋值“X”提示的class值

if dd == '':
    result = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form[1]/div[4]/div[1]/div[2]/a/span').get_attribute("data-original-title")  # 获取提示信息
    print result
# print result
elif dd == 'ng-hide':
    result = "没有错误"
    print result


# 获取df2中的inputbox_ID的值与相对应的tips_ID的值
'''for a in range(0,len(df2)):
    inputbox_ID = df2.iloc[a,0]   # df2中inputbox_ID与tips_ID相对应的取值
    #print inputbox_ID等待·
    tips_ID = df2.iloc[a,1]
    #print tips_ID
    Email_results = list(df1[tips_ID])  # 由df1中相对应的tips_ID创建一个列表

    for index, word in enumerate(list(df1[inputbox_ID])): # 遍历df1中inputbox_ID下的所有值
        #print word

        result = Email_results[index]
        if word is np.nan:
            print "该位置为空"
            break
        else:
            print "该位置不为空"
            driver.find_element_by_xpath(inputbox_ID).clear()  # 清空搜索框
            driver.find_element_by_xpath(inputbox_ID).send_keys(word)  # 输入关键词
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div[1]").click()
            time.sleep(1)  # 等待
            dd = driver.find_element_by_xpath(tips_ID).get_attribute("class")
            c = '/span'
            m = tips_ID+c
            try:
                driver.find_element_by_xpath(m)
                a = True
            except:
                a = False
            if a == False:
                result = "输入符合规范"
                print result
            elif a == True and dd == '':
                result = driver.find_element_by_xpath(m).get_attribute("data-original-title")  # 获取提示信息
                #print result
            elif a == True and dd == 'ng-hide':
                result = ""
            Email_results[index] = result  # 把搜索结果写入list

            df1[tips_ID] = Email_results  # 把list写入df1相对应的tips_ID下
            #print df1[m]

df1.to_excel("F:\\AutoTest\\Python\\GSRKOUT.xlsx", index=False)  # 把df1另存为excel
'''
time.sleep(8)
driver.quit()
# if os.system() #先判断是否有“geckodriver.exe”(暂时没有找到一个简单的方法)
os.system('taskkill /F /IM geckodriver.exe')