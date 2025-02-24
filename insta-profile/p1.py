
import re
from bs4 import BeautifulSoup
import requests


id = ""
url = "https://www.instagram.com/"+id

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Find all <img> tags and extract the 'src' attribute
image_urls = [img['src'] for img in soup.find_all('img') if 'src' in img.attrs]

# Display all image URLs
print("All Image URLs:")
for idx, url in enumerate(image_urls, start=1):
    print(f"{idx}: {url}")


