def get_contact_details():
    details = {}
    fields = ["first name", "last name", "address", "city", "state", "zip",
              "phone", "email"]

    for field in fields:
        details[field] = input(f'Enter {field}:')

    return details

if __name__ == "__main__":

   print(get_contact_details())