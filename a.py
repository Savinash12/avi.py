if 5>2:
    print("5 is greater than 2")
x = "Avinash"
print(type(x)) 
print("Wel come to the world of Python")
import requests

response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())
