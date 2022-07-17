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
