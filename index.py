try:
  from contact import contacts
  print(contacts)
except ModuleNotFoundError:
  print("Error: contacts.py file not found.")

def names_list(contacts):
    return ["Name"] in contacts()

print(names_list)