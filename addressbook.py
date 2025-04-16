from contact import Contact


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact_info):
        contact = Contact(contact_info)
        self.contacts.append(contact)

    def show_contacts(self):
        if not self.contacts:
            print("The Address Book is empty!!!")
        else:
            for contact in self.contacts:
                print(contact.details)

    def edit_contact(self, name, field, value):
        firstname, lastname = name.split()
        for contact in self.contacts:
            if contact.details['first name'] == firstname and contact.details[
                'last name'] == lastname:
                contact.edit_contact(field,value)
                break

    def delete_contact(self, name):
        firstname , lastname = None, None
        parts = name.strip().split()

        if len(parts) == 2:
            firstname, lastname = parts
        elif len(parts) == 1:
            firstname = parts[0]

        for contact in self.contacts:
            if contact.details['first name'] == firstname:
                if lastname is None or contact.details[
                    'last name'] == lastname:
                    self.contacts.remove(contact)
                    print(
                        f"Deleted contact: "
                        f"{firstname} {lastname or ''}".strip())
                    return

        print("No Such Contact Available!!!")


    def __contains__(self, item):
        firstname, lastname = item

        for contact in self.contacts:
            if contact.details['first name'] == firstname:
                if (lastname is None or
                        contact.details['last name'] == lastname):
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
    address_book.delete_contact("Kandlagsunta")
    address_book.show_contacts()
