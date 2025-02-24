import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineProfile, QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QTimer
import sys
import time
app = QApplication(sys.argv)
browser = QWebEngineView()
url = QUrl("https://vtop1.vitap.ac.in/winaddordrop2425/login")
browser.setUrl(url)
browser.page()
browser.show()
sys.exit(app.exec_())