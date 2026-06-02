from dataclasses import dataclass
import requests

from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime
from langgraph.checkpoint.memory import InMemorySaver
from langchain_ollama import ChatOllama


@dataclass
class Context:
    user_id: str


@dataclass
class ResponseFormat:
    summary: str
    temperature_celsius: float
    humidity: float


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


@tool('locate_user', description="Look up user's city based on the context")
def locate_user(runtime: ToolRuntime[Context]):
    match runtime.context.user_id:
        case 'ABC123':
            return 'Patna'
        case 'XYZ456':
            return 'London'
        case 'HJKL111':
            return 'Paris'
        case _:
            return 'Unknown'

model = ChatOllama(model='qwen3:14b', temperature=0.3, reasoning=False)

checkpointer = InMemorySaver()

agent = create_agent(
    model=model,
    tools=[get_weather, locate_user],
    system_prompt=(
        "You are helpful weather assistant, who always cracks jokes and is humorous while remaining useful. "
        "After gathering the weather data, you MUST deliver your final answer by calling the ResponseFormat tool "
        "(put your humorous reply in the summary field). Never give your final answer as plain text."
    ),
    context_schema=Context,
    response_format=ResponseFormat,
    checkpointer=checkpointer
)

config = {'configurable': {'thread_id': '1'}}

def main():
    response = agent.invoke({
        'messages': [
            {'role': 'user', 'content': 'What is weather today like?'}
        ]},
        config=config,
        context=Context(user_id='ABC123')
    )

    print(response['structured_response'].summary)

if __name__ == "__main__":
    main()
