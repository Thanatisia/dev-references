import os
import sys
from setup import Setup
from lib.sqlite_lib import sqlite3, validate_table_Exists, get_Values, get_row_ID, get_all_Tables, create_Table, insert_Row, close_Cursor, close_Connection

def display_help():
    """
    Display help menu
    """
    print("Help")

def display_Environment():
    """
    Display Environment Variable values
    """
    print("All Environment Variables:")
    cs_Env.list_all_Env()

def main():
    # Initialize Variables
    con = None 
    cur = None
    db_Path = env_var["DATABASE_PATH"]
    db_Name = env_var["DATABASE_NAME"]
    db_fullName = "{}/{}".format(db_Path, db_Name)
    database_Schema = {
        "tables" : [
            # Keys = 
            #   - row_id
            #   - table_Name
            #   - table_Columns
            {"row_id" : 0, "table_Name" : "movie", "table_Columns" : "title, year, score"}
        ]
    }
    database_Tables = database_Schema["tables"]

    # Check null value
    if (db_Path != None) and (db_Name != None):
        # Check if database exists
        if not os.path.isfile(db_fullName):
            # File does not exist
            print("Database {} does not exist, creating...".format(db_Name))

        try:
            """
            Connect to SQLite3 database and return the connection object
            """
            con = sqlite3.connect(db_Name)

            print("[+] Connected to database: {}".format(db_Name))

            """
            Generate the cursor pointing to the database connection object
            - i.e. 
                - like a mouse in a GUI application thats used to point to a memory address containing the database data
            """
            cur = con.cursor()

            print("[+] Cursor has been generated.")

            """
            Create database table(s)
            """
            print("=====================")
            print("Create Database Table")
            print("=====================")

            for table_id in range(len(database_Tables)):
                # Get current table
                curr_table = database_Tables[table_id]

                # Get table schema
                table_Name = curr_table["table_Name"]
                table_Columns = curr_table["table_Columns"]

                # Check table exists
                print("Verifying table [{}] exists...".format(table_Name))
                if validate_table_Exists(cur, table_Name):
                    print("[-] table {} is in database.".format(table_Name))
                else:
                    # Create table
                    # Execute SQL command
                    print("table [{}] does not exists, creating table...".format(table_Name))
                    create_Table(cur, table_Name, table_Columns)

                    # Verify new table has been created
                    if validate_table_Exists(cur, table_Name):
                        print("[+] table {} has been created.".format(table_Name))
                    else:
                        print("[-] error creating table {}".format(table_Name))

                print("")

            """
            List all tables
            """
            print("===============")
            print("List all tables")
            print("===============")
            res_All = get_all_Tables(cur)
            print("All Tables: {}".format(res_All))

            """
            Insert Data
            """
            target_Table = "movie"
            new_Data = [('Monty Python and the Holy Grail', 1975, 8.2), ('And Now for something completely different', 1971, 7.5)]
            rows_Affected = insert_Row(con, cur, target_Table, new_Data, commit=True)
            print("Rows Affected: {}".format(rows_Affected))

            """
            List all data in table
            """
            target_Table = "movie"
            target_Columns = "*"
            # Fetch all results from the result output
            out = get_Values(cur, target_Table, target_Columns)

            print("==============")
            print("List all Rows")
            print("==============")
            print(out)

            """
            Get Row ID of the search value
            """
            # Fetch row id
            row_id = get_row_ID(cur, target_Table, "year", "1971")

            if len(row_id) == 0 :
                print("No rows returned.")
            else:
                print("Row ID: {}".format(row_id))
        except Exception as ex:
            print("[-] Exception caught: {}".format(ex))
        finally:
            # Close SQLite3 connection cursor after use
            close_Cursor(cur)

            # Close SQLite3 connection after use
            close_Connection(con)
    else:
        print("Empty file path/name provided: [Path: {}, Name: {}]".format(db_Path, db_Name))

def setup():
    """
    Per-source setup
    """
    # Set global variables
    global cs_Env, env_var

    # Initialize Classes
    setup = Setup()

    # Obtain variables
    cs_Env = setup.cs_Env
    env_var = setup.env

    # Pre-Start checks
    display_Environment()

    print("")

if __name__ == "__main__":
    setup()
    main()


