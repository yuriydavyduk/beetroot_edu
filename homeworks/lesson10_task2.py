def my_def(a, b):
    return a * a / b


try:
    number_1 = int(input('Enter number a: '))
    number_2 = int(input('Enter number b: '))
    print(my_def(number_1, number_2))
except ZeroDivisionError:
    print('Cannot divide by zero')
except ValueError:
    print('You enter wrong number')
