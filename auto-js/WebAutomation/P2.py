from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import captcha_processing
import os
import base64
import json
import time
import csv

# Set up Selenium in headless mode
options = Options()
#1options.add_argument("--headless")
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
    if len(str(captcha_text))==6:
        return captcha_text
    else:
        captcha_processing.edge_detection("output.png","output.png")
        captcha_text = captcha_processing.img_to_text("output.png")
        return captcha_text
    
def set_login_details(driver,uname,pswd,captc):
    result = driver.execute_script("""
       document.querySelector("#username").value=arguments[0];
       document.querySelector("#password").value=arguments[1];
       document.querySelector("#captchaStr").value=arguments[2];
    """,uname,pswd,captc)
    
def login(driver):
    captcha = captcha_load(driver)
    username=os.getenv("VTOP_USERNAME")
    password=os.getenv("VTOP_PASSWORD")
    set_login_details(driver,username,password,captcha)
    verify_login(driver)
    
def verify_login(driver):
    result  = driver.execute_script("""                            
  document.querySelector("#submitBtn").click();
    """)
    if "https://vtop.vitap.ac.in/vtop/content" in driver.current_url:
        print("Login Sucessfull")
    else:
        driver.execute_script(""" window.location.reload(); """)
        login(driver)

def get_authorisedID(driver):
    result  = driver.execute_script("""                            
    var data = $('#authorizedIDX').val();
    return data;
    """)
    return result

def get_csrf(driver):
    result  = driver.execute_script("""                            
    var data = $('input[name="_csrf"]').val();
    return data;
    """)
    return result

def create_directory(auid):
    if not os.path.exists(auid):
        os.mkdir(auid)

def download_img(driver,auid):
    create_directory(auid)
    image_url ='https://vtop.vitap.ac.in/vtop/users/image/?id='+auid
    js_code = """
    var callback = arguments[arguments.length - 1];
    fetch(arguments[0])
      .then(response => response.blob())
      .then(blob => {
          var reader = new FileReader();
          reader.onloadend = function() {
              callback(reader.result);  // returns data URL
          };
          reader.readAsDataURL(blob);
      })
      .catch(err => callback(null));
    """
    data_url = driver.execute_async_script(js_code, image_url)
    if data_url:
    # Remove data URL header: "data:image/png;base64,"
      header, encoded = data_url.split(",", 1)
      image_data = base64.b64decode(encoded)
      with open(os.path.join(auid, auid + ".png"), "wb") as f:
        f.write(image_data)
      print("Image saved.")
    else:
      print("Failed to fetch image.")

def get_semids(driver, auid, csrf):
    result = driver.execute_script("""
        // Get the values from the arguments passed from Python
        var authorizedID = arguments[0];
        var csrfToken = arguments[1];

        // Build the data string by concatenating the variables into the URL-encoded string.
        var data = "verifyMenu=true" +
                   "&authorizedID=" + authorizedID +
                   "&_csrf=" + csrfToken +
                   "&nocache=" + new Date().getTime();

        // Prepare an empty response object that will be filled in the AJAX success callback.
        var response = {};

        // Use jQuery's ajax function to perform a synchronous POST request.
        $.ajax({
            type: 'POST',
            url: 'academics/common/StudentTimeTable',
            data: data,
            async: false,  // Synchronous call; the code waits until the request is complete.
            success: function(res) {
                if(res.toLowerCase().includes('time table')) {
        var doc = new DOMParser().parseFromString(res, 'text/html');
        var options = doc.getElementById('semesterSubId').getElementsByTagName('option');
        var semesters = [];
        for(var i = 0; i < options.length; ++i) {
            if(!options[i].value) {
                continue;
            }
            var semester = {
                name: options[i].innerText,
                id: options[i].value
            };
            semesters.push(semester);
        }
        response.semesters = semesters;
    }
}
});
return response;
    """, auid, csrf)
    return result

