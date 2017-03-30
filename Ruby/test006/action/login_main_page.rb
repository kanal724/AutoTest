#encoding: utf-8 
require File.dirname(__FILE__)+'/../tool/login_dialog'  
class LoginMainPage
	
	include LoginDialog  
	def initialize(dr)  
		@dr ||=dr  
	end

  
	#~ def open_login_dialog  
		#~ login_link.click  
		#~ sleep 2  
	#~ end  
  
	#~ def loginbtn_click
		#~ open_login_dialog  
		#~ sleep 8
		#~ to_dialog_frame 
		#~ to_U_P_login.click
		#~ sleep 2
	#~ end
	
	
	#~ def login(username,password)  
	def login(username)
		#~ open_login_dialog  
		#~ sleep 8
		#~ to_dialog_frame 
		#~ to_U_P_login.click
		#~ sleep 2
		usr_field.send_keys(username)  
		#~ psd_field.send_keys(password)  
		#~ login_btn.click  
		sleep 1

	end
	
	#使用“innerHTML”后，需要加下面这段代码
	def message
		err_message.attribute("innerHTML")
	end
	
end  