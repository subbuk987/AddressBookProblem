from contact import Contact
from utils.utility import print_contact

class AddressBook:
    """
    A class that represents an Address Book where contacts can be added, displayed,
    edited, deleted, and sorted.

    Attributes:
        contacts (list): A list to store Contact objects.

    Methods:
        add_contact(contact_info): Adds a new contact to the address book.
        show_contacts(): Displays all the contacts in the address book.
        edit_contact(name, field, value): Edits a specific field of an existing contact.
        delete_contact(name): Deletes a contact from the address book by name.
        sort_by_field(field): Sorts the contacts by a given field.
        __contains__(item): Checks if a contact exists in the address book.
    """

    def __init__(self):
        """
        Initializes an empty list of contacts for the address book.
        """
        self.contacts = []

    def add_contact(self, contact_info):
        """
        Adds a new contact to the address book.

        Args:
            contact_info (dict): A dictionary containing contact details.

        Returns:
            Contact: The Contact object that was added to the address book.
        """
        contact = Contact(contact_info)
        self.contacts.append(contact)
        return contact

    def show_contacts(self):
        """
        Displays all the contacts in the address book. If the address book is empty,
        a message is displayed indicating so.
        """
        if not self.contacts:
            print("The Address Book is empty!!!")
        else:
            # Loop through the contacts and print their details
            for contact in self.contacts:
                print_contact(contact)

    def edit_contact(self, name, field, value):
        """
        Edits a specific field of an existing contact.

        Args:
            name (str): The full name (first and last) of the contact to edit.
            field (str): The field of the contact to be edited (e.g., 'address').
            value (str): The new value to update the field with.
        """
        firstname, lastname = name.split()
        for contact in self.contacts:
            # Find the contact with the matching name
            if contact.info['first name'] == firstname and contact.info['last name'] == lastname:
                contact.edit_contact(field, value)
                break

    def delete_contact(self, name):
        """
        Deletes a contact from the address book by name.

        Args:
            name (str): The full name (first and last) of the contact to delete.
        """
        firstname, lastname = None, None
        parts = name.strip().split()

        # Check if the name is split into first and last names
        if len(parts) == 2:
            firstname, lastname = parts
        elif len(parts) == 1:
            firstname = parts[0]

        # Search for the contact and remove it
        for contact in self.contacts:
            if contact.info['first name'] == firstname:
                if lastname is None or contact.info['last name'] == lastname:
                    self.contacts.remove(contact)
                    print(f"Deleted contact: {firstname} {lastname or ''}".strip())
                    return

        print("No Such Contact Available!!!")

    def sort_by_field(self, field):
        """
        Sorts the contacts in the address book by a given field.

        Args:
            field (str): The field to sort contacts by. Options include 'name', 'city',
                         'state', and 'zip'.
        """
        if field == 'name':
            # Sort by first name and last name
            self.contacts.sort(key=lambda x: (x.info["first name"], x.info["last name"]))
        elif field == 'city':
            self.contacts.sort(key=lambda x: x.info["city"])
        elif field == 'state':
            self.contacts.sort(key=lambda x: x.info["state"])
        elif field == 'zip':
            self.contacts.sort(key=lambda x: x.info["zip"])

    def __contains__(self, item):
        """
        Checks if a contact exists in the address book.

        Args:
            item (tuple): A tuple containing first name and last name to check.

        Returns:
            bool: True if the contact exists, False otherwise.
        """
        firstname, lastname = item

        for contact in self.contacts:
            if contact.info['first name'] == firstname:
                if lastname is None or contact.info['last name'] == lastname:
                    return True

        return False


if __name__ == "__main__":
    # Sample contact details to add to the address book
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

    # Create AddressBook instance
    address_book = AddressBook()

    # Add a contact and display the address book
    address_book.add_contact(details)
    address_book.show_contacts()

    # Another contact to add
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

    # Add another contact and display the updated address book
    address_book.add_contact(detail)
    address_book.show_contacts()
