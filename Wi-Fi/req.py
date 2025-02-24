import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

# Initialize a session
session = requests.Session()
session.headers.update(headers)

# URL of the page to scrape
url = "http://172.18.10.10:1000/logout?"

# Perform a GET request
response = session.get(url)