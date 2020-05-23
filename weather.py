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
