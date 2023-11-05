import os
import sys
import sqlite3

def convert_Dictionary(search_Res:list, columns:list):
    """
    Convert search result list into dictionary, with each result mapped to the column name according to the index
    """
    # Initialize variables
    new_dict:dict = {}

    # Map search result to columns
    for i in range(len(columns)):
        # Get current column
        curr_column = columns[i]

        # Get current search result
        curr_row = search_Res[i]

        # Map Key-Value
        new_dict[curr_column] = curr_row

    return new_dict

def generate_Cursor(con):
    """
    Generate the cursor pointing to the database connection object
    - i.e. 
        - like a mouse in a GUI application thats used to point to a memory address containing the database data
    """
    cur = con.cursor()
    return cur

def close_Connection(con):
    if con != None:
        # Close SQLite3 connection after use
        con.close()

def close_Cursor(cur):
    if cur != None:
        # Close SQLite3 connection cursor after use
        cur.close()

def execute_command(cur, cmd_str):
    """
    Execute SQL command only

    :: Params
    - cur : The cursor generated from an SQLite connection object
        Type: SQLite3.Cursor
    - cmd_str : The command string you wish to execute
        Type: String
    """
    cur.execute(cmd_str)

def execute_and_fetch(cur, cmd_str):
    """
    Execute SQL command and fetch the result

    :: Params
    - cur : The cursor generated from an SQLite connection object
        Type: SQLite3.Cursor
    - cmd_str : The command string you wish to execute
        Type: String
    """
    res = cur.execute(cmd_str)
    return res.fetchall()

def get_Values(cur, table_Name, col_Name="*"):
    """
    Retrieve values of the specified column from the specified table
    """
    # Format SQL command
    sql_cmd = "SELECT {} FROM {}".format(col_Name, table_Name)

    # Execute SQL command
    ret = cur.execute(sql_cmd)

    # Fetch all results from the result output
    out = ret.fetchall()

    return out

def get_first_Value(cur, table_Name, col_Name="*"):
    """
    Retrieve the first result of the specified column from the specified table
    """
    # Format SQL command
    sql_cmd = "SELECT {} FROM {}".format(col_Name, table_Name)

    # Execute SQL command
    ret = cur.execute(sql_cmd)

    # Fetch all results from the result output
    out = ret.fetchone()

    return out

def get_Ascending(cur, table_Name, cols, order=""):
    """
    Obtain the highest/greatest value in a column of a table

    :: Params
    - table_Name : Name of the table to target
    - cols : List of all columns to retrieve
        Type: List
    - order : The order condition; specify the column to order with
        Type: String
    """
    # Initialize Variables
    cmd_str = "SELECT {} FROM {} ORDER BY {} ASC".format(cols, table_Name, order)

    # Execute command
    res = cur.execute(cmd_str)

    # Fetch one result from the output
    output = res.fetchall()

    return output

def get_Descending(cur, table_Name, cols, order=""):
    """
    Obtain the highest/greatest value in a column of a table

    :: Params
    - table_Name : Name of the table to target
    - cols : List of all columns to retrieve
        Type: List
    - order : The order condition; specify the column to order with
        Type: String
    """
    # Initialize Variables
    cmd_str = "SELECT {} FROM {} ORDER BY {} DESC".format(cols, table_Name, order)

    # Execute command
    res = cur.execute(cmd_str)

    # Fetch one result from the output
    output = res.fetchall()

    return output

def get_all_Tables(cur):
    """
    List all tables
    """
    # Verify new table has been created
    # sql_cmd = "SELECT name FROM sqlite_master"
    return get_Values(cur, "sqlite_master", "name")

def get_row_ID(cur, table_Name, col_Name, filter_Val):
    """
    Find the row ID/number of the specified filter string within the column of a table
    """
    # Initialize Variables
    row_id = []

    # Get results
    ret = get_Values(cur, table_Name, col_Name)

    # Loop through results and check filter keyword
    for i in range(len(ret)):
        # Get current row
        curr_row = ret[i]

        # Get value
        curr_val = curr_row[0]

        # Check if filter keyword is in list
        if str(filter_Val) == str(curr_val):
            # Append row ID to list of rows
            row_id.append(i)

    # Return
    return row_id

