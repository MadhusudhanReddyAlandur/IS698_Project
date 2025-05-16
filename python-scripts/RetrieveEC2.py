import requests

url = "http://169.254.169.254/latest/meta-data/"
response = requests.get(url)
print("Instance Metadata:\n", response.text)
