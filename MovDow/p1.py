import requests
# URL of the video stream or manifest file (if permitted/authorized)
url = "https://www.hotstar.com/in/movies/lover/1271271436/watch"

# Headers and cookies extracted from the browser (must be your own session)
headers = {
    "User-Agent": "Your User-Agent Here",  # Add the actual User-Agent from your browser
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.8",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Brave\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sec-gpc": "1",
    "referrer": "https://www.hotstar.com/",
    "referrerPolicy": "strict-origin-when-cross-origin",
    "body": None,
    "method": "GET",
    "mode": "cors",
    "credentials": "include"
}

# Flattened cookies
cookies = {
    "loc": "ENuMmMAGKAMiuwEIOIlUfPoWLyc7db163Z99T/RctoAOr7YMbjcqfUFzHidanbRDNkpmce00sFVNGl4YF5bXpbXmikfvUoS/2bM+RAvZ3qGVNdCYKhCHeoWETQudjLKuS7pgc3XXPadIfBkrz7vjXj576z/EGtijraZzPjOMk2g0erHFHjoVPkeYz2H+jewt3LqWj2iB7M3lE0YZpvfU5UI2xw8AWkX8LKwmautDDpiN2YsuxFhqGmobarE2lHKFmUzAE77W",
    "userHID": "d3b08a2a82c742ce88ad28fd2d176eb4",
    "_ga_VJTFGHZ5NH": "GS1.2.1745221579.1.0.1745221579.60.0.0",
    "_ga_2PV8LWETCX": "GS1.1.1745221579.1.1.1745221636.3.0.0",
    "userPID": "0f381b0ef4464baa87dafaff01600e4a",
    "sessionUserUP": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IiIsImF1ZCI6InVtX2FjY2VzcyIsImV4cCI6MTc0NTMxMTcwNywiaWF0IjoxNzQ1MjI1MzA3LCJpc3MiOiJUUyIsImp0aSI6IjY0MTk5M2EzMDc2ODRhNGJhY2FkOTgyZDc4NzNmMjIxIiwic3ViIjoie1wiaElkXCI6XCJkM2IwOGEyYTgyYzc0MmNlODhhZDI4ZmQyZDE3NmViNFwiLFwicElkXCI6XCIwZjM4MWIwZWY0NDY0YmFhODdkYWZhZmYwMTYwMGU0YVwiLFwiZHdIaWRcIjpcImY5ZmNkZjkwZDBlNjFmNDliODI2ZTEyMjAzY2QxYjM1MzBkMWMyNGZhN2IwMjliZTZhMDQ4ZDE1YjEwOTQ4M2FcIixcImR3UGlkXCI6XCI1ZmNlN2M3YzgxMzdlN2EyOGE2MzAyMDFmZTQ2ZjE4YzRhNWM0ODQ1ZTc2MmZjNDEzZDQ3NTU3MDlmYjEwODA4XCIsXCJvbGRIaWRcIjpcImQzYjA4YTJhODJjNzQyY2U4OGFkMjhmZDJkMTc2ZWI0XCIsXCJvbGRQaWRcIjpcIjBmMzgxYjBlZjQ0NjRiYWE4N2RhZmFmZjAxNjAwZTRhXCIsXCJpc1BpaVVzZXJNaWdyYXRlZFwiOmZhbHNlLFwibmFtZVwiOlwiVGFydW5cIixcInBob25lXCI6XCI2MzAxNTkyMTEzXCIsXCJpcFwiOlwiMTUyLjU3LjE1MC4xOTFcIixcImNvdW50cnlDb2RlXCI6XCJpblwiLFwiY3VzdG9tZXJUeXBlXCI6XCJudVwiLFwidHlwZVwiOlwicGhvbmVcIixcImlzRW1haWxWZXJpZmllZFwiOmZhbHNlLFwiaXNQaG9uZVZlcmlmaWVkXCI6dHJ1ZSxcImRldmljZUlkXCI6XCI0Y2Q5NGYtNWYyMTZjLTYzMWM1My0zNjYwNGVcIixcInByb2ZpbGVcIjpcIkFEVUxUXCIsXCJ2ZXJzaW9uXCI6XCJ2MlwiLFwic3Vic2NyaXB0aW9uc1wiOntcImluXCI6e1wiU2luZ2xlRGV2aWNlXCI6e1wic3RhdHVzXCI6XCJTXCIsXCJleHBpcryl_z1"
}

# Make the request to get the video content
response = requests.get(url, headers=headers, cookies=cookies)

# Check if the request was successful
if response.status_code == 200:
    # Save the content in chunks to avoid memory issues
    with open("video.ts", "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print("Video downloaded successfully.")
else:
    print(f"Failed to retrieve the video. Status code: {response.status_code}")
