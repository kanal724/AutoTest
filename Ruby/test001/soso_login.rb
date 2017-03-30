#encoding: utf-8
require 'rubygems'
require 'selenium-webdriver'  

dr=Selenium::WebDriver.for :firefox
url='http://www.soso.com'
dr.get url
  
links=dr.find_element(:id=>'ua').find_elements(:css=>'a')
links[1].click
links[1].send_keys(:enter)
  
dr.switch_to.frame('login_frame')
sleep 2
dr.find_element(:id=>'u').send_keys("test")
dr.find_element(:id=>'p').send_keys("test")
dr.find_element(:id=>'login_button').click