import webbrowser
import threading

def open_website(url):
    webbrowser.open(url)

def main():
    # URL of the website you want to open
    website_url = "https://instagram.com"
    
    # Create a new thread to open the website
    thread = threading.Thread(target=open_website, args=(website_url,))
    thread.start()

if __name__ == "__main__":
    main()

