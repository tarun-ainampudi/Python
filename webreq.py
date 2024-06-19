import requests
from ParameterFinding import scanparams

url = "https://vtop.vitap.ac.in/vtop"
response = requests.get(url)   
print(response.text)