class Parent:

    def __init__(self, name):

        self.name = name

    def greet(self):

        print(f"Hello, {self.name}!")

class Child(Parent):

    def __init__(self, name, age):

        super().__init__(name)

        self.age = age