from pythonping import ping
from keys import api_key
import requests


class WeatherLoc:
    all = [] 

    def __init__(self, city: str, country: str):
        # Assign to object
        self.city = city
        self.country = country

        # Action to execute upon instantiation
        WeatherLoc.all.append(self)

    def inputquery(self):
        # takes instance and creates a string from its attributes 
        location = f"{self.city},{self.country}"
        return location


    def getweather(self, str):
    # func to retrieve weather info
        url = f"http://api.openweathermap.org/data/2.5/weather?q={str}&appid={api_key}" # the f creates a format str.
        response = requests.get(url).json() #converts response into JSON allowing access to individual attributes
        country = response['sys']['country']
        place = response['name']
        gps = response['coord']
        temp = response['main']['temp']
        temp = round((temp -273.15),1) # Converts Kalvin into Celcius.
        output = f"In the city {place} of {country}. Location: {gps}, the temperature today is {temp}\u00b0C  "
        return print(output)


    @classmethod # Decorator, allows method to be accessed at class level rather than object level.
    def instantiate_from_input(cls):
        # Creates an instance from input
        var_inst = []
        inst_country = str(input('Choose a Country: '))
        inst_city = str(input('Now choose a city within that country: '))
        var_inst.append(inst_city)
        var_inst.append(inst_country)
        print(var_inst)
        inst_output = WeatherLoc(var_inst[0],var_inst[1])
        return inst_output.getweather(inst_output.inputquery())

    def __repr__(self):
        return f"WeatherLoc('{self.city}','{self.country}')" # documentation recommends keep format identical to instance 



'''---------Main function--------'''
def main():
    WeatherLoc.instantiate_from_input()

if __name__ == '__main__':
        main()

'''
instantiate_from_input(cls):
By default, methods need an existing instance to be called. In this case, 'Class method decorator' is used as we need to call this method 
BEFORE an instance is created. To do this, we make this function s.t. it can be called in the CLASS LEVEL.
i.e. WeatherLoc.instantiate_from_input() 
The "cls" is the class argument, it is called for the method to run
'''


