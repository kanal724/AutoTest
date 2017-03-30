module LoginDialog  
  
  #~ def ua_link  
    #~ @dr.find_element(:id=>'login')
  #~ end  
  
  #~ def login_link  
    #~ ua_link
  #~ end  
  
  #~ def to_dialog_frame  
    #~ begin  
      #~ @dr.switch_to.frame('login_frame')  
    #~ rescue  
      #~ raise 'Can not switch to login dialog, make sure the dialog was open'  
      #~ exit  
    #~ end  
  #~ end  

  #~ def to_U_P_login
	#~ @dr.find_element(:id=>'switcher_plogin')
  #~ end
  
  def usr_field  
    @dr.find_element(:id => 'ctl00_holderLeft_txt_email')  
  end  
  
  def psd_field  
    @dr.find_element(:id => 'ctl00_holderLeft_txt_userName')  
  end  
  
  #~ def login_btn  
    #~ @dr.find_element(:id => 'login_button')  
  #~ end  
  
  #~ def err_message  
   #~ @dr.find_element(:id=>'err_m').text #使用“innerHTML时，不需要“.text”，如下方
  #~ end  
  
  def blank
	  @dr.find_element(:class,'line_tip')
  end
  
  
  def err_message  
	  @dr.find_element(:id=>'tip_email')
  end  
  
  def close_browser  
    @dr.quit  
  end  
end