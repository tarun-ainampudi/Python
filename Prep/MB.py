import pyautogui
import time

msg=input("Enter the Message:")
num=int(input("Enter No.of Times:"))
tim=int(input("Enter Time Gap in Seconds:"))

with open(r"C:\Users\tarun\Desktop\Python\bing-points\query.txt","r+") as f:
    query_list = f.read().split(",")
    query_list.remove("")

time.sleep(3)
i=0
for _ in range(num):
    time.sleep(tim)
    pyautogui.typewrite(query_list[i%len(query_list)])
    pyautogui.press("enter")
    i+=1
