import requests
import os

session_id="27042317315%3APyMoctila2WTbr%3A13%3AAYeqbQJCnSqU66Q4C1HWc5euUuJ7BXSxAmh2uiHBFA"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Cookie": f"sessionid={session_id};"
}




media_url = "https://www.instagram.com/stories/taanishq_14/3487963776375483021/"
media_type = "image" if "image_versions2" in media_url else "video"
        
extension = ".jpg" if media_type == "image" else ".mp4"
filename = f"stories{extension}"
        
with requests.get(media_url, stream=True) as media_response:
       if media_response.status_code == 200:
        with open(filename, "wb") as f:
            for chunk in media_response.iter_content(1024):
                f.write(chunk)
            print(f"Downloaded {media_type} story: {filename}")

