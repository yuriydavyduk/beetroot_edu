# Task 1
name: str = 'Yuriy'
day = 'Monday'

s = 'Good day {}! {} is a perfect day to learn some python.'

print(s.format(name, day))
print(f'Good day {name}! {day} is a perfect day to learn some python.')
print('Good day {1}! {0} is a perfect day to learn some python.'.format(day, name), end='\n\n')
