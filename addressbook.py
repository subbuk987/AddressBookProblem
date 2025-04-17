from contact import Contact
from utils.utility import print_contact


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact_info):
        contact = Contact(contact_info)
        self.contacts.append(contact)
        return contact

    def show_contacts(self):
        if not self.contacts:
            print("The Address Book is empty!!!")
        else:
            for contact in self.contacts:
                print_contact(contact)

    def edit_contact(self, name, field, value):
        firstname, lastname = name.split()
        for contact in self.contacts:
            if contact.info['first name'] == firstname and contact.info[
                'last name'] == lastname:
                contact.edit_contact(field, value)
                break

    def delete_contact(self, name):
        firstname, lastname = None, None
        parts = name.strip().split()

        if len(parts) == 2:
            firstname, lastname = parts
        elif len(parts) == 1:
            firstname = parts[0]

        for contact in self.contacts:
            if contact.info['first name'] == firstname:
                if lastname is None or contact.info[
                    'last name'] == lastname:
                    self.contacts.remove(contact)
                    print(
                        f"Deleted contact: "
                        f"{firstname} {lastname or ''}".strip())
                    return

        print("No Such Contact Available!!!")

    def sort_by_field(self, field):
        if field == 'name':
            self.contacts.sort(
                key=lambda x: (
                    x.info["first name"], x.info["last name"]))
        elif field == 'city':
            self.contacts.sort(
                key=lambda x: x.info["city"])
        elif field == 'state':
            self.contacts.sort(
                key=lambda x: x.info["state"])
        elif field == 'zip':
            self.contacts.sort(
                key=lambda x: x.info["zip"])

    def __contains__(self, item):
        firstname, lastname = item

        for contact in self.contacts:
            if contact.info['first name'] == firstname:
                if (lastname is None or
                        contact.info['last name'] == lastname):
                    return True

        return False


if __name__ == "__main__":
    details = {
        "first name": "Kandlagunta",
        "last name": "Subramanyam",
        "address": "Chitlapakkam",
        "city": "Chennai",
        "state": "TamilNadu",
        "zip": "600064",
        "phone": "7200920651",
        "email": "subramanyamk2003@gmail.com"
    }

    address_book = AddressBook()
    address_book.add_contact(details)
    address_book.show_contacts()

    detail = {
        "first name": "Kandlagunta",
        "last name": "Anj",
        "address": "Chitlapakkam",
        "city": "Chennai",
        "state": "TamilNadu",
        "zip": "600064",
        "phone": "7200920651",
        "email": "subramanyamk2003@gmail.com"
    }
    address_book.add_contact(detail)
    address_book.show_contacts()
