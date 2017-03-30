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
		row2=2
	#~ end

	while works2.range("a#{row2}").value
		
		eidin=works2.range("a#{row2}")#.value.to_s
		emsgin=works2.range("b#{row2}")#.value.to_s
		eid=eidin.value.to_s
		emsg=emsgin.value.to_s
		row=2
		while worksheet.range("a#{row}").value

			emailIpt = dr.find_element(:id => eid)
			emailIpt.send_keys worksheet.range("a#{row}").value.to_s

			blank= dr.find_element(:class => 'line_tip')
			blank.click

			msgopt= dr.find_element(:id,emsg).text

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

		
		puts eidin.text
		puts emsgin.text
	end
		
		workbook.save
		system ("tskill EXCEL")
		
		dr.quit
	
	
#~ 解决while嵌套问题：
#~ 关键在于row的使用上出现问题，在每次while循环之前要做row=2，否则内部循环会跳过，（估计-个人猜测：是因为如果将row=1在内循环的while之前不写，或者在外循环的while之前写的话，会判定内循环的while不满足条件，导致不进行循环），并且现在分开row2和row，之前都用row，也是导致内部循环执行完以后，就不再做外部循环的原因

#~ 【LV3】kanho 2017/3/31 1:28:50
#~ 另外，确实使用了debug后能比较清晰知道是哪里可能出现问题，上网找到的是byebug，（在代码里设置断点（debugger））才会启动