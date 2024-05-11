import pywhatkit
import pyautogui
import time 
pywhatkit.sendwhatmsg("+916301592113",'Hello',1,24)
for i in range(10):
    time.sleep(2)
    pyautogui.write("Hello r  u there")
    pyautogui.press("Enter")