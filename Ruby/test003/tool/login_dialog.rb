module LoginDialog  
  
  def ua_link  
    @dr.find_element(:id=>'login')
  end  
  
  def login_link  
    ua_link
  end  
  
  def to_dialog_frame  
    begin  
      @dr.switch_to.frame('login_frame')  
    rescue  
      raise 'Can not switch to login dialog, make sure the dialog was open'  
      exit  
    end  
  end  

  def to_U_P_login
	@dr.find_element(:id=>'switcher_plogin')
  end
  
  def usr_field  
    @dr.find_element(:id => 'u')  
  end  
  
  def psd_field  
    @dr.find_element(:id => 'p')  
  end  
  
  def login_btn  
    @dr.find_element(:id => 'login_button')  
  end  
  
  def err_message  
   @dr.find_element(:id=>'err_m').text  
  end  
  
  def close_browser  
    @dr.quit  
  end  
end