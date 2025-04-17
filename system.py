import csv
import os
from addressbook import AddressBook
from utils.utility import get_contact_details, print_contact, read_from_file, \
    write_to_file
from utils.regex import FILE_INPUT_KEY, FILE_INPUT_VAL


class AddressBookManager:
    def __init__(self):
        self.address_books = {}
        self.city_people = {}
        self.state_people = {}

    def show_address_book_names(self):
        if not self.address_books:
            print("There are no Address Books to Show!!!")
        else:
            print("Available Address Books:")
            for name in self.address_books:
                print(f"- {name}")

    def add_address_book(self, name):
        if name in self.address_books:
            print(f"Address Book with {name} already Available!!!")
        else:
            self.address_books[name] = AddressBook()
            print(f"Address Book with name: {name} is created.")
            return self.address_books[name]

    def handle_add_contact(self, book, details):
        contact = book.add_contact(details)
        self.add_into_city(contact)
        self.add_into_state(contact)

    def get_address_book(self, name):
        if name not in self.address_books:
            return None
        return self.address_books[name]

    def add_into_city(self, contact):
        if contact.info["city"] not in self.city_people:
            self.city_people[contact.info["city"]] = [contact]
        else:
            self.city_people[contact.info["city"]].append(contact)

    def search_by_city(self, city):
        if not self.city_people or city not in self.city_people:
            print(f"No contacts found in city: {city}")
            return
        for i, contact in enumerate(self.city_people[city]):
            print(f"\n-------- PERSON {i + 1} --------")
            print_contact(contact)

    def add_into_state(self, contact):
        if contact.info["state"] not in self.state_people:
            self.state_people[contact.info["state"]] = [contact]
        else:
            self.state_people[contact.info["state"]].append(contact)

    def search_by_state(self, state):
        if not self.state_people or state not in self.state_people:
            print(f"No contacts found in State: {state}")
            return
        for i, contact in enumerate(self.state_people[state]):
            print(f"\n-------- PERSON {i + 1} --------")
            print_contact(contact)

    def count_by_state_or_city(self, field, name):
        return (f'There are {len(self.city_people[name])} People in {name}'
                f' city.') if field == 'city' else \
            f'There are {len(self.state_people[name])} People in {name} state.'

    def create_from_file(self, file_path):
        if os.path.exists(file_path) and os.path.getsize(file_path) == 0:
            print(f"The file {file_path} is empty.")
            return

        book = None
        details = {}
        count = 0
        lines = read_from_file(file_path)

        for line in lines:
            if not line:
                continue

            if "AddressBook Name :" in line:
                book_name = FILE_INPUT_VAL.findall(line)[0][2:]
                book = self.add_address_book(book_name)
            elif "Contact" in line or "====" in line:
                continue
            else:
                count += 1
                key = FILE_INPUT_KEY.findall(line)[0][:-2]
                val = FILE_INPUT_VAL.findall(line)[0][2:]
                details[key] = val

            if count == 8:
                self.handle_add_contact(book, details.copy())
                count = 0
                details.clear()

    def save_to_file(self, filepath):

        for name, book in self.address_books.items():
            with open(filepath, 'w') as file:
                file.write(f"AddressBook Name : {name}\n")
                file.write(f"===========================================\n")
            for contact in book.contacts:
                write_to_file(filepath, contact.info)
            with open(filepath, 'a') as file:
                file.write("\n")

    def save_all_contacts_to_csv(self, csv_file_path):
        if not self.address_books:
            print("No Address Books available to save.")
            return

        headers = ["AddressBook", "First Name", "Last Name", "Address", "City",
                   "State", "Zip", "Phone", "Email"]

        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)

            for name, book in self.address_books.items():
                for contact in book.contacts:
                    writer.writerow([
                        name,
                        contact.info["first name"],
                        contact.info["last name"],
                        contact.info["address"],
                        contact.info["city"],
                        contact.info["state"],
                        contact.info["zip"],
                        contact.info["phone"],
                        contact.info["email"]
                    ])

        print(f"All contacts saved to '{csv_file_path}' successfully!")

    def __len__(self):
        return len(self.address_books)


