import time
import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Setup Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the college website
driver.get("https://vtop.vitap.ac.in/vtop/login")

# Enter Username and Password
username = "23BCE9846"
password = "t@ruN12345"
driver.find_element(By.ID, "username_field_id").send_keys(username)
driver.find_element(By.ID, "password_field_id").send_keys(password)

# Check for CAPTCHA
def get_captcha_text():
    try:
        captcha_image = driver.find_element(By.ID, "captcha_image_id")
        captcha_image.screenshot("captcha.png")
        image = Image.open("captcha.png")
        captcha_text = pytesseract.image_to_string(image).strip()
        return captcha_text
    except:
        return None

# Reload the page until CAPTCHA is available
while True:
    captcha_text = get_captcha_text()
    if captcha_text:
        break
    else:
        driver.refresh()
        time.sleep(2)  # wait for the page to load

# Enter CAPTCHA and submit
driver.find_element(By.ID, "captcha_field_id").send_keys(captcha_text)
driver.find_element(By.ID, "submit_button_id").click()

# Close the driver after login
time.sleep(5)
driver.quit()
