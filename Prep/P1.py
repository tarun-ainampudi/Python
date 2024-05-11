import requests

def check_status_code(url):
    try:
        response = requests.get(url,timeout=0.04)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print(f"Success! Status code 200 - {url} is up and running.")
        else:
            print(f"Warning! {url} responded with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        # Request error occurred (e.g., connection timeout, invalid URL)
        if "SSL" in f"Error: Failed to connect to {url}. Exception: {e}":
            print(f"Error: Failed to connect to {url}. Exception: {e}")
# Example usage:
for i in range(65536):
    url_to_check = "https://172.18.10.10:"+str(i)+"/login?"
    check_status_code(url_to_check)



