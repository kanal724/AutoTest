require 'rspec'
require 'rubygems'
require 'selenium-webdriver'
require 'win32ole'

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
		#worksheet=workbook.worksheets("sheet name") 打开表名
		#读取excel文件
		row=2
	#~ end

	#~ it "read excel" do
		while worksheet.range("a#{row}").value
			#选择帐号，把第一列的值做为帐号
			emailIpt = dr.find_element(:id => 'ctl00_holderLeft_txt_email')
			emailIpt.send_keys worksheet.range("a#{row}").value.to_s
   
			#选择密码，将第二列值做为密码
			#~ pwdInput= dr.find_element(:id => 'pwdInput')
			#~ pwdInput.send_keys worksheet.range("b#{row}").value.to_s
   
			#单击登录按钮
			blank= dr.find_element(:class => 'line_tip')
			blank.click
			
			sleep 1
			
			#输入错误信息至excel
			msgopt= dr.find_element(:id,'tip_email').text
			worksheet.range("d#{row}").value = msgopt
			#~ worksheet.range("f#{row}").value = ['=IF(','c#{row}=d#{row}',',"P","F")']
			#~ puts msgopt.text
					cc=worksheet.range("c#{row}").value
		dd=worksheet.range("d#{row}").value
		ee=worksheet.range("e#{row}")
		
		#~ puts cc
		#~ puts dd
		
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
			elsif cc.nil?
				ee.value=['']
				elsif dd.nil?
					ee.value=['']
					else
						ee.value=['F']
		end
						
			
			row+=1
   
			emailIpt.clear()
			#~ pwdInput.clear()
   
			sleep 1
		end
		
		workbook.save
		system ("tskill EXCEL")
		
		dr.quit
	#~ end
#~ end


#~ ruby在windows下杀进程的方法
#~ 　　1.用OLE
#~ 　　require "win32ole" mgmt = WIN32OLE.connect('winmgmts:\\\\.') mgmt.ExecQuery("Select * from Win32_Process Where Name ='#{proc_name}'").each{ |item| item.Terminate() }
#~ 　　2.不用OLE
#~ 　　require 'sys/proctable' require 'time' Sys::ProcTable.ps.each { |ps| if ps.name.downcase == proc_name.downcase Process.kill('KILL', ps.pid) end }
