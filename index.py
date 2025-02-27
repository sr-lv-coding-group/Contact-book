import time
import functions as func

try:
  from contact import contacts
  print("Test to show all contacts in db file")
  print(contacts) # debug
  print()
except ModuleNotFoundError:
  print("Error: contacts.py file not found.")
  print()


time.sleep(2) #pause between showing file names and running script  


def sort_contacts_by_age(contacts):
  """Return a dict list view of contact details sorted by age from youngest to oldest."""

  return sorted(contacts.values(), key=lambda contact: contact["Age"])


def sort_contacts_by_name(contacts):
  """Return a dict list view of contact details sorted by name in alphabetical order."""

  return sorted(contacts.values(), key=lambda contact: contact["Name"])


def get_contacts_by_name(contacts):
  """Return a dict list view of contact details that matches the given name"""
  
  name = input("Enter the name to search for: ")  # request name
  print()

  filtered_contacts = {k: v for k, v in contacts.items() if v["Name"].lower() == name.lower()}  # filter contacts by name

  return filtered_contacts.values()


def get_contacts_by_location(contacts):
  """Return a dict list view of contact details that matches the given location"""

  location = input("Enter the location to search for: ")  # request location
  print()

  filtered_contacts = {k: v for k, v in contacts.items() if v["Location"].lower() == location.lower()}  # filter contacts by location

  return filtered_contacts.values()


def get_contacts_by_number(contacts):
  """Return a dict list view of contact details that matches the given number"""

  number = input("Enter the phone number to search for: ")  # request phone number
  print()

  filtered_contacts = {k: v for k, v in contacts.items() if v["PhoneNumber"] == int(number)}  # filter contacts by phone number

  return filtered_contacts.values()


"""List of options containing methods; all functions' only parameter is the contact list.

  Parameters:
    dict: contact list

"""
options = {
  0: (exit, "Exit"),
  
  # sorting
  1: (sort_contacts_by_age, "Get all contacts; sorted by age (youngest to oldest)"),
  2: (sort_contacts_by_name, "Get all contacts; sorted by name (alphabetically)"),
  
  # one additional input
  3: (get_contacts_by_location, "Look up contacts by location"),
  4: (get_contacts_by_name, "Look up contacts by name"),
  5: (get_contacts_by_number, "Look up contacts by phone number"),

  # one additional input; specific result
  6: (get_contacts_by_name, "Get phone number by name", "PhoneNumber"),
  
  # sorting; specific result
  7: (sort_contacts_by_name, "Get all names in contact list", "Name"),
}

# Main menu interface for user to to select options via CLI
def main_menu():
  # print available options
  print("Available Options:")
  for option_id, option_details in options.items():
    print(f"{option_id} - {option_details[1]}")
  print()

  user_input = input(f"Enter your choice from 1-{len(options)}: ")  # user input
  print()

  try:
    option_number = int(user_input)
  except ValueError:
    print("Invalid input; try again.\n")

  # check if choice is valid then execute selected option
  if 0 < option_number < len(options):
    filtered_contacts = options[option_number][0](contacts)
    if filtered_contacts is not None and 0 < len(filtered_contacts):
      print("Showing result(s)...\n")

      try:
        filtered_contact_field = options[option_number][2]

        for contact in filtered_contacts:
          for contact_field, contact_value in contact.items():
            if contact_field == "Name" or contact_field == filtered_contact_field:
              print(f"{contact_field}: {contact_value}")
          print()

      except IndexError:
        for contact in filtered_contacts:
          for contact_field, contact_value in contact.items():
            print(f"{contact_field}: {contact_value}")
          print()

    else:
      print("No results found.\n")
  else:
    print("Invalid number; try again.\n")

  print("Returning to main menu...\n")
  time.sleep(1)

# Running the main menu
while True:
    main_menu()