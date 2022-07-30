class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


person = Person('Carl', 'Johnson', 26)

print(f'Hello, my name is {person.firstname} {person.lastname} and I’m {person.age} years old')
