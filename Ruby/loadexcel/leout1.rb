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

	#~ it "read excel" do
	while works2.range("a#{row2}").value
		
		eid=works2.range("a#{row2}")#.value.to_s
		#~ eid=eidin.value.to_s
		emsg=works2.range("b#{row2}")#.value.to_s
		#~ emsg=emsgin.value.to_s
		
		while worksheet.range("a#{row}").value
			#选择帐号，把第一列的值做为帐号
			#~ emailIpt = dr.find_element(:id => 'ctl00_holderLeft_txt_email')
			
			emailIpt = dr.find_element(:id => eid.value.to_s)
			emailIpt.send_keys worksheet.range("a#{row}").value.to_s
   
			#选择密码，将第二列值做为密码
			#~ pwdInput= dr.find_element(:id => 'pwdInput')
			#~ pwdInput.send_keys worksheet.range("b#{row}").value.to_s
   
			#单击登录按钮
			blank= dr.find_element(:class => 'line_tip')
			blank.click
			
			#~ sleep 1
			
			#输入错误信息至excel
			#~ msgopt= dr.find_element(:id,'tip_email').text
			msgopt= dr.find_element(:id,emsg.value.to_s).text
			worksheet.range("d#{row}").value = msgopt
			#~ worksheet.range("f#{row}").value = ['=IF(','c#{row}=d#{row}',',"P","F")']
			#~ puts msgopt.text
			cc=worksheet.range("c#{row}").value
			dd=worksheet.range("d#{row}").value
			ee=worksheet.range("e#{row}")

			#~ if cc==['']
				#~ break
			#~ end
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
   
			sleep 0.5
			
		end
		
		puts eid.text
		puts emsg.text
		row2+=1
	end

		workbook.save
		system ("tskill EXCEL")
		
		dr.quit