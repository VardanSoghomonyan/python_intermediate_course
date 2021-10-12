class Class1:
    def print(self):
        print("In class 1")


class Class2(Class1):
    def print(self):
        print("In class 2")
        super().print()


class Class3(Class1):
    def print(self):
        print("In class 3")
        super().print()


class Class4(Class2, Class3):
    def print(self):
        print("In class 4")
        super(Class4, self).print()


# ete arajin jarangvac classi methodi mej super ka, mnacac methodnern el a run talis nuyn leveli calssi,
# hakarak depqum - menak et classi methodn a run talis aranc stugelu et leveli classneri methodner@
obj = Class4()
obj.print()
