def get_contact_details():
    details = {}
    fields = ["first name", "last name", "address", "city", "state", "zip",
              "phone", "email"]

    for field in fields:
        details[field] = input(f'Enter {field}:')

    return details


def print_contact(contact):
    print(f"""
==============================
First Name: {contact.details["first name"]}
Last Name: {contact.details["last name"]}
Address: {contact.details["address"]}
City: {contact.details["city"]}
State: {contact.details["state"]}
Zip: {contact.details["zip"]}
Phone: {contact.details["phone"]}
Email: {contact.details["Email"]}
==============================""")

if __name__ == "__main__":

   print(get_contact_details())