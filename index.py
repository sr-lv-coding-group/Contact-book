try:
  from contact import contacts
  print(contacts)
  
  
except ModuleNotFoundError:
  print("Error: contacts.py file not found.")

