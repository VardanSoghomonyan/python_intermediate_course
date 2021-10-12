class StaticClass(object):
    @staticmethod
    def hello():
        print("Hello world")


StaticClass.hello()
obj1 = StaticClass()
obj1.hello()
