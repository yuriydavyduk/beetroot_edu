class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print('woof woof')


class Cat(Animal):
    def talk(self):
        print('meow')


def get_talk(animal):
    animal.talk()


cat1 = Cat()
dog1 = Dog()

get_talk(dog1)
