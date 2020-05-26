#v.1.0
#5d9d9f7178756dbc78d68958da985841
listKey = ['weather']

s_city = input('Enter city: ')
import requests
#s_city = "Moscow,ru"
appid = "5d9d9f7178756dbc78d68958da985841"
try:
	res = requests.get("http://api.openweathermap.org/data/2.5/find",
		params={'q': s_city, 'APPID': appid})
	data = res.json()
	for k, v in data['list'][1].items():
		print(k, v)
except Exception as e:
	print("Exception (find):", e)
	pass

#-----------------------------------------------------------------------------------------------------
#v.1.1

#5d9d9f7178756dbc78d68958da985841
listKey = ['weather']

import requests
from geopy.geocoders import Nominatim

appid = "5d9d9f7178756dbc78d68958da985841"

def weather_data(lantitude, lontitude):
	try:
		res = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=' + str(lantitude) + '&lon=' + str(lontitude) + '&exclude=hourly,daily&units=metric&appid=' + appid)
		#print(res.text)
		data = res.json()
		for k, v in data.items():
			print(v['humidity'])
	except Exception as e:
		print("Exception (find):", e)
		
def geo_location():
	locator = Nominatim (user_agent = 'myGeocoder')
	location = locator.geocode ('Moscow')
	return location.latitude, location.longitude
	
lat, lon = geo_location()
weather_data(lat, lon)

