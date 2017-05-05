#encoding: UTF-8
  
require 'selenium-webdriver'  
  
#~ describe "soso mainpage login" do   
    #~ it "should return username and password is wrong" do  
        dr=Selenium::WebDriver.for :firefox  
        url='http://im.qq.com'  
        dr.get url  
  
        dr.find_element(:id=>'login').click
        
		sleep 3
		
        dr.switch_to.frame('login_frame')
		
		dr.find_element(:id=>'switcher_plogin').click
		
		sleep 1
		
        dr.find_element(:id=>'u').send_keys("test")  
        dr.find_element(:id=>'p').send_keys("test")  
        dr.find_element(:id=>'login_button').click  
		
		sleep 2
		
		#dr.find_element(:id=>'err_m').text.should eql ("请输入正确的帐号！")#旧的语法
        #~ expect(dr.find_element(:id=>'err_m').text).to eql ("请输入正确的帐号！")  #新语法
		
		  #获取元素“id”为“err_m”的数据，以text定义为“err”
  err=dr.find_element(:id=>'err_m').text
  #将预期结果定义为“dd”
  dd=("您还没有输入验证码！")
  #判断“err”和“dd”
  if
    err.eql? dd #使用“eql?”方法用于对比两个值
    puts "P" #打印“P”
    else puts "F"  #打印“F”
  end

		
		
		
		
		#puts dr.find_element(:id=>'err_m').text
		
		sleep 2
		
		dr.quit
    #~ end #it  
#~ end #describe 