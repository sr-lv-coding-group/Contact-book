import sqlite3

# collection of functions to perform basic db operations (C.R.U.D.)
# note: to check validity, sqlite3.complete_statement("SELECT foo FROM bar;")
# CREATE / INSERT


# READ / SELECT


# UPDATE / UPDATE


# DELETE /DELETE


# connect to DB (create DB if non-existent)
def connect_db(db_name):
    try:
        conn = sqlite3.connect(db_name)
        print(f"Success! Able to connect to db: {db_name}")
    except (NameError):
        print(f"Failure! Unable to create/connect to db: {db_name}"/
              + "\n\n" + NameError)

########################
# HELPER functions
########################
# request name of object
def request_object_name(obj):
    return input(f"Enter the name of the {obj}:")


if __name__ == "__main__":
    print("Testing... db-operations.py \n")
    print("Please select an option:")
    print("1. Connect Database (w/implicit creation)")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    match choice:
        case "1":
            db_name = request_object_name(obj="database")            
            connect_db(db_name)
        case "5":
            print("Exiting... ")
        case _:
            print("Invalid selection. Please choose from the available options.\n")
