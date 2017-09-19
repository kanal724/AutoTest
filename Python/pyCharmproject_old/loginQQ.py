# -*- coding: utf-8 -*-
import subprocess
import win32api
import win32con
from pykeyboard import PyKeyboard
import time

__author__ = 'Kan'

k = PyKeyboard()

# 启动qq
qq_exe = r"C:\Program Files (x86)\Tencent\QQ\Bin\QQ.exe"
subprocess.Popen([qq_exe])
time.sleep(5)

# 定位qq密码输入框
'''windll.user32.SetCursorPos(969, 583)'''
win32api.SetCursorPos((973, 581))
time.sleep(1)

# 双击输入框
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
time.sleep(2)

# 输入qq账号
k.type_string('XXXXXX')  # XXXXXX=qq账号
time.sleep(2)

# 按TAB
win32api.keybd_event(9, 0, 0, 0)
win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(2)

# 输入密码
k.type_string('YYYYYY')  # YYYYYY=密码
time.sleep(1)

# 按回车
win32api.keybd_event(13, 0, 0, 0)
win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(5)
