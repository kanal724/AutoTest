#encoding: utf-8  
  
require 'selenium-webdriver'  
  
describe "soso mainpage login" do   
    it "should return username and password is wrong" do  
        dr=Selenium::WebDriver.for :firefox  
        url='http://www.sogou.com/qq?ru=http%3A%2F%2Fwww.sogou.com%2Flogin%2Fqq_login_callback_page_new.html%3Fxy%3Dhttps%26from%3Dhttps%253A%252F%252Fwww.sogou.com%252F%253Frfrom%253Dsoso'  
        dr.get url  
  
        #dr.find_element(:id=>'loginBtn').click
        
		dr.switch_to.frame(:scrolling=>'no')
        #dr.switch_to.frame('ptlogin_iframe') 
		#出现报错：1) soso mainpage login should return username and password is wrong  Failure/Error: dr.switch_to.frame('ptlogin_iframe')  Selenium::WebDriver::Error::NoSuchElementError:  Unable to locate element: #ptlogin_iframe  # ./spec/soso_login_spec.rb:14:in `block (2 levels) in <top (required)>'
		
		
		dr.find_element(:id=>'switcher_plogin').click
		
		sleep 3
		
		
        #dr.find_element(:id=>'u').send_keys("test")  
        #dr.find_element(:id=>'p').send_keys("test")  
        #dr.find_element(:id=>'login_button').click  
          
        #dr.find_element(:id=>'err_m').text.should eql ("您输入的帐号或密码不正确，请重新输入。意见反馈")  
		
		dr.quit
    end #it  
end #describe 