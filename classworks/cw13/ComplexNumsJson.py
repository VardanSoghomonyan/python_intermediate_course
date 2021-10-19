import json


def is_complex(method_argument):
    if '__complex__' in method_argument:
        return complex(method_argument['real'], method_argument['img'])
    return method_argument


# check with the complex number
complex_object = json.loads('{"__complex__": true, "real": 7, "img": 5}', object_hook=is_complex)

# check without the complex number
simple_object = json.loads('{"real": 6, "img": 9}', object_hook=is_complex)

print("complex object is :", complex_object)
print("Without complex object is :", simple_object)
