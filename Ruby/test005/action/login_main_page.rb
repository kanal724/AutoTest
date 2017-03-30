#encoding: utf-8 
require File.dirname(__FILE__)+'/../tool/login_dialog'  
class LoginMainPage
	
	include LoginDialog  
	def initialize(dr)  
		@dr ||=dr  
	end

  
	def open_login_dialog  
		login_link.click  
		sleep 2  
	end  
  
	def login(username,password)  
		open_login_dialog  
		to_dialog_frame 
		sleep 2
		to_U_P_login.click
		sleep 2
		usr_field.send_keys(username)  
		psd_field.send_keys(password)  
		login_btn.click  
	end
	
	#使用“innerHTML”后，需要加下面这段代码
	def message
		err_message.attribute("innerHTML")
	end
	
end  