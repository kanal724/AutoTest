#~ 1.用OLE

 

#~ require "win32ole"
#~ mgmt = WIN32OLE.connect('winmgmts:\\\\.')
  #~ mgmt.ExecQuery("Select * from Win32_Process Where Name ='#{EXCEL.EXE}'").each{ |item|
    #~ item.Terminate()
 #~ }
 
#~ 2.不用OLE

 

#~ require 'sys/proctable'
#~ require 'time'

#~ Sys::ProcTable.ps.each { |ps|
  #~ if ps.name.downcase == proc_name.downcase
    #~ Process.kill('KILL', ps.pid)
  #~ end
#~ }


#~ system("ps -ef | grep EXECEL | grep -v grep | awk '{print $2}' | xargs -n1 kill -9")

system("tskill EXCEL")
 