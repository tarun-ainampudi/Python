from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import captcha_processing

# Set up Selenium in headless mode
options = Options()
#options.add_argument("--headless")
#options.add_argument("--disable-gpu")
options.add_experimental_option("detach", True)

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
    username="registration number"
    password="password"
    set_login_details(driver,username,password,captcha)
    verify_login(driver)
    
def verify_login(driver):
    if driver.current_url != "https://vtop.vitap.ac.in/vtop/content":
        driver.execute_script(""" window.location.reload(); """)
        login(driver)
    else:
        print("Login Sucessfull")
               

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://vtop.vitap.ac.in/vtop/open/page")
student_form_redirect(driver)
login(driver)


# Close browser
#driver.quit()
