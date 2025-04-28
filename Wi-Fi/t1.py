import http.client
import urllib.parse
import re
import time

LOGIN_URL = "172.18.10.10:1000"
USERNAME = "23BCE9846"
PASSWORD = "Admin@VITAP"


def send_request(method, endpoint, params=None, headers=None):
    """Helper function to send HTTP requests."""
    conn = http.client.HTTPConnection(LOGIN_URL)
    conn.request(method, endpoint, params, headers or {})
    response = conn.getresponse()
    response_data = response.read().decode()
    conn.close()
    return response, response_data


def log_in():
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
    print(f"Magic token: {magic}")

    # Perform login
    params = urllib.parse.urlencode({
        'username': USERNAME,
        'password': PASSWORD,
        '4Tredir': 'http://172.18.10.10:1000/login?',
        'magic': magic
    })
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    response, response_data = send_request("POST", "/login?", params, headers)

    if response.status == 200:
        print("Logged in successfully")
    else:
        print("Login failed:", response.status, response.reason)



def log_out():
    """Logs out of the Wi-Fi portal."""
    response, _ = send_request("GET", "/logout?")
    if response.status == 200:
        print("Logged out successfully")
    else:
        print("Logout failed:", response.status, response.reason)


# Main execution
if __name__ == "__main__":
    log_out()
    log_in()
    time.sleep(3)