def get_attendance(driver,auid,csrfid,subsemid):
    """ json{
        attendance : {cse1005:{slot:L2+L3,attended:24,total:28,percentage:97,percentage1:100},
        cse1005:{slot:A2+TA2,attended:25,total:27,percentage:97,percentage1:100}
        cse2007:{slot:A2+TA2,attended:25,total:27,percentage:97,percentage1:100}
        }
    }
    """
    result = driver.execute_script("""var authorizedID = arguments[0];
var csrfToken = arguments[1];
var subsemID = arguments[2];

var data = "_csrf=" + csrfToken + "&semesterSubId=" + subsemID + "&authorizedID=" + authorizedID;
var response = {
    attendance: []
};

$.ajax({
    type: 'POST',
    url: 'processViewStudentAttendance',
    data: data,
    async: false, // Consider changing to true
    success: function (res) {
        var doc = new DOMParser().parseFromString(res, 'text/html');
        var thead = doc.querySelector('#AttendanceDetailDataTable > thead');
        var headings = thead.getElementsByTagName('td');

        var course_detail, class_detail, faculty_detail, attended_classes, total_classes, attendance_percentage, cat2_fat_period_percentage;

        for (var i = 0; i < headings.length; ++i) {
            var heading = headings[i].innerText.toLowerCase();

            if (heading.includes('course') && heading.includes('detail')) {
                course_detail = i;
            } else if (heading.includes('class') && heading.includes('detail')) {
                class_detail = i;
            } else if (heading.includes('faculty') && heading.includes('detail')) {
                faculty_detail = i;
            } else if (heading.includes('attended') && heading.includes('classes')) {
                attended_classes = i;
            } else if (heading.includes('total') && heading.includes('classes')) {
                total_classes = i;
            } else if (heading.includes('attendance') && heading.includes('percentage')) {
                attendance_percentage = i;
            } else if (heading.includes('cat2') && heading.includes('fat') && heading.includes('period') && heading.includes('percentage')) {
                cat2_fat_period_percentage = i;
            }
        }

        var tbody = doc.querySelector('#AttendanceDetailDataTable > tbody');
        var cells = tbody.getElementsByTagName('td');

        for (var i = 0; i < Math.ceil(cells.length / headings.length); i++) {
            var course_index = course_detail + i * headings.length;
            var class_index = class_detail + i * headings.length;
            var faculty_index = faculty_detail + i * headings.length;
            var attended_index = attended_classes + i * headings.length;
            var total_index = total_classes + i * headings.length;
            var percentage_index = attendance_percentage + i * headings.length;
            var cat2_fat_index = cat2_fat_period_percentage + i * headings.length;

            var attendanceObject = {};
            attendanceObject.course_detail = cells[course_index].innerText.trim();
            attendanceObject.class_detail = cells[class_index].innerText.trim();
            attendanceObject.faculty_detail = cells[faculty_index].innerText.trim();
            attendanceObject.attended_classes = parseInt(cells[attended_index].innerText.trim());
            attendanceObject.total_classes = parseInt(cells[total_index].innerText.trim());
            attendanceObject.attendance_percentage = parseInt(cells[percentage_index].innerText.trim());
            attendanceObject.cat2_fat_period_percentage = parseInt(cells[cat2_fat_index].innerText.trim());

            response.attendance.push(attendanceObject);
        }
    }
});

return response;
""",auid,csrfid,subsemid)
    return result


def json_to_csv(data, file_path):
    """
    Converts JSON data to a CSV file.
    If the CSV exists, it updates rows based on 'class_detail', else it creates a new file.
    Maintains a specified column order.

    :param data: Dictionary containing the JSON data with an "attendance" key.
    :param file_path: Path where the CSV file should be saved.
    """
    if "attendance" not in data or not isinstance(data["attendance"], list) or not data["attendance"]:
        print("Invalid data format")
        return

    # Define custom column order
    column_order = [
        "course_detail",
        "faculty_detail",
        "class_detail",
        "attended_classes",
        "total_classes",
        "attendance_percentage",
        "cat2_fat_period_percentage"
    ]

    new_records = {entry["class_detail"]: entry for entry in data["attendance"]}
    updated_records = []

    # Check if the file exists and read existing data
    if os.path.exists(file_path):
        with open(file_path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            existing_records = {row["class_detail"]: row for row in reader}

        # Update existing records & add new ones
        existing_records.update(new_records)
        updated_records = list(existing_records.values())
    else:
        updated_records = list(new_records.values())

    # Write updated records to CSV in the specified order
    with open(file_path, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=column_order)
        writer.writeheader()
        for record in updated_records:
            writer.writerow({col: record.get(col, "") for col in column_order}) # Enforce order
    print("Attendance CSV Updated")

driver = webdriver.Chrome(service=Service(r"C:\Users\tarun\Desktop\Python\auto-js\WebAutomation\chromedriver-win64\chromedriver.exe"), options=options)
driver.get("https://vtop.vitap.ac.in/vtop/open/page")
student_form_redirect(driver)
login(driver)
authorisedID = get_authorisedID(driver)
csrfID=get_csrf(driver)
download_img(driver,authorisedID)
semids = get_semids(driver,authorisedID,csrfID)#{'semesters': [{'id': 'AP2024254', 'name': 'Winter Semester 2024-25'}, {'id': 'AP2024252', 'name': 'FALL SEM 2024-25'}, {'id': 'AP2023247', 'name': 'WIN  SEM (2023-24) FRESHERS'}, {'id': 'AP2023243', 'name': 'FALL SEM (2023-24) Freshers'}]}
subsemID = semids['semesters'][0]['id']
attendace=get_attendance(driver,authorisedID,csrfID,subsemID)
json_to_csv(attendace,f"{authorisedID}\\attendance.csv")

# Close browser
#driver.quit()
