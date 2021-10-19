import json
from json.decoder import JSONDecoder
from json.encoder import JSONEncoder

decoded_colour_dict = {"colour": ["red", "yellow", "blue"]}
print("Encoded result is: ", JSONEncoder().encode(decoded_colour_dict))

encoded_colour_dict = '{"colour": ["red", "yellow", "blue"]}'
print("Decoded result is: ", JSONDecoder().decode(encoded_colour_dict))

try:
    with open('json_file.json') as file_obj:
        data = json.load(file_obj)
        print(data)
except ValueError:
    print("Bad json format. Change it.")

student = {
    "student": [{"name": "Jack", "email": "Jack@gmail.com", "subject": "Java"},
                {"name": "Daniels", "email": "Daniels@gmail.com", "subject": "Python"},
                {"name": "Jone", "email": "Jone@gmail.com", "subject": "C#"}]}

with open('student_json.json', 'w') as file_create:
    json.dump(student, file_create)

try:
    with open('student_json.json') as file_read:
        data = json.load(file_read)
        for index in data["student"]:
            print("Student name is: ", index["name"])

except ValueError:
    print("Bad json format. Change it.")
