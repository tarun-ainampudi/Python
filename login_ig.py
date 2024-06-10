import requests

# Your Instagram session ID (obtained from the browser)
SESSION_ID = 'sessionid'

# Headers to mimic a legitimate browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

# URL for Instagram
INSTAGRAM_URL = 'https://www.instagram.com/'

# Initialize a session
session = requests.Session()
session.headers.update(headers)

# Set the session ID cookie
session.cookies.set('sessionid', SESSION_ID)

# Verify login by accessing the profile page
profile_url = f'https://www.instagram.com/accounts/edit/'
profile_response = session.get(profile_url)

if profile_response.ok:
    print("Successfully logged in using session ID")
    # You can now perform further requests using the session object
    # For example, get the home page
    home_response = session.get(INSTAGRAM_URL)
    print(home_response.text)
else:
    print("Failed to log in using session ID")
