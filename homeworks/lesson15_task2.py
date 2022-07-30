class Dog:
    age_factor = 7

    def __init__(self, dogs_age):
        self.dogs_age = dogs_age

    def human_age(self):
        return self.dogs_age * self.age_factor


dog = Dog(5)

print(dog.human_age())
