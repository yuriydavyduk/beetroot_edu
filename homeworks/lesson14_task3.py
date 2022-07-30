def arg_rules(type_: type, max_length: int, contains: list):
    def arg_rules_dec(func):
        def wrap(name):
            if type(name) != type_:
                print(f'{name} - wrong type, must be {type_}!')
                return False

            if len(name) > max_length:
                print(f'{name} - max length should be {max_length}!')
                return False

            if not all([word in name for word in contains]):
                print(f'{name} - must contain words {contains}')
                return False

            return func(name)
        return wrap
    return arg_rules_dec


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'