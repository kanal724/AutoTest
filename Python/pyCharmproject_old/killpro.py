# coding=utf-8
import win32com.client
import os

 #os.system('taskkill /F /IM geckodriver.exe')



#返回值大于0 则表明有这个进程名的程序在运行(不生效)
'''
def __Is_Process_Running(imagename):
    p = os.popen('tasklist /FI "IMAGENAME eq %s"' % imagename)
    print p.read().count(imagename)
    return p.read().count(imagename)
'''



#def check_exsit(process_name):
WMI = win32com.client.GetObject('winmgmts:')
process_name = 'geckodriver.exe'
processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
if len(processCodeCov) > 0:
    print '%s is exists' % process_name
    os.system('taskkill /F /IM geckodriver.exe')
else:
    print '%s is not exists' % process_name
#if __name__ == '__main__':
    #check_exsit('geckodriver.exe')