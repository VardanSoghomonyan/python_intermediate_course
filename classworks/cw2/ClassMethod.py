class ClassMethod(object):
    @classmethod
    def hello(cls):
        print("Class content is {}".format(cls.__name__))


ClassMethod.hello()
obj1 = ClassMethod()
obj1.hello()
