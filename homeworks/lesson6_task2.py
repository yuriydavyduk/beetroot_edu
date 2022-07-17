# Task 2
import random

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
