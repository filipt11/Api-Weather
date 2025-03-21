import requests
from requests_oauthlib import OAuth1
from config import consumer_key, consumer_secret, access_token, access_token_secret
def lambda_handler(event, context):
    weather_url = f"https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 53.01375,
        "longitude": 18.59814,
        "hourly": "temperature_2m,rain",
        "daily": "precipitation_probability_mean",
        "timezone": "auto",
        "forecast_days": 1
    }

    response = requests.get(weather_url,params=params)
    weather = response.json()

    temperatures = (weather['hourly']['temperature_2m'])

    temp_min = str(min(temperatures))
    temp_max = str(max(temperatures))

    rain = (weather['daily']['precipitation_probability_mean'])
    rain_prob = str(rain[0])


    output = f"Dzisiaj w Toruniu temperatura: {temp_min}°C - {temp_max}°C.\nPrawdopodobieństwo opadów: {rain_prob}%"

    print(output)


    twitter_url = "https://api.twitter.com/2/tweets"

    payload = {
        "text": output
    }


    auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

    response = requests.post(twitter_url, auth=auth, json=payload, headers={"Content-Type": "application/json"})

    print(response.text)

    return {}


