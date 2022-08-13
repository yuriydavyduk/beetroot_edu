class Person:

    def __init__(self, firstname, lastname, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def happy_birthday(self):
        print(f'Happy birthday {self.firstname} {self.lastname}')
        self.age += 1

    def __repr__(self):
        return f'{type(self)} {self.firstname} {self.lastname} - {self.age} age'


class Student(Person):

    def __init__(self, firstname, lastname, age: int, classroom, school):
        super().__init__(firstname, lastname, age)
        self.classroom = classroom
        self.school = school

    def move_to_new_class(self):
        if self.classroom == 11:
            print('Сongratulations on finishing school!!!')
            self.classroom = None
            return

        self.classroom += 1


class Teacher(Person):

    def __init__(self, firstname, lastname, age: int, salary):
        super().__init__(firstname, lastname, age)
        self.salary = salary
        self.subjects = list()

    def add_subject(self, subject):
        self.subjects.append(subject)


student1 = Student('Ivan', 'Pobyvan', 11, 5, 1)
student2 = Student('Stepan', 'Taran', 15, 10, 1)

teacher1 = Teacher('Igor', 'Feren', 27, 11000)

print(student1)
print(student2)
print(teacher1)

student1.happy_birthday()
teacher1.happy_birthday()

student2.move_to_new_class()

teacher1.add_subject('mathematics')
teacher1.add_subject('physics')

print(student1)
print(teacher1)
print(student2.classroom)
student2.move_to_new_class()
print(student2.classroom)
print(teacher1.subjects)
