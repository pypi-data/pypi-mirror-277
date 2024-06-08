import os
from json_repair import repair_json as rp
from cv_parsing.exceptions.JSONException import JSONException

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

ROOT_PATH = os.path.realpath(__file__).split('src')[0]


def load_schema(path=os.path.join(ROOT_PATH, "data", "schema.jsonl")) -> dict:
    global SCHEMA_DICT
    global JSON_STR

    with open(path, 'r', encoding='utf-8') as f:
        JSON_STR = f.read()

    SCHEMA_DICT = rp(JSON_STR, return_objects=True)
    print("Schema loaded successfully")


if os.path.exists(os.path.join(ROOT_PATH, "data")):
    load_schema()


def repair_json(json_str) -> dict:
    if json_str == "":
        raise JSONException("Empty JSON string")

    # Consider all text after the first '{' as a JSON object and the last '}' as the end of the JSON object
    first_bracket = json_str.find('{')
    last_bracket = json_str.rfind('}')

    if first_bracket == -1 or last_bracket == -1:
        raise JSONException("Invalid JSON string")

    return rp(json_str[first_bracket:last_bracket+1], return_objects=True)
