try:
    import requests
    import json
except ModuleNotFoundError:
    print('Modules not found. Please run pip install -r requirements.txt to install the required modules.')
    exit()


def weather_info(data):
    max_temp = data['daily'][1]['temp']['max']
    min_temp = data['daily'][1]['temp']['min']
    current_temp = data['current']['temp']
    weather = data['daily'][1]['weather'][0]['description']
    print(f'maximum temprature: {max_temp} C')
    print(f'minimum temprature: {min_temp} C')
    print(f'current temprature: {current_temp} C')
    print(f'today\'s condition: {weather}')


def api_data():
    # goto https://openweathermap.org/api/one-call-api for reference
    url = 'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={YOUR API KEY}'
    res = requests.get(url)
    data = res.text
    parsed = dict(json.loads(data))
    return parsed


if __name__ == '__main__':
    print('Today\'s weather forecast:\n')
    weather_info(api_data())
