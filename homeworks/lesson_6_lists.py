import random

# Task 1
random_numbers = list()

while len(random_numbers) < 10:
    random_numbers.append(random.randint(1, 100))

print('List:', random_numbers)

max_number = random_numbers.pop(0)
while len(random_numbers) != 0:
    number = random_numbers.pop(0)
    if number > max_number:
        max_number = number

print('Max number:', max_number)

# Task 2

list_1 = list()
list_2 = list()
new_list = list()

while len(list_1) < 10:
    list_1.append(random.randint(1, 10))
    list_2.append(random.randint(1, 10))

print('List 1:', list_1)
print('List 2:', list_2)

while len(list_1) != 0:
    element_of_list1 = list_1.pop(0)
    if element_of_list1 in list_2 and element_of_list1 not in new_list:
        new_list.append(element_of_list1)

print('Common numbers: ', new_list)

# Task 3

list_100 = list()
list_7 = list()
i = 1

while i < 100:
    list_100.append(i)
    i += 1

while len(list_100) != 0:
    number = list_100.pop(0)
    if number % 7 == 0 and number % 5 != 0:
        list_7.append(number)

print(list_7)