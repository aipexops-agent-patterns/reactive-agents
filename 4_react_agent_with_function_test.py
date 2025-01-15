from openai_module import generate_text_basic
from weather_sample_function import get_weather
from prompts import react_system_prompt
from json_helper import extract_json_function

#Avaiable actions are:
available_actions = {
    "get_weather": get_weather
} 

prompt = f"""should I take an umbrella in Chicago today?"""


response = generate_text_basic(prompt, model = "gpt-4o-mini", system_prompt = react_system_prompt)

print(response)

# Extract the JSON function from the response
json_function = extract_json_function(response)
print(json_function)

if json_function:
    # Extract the function name from the JSON function
    function_name = json_function["function_name"]
    print("Function name:", function_name)
    # Extract the arguments from the JSON function
    arguments = json_function["function_parms"]
    print("Arguments:", arguments)
    
    # print("Available actions:", available_actions)
    
    # Check if the function name is in the available actions
    if function_name not in available_actions:
        print(f"Function {function_name} is not available")
        exit()
    
    # Call the function with the arguments
    action_function = available_actions[function_name]
    
    # Call the function with the arguments
    result = action_function(arguments)
    
    function_result_message = f"Action_Response: {result}"
    print(function_result_message)





