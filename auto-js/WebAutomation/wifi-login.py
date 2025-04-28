from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

# You have successfully logged out
# Authentication Successful

options = Options()
#options.add_argument("--headless")
#options.add_argument("--disable-gpu")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-web-security")
options.add_experimental_option("detach", True)

def superscript_to_int(sup_char):
    superscript_map = {
        '⁰': 0, '¹': 1, '²': 2, '³': 3, '⁴': 4, '⁵': 5, '⁶': 6, '⁷': 7, '⁸': 8, '⁹': 9, 
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9 
    }
    return superscript_map.get(sup_char, None) 

def gen_list(reg_no : str):
    super_script = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
    sup_list = []
    sup_list.append(reg_no)
    for i in sup_list:
        for j in range(len(i)):
            if(i[j].isdigit()):
                temp = i[0:j] + super_script[superscript_to_int(i[j])] + i[j+1:]
                if temp not in sup_list:
                    sup_list.append(temp)
    return sup_list

def login(driver,username,password):
    result = driver.execute_script("""
       if( document.querySelector("#ft_un")){
       document.querySelector("#ft_un").value=arguments[0];
       document.querySelector("#ft_pd").value=arguments[1];
       document.querySelector("body > div > div > form > div.form-footer > button").click();}
    """,username,password)
    
def res(driver):
    return driver.execute_script("return document.documentElement.outerHTML;")
    
driver = webdriver.Chrome(service=Service(r"C:\Users\tarun\Desktop\Python\auto-js\WebAutomation\chromedriver-win64\chromedriver.exe"), options=options)
driver.get("http://172.18.10.10:1000/logout?")
count=1
username=os.getenv("wifi_username")
password=os.getenv("wifi_password")
username_list = gen_list(username)

while "login" in str(res(driver)).lower() and "success" not in str(res(driver)).lower():
    login(driver,username_list[count],password)
    count+=1
    
#print(str(res(driver)).lower())

#print("success" in str(res(driver)).lower())

if "success" in str(res(driver)).lower():
    time.sleep(1)
    driver.quit()
    