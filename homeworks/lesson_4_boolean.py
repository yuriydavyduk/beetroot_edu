# Task 1
sample_string = 'helloworld'
if len(sample_string) < 2:
    print('')
else:
    print(sample_string[:2], sample_string[-2:], sep='')

# Task 2
phone_number = '1254825486'
if not phone_number.isdigit():
    print('Phone number must contain only numbers.')
elif len(phone_number) != 10:
    print('Phone number must contain 10 characters.')
else:
    print('Phone number is correct')

# Task 3
if int(input('2+2=')) == 4:
    print('You are right.')
else:
    print('You are wrong.')

# Task 4
print(input('Input your name: ').lower() == 'yuriy')
