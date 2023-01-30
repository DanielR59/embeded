import json

def load_keys(filename : str):
    with open(filename,'r') as f:
        return json.load(f)