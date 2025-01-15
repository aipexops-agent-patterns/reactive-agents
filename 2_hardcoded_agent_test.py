from openai_module import generate_text_basic
from weather_sample_function import get_weather

current_weather = get_weather("San Francisco")

prompt = f"""What is the current weather in San Francisco based on the weather forcast: {current_weather}?"""


response = generate_text_basic(prompt)

print(response)