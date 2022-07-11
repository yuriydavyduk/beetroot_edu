# Task 1
name: str = 'Yuriy'
day = 'Monday'

s = 'Good day {}! {} is a perfect day to learn some python.'

print(s.format(name, day))
print(f'Good day {name}! {day} is a perfect day to learn some python.')
print('Good day {1}! {0} is a perfect day to learn some python.'.format(day, name), end='\n\n')

# Task 2
name = 'Yuriy'
surname = 'Davyduk'

full_name = name + ' ' + surname

print('Hello,', full_name,end='\n\n')

# Task 3
a = 4
b = 7

print('Addition:', a + b)
print('Subtraction:', a - b)
print('Division:', b / a)
print('Multiplication:', a * b)
print('Exponent (Power):', a ** b)
print('Modulus:', abs(a - b))
print('Floor division:', b // a)
