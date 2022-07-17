# Task 3
import random

word = input('Enter word: ')
for _ in range(5):
    print(''.join(random.sample(word, len(word))))
