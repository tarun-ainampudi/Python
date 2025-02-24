import requests
import os

# Session ID for authentication
session_id = "27042317315%3AVLz0ACmWXd4vso%3A15%3AAYd8KSzXCZMv6uK5Xn9XQ9D7RVSj5JLdM-PvTt4bbg"  # Replace with your session ID
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Cookie": f"sessionid={session_id};"
}

# Instagram user ID (use an API call to get this if needed)
target_user_id = "taanishq_14"  # Replace with the actual user ID of the target account

# Endpoint to retrieve the user's story
stories_url = f"https://i.instagram.com/api/v1/feed/user/{target_user_id}/reel_media/"
response = requests.get(stories_url, headers=headers)

# Check if the request was successful
if True:
    stories = response.json().get("items", [])
    print(f"Found {len(stories)} stories.")
    
    # Create a directory to store downloaded stories
    os.makedirs("stories", exist_ok=True)
    
    # Loop through each story and download it
    for story in stories:
        if "image_versions2" in story:
            media_url = story["image_versions2"]["candidates"][0]["url"]
            extension = ".jpg"
            media_type = "image"
        elif "video_versions" in story:
            media_url = story["video_versions"][0]["url"]
            extension = ".mp4"
            media_type = "video"
        else:
            print("Unknown media type.")
            continue
        
        # Save each story
        story_id = story["id"]
        filename = f"stories/{story_id}{extension}"
        
        with requests.get(media_url, stream=True) as media_response:
            if media_response.status_code == 200:
                with open(filename, "wb") as f:
                    for chunk in media_response.iter_content(1024):
                        f.write(chunk)
                print(f"Downloaded {media_type} story: {filename}")
            else:
                print(f"Failed to download {media_type} story: {story_id}")
else:
    print("Failed to retrieve stories. Check session ID or user privacy settings.")
