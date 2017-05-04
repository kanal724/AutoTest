# coding=utf-8
import pandas as pd
import time
from selenium import webdriver
df1 = pd.read_excel("D:\\python test excel\\401.xlsx") # 把excel内容读取为DataFrame对象
print (df1)
print "执行的excel中总共有%d列数据" %len(df1.columns)
print "执行的excel中总共有%d行数据" %len(df1)
df2 = pd.read_excel("D:\\python test excel\\register_Inputbox_ID.xlsx")
print (df2)
print "ID的excel中总共有%d列数据" %len(df2.columns)
print "ID的excel中总共有%d行数据" %len(df2)
driver = webdriver.Firefox() # 创建webdriver对象，调用火狐
driver.get("https://passport.cnblogs.com/register.aspx?ReturnUrl=http://home.cnblogs.com") # 访问网站
for a in range(1,len(df1.columns),2):
    print a
    Email_results = list(df1.iloc[:, a])  # 由df的第二列创建个列表
    def Email(word):
        driver.find_element_by_id("ctl00_holderLeft_txt_email").clear()  # 清空搜索框
        driver.find_element_by_id("ctl00_holderLeft_txt_email").send_keys(word)  # 输入关键词
        driver.find_element_by_id("aspnetForm").click()
        time.sleep(1)  # 等待
        result = driver.find_element_by_id("tip_email").text  # 获取提示信息
        # print (result)
        return result
    b = a-1
    print b
    for index, word in enumerate(list(df1.iloc[:, b])):  # 遍历
        Email_results[index] = Email(word)  # 把搜索结果写入list
        df1.iloc[:, a] = Email_results  # 把list写入df
    #print (df1)
df1.to_excel("D:\\python test excel\\403.xlsx", index=False)  # 把df另存为excel
# driver.quit()