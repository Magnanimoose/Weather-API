# Weather-API
This app receives users location input and returns the current weather in said region. 
## How to Setup
1. First of all download the repository: 
```
git clone https://github.com/Magnanimoose/Weather-API/
```
2. Now you need to create your own personal API key. [**Click here**](https://home.openweathermap.org/users/sign_in) to create an account with openweather.org 
and then generate your unique key.

3. Create a new python file: ```keys.py``` inside the directory.
In this file, add the variable ```api_key``` and attribute it with your newly acquired key in ```string()``` formatting. Save and close the file.

4. Now create and activate your python virtual environment. To do so, on your terminal type 
```
python3 -m venv [name of your venv] 
```
Now to activate it, for Linux, type:
```
. [name of your venv]/bin/activate
```

5. With your venv activated now install the relevant python modules stored in requirements:
```
pip install -r 'requirements.txt'
```
6. Run the WeatherAPI_v2.py and enjoy! 

# :smile:
