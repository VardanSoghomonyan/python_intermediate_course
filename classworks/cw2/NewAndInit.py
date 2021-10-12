class NewAndInit(object):
    def __new__(cls):
        print("new")
        return super(NewAndInit, cls).__new__(cls)

    def __init__(self):
        print("init")


obj = NewAndInit()
