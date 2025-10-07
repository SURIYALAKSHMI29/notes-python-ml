# Working with SQL in the terminal

```sql
sqlite3 products.sql
```

- sqlite3 → starts the SQLite command-line shell
- products.sql → SQLite will open this file
- After this command, it will enter SQLite prompt
    
    ```sql
    sqlite>
    ```
    

### .tables

- List the created table in SQLite

### .mode columns

- Changes the output display to a columnar format
- Each column gets aligned neatly, making it easier to read

### .header yes

- Show column headers (names of the table columns) in the output
    
    ```sql
    sqlite> .mode columns
    sqlite> .header yes
    sqlite> SELECT * FROM products;
    
    /*
    id  name       cost_per_unit  qty_on_hand
    1   Chips      20             100
    2   Chocolate  10             0
    */
    ```

### .schema

- Shows the CREATE TABLE statements for all tables in the database
- Useful to check table structure and column types
    
    ```sql
    sqlite> .schema products
    -- CREATE TABLE products (
    -- id INTEGER PRIMARY KEY AUTOINCREMENT,
    -- name TEXT NOT NULL,
    -- cost_per_unit numeric,
    -- qty_on_hand INTEGER DEFAULT 0
    -- );
    ```

### .import

- Imports data from a **CSV file** into a table
- Requires the table to exist first
    
    ```sql
    .mode csv
    .import data.csv Products
    ```
    
### .quit

- Exits the SQLite shell.
    
    ```sql
    .quit
    ```

### .dump

- Used to **export the entire database as SQL statements** that can recreate the database, including tables and all their data
- Useful for **backup or moving the database** to another system
    
    ```sql
    .dump
    ```
    

### .read

- Executes all SQL commands from a file
- Useful for running multiple statements at once
    
    ```sql
    .read setup.sql
    ```
    
### Output Mode

- .mode csv → output in CSV format
- .mode list → output as a plain list
- .mode html → output as HTML table
- .mode line → each row displayed as a key-value list
