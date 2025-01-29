try:
  from contact import contacts
  print(contacts)
except ModuleNotFoundError:
  print("Error: contacts.py file not found.")

# def names_list(contacts):
#     return ["Name"] in contacts()

# print(names_list(contacts))

# def get_phone_number(contacts, name):
#   for contact_id, contact_info in contacts.items():
#     if contact_info["Name"].lower() == name.lower():
#       return contact_info["PhoneNumber"]
#     return None
  
# name_to_search = input("Enter name: ")

# phone_number = get_phone_number(contacts, name_to_search)

# if phone_number:
#   print(f"{name_to_search.capitalize()} phone number is {phone_number}")
# else:
#   print(f"No contact found for {name_to_search}")

contacts = {
    1: {
        "Name": "Daniel",
        "Age": 35,
        "PhoneNumber": 5555551212,
        "Location": "Las Vegas"
    },
    
    2: {
        "Name": "Dennis",
        "Age": 27,
        "PhoneNumber": 1234567890,
        "Location": "New York"
    },
    3: {
        "Name": "Keegan",
        "Age": 39,
        "PhoneNumber": 4569876543,
        "Location": "New York"
    },
}

def find_contact(contacts, name):
  for contact_id, contact_info in contacts.items():
    if contact_info["Name"].lower() == name.lower():
      return contact_info
  return None

name_to_search = input("Enter the name to search for: ")

found_contact = find_contact(contacts, name_to_search)

if found_contact:
  print("Contact found for", name_to_search)
  for key, value in found_contact.items():
    print(key + ": " + str(value))
else:
  print("No contact found for", name_to_search)

def get_names(contacts):
  
  names = []
  for contact_id, contact_info in contacts.items():
    names.append(contact_info["Name"])
  return names

names_list = get_names(contacts)
print(names_list)

def get_contacts_by_age(contacts):
  def age_id(contact):
    return contact["Age"]
  sort_contacts = sorted(contacts.values(), key=age_id)
  return sort_contacts

sort_contacts = get_contacts_by_age(contacts)
for contact in sort_contacts:
  print("Name: " + contact['Name'] + ", Age: " + str(contact['Age']))