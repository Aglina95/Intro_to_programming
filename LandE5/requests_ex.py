# Write your code here :-)
import requests

print(requests.get("http://wttr.in?format=3").text)
