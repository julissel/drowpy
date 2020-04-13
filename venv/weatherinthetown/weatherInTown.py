import pprint
import requests
from configparser import ConfigParser


class OpenWeatherForecast:
    # API call
    def __init__(self):
        self._city_cache = {}

    # For temperature in Celsius use units=metric
    def get(self, city):
        if city in self._city_cache:
            return self._city_cache
        config = ConfigParser()
        config.read('weather.conf')
        api_id = config['CONFIG']['OPENWEATHER_API_ID']
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},ru&units=metric&APPID={api_id}"
        print('Sending HTTP request')
        data = requests.get(url).json()
        forecast_data = data['main']['temp']
        self._city_cache[city] = forecast_data
        return forecast_data


class CityInfo:

    def __init__(self, city, weather_forecast=None):
        self.city = city
        self._weather_forecast = weather_forecast or OpenWeatherForecast()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city)


def _main():
    weather_forecast = OpenWeatherForecast()
    for req in range(5):
        city_info = CityInfo("Moscow", weather_forecast=weather_forecast)
        city_info._weather_forecast()


if __name__ == '__main__':
    _main()
