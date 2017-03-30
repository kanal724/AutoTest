#encoding: utf-8  
require "rspec"  
require 'yaml'  
require 'selenium-webdriver'  
  
require File.dirname(__FILE__)+'/../action/login_main_page'  
require File.dirname(__FILE__)+'/../tool/login_dialog'  
  
describe "imqq login" do  
  include LoginDialog  

  before(:all) do  
	@problem=YAML.load(File.open(File.dirname(__FILE__)+'/../config/login_data.yml'))  
    #~ @dr=Selenium::WebDriver.for :firefox  
	@dr=Selenium::WebDriver.for :chrome
    @url=@problem["data"]["mainPage"]["url"]  
    @dr.get @url
    @login_element=LoginMainPage.new(@dr)  
  end  
  
  it "右侧出现“格式错误”" do  
	@login_element.login(@problem["data"]["login"]["wrong"]["username"])   
	blank.click
	#下面使用了“innerHTML”参考login_main_page.rb和login_dialog.rb
	expect(@login_element.message).to eql (@problem["data"]["login"]["wrong"]["message"])
	usr_field.clear() 
  end  
  
  it "右侧出现“不可为空”" do  
	@login_element.login(@problem["data"]["login"]["usernameNotExist"]["username"])
	blank.click
	#下面使用了“innerHTML”参考login_main_page.rb和login_dialog.rb
	expect(@login_element.message).to eql (@problem["data"]["login"]["usernameNotExist"]["message"])  
	usr_field.clear()  
end  

  it "右侧出现“输入成功”" do  
	@login_element.login(@problem["data"]["login"]["usernameRight"]["username"])
	blank.click
	#下面使用了“innerHTML”参考login_main_page.rb和login_dialog.rb
	expect(@login_element.message).to eql (@problem["data"]["login"]["usernameRight"]["message"])  
	usr_field.clear()  
  end  

  it "右侧出现“邮箱重复”" do  
	@login_element.login(@problem["data"]["login"]["unAlreadyExists"]["username"])
	blank.click
	sleep 2
	#下面使用了“innerHTML”参考login_main_page.rb和login_dialog.rb
	expect(@login_element.message).to eql (@problem["data"]["login"]["unAlreadyExists"]["message"])  
	#~ puts @login_element.message
	usr_field.clear()  
  end  

#~ it "输出元素" do
	#~ puts @login_element.message
#~ end

  
  #~ it "关闭浏览器" do
	  #~ sleep 10
	  #~ close_browser
  #~ end
  
  
end  