import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineProfile, QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QTimer
import sys
import time

#change reg_no in line 8 and pswd in line 9

def superscript_to_int(sup_char):
    superscript_map = {
        '⁰': 0, '¹': 1, '²': 2, '³': 3, '⁴': 4, '⁵': 5, '⁶': 6, '⁷': 7, '⁸': 8, '⁹': 9, 
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9 
    }
    return superscript_map.get(sup_char, None) 


def gen_list(reg_no : str):
    reg_no = reg_no
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


reg_no = "23BCE9846"
pswd = "Admin@VITAP"
reg_list = gen_list(reg_no)


def fill_username_password(view, username_xpath, password_xpath, username, password,xpath_expression):
    js_code = f"""
    (function() {{
        try {{
            let usernameField = document.evaluate('{username_xpath}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            let passwordField = document.evaluate('{password_xpath}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            let result = document.evaluate('{xpath_expression}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            if (usernameField && passwordField) {{
                usernameField.value = '{username}';
                passwordField.value = '{password}';
                console.log("Username and password filled.");
                console.log("Element found, clicking...");
                result.click();
            }} else {{
                console.log("Username or password field not found.");
            }}
        }} catch (e) {{
            console.error("JavaScript error:", e.message);
        }}
    }})();
    """
    view.page().runJavaScript(js_code)
    
    
def auto_close():
    print("Auto-closing browser and exiting application.")
    browser.close()  # Close the browser
    QApplication.quit()  # Exit the QApplication
    sys.exit(0) 
    
def check_for_keyword(html):
    """Check if the keyword is present in the HTML content of the page."""
    keyword_to_check="logged out"
    if keyword_to_check in html:
        print("Wi-Fi Logged Out Closing application.")
        time.sleep(1)
        app.quit()
    elif "logout" in html:
        print("Keyword found! Closing application.")
        app.quit()
        
         
    
    
app = QApplication(sys.argv)
browser = QWebEngineView()
url = QUrl("http://172.18.10.10:1000/logout?")
browser.setUrl(url)
xpath_to_button = '/html/body/div/div/form/div[3]/button'
username_xpath = '//*[@id="ft_un"]' 
password_xpath = '//*[@id="ft_pd"]'
count = 1

def on_page_loaded():
    global count
    fill_username_password(browser, username_xpath,password_xpath,reg_list[count],pswd,xpath_to_button)
    count+=1
    browser.page().toHtml(check_for_keyword)   
browser.page().loadFinished.connect(on_page_loaded)
browser.show()
app.exec_()

