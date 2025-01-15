# Description: This module is used to interact with the OpenAI API
from openai import OpenAI
import os
from dotenv import load_dotenv
 
# Load the environment variables
load_dotenv()

# Create an instance of the OpenAI class
openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_text_basic(prompt: str, model =  "gpt-4o-mini", system_prompt: str = None):
    
    print(prompt)
    
    response = openai_client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
            ]
    )
    
    return response.choices[0].message.content



def generate_text_with_conversation(messages: str, model =  "gpt-4o-mini"):
    
    response = openai_client.chat.completions.create(
        model=model,
        messages=messages
    )
    
    return response.choices[0].message.content


