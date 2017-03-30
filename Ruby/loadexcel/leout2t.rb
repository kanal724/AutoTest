require 'rspec'
require 'rubygems'
require 'selenium-webdriver'
require 'win32ole'
require 'byebug'

#~ describe "163mail login" do 

	#~ before(:all) do
		dr = Selenium::WebDriver.for :ff
		url='https://passport.cnblogs.com/register.aspx'
		dr.navigate.to url
		sleep 3
		excel = WIN32OLE.new("excel.application")
		filepath="F:\\autotest\\ruby\\loadexcel\\Data.xlsx" #路径用两斜杠
		workbook = excel.workbooks.open(filepath)
		worksheet=workbook.worksheets(1)
		works2=workbook.worksheets(2)
		#worksheet=workbook.worksheets("sheet name") 打开表名
		#读取excel文件
		row=2
		row2=2
	#~ end

	while works2.range("a#{row2}").value
		
		eid=works2.range("a#{row2}")
		emsg=works2.range("b#{row2}")
		
		while worksheet.range("a#{row}").value

			emailIpt = dr.find_element(:id => eid.value.to_s)
			emailIpt.send_keys worksheet.range("a#{row}").value.to_s

			blank= dr.find_element(:class => 'line_tip')
			blank.click

			msgopt= dr.find_element(:id,emsg.value.to_s).text

			cc=worksheet.range("c#{row}")
			dd=worksheet.range("d#{row}")
			ee=worksheet.range("e#{row}")

			row+=1
			emailIpt.clear()
			#~ pwdInput.clear()
   
			sleep 0.5
			puts msgopt
		end

		row2+=1

		
		puts eid.text
		puts emsg.text
	end
		
		workbook.save
		system ("tskill EXCEL")
		
		dr.quit
	