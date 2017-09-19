# -*- coding: utf-8 -*-
import subprocess
import win32api
import win32con
# import win32gui
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import time

__author__ = 'Kan'

k = PyKeyboard()
m = PyMouse()

# 启动skype
skype_exe = r"C:\Program Files (x86)\Skype\Phone\skype.exe"
subprocess.Popen([skype_exe])
time.sleep(5)  # 延迟5秒

# 定位账号输入框
'''windll.user32.SetCursorPos(882, 520)'''
win32api.SetCursorPos((882, 520))
time.sleep(1)

# 双击密码输入框
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
time.sleep(3)

# 输入skype账号
k.type_string('kanmax724')  # XXXXX=账号
time.sleep(3)

# 按下回车
win32api.keybd_event(13, 0, 0, 0)
win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(10)

# 输入密码
k.type_string('Iamatmu123')  # YYYYYY=密码
time.sleep(2)

# 按下回车
win32api.keybd_event(13, 0, 0, 0)
win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(15)

# win32gui.FindWindow("tSkMainForm", "Skype?? - kanmax724")
# 查找句柄后定位失败用下列方法alt+tab切换窗口
# 切换skype窗口（alt + tab）
win32api.keybd_event(18, 0, 0, 0)
win32api.keybd_event(9, 0, 0, 0)
win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(2)

# 快捷键最大化skype窗口（alt + spacebar + x）
win32api.keybd_event(18, 0, 0, 0)
win32api.keybd_event(32, 0, 0, 0)
win32api.keybd_event(32, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(88, 0, 0, 0)
win32api.keybd_event(88, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(5)

# 定位skype搜索框
win32api.SetCursorPos((75, 90))
time.sleep(1)

# 双击搜索框
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
time.sleep(2)

# 输入搜索条件
k.type_string('Edward')
time.sleep(2)

# 回车（会自动跳转光标到“信息输入框”）
win32api.keybd_event(13, 0, 0, 0)
win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(2)

# 输入发送内容
k.type_string('test test')
time.sleep(1)

# 回车（发送）
win32api.keybd_event(13, 0, 0, 0)
win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(5)

