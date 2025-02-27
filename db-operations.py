import sqlite3
import json



# collection of functions to perform basic db operations (C.R.U.D.)
# note: to check validity, sqlite3.complete_statement("SELECT foo FROM bar;")

# connect to DB (create DB if non-existent)

def connect_db(directory=".",db_name=None):
    if (not db_name):
        db_name = input(f">>> Write the name of the database you wish to connect: ")
    try:
        file_path = os.path.join(directory, db_name)
        # Check if the file exists at the specified path.
        assert(os.path.exists(file_path), )
        conn = sqlite3.connect(db_name)
        print(f"\tSuccess! Able to connect to db: {db_name}")
        return conn.cursor()
    except (AssertionError):
        print(f"\tFailure! Unable to create/connect to db: {db_name}"/
              + "\n\n" + NameError)
    return None



def execute_sql_cmd(cur=None, sql_cmd=None):
    while(not cur and not sql_cmd):
        if (not cur):
            cur = connect_db()
        if (not sql_cmd):
            sql_cmd = request_sql_cmd()
    try:
        print(cur.execute(sql_cmd))
        return cur
    except Error as e:
        print("\tFailure!" + "\n" + e)
        return None


########################
# HELPER FUNCTIONS
########################

def request_sql_cmd():
    return input(f">>> Please type SQL statement to execute: ")


def write_dict_to_json(dict_data=None):
    with open(dict_date, "w", encoding='utf-8') as f:
        json.dunp(json.dumps(dict_data), f)


def read_dict_from_json(json_data=None):
     with open(json_data, "r", encoding='utf-8') as f: 
         return json.loads(json.load(f))


def build_insert_from_json(json_data="contacts.json", TABLE_NAME="CONTACTS"):
    contacts = read_dict_from_json(json_data=json_data)
    sqlstatement = ''
    
    for contact_id, contact in contacts.items():
        keylist = "(ID"
        valuelist = f"('{contact_id}'"
        firstPair = True
        for key, value in contact.items():
#            print(f"key, value: {key}, {value}")
            keylist += ", "
            valuelist += ", "
            keylist += key
            if isinstance(value, str):
                valuelist += "'" + value + "'"
            else:
                valuelist += str(value)
        keylist += ")"
        valuelist += ")"

        sqlstatement += "INSERT INTO " + TABLE_NAME + " " + keylist + " VALUES " + valuelist + ";\n"
    print(sqlstatement)
    return sqlstatement


def initialize_db(db_data=None, db_name=None):
    cur = connect_db(db_name)
    #
    # verify structure is valid for contactbook 
    #
    return cur


def print_menu_options(options):
    for option_id, option in options.items():
        print(f"\t{option_id}: {option['desc']}")



if __name__ == "__main__":
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"testing... db-operations.py\n")    
    ########################
    # MENU OPTIONS
    ########################
    # define menu options
    # format: [OPTION#] : {"func": function call, "desc": description}
    menu = {
            0: {"func": exit, "desc": "Exit"},
            1: {"func": connect_db, "desc": "Connect to a database."},
            2: {"func": execute_sql_cmd, "desc": "Execute SQL statement"},
            3: {"func": build_insert_from_json, "desc": "Construct a SQL Insert Statement from JSON file"},
            }          
    cur = None
    while(menu):
        print_menu_options(menu)
        user_input = input(f">>> Enter your choice from 0-{len(menu)-1}: ")
        print("\tUser selected: " + user_input)

        try:
            user_choice = int(user_input)
            if ((user_choice < 0) or (user_choice >= len(menu))):
                raise ValueError('*** Invalid input:', user_choice)
            if callable(menu[user_choice]["func"]):
                results = menu[user_choice]["func"]() #  potentially use args to zip parameters?
                if (not results):
                    cur = results
        except ValueError as ve:
            print(f"*** Invalid input. Please select from the available options. {ve}\n\n")
         
    print("Exiting... ")

