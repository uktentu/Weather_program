import requests
import datetime
from pprint import pprint

def seperator(data):
    re_data={}
    if len(data)==2:
        print('City that you entered is not found')
    else:
        re_data['date']='Today i.e '+str(datetime.datetime.today().date())+' in '+str(data['name'])
        re_data['coord']='The Coordinates of '+str(data['name'])+' is '+str(data['coord'])
        re_data['temp']='Temperature is '+str(data['main']['temp'])+' F'
        re_data['feels_like']='Feels like '+str(data['main']['feels_like'])+' F'
        re_data['temp_min']='Minimum temperature of the day is '+str(data['main']['temp_min'])+' F'
        re_data['temp_max']='Maximum temperature of the day is '+str(data['main']['temp_max'])+' F'
        re_data['pressure']='Atmospheric pressure of the day is '+str(data['main']['pressure'])+' mb'
        re_data['humidity']='Humidity in '+str(data['name'])+' : '+str(data['main']['humidity'])+' %'
        re_data['country']=str(data['name'])+' is in '+str(data['sys']['country'])
        re_data['w_spped']='Wind speed today in '+str(data['name'])+' is '+str(data['wind']['speed'])+' m/s at an angle of '+str(data['wind']['deg'])+' to the equator'

        for i in re_data:
            print(re_data[i])




API_key='5022636779b5fff5d8f72b7aabae5ca7'

city = input("Enter a City:  ")

Base_url='http://api.openweathermap.org/data/2.5/weather?appid='+API_key+'&q='+city

weather_data=requests.get(Base_url).json()
# pprint(weather_data)
seperator(weather_data)
