# Table of Contents

- [SQL](#sql)
- [Column Types](#column-types)
- [Tables](#tables)
- [SQL Vulnerabilities](#sql-vulnerabilities)


# SQL

- Structured Query Language
- SQL is used when working with *relational databases*, where data is stored across multiple *Tables*
- Different RDBMS that are commonly used to store information → MySQL, PostgreSQL, SQLite
- MySQL and PostgreSQL run on servers separate from those running a website ; SQLite → lighter-weight system that can store all its data in a single file
- SQLite → default system used by Django

# Column Types

- TEXT: strings of text (Ex. a person’s name)
- NUMERIC: general form of numeric data (Ex. A date or boolean value)
- INTEGER: Any non-decimal number (Ex. a person’s age)
- REAL: Any real number (Ex. a person’s weight)
- BLOB (Binary Large Object): binary data  (Ex. an image)

# Tables

## Create Table

```sql
CREATE TABLE table_name(
	col1 type constraints, .. , coln type constraints,
	FOREIGN KEY (col) REFERENCES ParentTable(id)
)
```

### Constraints

- CHECK → Makes sure certain constraints are met before addition or modification of a row
- DEFAULT → Provides a default value
- NOT NULL → Value must be provided
- PRIMARY KEY → Used to uniquely identify the row
- UNIQUE → ensure no two rows have the same value in that column
- FOREIGN KEY → reference key, refers to the primary key in another table

**Example**

```sql
CREATE TABLE Products(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	cost_per_unit NUMERIC,
	quantity_on_hand INTEGER DEFAULT 0
)
```

## Insert

```sql
INSERT INTO table_name (col1, ..., coln) VALUES (val1,.... , valn);
```

- Values should be in the same order as the corresponding list of columns

## Select

```sql
SELECT [DISTINCT] column1, column2, ...
FROM table_name
[WHERE condition]
[GROUP BY column(s)]
[HAVING condition]
[ORDER BY column(s) [ASC|DESC]]
[LIMIT number_of_rows];
```

**Execution Order of a SELECT Query**

1. FROM → Determine which table(s) to read from.
2. WHERE → Filter rows based on conditions.
3. GROUP BY → Group remaining rows by specified column(s).
4. HAVING → Filter groups created by *GROUP BY*
5. SELECT → Compute/select the columns or expressions.
6. DISTINCT → Remove duplicate rows (if specified).
7. ORDER BY → Sort the result set.
8. LIMIT / OFFSET → Return only a subset of rows.

## Update

- Used to update existing row(s)

```sql
UPDATE table_name
SET column1 = value1,
column2 = value2,
...
WHERE condition;   # WHERE -> optional
```

## Delete

```sql
DELETE FROM table_name
WHERE condition;  # WHERE -> optional
```

## Functions

- SQL functions → can apply to the results of a query
- count(), avg(), sum(), min(), max()

## Joining tables

- Used to combine two tables horizontally
- Inner join, left join, right join, outer join

### Indexing

- To make queries efficient, columns can be indexed

```sql
CREATE INDEX index_name ON table_name(column_name);
```

# SQL Vulnerabilities

## SQL Injection

- Malicious users enter SQL code as input to bypass security
- Example:
    
    ```sql
    SELECT * FROM users
    WHERE username = "suriya"--" AND password = "12345";
    ```
    
- Here -- comments out the password check
- **Prevention:**
    - can use escape characters
    - By use abstraction layers/ORMs (Object Relational Mapping) to avoid raw SQL; for ex, prepared statements

## Race Condition

- Occurs when multiple database queries happen simultaneously
- To prevent, Lock the database until a transaction completes
