# Task 2
phone_number = '1254825488'
if not phone_number.isdigit():
    print('Phone number must contain only numbers.')
elif len(phone_number) != 10:
    print('Phone number must contain 10 characters.')
else:
    print('Phone number is correct')
