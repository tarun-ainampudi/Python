import os
import sys
import time
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineProfile, QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QUrl, QTimer

# === Windows Optimizations ===
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--enable-gpu-rasterization --enable-zero-copy"
os.environ["QTWEBENGINE_DISABLE_SANDBOX"] = "1"
os.environ["QTWEBENGINE_DISABLE_GPU"] = "0"

# === Update these from env ===
reg_no = os.getenv("wifi_username")
pswd = os.getenv("wifi_password")

# === Generate registration variants with superscript digits ===
def superscript_to_int(sup_char):
    superscript_map = {
        '⁰': 0, '¹': 1, '²': 2, '³': 3, '⁴': 4,
        '⁵': 5, '⁶': 6, '⁷': 7, '⁸': 8, '⁹': 9,
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
    }
    return superscript_map.get(sup_char, None)

def gen_list(reg_no: str):
    super_script = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
    sup_list = [reg_no]
    for i in sup_list:
        for j in range(len(i)):
            if i[j].isdigit():
                temp = i[0:j] + super_script[superscript_to_int(i[j])] + i[j+1:]
                if temp not in sup_list:
                    sup_list.append(temp)
    return sup_list

reg_list = gen_list(reg_no)

# === Auto fill function using JavaScript ===
def fill_username_password(view, username_xpath, password_xpath, username, password, button_xpath):
    js_code = f"""
    (function() {{
        try {{
            let usernameField = document.evaluate('{username_xpath}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            let passwordField = document.evaluate('{password_xpath}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            let loginButton = document.evaluate('{button_xpath}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            if (usernameField && passwordField && loginButton) {{
                usernameField.value = '{username}';
                passwordField.value = '{password}';
                loginButton.click();
                console.log("Credentials filled and login clicked.");
            }} else {{
                console.log("Element(s) not found.");
            }}
        }} catch (e) {{
            console.error("JS error:", e.message);
        }}
    }})();
    """
    view.page().runJavaScript(js_code)

# === Detect logout keyword in HTML or URL ===
def check_for_keyword(html):
    if "logged out" in html or "logout" in html:
        print("Detected logout message in page content.")
        QTimer.singleShot(1000, app.quit)

def on_url_changed(url):
    if "logout" in url.toString():
        print("Detected logout in URL.")
        QTimer.singleShot(1000, app.quit)

# === PyQt App Setup ===
app = QApplication(sys.argv)
browser = QWebEngineView()

# ✅ FIX: Use QWebEnginePage with persistent profile
profile = QWebEngineProfile("MyProfile", browser)
page = QWebEnginePage(profile, browser)
browser.setPage(page)

# Set login URL and XPaths
url = QUrl("http://172.18.10.10:1000/logout?")
username_xpath = '//*[@id="ft_un"]'
password_xpath = '//*[@id="ft_pd"]'
login_button_xpath = '/html/body/div/div/form/div[3]/button'

browser.setUrl(url)
count = 0

def on_page_loaded(ok):
    global count
    if ok:
        if count < len(reg_list):
            QTimer.singleShot(200, lambda: fill_username_password(
                browser, username_xpath, password_xpath,
                reg_list[count], pswd, login_button_xpath
            ))
            QTimer.singleShot(500, lambda: browser.page().toHtml(check_for_keyword))
            count += 1
        else:
            print("All registration formats tried. Exiting.")
            app.quit()

browser.page().loadFinished.connect(on_page_loaded)
browser.urlChanged.connect(on_url_changed)

browser.show()
sys.exit(app.exec_())
