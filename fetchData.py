import json
import requests
from requests.exceptions import HTTPError

username = "interviewee"
password = "muchpassword"

try:
    response = requests.get('https://hgy780tcj2.execute-api.eu-central-1.amazonaws.com/dev/data', auth = (username, password))
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    print("Entire JSON response")
    print(jsonResponse)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')


# Serializing json  
json_object = json.dumps(jsonResponse, indent = 1) 
  
# Writing to data.json 
with open("data.json", "w") as outfile: 
    outfile.write(json_object) 