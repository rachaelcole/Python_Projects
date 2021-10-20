#! python3
# getOpenWeather.py - Prints the weather for a location from the command line

APPID = '15616b88f662a39612975210bd21e2b8'

import json
import requests
import sys

# Compute location from command line args
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API
url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s' % (location, APPID)
response = requests.get(url)
response.raise_for_status()

# Un-comment to see the raw JSON text:
# print(response.text)

# Load JSON data into a Python variable
weather_data = json.loads(response.text)

# Print weather descriptions
w = weather_data['list']
print(f'Current weather in {location}:')
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
