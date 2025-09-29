import json

# x = '{ "name":"Liubov", "age":25, "city":"Lviv"}'
# y = json.loads(x)
# print(y)
# print(y["age"])
# try:
#     with open("lessons/lesson14/data.json", "r") as f:
#         data = json.load(f)
#         print(data)
#         for person in data:
#             print(f"{person['name']} is {person['age']} years old and lives in {person['city']}")
# except FileNotFoundError:
#     print("File not found.")
# except json.JSONDecodeError:
#     print("Error decoding JSON.")
#     print("Invalid JSON format.")
# except Exception as e:
#     print(f"An error occurred: {e}")

data2 = [
    {"name": "Liubomyr", "age": 39, "city": "Lviv"},
    {"name": "Allina", "age": 18, "city": "Odesa"},
]

text_json = json.dumps(data2, indent=2)
print(text_json)
with open("lessons/lesson14/data2.json", "w") as f:
    json.dump(data2, f, indent=2)
