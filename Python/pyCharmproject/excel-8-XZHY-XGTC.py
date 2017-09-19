# coding=utf-8
import pandas as pd
import time
from selenium import webdriver
import numpy as np
import os
df1 = pd.read_excel("F:\\AutoTest\\Python\\XZHY-XGTC.xlsx") # 把excel内容读取为DataFrame对象
#print (df1)
#print "执行的excel中总共有%d列数据" %len(df1.columns)
#print "执行的excel中总共有%d行数据" %len(df1)
df2 = pd.read_excel("F:\\AutoTest\\Python\\lambor_Inputbox_XZHY-XGTC.xlsx")
#print (df2)
#print "ID的excel中总共有%d列数据" %len(df2.columns)
#print "ID的excel中总共有%d行数据" %len(df2)
driver = webdriver.Firefox()  # 创建webdriver对象，调用火狐
driver.get("http://backoffice.qc.lambor.ptg/")  # 访问网站
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[2]/div/input").send_keys("TK001")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[4]/div/input").send_keys("0000aaaaAAAA")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[7]/div/input").send_keys("94qa")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[9]/button").click()
time.sleep(3)
driver.get("http://backoffice.qc.lambor.ptg/Main/Member/MemberShipQuery/")
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[3]/a").click()
time.sleep(20)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[3]/a[4]").click()
time.sleep(3)
# 获取df2中的inputbox_ID的值与相对应的tips_ID的值
for a in range(0,len(df2)):
    inputbox_ID = df2.iloc[a,0]   # df2中inputbox_ID与tips_ID相对应的取值
    #print inputbox_ID
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
            driver.find_element_by_xpath("//*[@id=\"myModal_editmember\"]/div[2]/div/div").click()
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
            elif a == True and dd == 'errorinfo':
                result = driver.find_element_by_xpath(tips_ID).get_attribute("data-original-title")  # 获取提示信息
                #print result
            elif a == True and dd == 'errorinfo ng-hide':
                result = ""
            Email_results[index] = result  # 把搜索结果写入list

            df1[tips_ID] = Email_results  # 把list写入df1相对应的tips_ID下
            #print df1[m]

df1.to_excel("F:\\AutoTest\\Python\\OUTXZHY-XGTC.xlsx", index=False)  # 把df1另存为excel

time.sleep(3)
driver.quit()
# if os.system() #先判断是否有“geckodriver.exe”(暂时没有找到一个简单的方法)
os.system('taskkill /F /IM geckodriver.exe')
