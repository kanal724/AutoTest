#encoding: utf-8  
require "rspec"  
require 'yaml'  
require 'selenium-webdriver'  
  
require File.dirname(__FILE__)+'/../action/login_main_page'  
require File.dirname(__FILE__)+'/../tool/login_dialog'  
  
describe "imqq login" do  
  include LoginDialog  
  before(:all) do  
    @dr=Selenium::WebDriver.for :firefox  
    @url='http://im.qq.com'  
    @dr.get @url  
  end  
  before(:each) do  
  
    @login_element=LoginMainPage.new(@dr)  
  end  
  
  it "should return username and password is wrong" do  
    @login_element.login("test","test")  
	sleep 2
    err_message.should eql ("请输入正确的帐号！")  
    close_browser  
  end  
end  