import requests

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_ollama import ChatOllama


@tool('get_weather', description='Return current weather for a given city')
def get_weather(city: str) -> str:
    # 1. City name -> coordinates (Open-Meteo geocoding, free, no key)
    geo = requests.get(
        'https://geocoding-api.open-meteo.com/v1/search',
        params={'name': city, 'count': 1},
    ).json()
    if not geo.get('results'):
        return f"Could not find a location named '{city}'."
    loc = geo['results'][0]

    # 2. Current weather for those coordinates
    data = requests.get(
        'https://api.open-meteo.com/v1/forecast',
        params={
            'latitude': loc['latitude'],
            'longitude': loc['longitude'],
            'current': 'temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code',
        },
    ).json()
    c = data['current']

    # 3. Return a SHORT string, not a giant JSON blob — this is the key change
    return (
        f"Current weather in {loc['name']}, {loc.get('country', '')}: "
        f"{c['temperature_2m']}°C, humidity {c['relative_humidity_2m']}%, "
        f"wind {c['wind_speed_10m']} km/h (WMO code {c['weather_code']})."
    )

agent = create_agent(
    model=ChatOllama(model="llama3.1:8b"),
    tools=[get_weather],
    system_prompt="You are helpful weather assistant, who always cracks jokes and is humorous while remaining useful."
)



def main():
    response = agent.invoke({
        'messages': [
            {'role': 'user', 'content': 'What is weather today like in Mumbai?'}
        ]
    })

    print(response)
    print(response['messages'][-1].content)

if __name__ == "__main__":
    main()
