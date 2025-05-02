import json
import os
from pathlib import Path
from datetime import datetime

class ContactBook:
    def __init__(self, file_path='contacts.json'):
        self.file_path = Path(file_path)
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        """Load contacts from JSON file"""
        if self.file_path.exists():
            try:
                with open(self.file_path, 'r') as f:
                    self.contacts = json.load(f)
            except json.JSONDecodeError:
                self.contacts = []
        else:
            self.contacts = []

    def save_contacts(self):
        """Save contacts to JSON file"""
        with open(self.file_path, 'w') as f:
            json.dump(self.contacts, f, indent=2)

    def add_contact(self, name, phone, email=None, address=None):
        """Add a new contact"""
        contact = {
            'id': len(self.contacts) + 1,
            'name': name,
            'phone': phone,
            'email': email,
            'address': address,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        self.contacts.append(contact)
        self.save_contacts()
        return contact

    def get_contact(self, contact_id):
        """Get a contact by ID"""
        for contact in self.contacts:
            if contact['id'] == contact_id:
                return contact
        return None

    def update_contact(self, contact_id, **kwargs):
        """Update contact information"""
        for contact in self.contacts:
            if contact['id'] == contact_id:
                for key, value in kwargs.items():
                    if key in contact and value is not None:
                        contact[key] = value
                contact['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_contacts()
                return contact
        return None

    def delete_contact(self, contact_id):
        """Delete a contact"""
        for i, contact in enumerate(self.contacts):
            if contact['id'] == contact_id:
                deleted_contact = self.contacts.pop(i)
                self.save_contacts()
                return deleted_contact
        return None

    def search_contacts(self, search_term):
        """Search contacts by name, phone, or email"""
        results = []
        search_term = search_term.lower()
        
        for contact in self.contacts:
            if (search_term in contact['name'].lower() or
                search_term in contact['phone'].lower() or
                (contact['email'] and search_term in contact['email'].lower())):
                results.append(contact)
        
        return results

    def list_contacts(self):
        """List all contacts"""
        return self.contacts

def display_contact(contact):
    """Display a single contact"""
    if not contact:
        print("Contact not found.")
        return
    
    print(f"\nID: {contact['id']}")
    print(f"Name: {contact['name']}")
    print(f"Phone: {contact['phone']}")
    if contact['email']:
        print(f"Email: {contact['email']}")
    if contact['address']:
        print(f"Address: {contact['address']}")
    print(f"Created: {contact['created_at']}")
    print(f"Last Updated: {contact['updated_at']}")

def display_menu():
    """Display the main menu"""
    print("\nContact Book Menu:")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search contacts")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Exit")

def main():
    contact_book = ContactBook()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            print("\nAdd New Contact")
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            email = input("Email (optional): ").strip() or None
            address = input("Address (optional): ").strip() or None
            
            if name and phone:
                contact = contact_book.add_contact(name, phone, email, address)
                print(f"\nContact added successfully (ID: {contact['id']})")
            else:
                print("Name and phone are required!")
        
        elif choice == '2':
            contacts = contact_book.list_contacts()
            if contacts:
                print("\nAll Contacts:")
                for contact in contacts:
                    print(f"{contact['id']}: {contact['name']} - {contact['phone']}")
            else:
                print("\nNo contacts found.")
        
        elif choice == '3':
            search_term = input("\nEnter search term: ").strip()
            if search_term:
                results = contact_book.search_contacts(search_term)
                if results:
                    print("\nSearch Results:")
                    for contact in results:
                        print(f"{contact['id']}: {contact['name']} - {contact['phone']}")
                else:
                    print("\nNo matching contacts found.")
            else:
                print("\nPlease enter a search term.")
        
        elif choice == '4':
            contact_id = input("\nEnter contact ID to update: ").strip()
            if contact_id.isdigit():
                contact_id = int(contact_id)
                contact = contact_book.get_contact(contact_id)
                if contact:
                    display_contact(contact)
                    print("\nEnter new information (leave blank to keep current):")
                    
                    name = input(f"Name [{contact['name']}]: ").strip() or None
                    phone = input(f"Phone [{contact['phone']}]: ").strip() or None
                    email = input(f"Email [{contact['email'] or 'None'}]: ").strip() or None
                    if email == 'None':
                        email = None
                    address = input(f"Address [{contact['address'] or 'None'}]: ").strip() or None
                    if address == 'None':
                        address = None
                    
                    updated = contact_book.update_contact(
                        contact_id,
                        name=name,
                        phone=phone,
                        email=email,
                        address=address
                    )
                    
                    if updated:
                        print("\nContact updated successfully:")
                        display_contact(updated)
                else:
                    print("\nContact not found.")
            else:
                print("\nPlease enter a valid contact ID.")
        
        elif choice == '5':
            contact_id = input("\nEnter contact ID to delete: ").strip()
            if contact_id.isdigit():
                contact_id = int(contact_id)
                contact = contact_book.get_contact(contact_id)
                if contact:
                    display_contact(contact)
                    confirm = input("\nAre you sure you want to delete this contact? (y/n): ").lower()
                    if confirm == 'y':
                        deleted = contact_book.delete_contact(contact_id)
                        if deleted:
                            print("\nContact deleted successfully.")
                else:
                    print("\nContact not found.")
            else:
                print("\nPlease enter a valid contact ID.")
        
        elif choice == '6':
            print("\nGoodbye!")
            break
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
