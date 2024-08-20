from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import base64
from PIL import Image
from io import BytesIO


service = Service("C:\\Users\\tarun\\Desktop\\Python\\Web Browser\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

url = "https://vtop.vitap.ac.in/vtop/login"
driver.get(url)

student_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="stdForm"]/a/div/div[2]/button')))
student_button.click()

username = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,'username')))
username.send_keys("REGISTRATION NUMBER")
password = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,'password')))
password.send_keys("PASSWORD")

captcha = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="captchaBlock"]/img')))

captcha_url=captcha.get_attribute("src")

base64_image = captcha_url.split(",")[1]

# Decode the base64 string into bytes
image_data = base64.b64decode(base64_image)

image = Image.open(BytesIO(image_data))

# Save the image to a file
image.save("captcha.jpg")  # You can change the filename and extension as needed

print("CAPTCHA image saved successfully!")

input("Press Enter to close the browser...")

driver.quit() 
