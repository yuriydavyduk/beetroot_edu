# Task 1
# my_phrase = input('Enter phrase: ')
# my_dict = dict()
# my_list = my_phrase.split(' ')
#
# for word in my_list:
#     if word in my_dict:
#         my_dict[word] +=1
#     else:
#         my_dict[word] = 1
#
# for key, value in my_dict.items():
#     print(key, ':', value)

# Task 2
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
#
# total_price = 0
#
# for key, value in stock.items():
#     if key in prices:
#         total_price += value * prices[key]
#
# print(total_price)

# Task 3
# my_dict = list()
#
# for i in range(1,11):
#     my_dict.append((i, i * i))
#
# print(my_dict)

# Task 4
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dict_1 = dict()
dict_2 = dict()

for i, value in enumerate(week_days, 1):
    dict_1[i] = value
    dict_2.update({value: i})

print(dict_1)
print(dict_2)
