import json

def read_json(_path):
    with open(_path, "r") as f:
        return json.load(f)