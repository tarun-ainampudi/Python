import requests
username=input("Enter Username:").lower().split()
def check_status_code_insta(url,username):
    try:
        response = requests.get(url)
        if "<title>Instagram</title>" in str(response.content) and username!="instagram":
           print(f'Username : "{username}" is Available')
        elif response.status_code==200:
            print(f'Username : "{username}" is not Available')
            print(f"Refer Profile Link : {url}")
        else:
            print("Error Occured")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
#instagram
if len(username)==1:
    username=username[0]
    url = "https://www.instagram.com/"+username
    check_status_code_insta(url,username)

    