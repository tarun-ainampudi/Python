import requests
import scanparams

url = "https://www.instagram.com/virat.kohli/"
response = requests.get(url)   

scanparams.parameters_text(response.text)