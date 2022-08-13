from calendar import isleap


class Mathematician:

    @staticmethod
    def square_nums(my_list):
        return [n*n for n in my_list]

    @staticmethod
    def remove_positives(my_list):
        return list(filter(lambda a: a < 0, my_list))

    @staticmethod
    def filter_leaps(my_list):
        return list(filter(lambda a: isleap(a), my_list))


m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
