import geckoboard
from pythonping import ping
import requests

city_name = "Cuiabá,Brazil"
api_key = "71062a67366b8edf1ba3e48d950ddc2d"

def getweather(api_key,city):
    # func to retrieve weather info 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}" # the f creates a format str.
    response = requests.get(url).json() #converts response into JSON allowing access to individual attributes

    country = response['sys']['country']
    place = response['name']
    gps = response['coord']
    temp = response['main']['temp']
    temp = round((temp -273.15),1) # Converts Kalvin into Celcius.
    print(response) # This reveals complete datatable.
    print('I am from ' + str(country)+', '+ place,gps,str(temp)+ '\u00b0' +'C')
    

getweather(api_key, city_name)


"""Connecting my Weather API to Geckoboard"""
client = geckoboard.client('01eebb785fa1e137ffe6ffda3279aa1b')

# Check if API key for Geckboard is valid.
getresp = client.ping() 
if getresp:
    print('Response from Geckoboard Successful')
else:
    print('Error.')

# field = { 
#     "coord":{"lon": 'number', "lat": 'number'},
#     "main":{"temp": 'number'} ,
#     "sys":{"country": [], "name":[]}}


# dataset = client.datasets.find_or_create(f'http://api.openweathermap.org/data/2.5/weather?id={803}&appid={"71062a67366b8edf1ba3e48d950ddc2d"}', field)
