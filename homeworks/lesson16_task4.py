import os

dir_name = os.path.dirname(__file__)
file_name = 'logs.txt'


class CustomException(Exception):
    def __init__(self, msg):
        with open(os.path.join(dir_name, 'my_file.txt'), 'a') as f:
            f.write(f'{msg}\n')


try:
    raise CustomException('My error')
except:
    pass
