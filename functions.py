def find_contact(contacts, name):
   for contact in contacts.values():  # We only need the contact information 
    if contact["Name"].lower() == name.lower(): 
      return contact
    return None


def get_names(contacts):
  names = []
  for contact_id, contact_info in contacts.items():
    names.append(contact_info["Name"])
  return names

def get_contacts_by_age(contacts):
  return sorted(contacts.values(), key=lambda contact: contact["Age"])

def get_phone_number_by_name(contacts, name):
  for contact_id, contact_info in contacts.items():
    if contact_info['Name'].lower() == name.lower():
      return contact_info['PhoneNumber']
    return None


def sort_contacts_by_name(contacts):
  sorted_contact_details = sorted(contacts.items(), key=lambda item: item[1]["Name"].lower())
  return {contact_id: details for contact_id, details in sorted_contact_details}