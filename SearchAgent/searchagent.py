import requests
username=input("Enter Username:")
def print_status_message(status_code):
    if isinstance(status_code, int):
        if status_code == 200:
            print("The request was successful (200 OK).")
        elif status_code == 404:
            print("The requested resource was not found (404 Not Found).")
        elif status_code == 500:
            print("The server encountered an internal error (500 Internal Server Error).")
        elif 200 <= status_code < 300:
            print(f"Success with status code {status_code}.")
        elif 300 <= status_code < 400:
            print(f"Redirection with status code {status_code}.")
        elif 400 <= status_code < 500:
            print(f"Client error with status code {status_code}.")
        elif 500 <= status_code < 600:
            print(f"Server error with status code {status_code}.")
        else:
            print(f"Received unexpected status code {status_code}.")
    else:
        print(status_code)
def check_status_code_insta(url,username):
    try:
        response = requests.get(url)
        if "<title>Instagram</title>" in str(response.content) and username!="instagram":
           print("Page Not Found")
        else:
            print_status_message(response.status_code)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
#instagram
url = "https://www.instagram.com/"+username
check_status_code_insta(url,username)