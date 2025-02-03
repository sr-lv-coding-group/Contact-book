import time
try:
  from contact import contacts
  print("Test to show all contacts in db file")
  time.sleep(2)
  print(contacts)
except ModuleNotFoundError:
  print("Error: contacts.py file not found.")

#pause between showing file names and running script  
time.sleep(2)

def find_contact(contacts, name):
   for contact in contacts.values():  # We only need the contact information 
    if contact["Name"].lower() == name.lower(): 
      return contact
    return None

#name_to_search = input("Enter the name to search for: ")

#found_contact = find_contact(contacts, name_to_search)

#if found_contact:
 # print("Contact found for", name_to_search)
 # for key, value in found_contact.items():
  #  print(key + ": " + str(value))
#else:
 # print("No contact found for", name_to_search)
#Imputs Name returns contact card
def get_names(contacts):
  names = []
  for contact_id, contact_info in contacts.items():
    names.append(contact_info["Name"])
  return names

#names_list = get_names(contacts)
#print(names_list)
#sorts contacts by age
def get_contacts_by_age(contacts):
  return sorted(contacts.values(), key=lambda contact: contact["Age"])

#sort_contacts = get_contacts_by_age(contacts)
#for contact in sort_contacts:
  #print("Name: " + contact['Name'] + ", Age: " + str(contact['Age']))



#print("\nTESTING GET PHONE NUMBER BY NAME")

#searches through a list for the specified name and returns their phone number
def get_phone_number_by_name(contacts, name):
  for contact_id, contact_info in contacts.items():
    if contact_info['Name'].lower() == name.lower():
      return contact_info['PhoneNumber']
    return None
      #print(f"Name: {contact_info['Name']}, Phone: {contact_info['PhoneNumber']}")

# usage
get_phone_number_by_name(contacts, "Daniel")

#print("\nTESTING PRINT SORTED CONTACT LIST BY NAME")

# returns a sorted contact list in alphabetically order
def sort_contacts_by_name(contacts):
  sorted_contact_details = sorted(contacts.items(), key=lambda item: item[1]["Name"].lower())
  return {contact_id: details for contact_id, details in sorted_contact_details}

# usage
#sorted_contacts = sort_contacts_by_name(contacts)
#for contact_id, details in sorted_contacts.items():
  #print(f"Name: {details['Name']}, Phone: {details['PhoneNumber']}")

#print()
#CLI menue of options for user to input
def main_menu():
    print("\nSelect an option:")
    print("1. Find a contact")
    print("2. Get all names in contact list")
    print("3. Get all contacts sorted by age")
    print("4. Get phone number by name")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name_to_search = input("Enter the name to search for: ")
        found_contact = find_contact(contacts, name_to_search)
        if found_contact:
            print(f"Contact found for {name_to_search}:")
            for key, value in found_contact.items():
                print(f"{key}: {value}")
        else:
            print(f"No contact found for {name_to_search}")
            
    if choice == "1":
      name_to_search = input("Enter the name to search for: ")
      found_contact = find_contact(contacts, name_to_search)
      if found_contact:
          print(f"Contact found for {name_to_search}:")
          for key, value in found_contact.items():
              print(f"{key}: {value}")
      else:
            print(f"No contact found for {name_to_search}")

    elif choice == "2":
        names_list = get_names(contacts)
        print("Names in contact list:")
        for name in names_list:
            print(name)

    elif choice == "3":
        sorted_contacts = get_contacts_by_age(contacts)
        print("Contacts sorted by age:")
        for contact in sorted_contacts:
            print(f"Name: {contact['Name']}, Age: {contact['Age']}")

    elif choice == "4":
        name_to_search = input("Enter the name to get the phone number: ")
        phone_number = get_phone_number_by_name(contacts, name_to_search)
        if phone_number:
            print(f"Phone number for {name_to_search}: {phone_number}")
        else:
            print(f"No phone number found for {name_to_search}")

    elif choice == "5":
        print("Exiting program...")
        exit()

    else:
        print("Invalid choice! Please select a number between 1 and 5.")

# Running the main menu
while True:
    main_menu()