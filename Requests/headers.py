import requests
import simplejson as json

url = "https://www.googleapis.com/urlshortner/v1/url"
payload = {"longUrl": "http://example.com"}
headers = {"Content-Type": "application/json"}
r = requests.post(url, json=payload, headers=headers)

print(r.headers)
