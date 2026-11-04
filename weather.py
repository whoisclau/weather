import json
import requests


def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["current_weather"]


cities = {
    "Berlin": (52.52, 13.41),
    "Paris": (48.85, 2.35),
    "Tokyo": (35.68, 139.69),
    "New York": (40.71, -74.01),
    "Porto Alegre": (-30.03, -51.23),
}

results = {}

for name, (lat, lon) in cities.items():
    results[name] = get_weather(lat, lon)

with open("weather.json", "w") as f:
    json.dump(results, f, indent=2)

print("Saved weather.json")