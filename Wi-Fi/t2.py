import http.client
import urllib.parse
import re
import time

LOGIN_URL = "172.18.10.10:1000"
USERNAME = "23BCE9846"
PASSWORD = "Admin@VITAP"
Inx = 1
us_lis = []


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

def send_request(method, endpoint, params=None, headers=None):
    """Helper function to send HTTP requests."""
    conn = http.client.HTTPConnection(LOGIN_URL)
    conn.request(method, endpoint, params, headers or {})
    response = conn.getresponse()
    response_data = response.read().decode()
    conn.close()
    return response, response_data


def log_in():
    global Inx
    """Logs into the Wi-Fi portal."""
    # Fetch the magic token
    response, html = send_request("GET", "/login?")
    if response.status != 200:
        print("Failed to fetch login page:", response.status, response.reason)
        return

    magic_match = re.search(r'name="magic" value="([^"]+)"', html)
    if not magic_match:
        print("Magic token not found.")
        return

    magic = magic_match.group(1)
    #print(f"Magic token: {magic}")
    controller = True
    # Perform login
    while(controller):
        params = urllib.parse.urlencode({
        'username': us_lis[Inx],
        'password': PASSWORD,
        '4Tredir': 'http://172.18.10.10:1000/login?',
        'magic': magic})
        headers = {"Content-type": "application/x-www-form-urlencoded"}
        response, response_data = send_request("POST", "/login?", params, headers)
        if("over" in response_data.lower()):
            controller = True
            Inx = (Inx + 1) % 64
        else:
            controller=False
    if "keepalive" in response_data.lower():
        print(f"Logged in successfully - {us_lis[Inx]}")
    else:
        print("Login failed:", response.status, response.reason)



def log_out():
    """Logs out of the Wi-Fi portal."""
    response, data = send_request("GET", "/logout?")
    if response.status == 200:
        if("successfully" in data.lower() and "logged" in data.lower() and "out" in data.lower()):
            print("Logged out successfully")
        else:
            #print("Already logged out calling log_in().............")
            log_in()
    else:
        print("Logout failed:", response.status, response.reason)


# Main execution
if __name__ == "__main__":
    us_lis = gen_list(USERNAME)
    log_out()
    time.sleep(1.5)
