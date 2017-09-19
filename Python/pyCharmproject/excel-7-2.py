# coding=utf-8
import pandas as pd
import time
from selenium import webdriver
import os

df1 = pd.read_excel("F:\\AutoTest\\Python\\601.xlsx")  # 把excel内容读取为DataFrame对象
# print (df1)
# print "执行的excel中总共有%d列数据" %len(df1.columns)
# print "执行的excel中总共有%d行数据" %len(df1)
df2 = pd.read_excel("F:\\AutoTest\\Python\\lambor_Inputbox_ID.xlsx")
# print df2.iloc[1,0]
# print (df2)
# print "ID的excel中总共有%d列数据" %len(df2.columns)
# print "ID的excel中总共有%d行数据" %len(df2)
# ldf=len(df2)
driver = webdriver.Firefox()  # 创建webdriver对象，调用火狐
driver.get("http://bkweb.qc.lambor.ptg/")  # 访问网站
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[2]/div/input").send_keys("MasterTester24")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[4]/div/input").send_keys("123456")
time.sleep(8)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/fieldset/div[9]/button").click()
time.sleep(3)
driver.get("http://bkweb.qc.lambor.ptg/Main/System/SystemBonusActivityAdd")
time.sleep(8)
# 获取df2中的inputbox_ID的值与相对应的tips_ID的值
for a in range(0, len(df2)):

    # print a
    inputbox_ID = df2.iloc[a, 0]  # df2中inputbox_ID与tips_ID相对应的取值
    # print inputbox_ID
    tips_ID = df2.iloc[a, 1]
    # print tips_ID
    Email_results = list(df1[tips_ID])  # 由df1中相对应的tips_ID创建一个列表


    def DisplayName(word):
        # if word == None #需要增加判断当单元格无数据时应该重新循环（未添加）
        # print df2.iloc[10,1]

        driver.find_element_by_xpath(inputbox_ID).clear()  # 清空搜索框
        driver.find_element_by_xpath(inputbox_ID).send_keys(word)  # 输入关键词
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div").click()
        time.sleep(1)  # 等待
        result = driver.find_element_by_xpath(tips_ID).text  # 获取提示信息
        # print (result)
        return result

        # else :
        # print "dd"


    for index, word in enumerate(list(df1[inputbox_ID])):  # 遍历df1中inputbox_ID下的所有值
        Email_results[index] = DisplayName(word)  # 把搜索结果写入list
        df1[tips_ID] = Email_results  # 把list写入df1相对应的tips_ID下
        # print df1[tips_ID]

df1.to_excel("F:\\AutoTest\\Python\\603.xlsx", index=False)  # 把df1另存为excel

time.sleep(3)
driver.quit()
# if os.system() #先判断是否有“geckodriver.exe”(暂时没有找到一个简单的方法)
os.system('taskkill /F /IM geckodriver.exe')

# os.system('taskkill /F /IM geckodriver.exe')
# df1.to_excel("F:\\AutoTest\\Python\\403.xlsx", index=False)  # 把df1另存为excel
