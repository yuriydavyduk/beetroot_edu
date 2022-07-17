# Task 3
def make_operation(operation, *args):
    if not args or operation not in ('+', '-', '*'):
        print('Wrong operation or empty arguments')
        return

    arguments = list(args)
    argument = arguments.pop(0)

    while arguments:
        if operation == '+':
            argument += arguments.pop(0)
        elif operation == '-':
            argument -= arguments.pop(0)
        elif operation == '*':
            argument *= arguments.pop(0)

    return argument


print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))
