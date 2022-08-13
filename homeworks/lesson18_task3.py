class TypeDecorators:
    @staticmethod
    def to_int(star):
        print('to_int')

    def to_str(self):
        print('to_str')


@TypeDecorators.to_int
def do_nothing(star):

    return star

print(do_nothing('123'))
