# coding=utf-8
import pandas as pd
import time
from selenium import webdriver
import os
#import numpy as np

df1 = pd.read_excel("F:\\AutoTest\\Python\\501.xlsx")  # 把excel内容读取为DataFrame对象
# print (df1)
# print "执行的excel中总共有%d列数据" %len(df1.columns)
# print "执行的excel中总共有%d行数据" %len(df1)
df2 = pd.read_excel("F:\\AutoTest\\Python\\Range_Inputbox_ID.xlsx")
# print df2.iloc[1,0]
# print (df2)
# print "ID的excel中总共有%d列数据" %len(df2.columns)
# print "ID的excel中总共有%d行数据" %len(df2)
# ldf=len(df2)
driver = webdriver.Firefox()  # 创建webdriver对象，调用火狐
driver.get("https://passport.cnblogs.com/register.aspx?ReturnUrl=http://home.cnblogs.com")  # 访问网站
# 获取df2中的inputbox_ID的值与相对应的tips_ID的值
for a in range(0, len(df2)):

    # print a
    inputbox_ID1 = df2.iloc[a, 0]  # df2中inputbox_ID与tips_ID相对应的取值
    # print inputbox_ID1
    inputbox_ID2 = df2.iloc[a, 1]
    # print inputbox_ID2
    tips_ID1 = df2.iloc[a, 2]
    tips_ID2 = df2.iloc[a, 3]
    # print tips_ID
    Email_results1 = list(df1[tips_ID1])  # 由df1中相对应的tips_ID创建一个列表
    Email_results2 = list(df1[tips_ID2])
    ldi1 = list(df1[inputbox_ID1])
    ldi2 = list(df1[inputbox_ID2])
    #if pd.isnull(inputbox_ID) #需要增加判断当单元格无数据时应该重新循环（未添加）
        #continue

    def Password(word):

        driver.find_element_by_id(inputbox_ID1).clear()  # 清空搜索框
        driver.find_element_by_id(inputbox_ID1).send_keys(word)  # 输入关键词
        driver.find_element_by_id("registerForm").click()
        time.sleep(1)  # 等待
        result1 = driver.find_element_by_id(tips_ID1).text  # 获取提示信息
        # print (result)
        return result1

    def CPassword(word):
        driver.find_element_by_id(inputbox_ID2).clear()  # 清空搜索框
        driver.find_element_by_id(inputbox_ID2).send_keys(word)  # 输入关键词
        driver.find_element_by_id("registerForm").click()
        time.sleep(1)  # 等待
        result2 = driver.find_element_by_id(tips_ID2).text  # 获取提示信息
        return result2

    for index, word in enumerate(ldi1):  # 遍历df1中inputbox_ID下的所有值
        Email_results1[index] = Password(word)  # 把搜索结果写入list
        df1[tips_ID1] = Email_results1  # 把list写入df1相对应的tips_ID下
        # print df1[tips_ID]
        for index, word in enumerate(ldi2):  # 遍历df1中inputbox_ID下的所有值
            Email_results2[index] = CPassword(word)  # 把搜索结果写入list
            df1[tips_ID2] = Email_results2
            # print df1[tips_ID]


'''
    def CPassword(word):
        driver.find_element_by_id(inputbox_ID2).clear()  # 清空搜索框
        driver.find_element_by_id(inputbox_ID2).send_keys(word)  # 输入关键词
        driver.find_element_by_id("registerForm").click()
        time.sleep(1)  # 等待
        result2 = driver.find_element_by_id(tips_ID2).text  # 获取提示信息
        return result2
        # else :
        # print "dd"
    for index, word in enumerate(list(df1[inputbox_ID2])):  # 遍历df1中inputbox_ID下的所有值
        Email_results2[index] = CPassword(word)  # 把搜索结果写入list
        df1[tips_ID2] = Email_results2
        # print df1[tips_ID]
'''

df1.to_excel("F:\\AutoTest\\Python\\503.xlsx", index=False)  # 把df1另存为excel

time.sleep(3)
driver.quit()
# if os.system() #先判断是否有“geckodriver.exe”(暂时没有找到一个简单的方法)
os.system('taskkill /F /IM geckodriver.exe')

# os.system('taskkill /F /IM geckodriver.exe')
# df1.to_excel("F:\\AutoTest\\Python\\403.xlsx", index=False)  # 把df1另存为excel
