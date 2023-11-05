# Python Library - SQLite3

## Quickstart Flow
- Import library 'sqlite3'
    ```python
    import sqlite3
    ```

- Open SQLite Database connection and return object
    - Standalone
        ```python
        con = sqlite3.connect("database-name", **other_options)
        ```
    - Using 'with' keyword for temporary run
        ```python
        with sqlite3.connect("database-name", **other_options) as con:
            ...
        ```

- Generate SQLite Database cursor pointing to the database connection
    ```python
    cur = con.cursor()
    ```

- Format SQL query string
    - SELECT
        ```python
        sql_cmd = "SELECT [columns,...] FROM [table-name] WHERE [conditionals, {AND ...}] ORDER BY [order-column=order-value] {DESC|ASC} ..."
        ```

- Execute SQL command
    - Fetching/Select rows from database
        ```python
        results = cur.execute(sql_cmd)
        ```
    - Writing to database
        ```python
        cur.execute(sql_cmd)
        ```

- Fetching/Select rows
    - Only one row from the results
        ```python
        row = results.fetchone()
        ```

    - Many results in a list
        ```python
        row = results.fetchmany()
        ```

    - All rows from the results
        ```python
        row = results.fetchall()
        ```

- Close database cursor after use
    ```python
    cur.close()
    ```
- Close connection to SQLite3 database after use
    ```python
    con.close()
    ```

## Documentations

### Classes

### Functions

### Attributes/Variables

## Wiki

## Resources

## References

## Remarks