def get_Conditional(cur, table_Name, result_Cols, filter_Conditions:dict):
    """
    Search and get a specified filter value/condition in a table

    :: Params
    - filter_Conditions : Key-Value (Dictionary) mapping of the search/conditional columns and values
    """
    # Initialize Variables
    sql_cmd = "SELECT {} FROM {} WHERE ".format(','.join(result_Cols), table_Name)
    number_of_Filters = len(filter_Conditions)
    curr_col = 0

    # Format conditions
    for k,v in filter_Conditions.items():
        # Key = Column Name
        # Value = Conditional Value
        sql_cmd += "{}={}".format(k,v)

        # Add delimiter if still have data
        if not (curr_col == (number_of_Filters-1)):
            # Add delimiter
            sql_cmd += ","

        # Increment Counter
        curr_col += 1

    # Execute SQL command
    res = cur.execute(sql_cmd)

    # Fetch results
    out = res.fetchall()
    return out

def search_Value(cur, table_Name, result_Cols, filter_Col, filter_Value):
    """
    Search for a specified filter value/condition in a table
    """
    """
    # Execute SQL command
    sql_cmd = "SELECT {} FROM {} WHERE {}={}".format(','.join(result_Cols), table_Name, filter_Col, filter_Value)
    res = cur.execute(sql_cmd)

    # Fetch results
    out = res.fetchall()
    """
    out = get_Conditional(cur, table_Name, result_Cols, **{filter_Col : filter_Value})
    return out

def create_Table(cur, table_Name, table_Columns):
    # Execute SQL command
    sql_cmd = "CREATE TABLE {}({})".format(table_Name, table_Columns)
    cur.execute(sql_cmd)

def validate_table_Exists(cur, table_Name):
    # Initialize Variables
    table_Exists = False

    # Check table exists
    sql_cmd = "SELECT name FROM sqlite_master"
    res = cur.execute(sql_cmd) # Execute command and return the result

    # Fetch one result from the result list
    res_filtered = res.fetchone()

    if res_filtered != None:
        if table_Name in res_filtered:
            table_Exists = True

    return table_Exists

def insert_Row(con, cur, target_Table, new_Data=None, index=-1, commit=False):
    """
    C.R.U.D
    - Insert a new row between existing rows

    :: Params
    - Positionals
        - con : The SQLite3 connection object created after opening the database
            Type: SQLite3.Connection
        - cur : The cursor generated from an SQLite connection object
            Type: SQLite3.Cursor
        - target_Table : The table to insert into
            Type: String
        - new_Data : List of all rows to insert/append into the table
            Type: List of Lists
    - Optionals
        - index : The index position to insert into; Enter '-1' to append as the newest element
            Type: Integer
        - commit : Flag to automatically commit/dont commit
            Type: Bool

    :: Return
    - The number of rows affected
        Type: Integer
    """
    # Initialize Variables
    sql_cmd = "INSERT INTO {} VALUES".format(target_Table)

    # Get list of items in table before proceeding
    values_before_Insert = get_Values(cur, target_Table)
    number_of_rows_Before = len(values_before_Insert)

    # Loop through all data to be inserted and append to the command
    if new_Data != None:
        for row_id in range(len(new_Data)):
            # Get current row
            row = new_Data[row_id]
            
            # Format row
            row_str = str(row)

            # Debug
            # print("Inserting [{}]...".format(row_str))

            # Append and concatenate
            sql_cmd += "{}".format(row_str)

            # Add delimiter if still have data
            if not (row_id == (len(new_Data)-1)):
                # Add delimiter
                sql_cmd += ","

        # Execute SQL command
        cur.execute(sql_cmd)

        if commit == True:
            """
            Commit all changes made to the database
            - like git, all changes made are temporary until you confirm you wish to write to the file
            """
            con.commit()
    else:
        print("No data provided.")

    # Get list of items in table after inserting
    values_after_Insert = get_Values(cur, target_Table)
    number_of_rows_After = len(values_after_Insert)

    # Verify rows affected
    rows_Affected = (number_of_rows_After - number_of_rows_Before)

    return rows_Affected

def update_Row():
    """
    C.R.U.D
    - Update/Modify/Replace data in a row
    """

def delete_Row():
    """
    C.R.U.D
    - Delete the row
    """

def filter_Highest(cur, table_Name, cols, order=""):
    """
    Obtain the highest/greatest value in a column of a table

    :: Params
    - table_Name : Name of the table to target
    - cols : List of all columns to retrieve
        Type: List
    - order : The order condition; specify column and ASC for Ascending and DESC for Descending
        Type: String
    """
    # Initialize Variables
    cmd_str = "SELECT {} FROM {} ORDER BY {}".format(cols, table_Name, order)
    number_of_Cols = len(cols)

    # Execute command
    res = cur.execute(cmd_str)

    # Fetch one result from the output
    output = res.fetchone()

    return output


