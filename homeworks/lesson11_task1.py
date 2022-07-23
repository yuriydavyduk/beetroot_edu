import os

dir_name = os.path.dirname(__file__)

def create_file():
    with open(os.path.join(dir_name,'myfile.txt'), 'a') as f:
        f.write('Hello file world!\n')
        f.close()


def print_file():
    with open(os.path.join(dir_name,'myfile.txt')) as f:
        print(f.read())
        f.close()

create_file()
print_file()