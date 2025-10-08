import json

# python data -> json
available_nums = {(1, 2): True, 3: False}
# print(json.dumps(available_nums))
# throws TypeError
# TypeError: keys must be str, int, float, bool or None, not tuple


print(json.dumps(available_nums, skipkeys=True))  # {"3": false}

dic1 = {4: "suriya", 3: "raji", 5: "karthiga"}

# json -> file
with open("json_data.json", "w") as file:
    json.dump(dic1, file, indent=2)

dic1_json = json.dumps(dic1, sort_keys=True)
print(dic1_json)  # {"3": "raji", "4": "suriya", "5": "karthiga"}


# json -> python data
dic1_py = json.loads(dic1_json)
print(dic1_py)  # {'3': 'raji', '4': 'suriya', '5': 'karthiga'}


print(dic1 == dic1_py)  # False -> keys' types are changed

print()

# json file -> python obj
with open("json_data.json", "r") as file:
    data = json.load(file)
    print(data)  # {"3": "raji", "4": "suriya", "5": "karthiga"}


# prettify
dic1_json = json.dumps(dic1, sort_keys=True, indent=2)
print(dic1_json)


# $ python -m json.tool json_data.json json_data_2.json --indent=4
