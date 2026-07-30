import json

employee = {
    "name": "Sumanth",
    "age": 20,
    "Department": "AI"
}
# Python dict -> Json string
print(employee)
json_data = json.dumps(employee)
print(type(json_data))

#Json string - > Python dict
python_data = json.loads(json_data)
print(python_data)
print(type(python_data))