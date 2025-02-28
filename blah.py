"""
 - needs to be able to read json and csv files
 - needs to write back into the orig files format
 - needs classes for contacts
 -- first name, last name, phone, email, contact type
 - needs to load contacts in memory
"""

import json

READ_FILE = 'contact.json'
WRITE_FILE = 'spare.json'


class Contact:
    def __init__(self, fname, lname, phone, email, contact_type):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email
        self.contact_type = contact_type

    def to_string(self):
        print(f"\n\
                First: {self.fname}\n\
                Last: {self.lname}\n\
                Phone: {self.phone}\n\
                Email: {self.email}\n\
                Contact Type: {self.contact_type}")
    
    def __iter__(self):
        for item in self.__dict__.items():
            yield item


def show_program_desc():
    print("welcome to this contacts program rewrite in python")


def show_menu():
    menu = "\na. Add contact\nb. Remove contact\nl. List contacts\nq. (Q)uit"
    print(menu)


def switch(arg, in_memory_dict):
    if arg == "a":
        print("\nadd, not implemented")
    elif arg == "b":
        print("\nremove, not implemented")
    elif arg == "l":
        print("\nlist, not implemented")
        for i in in_memory_dict:
            in_memory_dict[i].to_string()
    elif arg == "q":
        write_json_file(in_memory_dict)
        print("\nty for using, gb")
    else:
        print("\ninvalid input, try again")


def load_json_file(in_memory_dict):
    file = open(READ_FILE, 'r')
    data = json.load(file)
    index = 0;
    for item in data['contacts']:
        new_contact = Contact(item['fname'], item['lname'], item['phone'],
                              item['email'], item['contact_type'])
        in_memory_dict[index] = new_contact
        index += 1

    return in_memory_dict


def write_json_file(in_memory_dict):
    # using dict, write to file
    contact_dict = []

    for contact in in_memory_dict:
        contact_dict.append(in_memory_dict[contact].__dict__)

    formatted_json = '{ "contacts": ' + \
                    str(contact_dict).replace("\'", "\"") + \
                     '}'

    try:
        with open(WRITE_FILE, 'w') as file:
            json.dump(json.loads(formatted_json), file,
                      ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Except: {e}")


def main():
    contacts_memory = {}
    user_input = ""

    load_json_file(contacts_memory)

    show_program_desc()

    while user_input != "q":
        show_menu()
        user_input = str(input("\nChoice: ")).lower()
        switch(user_input, contacts_memory)


main()
