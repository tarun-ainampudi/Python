import subprocess
import webbrowser
import pyautogui
import time

def change_ip(new_ip):
    # Command to change the IP address
    interface="Wi-Fi"
    dns1="172.18.8.222"

    ip_command = f"netsh interface ip set address name=\"{interface}\" static {new_ip} 255.255.248.0 172.19.128.1" 
    
    # Commands to set DNS servers
    dns_command1 = f"netsh interface ip set dns name=\"{interface}\" static {dns1}"

    # Run the commands
    subprocess.run(ip_command, shell=True)
    subprocess.run(dns_command1, shell=True)
    time.sleep(3)
    webbrowser.open("http://172.18.10.10:1000/logout?")
    time.sleep(3)
    pyautogui.hotkey('ctrl','w')
   

for i in range(128,136,1):
    for j in range(0,256,1):
        ip ="172.19." +str(i)+"."+str(j)
        change_ip(ip)


