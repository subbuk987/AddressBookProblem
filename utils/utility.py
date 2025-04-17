

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
First Name: {contact.info["first name"]}
Last Name: {contact.info["last name"]}
Address: {contact.info["address"]}
City: {contact.info["city"]}
State: {contact.info["state"]}
Zip: {contact.info["zip"]}
Phone: {contact.info["phone"]}
Email: {contact.info["email"]}
==============================""")


def read_from_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines if line.strip()]


def write_to_file(file_path, details):
    with open(file_path, 'a') as file:
        for k, v in details.items():
            file.write(f"{k} : {v}\n")
        file.write("===========================================\n")




if __name__ == "__main__":
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
    write_to_file("../files/contact_details.txt", detail)
