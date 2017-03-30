require 'rspec'
require 'rubygems'
require 'selenium-webdriver'
require 'win32ole'

		#~ dr = Selenium::WebDriver.for :ff
		#~ url='https://passport.cnblogs.com/register.aspx'
		#~ dr.navigate.to url
		#~ sleep 3
		excel = WIN32OLE.new("excel.application")
		filepath="F:\\autotest\\ruby\\loadexcel\\Data.xlsx" #路径用两斜杠
		workbook = excel.workbooks.open(filepath)
		worksheet=workbook.worksheets(1)
		worksheet.select
		#worksheet=workbook.worksheets("sheet name") 打开表名
		#读取excel文件
		row=1
		
		#~ userNameIpt = dr.find_element(:id => 'ctl00_holderLeft_txt_email')
		#~ userNameIpt.send_keys worksheet.range("a#{row}").value.to_s
			
		#~ sleep 1
			
		#~ blank= dr.find_element(:class => 'line_tip')
		#~ blank.click
			
		#~ sleep 1
		
		#~ msgopt= dr.find_element(:id,'tip_email').text
		#~ puts msgopt.text worksheet.range("c#{row}").value.to_s
		#~ worksheet.range("c#{row}").value = msgopt
		#~ worksheet.range('f3').value = ['i']
		cc=worksheet.range("c#{row}").value
		dd=worksheet.range("d#{row}").value
		ee=worksheet.range("e#{row}")
		
		puts cc
		puts dd
		
		#~ if  cc.eql? dd
			#~ worksheet.range("e#{row}").value=['P']
			#~ elsif cc.nil?
				#~ worksheet.range("e#{row}").value=['']
				#~ elsif dd.nil?
					#~ worksheet.range("e#{row}").value=['']
					#~ else
						#~ worksheet.range("e#{row}").value=['F']
		#~ end

		if  cc.eql? dd
			ee.value=['P']
			#~ elsif cc.nil?
				#~ ee.value=['']
				#~ elsif dd.nil?
					#~ ee.value=['']
					else
						ee.value=['F']
		end
		
		#~ puts worksheet.range("e#{row}").value
			
		workbook.save
		
		system ("tskill EXCEL")
		
		