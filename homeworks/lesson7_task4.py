# Task 4
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dict_1 = dict()
dict_2 = dict()

for i, value in enumerate(week_days, 1):
    dict_1[i] = value
    dict_2.update({value: i})

print(dict_1)
print(dict_2)
