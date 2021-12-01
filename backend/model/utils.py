import json
import pathlib


def get_json_from_file(file_name: str):
    with open(pathlib.Path(__file__).parent / 'data' / file_name, 'rb') as f:
        return json.load(f)
