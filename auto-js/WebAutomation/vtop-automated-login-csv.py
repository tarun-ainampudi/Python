from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import captcha_processing
import os
import pandas as pd
from datetime import datetime

# Set up Selenium in headless mode
options = Options()
#options.add_argument("--headless")
#options.add_argument("--disable-gpu")
options.add_experimental_option("detach", True)

csv_file_path = "login_attempts.csv"

no_of_attempts = 0

def student_form_redirect(driver) :
    result = driver.execute_script("""
    var student_button =  document.querySelector("#stdForm > a > div > div.flex-grow-1 > button")
    if(student_button){
        student_button.click()
    }
    else{
        console.log("student_button not found")
    }""")
    return result

def captcha_load(driver) :
    global no_of_attempts
    no_of_attempts +=1
    result = driver.execute_script("""
        var xpath = '//*[@id="captchaBlock"]/img';
        var result = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
        var captchaElement = result.singleNodeValue;
        if (captchaElement) {
            return captchaElement.getAttribute('src');
        } else {
            console.log("Captcha xpath not found");
            return null;
        }
    """)
    if result is not None:
        captcha_text = get_captcha_text(result)
        print(captcha_text)
        return captcha_text
    else:
        driver.execute_script(""" window.location.reload(); """)
        captcha_load(driver)
        
def get_captcha_text(captcha_url):
    captcha_processing.download_image_urllib(captcha_url,"captcha.jpeg")
    captcha_processing.remove_white_from_image("captcha.jpeg","output.png")
    captcha_text = captcha_processing.img_to_text("output.png")
    return captcha_text
    
def set_login_details(driver,uname,pswd,captc):
    result = driver.execute_script("""
       document.querySelector("#username").value=arguments[0];
       document.querySelector("#password").value=arguments[1];
       document.querySelector("#captchaStr").value=arguments[2];
       document.querySelector("#submitBtn").click();
    """,uname,pswd,captc)
    
def login(driver):
    captcha = captcha_load(driver)
    username=os.getenv("VTOP_USERNAME")
    password=os.getenv("VTOP_PASSWORD")
    set_login_details(driver,username,password,captcha)
    verify_login(driver)
    
def verify_login(driver):
    if "https://vtop.vitap.ac.in/vtop/content" in driver.current_url:
        update_csv()
        print("Login Sucessfull")
    else:
        driver.execute_script(""" window.location.reload(); """)
        login(driver)
               
def update_csv():
    """
    Adds a new login attempt entry to the specified CSV file.

    Parameters:
    - no_of_attempts (int): Number of attempts made.
    - file_path (str): Path to the CSV file where logs should be stored.
    """
    global no_of_attempts
    global csv_file_path
    # Get the current timestamp
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Determine login status based on attempts
    status = "Success" if no_of_attempts == 1 else "Failure"

    # Check if the CSV file exists
    if os.path.exists(csv_file_path):
        # Read the existing file
        df = pd.read_csv(csv_file_path)
        # Create a new row as a DataFrame
        new_row = pd.DataFrame([[timestamp, status, no_of_attempts]], columns=df.columns)
        # Append the new row
        df = pd.concat([df, new_row], ignore_index=True)
    else:
        # Create a new DataFrame with column headers
        df = pd.DataFrame([[timestamp, status, no_of_attempts]], columns=["Timestamp", "Status", "No_of_Attempts"])

    # Save back to CSV
    df.to_csv(csv_file_path, index=False)

    

driver = webdriver.Chrome(service=Service(r"C:\Users\tarun\Desktop\Python\auto-js\WebAutomation\chromedriver-win64\chromedriver.exe"), options=options)
driver.get("https://vtop.vitap.ac.in/vtop/open/page")
student_form_redirect(driver)
login(driver)


# Close browser
#driver.quit()
