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
		idsh=1
		
		#~ worksheet=workbook.worksheets(iptsh)
		works2=workbook.worksheets(idsh)
		#worksheet=workbook.worksheets("sheet name") 打开表名
		#读取excel文件

		eler=2
		iptsh=2
	#~ end

	#~ it "read excel" do
	while works2.range("a#{eler}").value
		
		worksheet=workbook.worksheets(iptsh)
		
		eidin=works2.range("a#{eler}")#.value.to_s
		eid=eidin.value.to_s
		
		emsgin=works2.range("b#{eler}")#.value.to_s
		emsg=emsgin.value.to_s
		
		inr=2
		while worksheet.range("a#{inr}").value
			#选择帐号，把第一列的值做为帐号
			#~ emailIpt = dr.find_element(:id => 'ctl00_holderLeft_txt_email')
			emailIpt = dr.find_element(:id => eid)
			emailIpt.send_keys worksheet.range("a#{inr}").value.to_s
   
			#选择密码，将第二列值做为密码
			#~ pwdInput= dr.find_element(:id => 'pwdInput')
			#~ pwdInput.send_keys worksheet.range("b#{inr}").value.to_s
   
			#单击登录按钮
			blank= dr.find_element(:class => 'line_tip')
			blank.click
			
			sleep 1
			
			#输入错误信息至excel
			#~ msgopt= dr.find_element(:id,'tip_email').text
			msgopt= dr.find_element(:id,emsg).text
			worksheet.range("d#{inr}").value = msgopt
			#~ worksheet.range("f#{inr}").value = ['=IF(','c#{row}=d#{row}',',"P","F")']
			#~ puts msgopt.text
			cc=worksheet.range("c#{inr}").value
			dd=worksheet.range("d#{inr}").value
			ee=worksheet.range("e#{inr}")

			#~ if cc==['']
				#~ break
			#~ end
		#~ puts cc
		#~ puts dd
		
		#~ if  cc.eql? dd
			#~ worksheet.range("e#{inr}").value=['P']
			#~ elsif cc.nil?
				#~ worksheet.range("e#{inr}").value=['']
				#~ elsif dd.nil?
					#~ worksheet.range("e#{inr}").value=['']
					#~ else
						#~ worksheet.range("e#{inr}").value=['F']
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

			inr+=1

			emailIpt.clear()
			#~ pwdInput.clear()
   
			sleep 0.5
			
		end
		
		#~ puts eid.text
		#~ puts emsg.text
		eler+=1
		iptsh+=1
	end

		workbook.save
		system ("tskill EXCEL")
		
		dr.quit