class TypeDecorators:
    @staticmethod
    def to_int(func):
        def wrap(param):
            try:
                return int(param)
            except TypeError:
                return param

        return wrap

    @staticmethod
    def to_str(func):
        def wrap(param):
            try:
                return str(param)
            except TypeError:
                return param

        return wrap

    @staticmethod
    def to_bool(func):
        def wrap(param):
            try:
                return True if param == 'True' else False
            except TypeError:
                return param

        return wrap

    @staticmethod
    def to_float(func):
        def wrap(param):
            try:
                return float(param)
            except TypeError:
                return param

        return wrap


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25

assert do_something('True') is True
