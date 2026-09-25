"""
TASK 5 - Contact Book
CodSoft Python Programming Internship

A command-line Contact Book application that lets users add, view,
search, update, and delete contacts (name, phone, email, address).
Contacts are stored persistently in contacts.json.

Run:
    python contact_book.py
"""

import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contacts.json")


def load_contacts():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def save_contacts(contacts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2)


def next_id(contacts):
    return max([c["id"] for c in contacts], default=0) + 1


def add_contact(contacts):
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty.\n")
        return
    phone = input("Phone number: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()

    contact = {
        "id": next_id(contacts),
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
    }
    contacts.append(contact)
    save_contacts(contacts)
    print(f"Contact '{name}' added.\n")


def view_contacts(contacts):
    if not contacts:
        print("No contacts saved yet.\n")
        return
    print("\n--- CONTACT LIST ---")
    for c in contacts:
        print(f"{c['id']:>3}. {c['name']:<20} {c['phone']}")
    print()


def view_contact_detail(contact):
    print("\n--- CONTACT DETAILS ---")
    print(f"Name:    {contact['name']}")
    print(f"Phone:   {contact['phone']}")
    print(f"Email:   {contact['email']}")
    print(f"Address: {contact['address']}\n")


def search_contact(contacts):
    if not contacts:
        print("No contacts saved yet.\n")
        return
    term = input("Search by name or phone number: ").strip().lower()
    results = [
        c for c in contacts
        if term in c["name"].lower() or term in c["phone"].lower()
    ]
    if not results:
        print("No matching contacts found.\n")
        return
    print(f"\nFound {len(results)} match(es):")
    for c in results:
        view_contact_detail(c)


def find_contact_by_id(contacts, contact_id):
    for c in contacts:
        if c["id"] == contact_id:
            return c
    return None


def update_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        contact_id = int(input("Enter contact number to update: "))
    except ValueError:
        print("Please enter a valid number.\n")
        return
    contact = find_contact_by_id(contacts, contact_id)
    if not contact:
        print("Contact not found.\n")
        return

    print("Leave a field blank to keep its current value.")
    name = input(f"Name [{contact['name']}]: ").strip()
    phone = input(f"Phone [{contact['phone']}]: ").strip()
    email = input(f"Email [{contact['email']}]: ").strip()
    address = input(f"Address [{contact['address']}]: ").strip()

    if name:
        contact["name"] = name
    if phone:
        contact["phone"] = phone
    if email:
        contact["email"] = email
    if address:
        contact["address"] = address

    save_contacts(contacts)
    print("Contact updated.\n")


def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        contact_id = int(input("Enter contact number to delete: "))
    except ValueError:
        print("Please enter a valid number.\n")
        return
    contact = find_contact_by_id(contacts, contact_id)
    if not contact:
        print("Contact not found.\n")
        return
    contacts.remove(contact)
    save_contacts(contacts)
    print(f"Contact '{contact['name']}' deleted.\n")


def print_menu():
    print("=" * 32)
    print("        CONTACT BOOK MENU")
    print("=" * 32)
    print("1. View all contacts")
    print("2. Add contact")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")


def main():
    contacts = load_contacts()
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose 1-6.\n")


if __name__ == "__main__":
    main()
