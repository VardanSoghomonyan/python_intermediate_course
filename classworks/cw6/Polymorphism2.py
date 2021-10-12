class English:
    def greeting(self):
        print("Hello")


class French:
    def greeting(self):
        print("Bonjour")


class Armenian:
    def greeting(self):
        print("Barev")


def intro(language):
    language.greeting()


english = English()
french = French()
armenian = Armenian()
intro(english)
intro(french)
intro(armenian)
