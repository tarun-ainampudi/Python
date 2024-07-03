import requests
from ParameterFinding import scanparams

# Headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://vtop.vitap.ac.in/vtop/"
}

# Initialize a session
session = requests.Session()
session.headers.update(headers)

# URL of the page to scrape
url = "https://vtop.vitap.ac.in/vtop/login"

# Perform a GET request
response = session.get(url)

# Debugging: print the status code and headers
print(f"Status Code: {response.status_code}")
print(f"Response Headers: {response.headers}")

# Check if the request was successful
if response.status_code == 200:
    # Print the response text for debugging
    print(response.text)

    # Use scanparams to find parameters in the response text
    scanparams.parameters_text(response.text)
else:
    print("Failed to retrieve the page. Please check the URL and your network connection.")
