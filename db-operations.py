import sqlite3

# collection of functions to perform basic db operations (C.R.U.D.)
# note: to check validity, sqlite3.complete_statement("SELECT foo FROM bar;")

# connect to DB (create DB if non-existent)
def db_connect(db_name):
    directory = "."
    try:
        file_path = os.path.join(directory, db_name)
        # Check if the file exists at the specified path.
        assert(os.path.exists(os.path.join(directory, db_name)))
        conn = sqlite3.connect(db_name)
        print(f"Success! Able to connect to db: {db_name}")
        return conn.cursor()
    except (NameError):
        print(f"Failure! Unable to create/connect to db: {db_name}"/
              + "\n\n" + NameError)
    return None


def db_execute_cmd(sql_cmd, cur):
    try:
        return cur.execute(sql_cmd)
    except e:
        print("Failure!" + "\n" + e)
        return None


########################
# HELPER FUNCTIONS
########################
def request_sql_cmd(sql_cmd):
    return input(f"Please type SQL statement to execute")


########################
# MENU OPTIONS
########################
# define menu options


if __name__ == "__main__":
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Testing... db-operations.py \n")
    db_name = input(f"Write the name of the database you wish to connect: ")
    cur = db_connect(db_name)
    
    choice = "1"
    while (choice != "2"):
        print("\n\n")
        print("Please select an option:")
        print("1. Execute SQL Statement")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")
        match choice:
            case "1":
                print("selection is '1' - Execute SQL statement")
                sql_cmd = input("Type SQL command:")
                if (sqlite3.complete_statement(sql_cmd)):
                    print(f"Valid SQL command: {sql_cmd}")
                    result = db_execute_cmd(sql_cmd, cur)
                    print(result.fetchall())
                else:
                    print(f"Invalid SQL command! {sql_cmd}")
                    break
            case "2":
                print("selection is '2' - Exit")
            case _:
                print("Invalid selection. Please choose from the available options.\n")

print("Exiting... ")
