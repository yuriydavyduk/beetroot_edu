# Task 1
import random

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
