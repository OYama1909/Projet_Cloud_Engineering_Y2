import requests

response = requests.get("http://localhost:5000/votre_endpoint")
if response.status_code == 200:
    data = response.json()
    print(data)
