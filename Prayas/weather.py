import requests
import json
from datetime import datetime

now=datetime.now()
print(now)

api_key = "3ae8e6cebf3576a23100de8d3449c274"

url = "http://ip-api.com/json/?fields=61439"
response = requests.get(url)
data = json.loads(response.text)

lat = data['lat']
lon = data['lon']



url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
response = requests.get(url)
data = json.loads(response.text)
temp=data['main']['temp']
print(data)
print("\n \n")
print(temp)

print("\n \n")
'''temp = data['main']['temp']
humidity= data['main']['humidity']
print(temp,"\n \n")
print(humidity)
duration=31
if temp>=24 and temp<=30 and duration>=30:
    if humidity>=16:
        print("kello")
    print(f"Your fan has been on for more than 30 minutes in ",temp,"  temperature \n")'''


