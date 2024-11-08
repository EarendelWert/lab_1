# TODO решите задачу
import json

def task() -> float:
    filename = "input.json"
    with open(filename) as r:
        json_data = json.load(r)
    sum_val = sum([item["score"] * item["weight"] for item in json_data])
    return round(sum_val, 3)
print(task())
