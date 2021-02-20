import json

# a Python object (dict):
python_dict = {"name": "Jim & Por", "age": 26, "city": "Bangkok"}

# convert into json:
json_string = json.dumps(python_dict)

# the result is a Json string:
print(json_string)