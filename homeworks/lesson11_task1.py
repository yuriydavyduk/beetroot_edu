import os

dir_name = os.path.dirname(__file__)

def create_file():
    with open(os.path.join(dir_name,'myfile.txt'), 'a') as f:
        f.write('Hello file world!\n')


def print_file():
    with open(os.path.join(dir_name,'myfile.txt')) as f:
        print(f.read())

        
create_file()
print_file()