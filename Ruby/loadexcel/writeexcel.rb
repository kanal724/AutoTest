require 'rspec'
require 'rubygems'
require 'selenium-webdriver'
require 'win32ole'

		#~ dr = Selenium::WebDriver.for :ff
		#~ url='https://passport.cnblogs.com/register.aspx'
		#~ dr.navigate.to url
		#~ sleep 3
		excel = WIN32OLE.new("excel.application")
		filepath="D:\\loadexcel\\Data.xlsx" #路径用两斜杠
		workbook = excel.workbooks.open(filepath)
		worksheet=workbook.worksheets(1)
		worksheet.select
		#worksheet=workbook.worksheets("sheet name") 打开表名
		#读取excel文件
		#~ row=1
		
		#~ userNameIpt = dr.find_element(:id => 'ctl00_holderLeft_txt_email')
		#~ userNameIpt.send_keys worksheet.range("a#{row}").value.to_s
			
		#~ sleep 1
			
		#~ blank= dr.find_element(:class => 'line_tip')
		#~ blank.click
			
		#~ sleep 1
		
		#~ msgopt= dr.find_element(:id,'tip_email').text
		#~ puts msgopt.text worksheet.range("c#{row}").value.to_s
		#~ worksheet.range("c#{row}").value = msgopt
		worksheet.range('d2').value = ['s''h']
		
		workbook.save
		
		system ("tskill EXCEL")
		
		