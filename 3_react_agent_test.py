from openai_module import generate_text_basic
from weather_sample_function import get_weather
from prompts import react_system_prompt

# current_weather = get_weather("San Francisco")

prompt = f"""should I take an umbrella in Chicago today?"""


response = generate_text_basic(prompt, model = "gpt-4o-mini", system_prompt = react_system_prompt)

print(response)