def main():
    print("Welcome to Address Book Program!!!")
    default_file = 'files/contact_details.txt'
    manager = AddressBookManager()
    manager.create_from_file(default_file)

    run = True
    while run:
        try:
            choice = int(input('''
==============================
1. Show Address Books
2. Show Contacts
3. Add New Address Book
4. Add a Contact to an Address Book
5. Search Contacts by City
6. Search Contacts by State
7. Count By City or State
8. Sort an Address Book By any Field
9. Save contacts to CSV
10. Quit
==============================
Enter your choice: '''))

            print("\n")

            match choice:
                case 1:
                    manager.show_address_book_names()

                case 2:
                    manager.show_address_book_names()
                    selected_name = input("Enter Address Book Name: ").strip()
                    book = manager.get_address_book(selected_name)
                    if not book:
                        print("Invalid Address Book Name!")
                        continue
                    book.show_contacts()

                case 3:
                    while True:
                        book_name = input("Enter Address Book Name: ").strip()
                        manager.add_address_book(book_name)
                        add_more = input(
                            "Do you want to Create more Address Books? [Y/N]: ")
                        if add_more.lower() != 'y':
                            break

                case 4:
                    if len(manager) == 0:
                        print(
                            "No Address Books available. Please create one first.")
                        continue

                    while True:
                        manager.show_address_book_names()
                        selected_name = input(
                            "Enter Address Book Name: ").strip()
                        book = manager.get_address_book(selected_name)

                        if book:
                            details = get_contact_details()
                            if (details["first name"], details[
                                "last name"]) in book:
                                print(
                                    f"Contact With {details['first name']} "
                                    f"{details['last name']} already "
                                    f"in Address Book!!!")
                            else:
                                manager.handle_add_contact(book, details)
                                print("Contact added successfully.")

                            add_more = input(
                                "Do you want to add more contacts? [Y/N]: ")
                            if add_more.lower() != 'y':
                                break
                        else:
                            print(
                                f"No Address Book named '{selected_name}' found.")
                            break

                case 5:
                    city_choice = input("Please enter the City Name: ")
                    manager.search_by_city(city_choice)

                case 6:
                    state_choice = input("Please enter the State Name: ")
                    manager.search_by_state(state_choice)

                case 7:
                    lookup_choice = input("Enter 'city' for lookup by city.\
                           Enter 'state' for lookup by State: ").strip().lower()

                    if lookup_choice == 'city':
                        city_lookup = input("Enter City Name: ").strip()
                        if city_lookup in manager.city_people:
                            print(manager.count_by_state_or_city('city',
                                                                 city_lookup))
                        else:
                            print(f"No contacts found in city: {city_lookup}")
                    elif lookup_choice == 'state':
                        state_lookup = input("Enter State Name: ").strip()
                        if state_lookup in manager.state_people:
                            print(manager.count_by_state_or_city('state',
                                                                 state_lookup))
                        else:
                            print(
                                f"No contacts found in state: {state_lookup}")
                    else:
                        print(
                            "Invalid choice. Please enter 'city' or 'state'.")

                case 8:
                    manager.show_address_book_names()
                    address_book = manager.get_address_book(input(
                        "Select the Address Book to sort By Name:"))
                    field = input("""
Enter The field name to sort by:
- name
- city
- state
- zip""")
                    address_book.sort_by_field(field)
                    print("The Address Book is Now Sorted By Name...")

                case 9:
                    manager.save_all_contacts_to_csv('files/contacts.csv')

                case 10:
                    print("Exiting Address Book Program. Goodbye!")
                    manager.save_to_file(default_file)
                    run = False

                case _:
                    print("Invalid choice. Please select a valid option.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
