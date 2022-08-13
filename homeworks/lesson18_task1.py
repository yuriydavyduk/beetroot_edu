class User:

    def __init__(self, name, email):
        self.validate(email)

        self.name = name
        self.email = email

    @staticmethod
    def validate(email: str):

        if email == '':
            raise ValueError('Email is empty')

        if email.count('@') != 1:
            raise ValueError('Email must have 1 "@" character')

        snail_position = email.find('@')

        if snail_position == 0:
            raise ValueError('Email prefix is empty')

        if email.find('.', snail_position) <= snail_position + 1:
            raise ValueError('Bad domain')

        if email[::-1].find('.') < 2:
            raise ValueError('The last portion of the domain must be at least two characters')

        if email.find(' ') != -1:
            raise ValueError('Email contains a space')


user1 = User('Yuriy', 'yuriy@mail.com')
