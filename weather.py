import requests
from pprint import pprint as print

def weather_by_city(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key": "ce3cfe6c55b14b34b54184606211703",
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }

    result = requests.get(weather_url, params=params)
    weather = result.json()
    return weather

if __name__ == "__main__":
    w = weather_by_city(" Moscow, Russia ")
    print (w)


