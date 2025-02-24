import requests
import json

apikey = '56a8fbcf7bce4e1895c115816252402'
url = "http://api.weatherapi.com/v1/current.json?key=56a8fbcf7bce4e1895c115816252402&q=Manila&aqi=no"
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_c')
condition = weather_json.get('current').get('condition').get('text')

print("Today's weather in Manila is", condition, 'and', temp, 'celcius')

# print(weather_json)

# Pretty print the JSON response
print(json.dumps(weather_json, indent=2, sort_keys=True))



