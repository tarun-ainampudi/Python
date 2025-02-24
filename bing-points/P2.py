import os
import time

# Path to the Chrome executable
chrome_path = r'C:\Users\tarun\Desktop\Python\bing-points\chrome.exe'  # Ensure this path is correct

index = 0
ntabs = 5
tgap = 1  # Time gap between opening tabs
query_list = ["query1", "query2", "query3"]  # Example queries

for i in range(index, index + ntabs):
    query = query_list[i % len(query_list)]
    url = f"https://www.bing.com/search?q={query}&PC=U316&FORM=CHROMN"
    
    # Properly quote the path and URL
    command = f'"{chrome_path}" --new-tab "{url}" --disable-background-mode --disable-extensions'
    os.system(command)  # Execute the command
    
    time.sleep(tgap)
