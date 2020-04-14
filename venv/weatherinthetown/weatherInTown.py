import requests
from configparser import ConfigParser


class OpenWeatherForecast:

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
        try:
            data = requests.get(url).json()
        except ConnectionError:
            print('Connection error! Try later.')
            return None

        try:
            forecast_data = data['main']['temp']
        except IndexError:
            print('Index error! Look response sample in API documentation.')
            return None

        self._city_cache[city] = forecast_data
        return forecast_data


class CityInfo:

    def __init__(self, city, weather_forecast=None):
        self.city = city
        self._weather_forecast = weather_forecast or OpenWeatherForecast()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city)


def _main():
    city = "Moscow"
    city_info = CityInfo(city)
    forecast = city_info.weather_forecast()
    print(f"Today in {city} is {forecast} degrees Celsius.")


if __name__ == '__main__':
    _main()
