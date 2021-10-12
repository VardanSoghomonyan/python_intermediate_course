class Singleton(object):
    obj = None

    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
        return cls.obj


single = Singleton()
single.attr = 40
print("single object attr is: ", single.attr)

single2 = Singleton()
single2.attr = 42
print("single object attr is: ", single.attr)

print("Is they are the same object: ", single2 is single)
