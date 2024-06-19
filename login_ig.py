import requests
import re
from ParameterFinding import scanparams


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
else:
    print("Failed to log in using session ID")
url = "https://www.instagram.com/"
string=session.get(url).text

# Define the regex pattern to extract the username
pattern = r'"username":"([^"]+)"'

# Use re.search() to find the match
match = re.search(pattern, string)

if match:
    username = match.group(1)
    print("Username:", username)
else:
    print("Username not found")

url = f"https://www.instagram.com/{username}/followers/"
string=session.get(url).text

scanparams.parameters_text(string)