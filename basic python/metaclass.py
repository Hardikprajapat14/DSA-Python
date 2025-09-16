class Meta(type):
    def __new__(cls, name, bases, dct):
        print("Creating class:", name)
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass
