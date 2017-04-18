require 'rubygems'
require 'selenium-webdriver'
require 'win32ole'
require 'byebug'


		dr = Selenium::WebDriver.for :ff
		url='http://web.rd.lambor.ptg/'
		dr.navigate.to url
		sleep 3
		uname = dr.find_element(:name,'account') 
		uname.send_keys ("MasterTest00014")#.text
		sleep 0.5
		pword = dr.find_element(:name,'password')
		pword.send_keys ("123456")#.text
		sleep 5
		
		#~ ybutton=dr.find_element(:xpath,"/html/body/div[1]/div/form/fieldset/div[4]/div/input")
		
		#~ puts ybutton.text
		
		
		#想办法判断验证码输入框，未成功
		#~ while ybutton
		  #~ if ybutton < 4
			#~ sleep 5
			#~ else
				#~ break
			#~ end
		#~ end
		
		
		
		lbutton=dr.find_element(:xpath,"/html/body/div[1]/div/form/fieldset/button")
		lbutton.click
		sleep 2
		HLSD='http://web.rd.lambor.ptg/Main/System/SystemBonusSetAdd'
		dr.navigate.to HLSD
		
		excel = WIN32OLE.new("excel.application")
		filepath="F:\\autotest\\ruby\\loadexcel\\HLSDData.xlsx" #路径用两斜杠
		workbook = excel.workbooks.open(filepath)
		
		idsh=1 #声明变量
		works2=workbook.worksheets(idsh) #读取"idsh(变量)个sheet的数据
		
		#worksheet=workbook.worksheets("sheet name")  #打开表名
		
		#循环前必须做的变量声明，否则在判断while时会出现不成立情况
		eler=2
		iptsh=2
		
	#根据第一张表的a列第二行开始做while循环
	while works2.range("a#{eler}").value 
		
		worksheet=workbook.worksheets(iptsh)
		
		eidin=works2.range("a#{eler}")#.value.to_s
		eid=eidin.value.to_s
		
		emsgin=works2.range("b#{eler}")#.value.to_s
		emsg=emsgin.value.to_s
		
		inr=2 #循环前必须做的变量声明，否则在判断while时会出现不成立情况
		
		#根据“第iptsh(变量)张表”的“第a列第inr行”开始做while循环
		while worksheet.range("a#{inr}").value
			
			#在网页查找元素并输入数据
			ipt = dr.find_element(:name=> eid) #根据“第一个sheet的eid(变量)”数据开始查找元素id
			ipt.send_keys worksheet.range("a#{inr}").text.to_s #把“第a列第inr(变量)行”开始的text作为输入的数据
			ipt.click
			#选择密码，将第二列值做为密码
			#~ pwdInput= dr.find_element(:id => 'pwdInput')
			#~ pwdInput.send_keys worksheet.range("b#{inr}").value.to_s
   
			#单击登录按钮
			blank= dr.find_element(:class => 'col-sm-3')
			blank.click
			
			sleep 0.5
			
			#将获取的错误信息输出至excel
			msgopt= dr.find_element(:xpath,emsg).text #获取id=emsg的数据转换成text
			worksheet.range("d#{inr}").value = msgopt #将错误信息输入到excel的“第d列第inr(变量)行“单元格
			#~ worksheet.range("f#{inr}").value = ['=IF(','c#{row}=d#{row}',',"P","F")']
			#~ puts msgopt.text
		
		#~ if  cc.eql? dd
			#~ worksheet.range("e#{inr}").value=['P']
			#~ elsif cc.nil?
				#~ worksheet.range("e#{inr}").value=['']
				#~ elsif dd.nil?
					#~ worksheet.range("e#{inr}").value=['']
					#~ else
						#~ worksheet.range("e#{inr}").value=['F']
		#~ end
		
			cc=worksheet.range("c#{inr}").value
			dd=worksheet.range("d#{inr}").value
			ee=worksheet.range("e#{inr}")
			#判断两个单元格的数据，相等为P，否则为F
			if  cc.eql? dd
				ee.value=['P']
				#~ elsif cc.nil?
					#~ ee.value=['']
					#~ elsif dd.nil?
						#~ ee.value=['']
						else
							ee.value=['F']
			end

			inr+=1 #inr(变量)，循环+1
			
			ipt.clear() #清空输入框数据
   
			sleep 0.5
			
		end
		
		eler+=1 #eler(变量)，循环+1
		iptsh+=1 #iptsh(变量)，循环+1
	end

		workbook.save #保存excel
		system ("tskill EXCEL") #kil掉名为EXCEL的进程
		
		dr.quit #关闭浏览器