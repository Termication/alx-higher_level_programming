# MySQL Database Management

This README outlines essential concepts and techniques for managing MySQL databases.

## Creating Users

CREATE USER Statement: Use the CREATE USER statement to create a new user account. Specify the username, hostname (where the user can access from), and a secure password.

SQL
```sql
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'strong_password';
```

-Replace new_user with your desired username.
-Replace strong_password with a strong, unique password.
-localhost allows access from the local machine. Use a specific IP address or wildcard (%) for remote access.
-GRANT Privileges: Once a user is created, use GRANT statements to define their permissions on databases and tables. Specify the user, privilege type (e.g., SELECT, INSERT, UPDATE, DELETE), and the database/table object.

SQL
```sql
GRANT SELECT, INSERT ON my_database.* TO 'new_user'@'localhost';
```

This grants SELECT (read) and INSERT (create) privileges to the my_database for new_user.
Data Integrity Constraints

PRIMARY KEY: A column (or combination of columns) that uniquely identifies each row in a table. Enforces data integrity and allows for efficient retrieval using indexes.

SQL
```sql
CREATE TABLE customers (
    customer_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,  -- Ensures unique ID
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE  -- Allows only unique email addresses
);
```
FOREIGN KEY: References a primary key in another table to establish a relationship between tables. Maintains data consistency by preventing orphaned records (referencing non-existent values).

SQL
```sql
CREATE TABLE orders (
    order_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)  -- Links orders to customers
);
```

NOT NULL: Ensures a column cannot have missing values (NULL). Use with caution as it might not always be suitable.

UNIQUE: Allows only distinct values in a column or column combination. Enforces data integrity for specific attributes.

Multi-Table Data Retrieval

JOINs: Combine data from multiple tables based on a related column. Common types include:

INNER JOIN: Returns rows where the join condition is met in both tables.

SQL
```sql
SELECT customers.name, orders.order_id
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id;
```

LEFT JOIN: Includes all rows from the left table, even if there's no match in the right table.

SQL
```sql
SELECT customers.name, orders.order_id
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id;
```

RIGHT JOIN: Includes all rows from the right table, even if there's no match in the left table.

FULL JOIN: Combines all rows from both tables, including unmatched rows.

UNION: Combines the results of two or more SELECT statements, removing duplicates by default. Use UNION ALL to include duplicates.

SQL
```sql
SELECT name FROM customers
UNION
SELECT email FROM customers;
```

## Subqueries

Nested SELECT statements within a larger SELECT statement. Used to filter or aggregate data based on results from another query.

SQL
```sql
SELECT customer_id, COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 5;  -- Filter customers with more than 5 orders
```

### Additional Notes

Secure your MySQL installation by following best practices for password management and user permissions.
Consider using a database schema design tool or a visual representation to plan your database structure effectively.
Explore advanced topics like stored procedures, functions, and triggers for complex database operations.

