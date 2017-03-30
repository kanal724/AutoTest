#encoding: utf-8  
  
require 'selenium-webdriver'  
  
describe "soso mainpage login" do   
    it "should return username and password is wrong" do  
			
        dr=Selenium::WebDriver.for :firefox  
        url='http://192.168.200.211/share/Lambo/login.html'  
        dr.get url  
		
		puts dr.title
		
        dr.find_element(:name=>'account').send_keys("test")  
        dr.find_element(:name=>'password').send_keys("testdddddd222323")  
		
		links=dr.find_element(:xpath=>"//button")
        links.click  
		
		sleep 3
		
		dr.quit
          
        #dr.find_element(:class=>'mainer').text.should eql ("您输入的帐号或密码错误")  
    end #it  
end #describe  