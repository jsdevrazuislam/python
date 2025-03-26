import json

def main():
    def isExits(contracts, name):
        for contact in contracts:
            if contact['name'] == name:
                return contact
        return None

    def save_contract(contracts):
        try:
            with open('contacts.txt', 'w') as file:
                json.dump(contracts, file)
        except Exception as e:
            print("Error:", e)

    def load_contract():
        try:
            with open('contacts.txt', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def add_new_contract(contracts):
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        contracts.append({'name': name, 'phone': phone, 'email': email})
        save_contract(contracts)
        print('✅ Contact Added Successfully!')

    def view_all_contract(contracts):
        print("📌 All Contacts: ")
        for index, contact in enumerate(contracts, start=1):
            print(f"{index}. {contact['name']} - {contact['phone']} - {contact['email']}")

    def search_by_contract(contracts):
        name = input("Enter Name to Search: ")
        data = isExits(contracts, name)
        if data:
            print(f"✅ Found: {data['name']} - {data['phone']} - {data['email']}")
        else:
            print("No match found")

    def update_contract(contracts):
        name = input("Enter Name to Update: ")
        new_name = input("Enter New Name: ")
        phone = input("Enter New Phone: ")
        email = input("Enter New Email: ")
        data = isExits(contracts, name)
        if data:
            for item in contracts:
                if item["name"] == name:
                    item.update({'name': new_name, 'phone': phone, 'email': email})
            save_contract(contracts)
            print('✅ Contact Updated!')
        else:
            print("No match found to update")

    def delete_contract(contracts):
        name = input("Enter Name to Delete: ")
        data = isExits(contracts, name)
        if data:
            contracts = [contact for contact in contracts if contact['name'] != name]
            save_contract(contracts)
            print('✅ Contact Deleted Successfully!')
        else:
            print("No match found to delete")

    while True:
        print("\nWelcome to Contact Management System!")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        try:
            choose = int(input('Enter your choice: '))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue

        contracts = load_contract()

        match choose:
            case 1:
                add_new_contract(contracts)
            case 2:
                view_all_contract(contracts)
            case 3:
                search_by_contract(contracts)
            case 4:
                update_contract(contracts)
            case 5:
                delete_contract(contracts)
            case 6:
                print("Exiting... Goodbye! 👋")
                break
            case _:
                print("❌ Invalid choice! Please try again.")

if __name__ == '__main__':
    main()