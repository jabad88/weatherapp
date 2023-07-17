#openweatherapi pw: weatherboy27
import json
import requests
import argparse
from dotenv import load_dotenv
import os


def main():
    load_dotenv()

    city, unit = get_args()
    print (get_weather(city, unit))
 

def get_args():
    parser = argparse.ArgumentParser(description='Input the city and temperature unit')
    parser.add_argument('city',type=str, nargs = "+", help="Input a city")
    parser.add_argument('-f','--fahrenheit',required=False,help='Gets temperature in fahrenheit',action='store_true')
    args = parser.parse_args()

    city = args.city
    city = " ".join(city)
    city = city.replace(" ", "+")
    
    if args.fahrenheit:
        return city, True
    else:
        return city, None

def get_weather(city, unit):
    if unit == True:
        unit = "imperial"
        degree = "°F"
    else:
        unit = "metric"
        degree = "°C"

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={unit}&appid={os.getenv('api_key')}")
    weather = json.loads(response.text)
    # weather = (json.dumps(weather,indent=2))
    name = weather["name"]
    temp = round(weather["main"]["temp"])
    feels_like = round(weather["main"]["feels_like"])
    for _ in weather['weather']:
        for k,v in _.items():
            if k == "main":
                conditions = v
            if k == "description":
                description = v

    return f"City: {name}\nTemperature: {temp}{degree}\nFeels Like: {feels_like}{degree}\nConditions: {conditions}\nDescription: {description}"



if __name__ == "__main__":
    main()

