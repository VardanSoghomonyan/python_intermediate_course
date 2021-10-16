import json


def complex_encode(method_argument):
    # check using instance method
    if isinstance(method_argument, complex):
        return [method_argument.real, method_argument.imag]
    # raise exception if the object is not complex
    raise TypeError(repr(method_argument) + " is not JSON serialized")


# check if the number is complex
complex_object = json.dumps(4 + 5j, default=complex_encode)
print(complex_object)
complex_encode(6 + 2j)
