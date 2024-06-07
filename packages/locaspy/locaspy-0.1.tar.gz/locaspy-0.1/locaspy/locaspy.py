import requests

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_location(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude"),
        "timezone": response.get("timezone"),
        "country_code": response.get("country_code_iso3"),
        "country_capital": response.get("country_capital"),
        "isp": response.get("org"),
        "asn": response.get("asn"),
        "organization": response.get("org"),
        "postal": response.get("postal"),
        "utc_offset": response.get("utc_offset"),
        "continent": response.get("continent_code"),
        "currency": response.get("currency"),
        "languages": response.get("languages"),
    }
    return location_data

def get_weather(latitude, longitude):
    response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true').json()
    if 'current_weather' in response:
        weather_data = response['current_weather']
        weather = {
            "temperature": weather_data['temperature'],
            "wind_speed": weather_data['windspeed'],
            "condition": weather_data['weathercode']
        }
    else:
        weather = {
            "temperature": "Unknown",
            "wind_speed": "Unknown",
            "condition": "Unknown"
        }
    return weather

def get_google_maps_link(latitude, longitude):
    return f"https://www.google.com/maps/@{latitude},{longitude},10z"

def get_data(ip_address, data_type):
    location_data = get_location(ip_address)
    if data_type == "map":
        return get_google_maps_link(location_data["latitude"], location_data["longitude"])
    elif data_type == "weather":
        weather = get_weather(location_data["latitude"], location_data["longitude"])
        return f"Condition Code {weather['condition']} - Temperature: {weather['temperature']}°C - Wind Speed: {weather['wind_speed']} km/h"
    elif data_type == "location":
        return (
            f"{location_data['ip']}\n"
            f"{location_data['city']}, {location_data['region']}, {location_data['country']}\n"
            f"{location_data['latitude']}, {location_data['longitude']}\n"
            f"{location_data['timezone']}\n"
            f"{location_data['country_code']}\n"
            f"{location_data['country_capital']}\n"
            f"{location_data['isp']}\n"
            f"{location_data['asn']}\n"
            f"{location_data['organization']}\n"
            f"{location_data['postal']}\n"
            f"{location_data['utc_offset']}\n"
            f"{location_data['continent']}\n"
            f"{location_data['currency']}\n"
            f"{location_data['languages']}\n"
        ).strip()
    else:
        raise ValueError("Invalid data type requested")
