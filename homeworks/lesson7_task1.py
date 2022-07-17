# Task 1
my_phrase = input('Enter phrase: ')
my_dict = dict()
my_list = my_phrase.split(' ')

for word in my_list:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1

for key, value in my_dict.items():
    print(key, ':', value)
