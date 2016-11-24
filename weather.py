import requests

payload = {'apikey': 'xxxxxxxxxxxxxxxxxxxxxx', 'q': 'Chennai', 'language': 'en-us'}

response = requests.get('http://dataservice.accuweather.com/locations/v1/cities/autocomplete', params=payload)

location_key = response.json()[0]['Key']

print 'Location Key for %s' % response.json()[0]['LocalizedName'], response.json()[0]['Key']

# For getting weather details

payload_weather = {'apikey': 'xxxxxxxxxxxxxxxxxxxxxxxx', 'details': 'true', 'language': 'en-us'}

response_weather = requests.get('http://dataservice.accuweather.com/currentconditions/v1/%s' % location_key, params=payload_weather)

print "Weather Details for %s:" % response.json()[0]['LocalizedName'], response_weather.status_code

for weather in response_weather.json():

    print "Weather Condition:", weather['WeatherText']
    print "Temperature:", str(weather['Temperature']['Metric']['Value']) + ' ' + weather['Temperature']['Metric']['Unit']
    print "Humidity:", weather['RelativeHumidity']
    print "Wind", str(weather['Wind']['Speed']['Metric']['Value'])+ ' ' + weather['Wind']['Speed']['Metric']['Unit']
