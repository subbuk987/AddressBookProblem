from addressbook import AddressBook
from utils.utility import get_contact_details, print_contact


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

    def get_address_book(self, name):
        if name not in self.address_books:
            return None
        return self.address_books[name]

    def add_into_city(self, contact):
        if contact.details["city"] not in self.city_people:
            self.city_people[contact.details["city"]] = [contact]
        else:
            self.city_people[contact.details["city"]].append(contact)

    def search_by_city(self, city):
        if not self.city_people or city not in self.city_people:
            print(f"No contacts found in city: {city}")
            return
        for i, contact in enumerate(self.city_people[city]):
            print(f"\n-------- PERSON {i + 1} --------")
            print_contact(contact)

    def add_into_state(self, contact):
        if contact.details["state"] not in self.state_people:
            self.state_people[contact.details["state"]] = [contact]
        else:
            self.state_people[contact.details["state"]].append(contact)

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

    def __len__(self):
        return len(self.address_books)


def main():
    print("Welcome to Address Book Program!!!")
    manager = AddressBookManager()

    run = True
    while run:
        try:
            choice = int(input('''
==============================
1. Show Address Books
2. Add New Address Book
3. Add a Contact to an Address Book
4. Search Contacts by City
5. Search Contacts by State
6. Count By City or State
7. Sort an Address Book By Name
8. Quit
==============================
Enter your choice: '''))

            print("\n")

            match choice:
                case 1:
                    manager.show_address_book_names()

                case 2:
                    while True:
                        book_name = input("Enter Address Book Name: ").strip()
                        manager.add_address_book(book_name)
                        add_more = input(
                            "Do you want to Create more Address Books? [Y/N]: ")
                        if add_more.lower() != 'y':
                            break

                case 3:
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
                                contact = book.add_contact(details)
                                manager.add_into_city(contact)
                                manager.add_into_state(contact)
                                print("Contact added successfully.")

                            add_more = input(
                                "Do you want to add more contacts? [Y/N]: ")
                            if add_more.lower() != 'y':
                                break
                        else:
                            print(
                                f"No Address Book named '{selected_name}' found.")
                            break

                case 4:
                    city_choice = input("Please enter the City Name: ")
                    manager.search_by_city(city_choice)

                case 5:
                    state_choice = input("Please enter the State Name: ")
                    manager.search_by_state(state_choice)

                case 6:
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

                case 7:
                    manager.show_address_book_names()
                    address_book = manager.get_address_book(input(
                        "Select the Address Book to sort By Name:"))
                    address_book.sort_by_name()
                    print("The Address Book is Now Sorted By Name...")

                case 8:
                    print("Exiting Address Book Program. Goodbye!")
                    run = False

                case _:
                    print("Invalid choice. Please select a valid option.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
