import instaloader

# Initialize Instaloader
L = instaloader.Instaloader()

# Load session ID
session_id = "27042317315%3APyMoctila2WTbr%3A13%3AAYeqbQJCnSqU66Q4C1HWc5euUuJ7BXSxAmh2uiHBFA"  # Replace with your actual session ID
L.context.session = session_id
L.context._session.cookies.set('sessionid', session_id)

# Target user whose stories you want to download
target_user = "tarun.fy"

# Get the target user's ID
profile = instaloader.Profile.from_username(L.context, target_user)

# Download stories
for story in L.get_stories(userids=[profile.userid]):
    for item in story.get_items():
        L.download_storyitem(item, target=f"{target_user}_stories")
