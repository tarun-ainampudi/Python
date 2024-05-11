import pyautogui
import time

msg=input("Enter the Message:")
num=int(input("Enter No.of Times:"))
time.sleep(3)
for _ in range(num):
    time.sleep(0.01)
    pyautogui.typewrite(msg)
    pyautogui.press("enter")
