import json

with open('result.json', 'r') as f:
    data = json.load(f)

sorted_json = {}

for data_entry in data:
    if data_entry[1] not in sorted_json:
        sorted_json[data_entry[1]] = {
            data_entry[0]: {}
        }
    elif data_entry[0] not in sorted_json[data_entry[1]]:
        sorted_json[data_entry[1]][data_entry[0]] = {}
    sorted_json[data_entry[1]][data_entry[0]][data_entry[2]] = (
        data_entry[3], data_entry[4])

with open('sorted_json.json', 'w') as f:
    json.dump(sorted_json, f, indent=3)
