import requests
import json
import sys

prompt = sys.argv[1] # Retrieve the prompt from command-line arguments
url = "http://1343-35-240-238-206.ngrok-free.app/generate"
payload = {"prompt": prompt}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(payload), headers=headers)

if response.status_code == 200:
    print(json.dumps(response.json()))
else:
    print(f"Failed to make request. Status code: {response.status_code}")