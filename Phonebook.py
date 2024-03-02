import time

class PhoneContact:
    def __init__(self):
        self.data = {}

    def add(self, name, number, email):
        # Check if the name is already in the data
        if name in self.data:
            # Update the existing contact information
            self.data[name] = {'number': number, 'email': email}
        else:
            # Add a new contact
            self.data[name] = {'number': number, 'email': email}

    def search(self, name=None, number=None):
        for key, value in self.data.items():
            if (name and name == key) or (number and number == value['number']):
                return value

        # If no matching information is found
        print("None existing information")
        return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print("Invalid name, or it doesn't exist!")

    def display(self):
        for key, value in self.data.items():
            print(f"{key}: {value['number']} - {value['email']}")


def main():
    phone_contact = PhoneContact()  # Corrected the variable name
    while True:
        time.sleep(2)
        print("\nPhonebook Management System:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display All Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':  # Convert choice to string for comparison
            name = input("Please enter the name: ")
            number = input("Enter the Number: ")
            email = input("Enter the email: ")
            phone_contact.add(name, number, email)
            print("The contact has been registered successfully!")
        elif choice == '2':  # Convert choice to string for comparison
            chosse = input("Do you want to use the name(1) or number information(2) for searching?(1/2): ")
            if chosse == '1':  # Convert chosse to string for comparison
                chose1 = input("Please Enter the name: ")
                print(phone_contact.search(chose1))
            else:
                chose2 = input("Please Enter the number: ")
                print(phone_contact.search(chose2))
        elif choice == '3':  # Convert choice to string for comparison
            t = input("Please enter the name of the contact you want to delete: ")
            phone_contact.delete(t)
        elif choice == '4':  # Convert choice to string for comparison
            phone_contact.display()
        elif choice == '5':  # Convert choice to string for comparison
            break
    print("Have a nice Day!")

if __name__ == "__main__":
    main()
