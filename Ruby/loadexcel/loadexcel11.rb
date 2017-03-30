require 'rubygems'
require 'selenium-webdriver'
require 'win32ole'
dr = Selenium::WebDriver.for :ff
url='http://email.163.com/'
dr.navigate.to url
sleep 3
excel = WIN32OLE.new("excel.application")
filepath="D:\\loadexcel\\Data.xlsx" #路径用两斜杠
workbook = excel.workbooks.open(filepath)
worksheet=workbook.worksheets(1)
#worksheet=workbook.worksheets("sheet name") 打开表名
#读取excel文件
row=1
while worksheet.range("a#{row}").value
   #选择帐号，把第一列的值做为帐号
   userNameIpt = dr.find_element(:id => 'userNameIpt')
   userNameIpt.send_keys worksheet.range("a#{row}").value.to_s
   #选择密码，将第二列值做为密码
   pwdInput= dr.find_element(:id => 'pwdInput')
   pwdInput.send_keys worksheet.range("b#{row}").value.to_s
   #单击登录按钮
   btnSubmit= dr.find_element(:id => 'btnSubmit')
   btnSubmit.click
   row+=1
   
   userNameIpt.clear()
   pwdInput.clear()
   
   sleep 1
 end