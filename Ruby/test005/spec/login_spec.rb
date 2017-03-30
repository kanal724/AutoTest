#encoding: utf-8  
require "rspec"  
require 'yaml'  
require 'selenium-webdriver'  
  
require File.dirname(__FILE__)+'/../action/login_main_page'  
require File.dirname(__FILE__)+'/../tool/login_dialog'  
  
describe "imqq login" do  
  include LoginDialog  
#  before(:all) do  
#	@problem=YAML.load(File.open(File.dirname(__FILE__)+'/../config/login_data.yml'))
#    @dr=Selenium::WebDriver.for :firefox 
#	@url=@problem["data"]["mainPage"]["url"]
#    #@url='http://im.qq.com'  
#    @dr.get @url  
#  end  
  before(:each) do  
	@problem=YAML.load(File.open(File.dirname(__FILE__)+'/../config/login_data.yml'))  
    @dr=Selenium::WebDriver.for :firefox  
    @url=@problem["data"]["mainPage"]["url"]  
    @dr.get @url
    @login_element=LoginMainPage.new(@dr)  
  end  
  
  it "should return username and password is wrong" do  
    @login_element.login(@problem["data"]["login"]["wrong"]["username"],@problem["data"]["login"]["wrong"]["password"])   
	sleep 2
    #err_message.should eql (@problem["data"]["login"]["wrong"]["message"])#会报“旧语法”
	#expect(@login_element.err_message).to eql (@problem["data"]["login"]["wrong"]["message"])#不会报“旧语法”,未用“innerHTML”
	expect(@login_element.message).to eql (@problem["data"]["login"]["wrong"]["message"])#使用了“innerHTML”参考login_main_page.rb和login_dialog.rb
	sleep 2
    close_browser  
  end  
  
  it "should return username and password are not exist" do  
    @login_element.login(@problem["data"]["login"]["allNotExist"]["username"],@problem["data"]["login"]["allNotExist"]["password"])  
	sleep 2
#    err_message.should eql (@problem["data"]["login"]["allNotExist"]["message"])  #会报“旧语法”
#	expect(@login_element.err_message).to eql (@problem["data"]["login"]["allNotExist"]["message"])  #不会报“旧语法”,未用“innerHTML”
		expect(@login_element.message).to eql (@problem["data"]["login"]["allNotExist"]["message"])  #使用了“innerHTML”参考login_main_page.rb和login_dialog.rb
	sleep 2
    close_browser  
  end  
  
  it "should return username is not exist" do  
    @login_element.login(@problem["data"]["login"]["usernameNotExist"]["username"],@problem["data"]["login"]["usernameNotExist"]["password"])  
	sleep 2
    #err_message.should eql (@problem["data"]["login"]["usernameNotExist"]["message"])  #会报“旧语法”
#	expect(@login_element.err_message).to eql (@problem["data"]["login"]["usernameNotExist"]["message"])  #不会报“旧语法”,未用“innerHTML”
		expect(@login_element.message).to eql (@problem["data"]["login"]["usernameNotExist"]["message"])  #使用了“innerHTML”参考login_main_page.rb和login_dialog.rb
	sleep 2
    close_browser  
  end  
  
  it "should return password is not exist" do  
    @login_element.login(@problem["data"]["login"]["passwordNotExist"]["username"],@problem["data"]["login"]["passwordNotExist"]["password"])  
	sleep 2
    #err_message.should eql (@problem["data"]["login"]["passwordNotExist"]["message"])  #会报“旧语法”
#	expect(@login_element.err_message).to eql (@problem["data"]["login"]["passwordNotExist"]["message"])#不会报“旧语法”,未用“innerHTML”
	expect(@login_element.message).to eql (@problem["data"]["login"]["passwordNotExist"]["message"])#使用了“innerHTML”参考login_main_page.rb和login_dialog.rb

	sleep 2
    close_browser  
  end  
end  