import json
import os
from rich.console import Console
from rich.table import Table


dir_name = os.path.dirname(__file__)


menu = """
a - add contact;
f - find
r - remove
u - update
q - quite
p - print contacts
m - print menu
s - save contacts to file
"""


contacts = []


def get_contacts(f_name):
    f = open(os.path.join(dir_name, f_name))
    contacts_list = json.loads(f.read())
    f.close()

    return contacts_list


def save_contacts(f_name, contacts_list):
    with open(os.path.join(dir_name, f_name), 'w') as f:
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


def find_contact(contacts_list):
    if len(contacts_list) == 0:
        print('Contacts are empty!')
        return None

    first_contact = contacts_list[0]

    table = Table(title='Fields for find')
    table.add_column('Field_name', justify="left", style="white")

    for _ in first_contact.keys():
        table.add_row(_)

    console = Console()
    console.print(table)

    key = input('Which field to search for? ').lower()

    if key not in first_contact.keys():
        print('Wrong field name!')
        return None

    value = input('What to search: ')

    for contact in contacts:
        if contact[key].lower() == value.lower():
            return contact
    else:
        print('Contact not found!')
        return None


def print_contacts(contacts_list):
    title = "List of contacts"

    if type(contacts_list) != list:
        contacts_list = [contacts_list]
        title = "Contact"

    table = Table(title=title)

    table.add_column('N', justify="center", style="red")
    table.add_column('first_name', justify="center", style="blue")
    table.add_column('last_name', justify="center", style="blue")
    table.add_column('full_name', justify="center", style='blue')
    table.add_column('phone_number', justify="center", style="yellow")
    table.add_column('city', justify="center", style="yellow")
    table.add_column('state', justify="center", style="yellow")

    for i, contact in enumerate(contacts_list, 1):
        table.add_row(
            str(i),
            contact['first_name'],
            contact['last_name'],
            contact['full_name'],
            contact['phone_number'],
            contact['city'],
            contact['state']
        )

    console = Console()
    console.print(table)


def remove_contact(contacts_list, contact):
    print_contacts(contact)

    answer = input('Remove this contact? y/n? ').lower()

    if answer == 'n':
        return

    contacts_list.remove(contact)
    print('Contact are removed!')


def update_contact(contact):
    print_contacts(contact)

    answer = input('Update this contact? y/n? ').lower()

    if answer == 'n':
        return

    table = Table(title='Fields for update')
    table.add_column('Field_name', justify="left", style="white")

    for _ in contact.keys():
        table.add_row(_)

    console = Console()
    console.print(table)

    key = input('Which field to update for? ').lower()

    if key not in contact.keys():
        print('Wrong field name!')
        return None

    value = input(f'Enter new {key}: ')

    if value == '':
        return

    contact[key] = value
    print('Contact update!')


file_name = input('Enter filename with contacts: ')


if file_name == '':
    print('Filename is not empty')
    exit()

try:
    contacts = get_contacts(file_name)
except FileNotFoundError:
    print('File not found!')
    answer = input('Create file? y/n? ')
    if answer == 'n':
        exit()

    save_contacts(file_name, contacts)

print(menu)

while True:

    answer = input('\nChoose an action: ').lower()

    if answer == 'q':
        print('Good luck')
        save_contacts(file_name, contacts)
        break
    if answer == 'a':
        add_contact(contacts)
    elif answer == 'f':
        contact = find_contact(contacts)
        if contact is not None:
            print_contacts(contact)
    elif answer == 'p':
        print_contacts(contacts)
    elif answer == 'm':
        print(menu)
    elif answer == 'r':
        contact = find_contact(contacts)
        if contact is None:
            continue

        remove_contact(contacts, contact)
    elif answer == 'u':
        contact = find_contact(contacts)
        if contact is None:
            continue

        update_contact(contact)
    elif answer == 's':
        save_contacts(file_name, contacts)
        print('Contacts saved!')
    else:
        print('Wrong operation')
