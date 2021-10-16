import json

person_data = {"person": {"name": "Ken", "sex": "male", "age": 28}}

with open("json_file.json", "w") as file_write:
    # convert person_data dict into JSON format by using json.dumps.
    # Indent is used for JSON prettify and sort_keys is sorting by JSON keys
    print("Dumped json is: ", json.dumps(person_data, indent=4, sort_keys=True))

    # write json data into file
    json.dump(person_data, file_write)
    print("The new file with person_data is created")

# here is some json
x = '{"person":{"name":"John", "age":[30,20], "city":"New York"}}'

# parse x:
y = json.loads(x)

print('Type of y is: ', type(y))
print('y["person"]["age"][0] is: ', y["person"]["age"][0])
print(y.get("person"))

with open("json_file.json") as file_read:
    data = json.load(file_read)

print("data from file is: ", data)

lst = ['a:a,4', 'b', 'c', {'4': 5, '6': 7}]
# removes spaces from above line
compact_obj = json.dumps(lst, separators=(',', ':'), indent=2)
print("compact_obj is: ", compact_obj)
