import json
import os

# Define the file to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from JSON file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

# Save contacts to JSON file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"Contact {name} added successfully!")

# Search for a contact
def search_contact(contacts):
    query = input("Enter name or phone number to search: ").strip().lower()
    results = [contact for contact in contacts if query in contact["name"].lower() or query in contact["phone"]]
    if results:
        print("Search Results:")
        for i, contact in enumerate(results, 1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contacts found.")

# Edit a contact
def edit_contact(contacts):
    search_contact(contacts)
    try:
        index = int(input("Enter the number of the contact to edit: ")) - 1
        if 0 <= index < len(contacts):
            contact = contacts[index]
            print(f"Editing Contact: {contact['name']}")
            contact['name'] = input(f"New name ({contact['name']}): ").strip() or contact['name']
            contact['phone'] = input(f"New phone ({contact['phone']}): ").strip() or contact['phone']
            contact['email'] = input(f"New email ({contact['email']}): ").strip() or contact['email']
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Delete a contact
def delete_contact(contacts):
    search_contact(contacts)
    try:
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted = contacts.pop(index)
            print(f"Contact {deleted['name']} deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Display all contacts
def display_contacts(contacts):
    if contacts:
        print("All Contacts:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contacts to display.")

# Main program loop
def main():
    contacts = load_contacts()
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            display_contacts(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
