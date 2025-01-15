import json
import re

def read_json(file_path):
    """Read JSON data from a file and return it as a dictionary."""
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json(data, file_path):
    """Write a dictionary to a file as JSON data."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def pretty_print_json(data):
    """Print JSON data in a pretty format."""
    print(json.dumps(data, indent=4))
    
    
def extract_json_function(response):
    """Extract JSON function from the response."""
    match = re.search(r'\{.*\}', response, re.DOTALL)
    if match:
        return json.loads(match.group())
    return None