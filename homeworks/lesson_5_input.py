# Task 1
import random
while True:
    random_int = random.randint(1, 10)
    input_number = input('Input number between 1 and 10 or q to exit: ')
    if input_number == 'q':
        print('Finished')
        break
    print(random_int, input_number, int(input_number) == random_int,sep=' = ')

# Task 2
name = input('Enter your name: ')
age = input('Entar yout age: ')

print(f'Hello {name.title()}, on your next birthday you’ll be {int(age) + 1} years')

# Task 3
word = input('Enter word: ')
for _ in range(5):
    print(''.join(random.sample(word, len(word))))