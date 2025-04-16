class Contact:
    def __init__(self, contact_details):
        self.details = contact_details


if __name__ ==  "__main__":
    details = {
        "first name" : "Kandlagunta",
        "last name" : "Subramanyam",
        "address" : "Chitlapakkam",
        "city" : "Chennai",
        "state" : "TamilNadu",
        "zip" : "600064",
        "phone" : "7200920651",
        "email" : "subramanyamk2003@gmail.com"
    }

    contact = Contact(details)
    print(contact.details)
