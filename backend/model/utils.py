import json
import pathlib
from typing import Union, List


def get_json_from_file(file_name: str) -> Union[List[dict], dict]:
    with open(pathlib.Path(__file__).parent / 'data' / file_name, 'rb') as f:
        return json.load(f)
