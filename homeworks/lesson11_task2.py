import os
import json

dir_name = os.path.dirname(__file__)

menu = """
a - add contact;
f - find
r - remove
u - update
q - quite
p - print contacts
m - print menu
"""

contacts = []


def get_contacts(f_name):
    f = open(os.path.join(dir_name, f_name + '.txt'))
    contacts_list = json.loads(f.read())
    f.close()
    return contacts_list


def save_contacts(f_name, contacts_list):
    with open(os.path.join(dir_name, f_name + '.txt'), 'w') as f:
        f.write(json.dumps(contacts_list, indent=2))
        f.close()


def add_contact(contacts_list):
    contact = dict()
    first_name = input('Enter first name : ')
    last_name = input('Enter last name : ')
    contact['first_name'] = first_name
    contact['last_name'] = last_name
    contact['full_name'] = first_name + ' ' + last_name
    contact['phone_number'] = input('Enter phone number : ')
    contact['city'] = input('Enter city : ')
    contact['state'] = input('Enter state : ')

    contacts_list.append(contact)
    print('Contact added\n\n')


file_name = input('Enter filename with contacts: ')

if file_name == '':
    print('Filename is not filled')
    exit()

try:
    contacts = get_contacts(file_name)
except FileNotFoundError:
    print('File not found!')
    a = input('Create file? y/n? ')
    if a.lower() == 'n':
        exit()

    save_contacts(file_name, contacts)

print(menu)

while True:
    a = input('Choose an action: ')
    print(contacts[0].keys())

    if a == 'q':
        print('Good luck')
        save_contacts(file_name, contacts)
        exit()

    if a == 'a':
        add_contact(contacts)

