# Utility functions for handling contacts, file operations, and displaying contact details

def get_contact_details():
    """
    Prompts the user to enter contact details and returns them in a dictionary format.

    Fields:
        - first name
        - last name
        - address
        - city
        - state
        - zip
        - phone
        - email

    Returns:
        dict: A dictionary containing contact details.
    """
    details = {}
    fields = ["first name", "last name", "address", "city", "state", "zip",
              "phone", "email"]

    # Prompt user for each field and store the entered value in the 'details' dictionary
    for field in fields:
        details[field] = input(f'Enter {field}:')

    return details


def print_contact(contact):
    """
    Prints the details of a contact in a formatted manner.

    Args:
        contact (object): A contact object containing the contact information.
    """
    # Display the contact details in a readable format
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
    """
    Reads the contents of a file and returns a list of non-empty lines.

    Args:
        file_path (str): The path to the file that needs to be read.

    Returns:
        list: A list of non-empty lines read from the file.
    """
    # Open the file in read mode and return all non-empty lines
    with open(file_path, "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines if line.strip()]


def write_to_file(file_path, details):
    """
    Writes contact details to a file in a formatted manner.

    Args:
        file_path (str): The path to the file where contact details need to be written.
        details (dict): A dictionary containing contact details to write to the file.
    """
    # Open the file in append mode and write the details in a readable format
    with open(file_path, 'a') as file:
        for k, v in details.items():
            file.write(f"{k} : {v}\n")  # Write each key-value pair
        file.write(
            "===========================================\n")  # Separate each contact with a line


# Main execution block to demonstrate file writing
if __name__ == "__main__":
    # Sample contact details to demonstrate the write_to_file function
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

    # Writing the sample contact details to the file
    write_to_file("../files/contact_details.txt", detail)
