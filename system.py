from addressbook import AddressBook
from utils.utility import get_contact_details


class AddressBookManager:
    def __init__(self):
        self.address_books = {}

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
4. Quit
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
                            book.add_contact(details)
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
                    print("Exiting Address Book Program. Goodbye!")
                    run = False

                case _:
                    print("Invalid choice. Please select a valid option.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
