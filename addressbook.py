from contact import Contact

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self,contact_info):
        contact = Contact(contact_info)
        self.contacts.append(contact)

    def show_contacts(self):
        for contact in self.contacts:
            print(contact)

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


