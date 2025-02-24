import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineProfile, QWebEngineView
from PyQt5.QtCore import QUrl
import sys
import time

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
    print("Generated JavaScript for filling username and password:\n") 
    view.page().runJavaScript(js_code)
    

app = QApplication(sys.argv)
browser = QWebEngineView()

# Set cache directory to avoid permission errors
cache_dir = os.path.expanduser("~/.custom_qt_cache")
os.makedirs(cache_dir, exist_ok=True)
QWebEngineProfile.defaultProfile().setCachePath(cache_dir)
QWebEngineProfile.defaultProfile().setPersistentStoragePath(cache_dir)

url = QUrl("http://172.18.10.10:1000/logout?")
browser.setUrl(url)
xpath_to_button = '/html/body/div/div/form/div[3]/button'
username_xpath = '//*[@id="ft_un"]' 
password_xpath = '//*[@id="ft_pd"]'
username = "²³BCE7452"
password = "HH9jzUjy"

def on_page_loaded():
    print("Page loaded\nattempting to fill username , password")
    fill_username_password(browser, username_xpath, password_xpath, username, password,xpath_to_button)
    print("Button clicked succesfully")
    
browser.page().loadFinished.connect(on_page_loaded)
browser.show()
sys.exit(app.exec_())


