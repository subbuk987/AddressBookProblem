class Contact:
    """
    A class to represent a Contact.

    Attributes:
        info (dict): A dictionary to store contact details such as name, address, phone, etc.

    Methods:
        edit_contact(field, value): Edits a specific field of the contact's information.
    """

    def __init__(self, contact_details):
        """
        Initializes a Contact object with the provided details.

        Args:
            contact_details (dict): A dictionary containing the contact's information.
        """
        self.info = contact_details

    def edit_contact(self, field, value):
        """
        Edits a specific field of the contact's information.

        Args:
            field (str): The field to be edited (e.g., 'address', 'phone').
            value (str): The new value to update the field with.
        """
        self.info[field] = value


if __name__ == "__main__":
    # Contact details as a dictionary
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

    # Create an instance of Contact class with the given details
    contact = Contact(details)

    # Print the contact's information
    print(contact.info)
