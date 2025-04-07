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
        return f"\n\
                First: {self.fname}\n\
                Last: {self.lname}\n\
                Phone: {self.phone}\n\
                Email: {self.email}\n\
                Contact Type: {self.contact_type}"

    def __iter__(self):
        for item in self.__dict__.items():
            yield item


class ContactList:
    def __init__(self):
        self.contacts_memory = {}

    def add_members(self, new_contact) -> None:
        self.contacts_memory[len(self.contacts_memory)+1] = new_contact

    def list_members(self) -> None:
        print("\ncontact list members\n")
        for i in self.contacts_memory:
            print(self.contacts_memory[i].to_string())

    def find_if_member_by_first_name(self, fname) -> bool:
        for k in self.contacts_memory.keys():
            # print(self.contacts_memory.get(k).fname)
            if self.contacts_memory.get(k).fname == fname:
                return True
        return False

    def remove_member(self, fname) -> None:
        for k in self.contacts_memory.keys():
            if self.contacts_memory.get(k).fname == fname:
                del self.contacts_memory[k]
                break


def show_program_desc() -> None:
    print("welcome to this contacts program rewrite in python")


def show_menu() -> None:
    menu = "\nMenu" + \
           "\na. Add contact" + \
           "\nd. Remove contact" + \
           "\ne. Edit contact" + \
           "\nl. List contacts" + \
           "\nq. (Q)uit"

    print(menu)


def switch(arg, in_memory_dict):
    if arg == "a":
        add_contact(in_memory_dict)
    elif arg == "d":
        delete_contact(in_memory_dict)
    elif arg == "l":
        in_memory_dict.list_members()
    elif arg == "q":
        write_json_file(in_memory_dict)
        print("\nty for using, gb")
    else:
        print("\ninvalid input, try again")


def add_contact(in_memory_dict):
    new_fname = ""
    new_lname = ""
    new_phone = 0
    new_email = ""
    new_contact_type = ""

    new_fname = str(input("first name: "))
    new_lname = str(input("last name: "))
    new_phone = str(input("phone: "))
    new_email = str(input("email: "))
    new_contact_type = str(input("contact type: "))

    new_contact = Contact(new_fname, new_lname, new_phone,
                          new_email, new_contact_type)

    in_memory_dict.add_members(new_contact)
    in_memory_dict.list_members()


def delete_contact(in_memory_dict):
    name_to_find = str(input("first name to find: "))
    if in_memory_dict.find_if_member_by_first_name(name_to_find) is True:
        in_memory_dict.remove_member(name_to_find)
        print("contact removed")
    else:
        print("contact not found")


def load_json_file(in_memory_dict):
    file = open(READ_FILE, 'r')
    data = json.load(file)
    file.close()

    for item in data['contacts']:
        new_contact = Contact(item['fname'], item['lname'], item['phone'],
                              item['email'], item['contact_type'])
        in_memory_dict.add_members(new_contact)

    return in_memory_dict


def write_json_file(in_memory_dict):
    contact_dict = []
    
    for k in in_memory_dict.contacts_memory.keys():
        contact_dict.append(in_memory_dict.contacts_memory.get(k).__dict__)

    formatted_json = '{ "contacts": ' + \
        str(contact_dict).replace("\'", "\"") + \
        '}'

    try:
        with open(WRITE_FILE, 'w') as file:
            json.dump(json.loads(formatted_json), file,
                      ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Exception: {e}")


def main():
    contacts_memory = ContactList()
    user_input = ""

    load_json_file(contacts_memory)

    show_program_desc()

    while user_input != "q":
        show_menu()
        user_input = str(input("\nChoice: ")).lower()
        switch(user_input, contacts_memory)


if __name__ == "__main__":
    main()
