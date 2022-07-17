import random

# Task 1
random_numbers = list()

i = 0
while i < 10:
    random_numbers.append(random.randint(1, 100))
    i += 1

max_number = 0
i = 0
while i < len(random_numbers):
    if random_numbers[i] > max_number:
        max_number = random_numbers[i]
    i += 1

print('List:', random_numbers)
print('Max number:', max_number)

# Task 2

list_1 = list()
list_2 = list()
new_list = list()

i = 0
while i < 10:
    list_1.append(random.randint(1, 10))
    list_2.append(random.randint(1, 10))
    i += 1

print('List 1:', list_1)
print('List 2:', list_2)
i = 0

while i < len(list_1):
    element_of_list1 = list_1[i]
    if element_of_list1 in list_2 and element_of_list1 not in new_list:
        new_list.append(element_of_list1)
    i += 1

print('Common numbers: ', new_list)

# Task 3

list_100 = list()
list_7 = list()
i = 1

while i < 100:
    list_100.append(i)
    i += 1

i = 0

while i < len(list_100):
    number = list_100[i]
    if number % 7 == 0 and number % 5 != 0:
        list_7.append(number)
    i += 1
print(list_7)
