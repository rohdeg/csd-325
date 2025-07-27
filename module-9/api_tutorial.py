""" api_tutorial by Garrett Rohde
    07/27/2025
    Assignment 9.2
    completing API tutorial from https://www.dataquest.io/blog/api-in-python/
"""

import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("http://api.open-notify.org/astros.json")

print(response.status_code)

jprint(response.json())