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
    @dr=Selenium::WebDriver.for :firefox 
	@url=@problem["data"]["mainPage"]["url"]
    #@url='http://im.qq.com'  
    @dr.get @url  
  end  
  before(:each) do  
  
    @login_element=LoginMainPage.new(@dr)  
  end  
  
  it "should return username and password is wrong" do  
    @login_element.login(@problem["data"]["login"]["wrong"]["username"],@problem["data"]["login"]["wrong"]["password"])   
	sleep 2
    err_message.should eql (@problem["data"]["login"]["wrong"]["message"])
    close_browser  
  end  
end  