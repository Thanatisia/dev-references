import os
import sys
import sqlite3

def main():
    # Initialize Variables
    con = None 
    cur = None
    db_Path = "."
    db_Name = "file.db"
    db_fullName = "{}/{}".format(db_Path, db_Name)

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

        except Exception as ex:
            print("[-] Exception caught: {}".format(ex))
        finally:
            # Close SQLite3 connection cursor after use
            if cur != None:
                cur.close()

            # Close SQLite3 connection after use
            if con != None:
                con.close()
    else:
        print("Empty file path/name provided: [Path: {}, Name: {}]".format(db_Path, db_Name))

if __name__ == "__main__":
    main()

