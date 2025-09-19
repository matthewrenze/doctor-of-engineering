import os
import requests

api_key = os.getenv("GOOGLE_SEARCH_KEY")
r = requests.post(
    "https://apikeys.googleapis.com/v2/keys:lookupKey",
    params={"key": api_key},  # this param authenticates the call
    json={"keyString": api_key},
    timeout=30
)
print(r.json())