import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineProfile, QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QTimer
import sys
import time


app = QApplication(sys.argv)
browser = QWebEngineView()
url = QUrl("http://172.18.10.10:1000/logout?")
browser.setUrl(url)

student_xpath = '//*[@id="stdForm"]/a/div/div[2]/button'
captcha_xpath = '//*[@id="captchaBlock"]/img'

def click_student():
    js_code="""function clickButtonByXPath(xpath) {
  const element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
  if (element) {
    element.click(); // Simulate a click on the element
    console.log("Button clicked!");
  } else {
    console.log("No element found for the given XPath");
  }
}"""

browser.page().loadFinished.connect()
browser.show()