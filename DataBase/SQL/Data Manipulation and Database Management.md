

## **Section 5: Data Manipulation and Database Management**

### 1. **Inserting Data (INSERT)**

   - **Concept**: The `INSERT` statement adds new rows to a table.
   - **Usage**: Used to populate tables with initial or new data.

   #### **Interview Question 1**: Write a query to add a new employee to the `Employees` table.

   ```sql
   INSERT INTO Employees (name, department_id, salary, hire_date)
   VALUES ('John Doe', 2, 75000, '2022-01-15');
   ```

   **Explanation**: This query inserts a new row with specified values into the `Employees` table. The columns listed in parentheses correspond to the values provided in `VALUES`.

---

### 2. **Updating Data (UPDATE)**

   - **Concept**: The `UPDATE` statement modifies existing data in a table.
   - **Usage**: Used to change values in specific columns based on conditions.

   #### **Interview Question 2**: Write a query to update the salary of an employee named "Jane Smith" to 80,000.

   ```sql
   UPDATE Employees
   SET salary = 80000
   WHERE name = 'Jane Smith';
   ```

   **Explanation**: The `UPDATE` statement changes `salary` for the employee with the name "Jane Smith" to 80,000. The `WHERE` clause specifies the condition to match the row.

---

### 3. **Deleting Data (DELETE)**

   - **Concept**: The `DELETE` statement removes rows from a table based on a condition.
   - **Usage**: Used to delete specific rows that match a condition.

   #### **Interview Question 3**: Write a query to delete employees from the `Employees` table who have been with the company for over 20 years.

   ```sql
   DELETE FROM Employees
   WHERE DATEDIFF(CURDATE(), hire_date) > 7300;
   ```

   **Explanation**: `DATEDIFF(CURDATE(), hire_date) > 7300` calculates employees who have been with the company for more than 20 years (approximately 7300 days) and deletes those rows.

---

### 4. **Creating Tables (CREATE TABLE)**

   - **Concept**: The `CREATE TABLE` statement defines a new table with specified columns and data types.
   - **Usage**: Used for database schema setup or to add new tables to the database.

   #### **Interview Question 4**: Write a query to create a `Departments` table with columns for `department_id`, `department_name`, and `manager_id`.

   ```sql
   CREATE TABLE Departments (
       department_id INT PRIMARY KEY,
       department_name VARCHAR(50) NOT NULL,
       manager_id INT
   );
   ```

   **Explanation**: This query creates a `Departments` table with `department_id` as the primary key, `department_name` as a required column, and `manager_id` as an optional column.

---

### 5. **Altering Tables (ALTER TABLE)**

   - **Concept**: The `ALTER TABLE` statement modifies an existing table’s structure, such as adding, removing, or changing columns.
   - **Usage**: Commonly used to update database schema as requirements change.

   #### **Interview Question 5**: Write a query to add a new column called `email` to the `Employees` table.

   ```sql
   ALTER TABLE Employees
   ADD email VARCHAR(100);
   ```

   **Explanation**: This query adds a new column `email` with a `VARCHAR` data type to the `Employees` table.

   #### **Interview Question 6**: Write a query to modify the `salary` column in the `Employees` table to hold larger values.

   ```sql
   ALTER TABLE Employees
   MODIFY salary DECIMAL(12, 2);
   ```

   **Explanation**: This query changes the `salary` column’s data type to `DECIMAL(12, 2)`, allowing larger salary values with two decimal points.

---

### 6. **Dropping Tables and Columns (DROP TABLE, DROP COLUMN)**

   - **Concept**: The `DROP` statement deletes entire tables or specific columns from a table.
   - **Usage**: Used to permanently remove tables or columns no longer needed in the database.

   #### **Interview Question 7**: Write a query to drop the `Departments` table.

   ```sql
   DROP TABLE Departments;
   ```

   **Explanation**: `DROP TABLE Departments` permanently removes the `Departments` table from the database.

   #### **Interview Question 8**: Write a query to remove the `email` column from the `Employees` table.

   ```sql
   ALTER TABLE Employees
   DROP COLUMN email;
   ```

   **Explanation**: `DROP COLUMN` deletes the `email` column from the `Employees` table structure.

---

### 7. **Constraints and Indexes**

   - **Concept**:
     - **Constraints** enforce rules on data (e.g., `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, `CHECK`).
     - **Indexes** improve query performance by providing quick access to data in columns.
   - **Usage**: Constraints ensure data integrity, while indexes optimize query speed.

   #### **Interview Question 9**: Write a query to add a unique constraint on the `email` column in the `Employees` table.

   ```sql
   ALTER TABLE Employees
   ADD CONSTRAINT unique_email UNIQUE (email);
   ```

   **Explanation**: `UNIQUE` ensures that each value in the `email` column is distinct, preventing duplicate emails.

   #### **Interview Question 10**: Write a query to create an index on the `salary` column in the `Employees` table.

   ```sql
   CREATE INDEX idx_salary ON Employees(salary);
   ```

   **Explanation**: `CREATE INDEX` creates an index on the `salary` column, allowing faster search and filtering on salary data.

---

### 8. **Transactions and ACID Properties**

   - **Concept**: Transactions allow multiple SQL operations to be treated as a single unit of work, with `BEGIN`, `COMMIT`, and `ROLLBACK` commands.
   - **ACID Properties**: Ensure data integrity by making transactions **Atomic**, **Consistent**, **Isolated**, and **Durable**.
   - **Usage**: Commonly used in complex operations that require multiple steps to ensure consistency.

   #### **Interview Question 11**: Write a transaction to transfer 5000 from one employee’s salary to another’s.

   ```sql
   BEGIN;

   UPDATE Employees
   SET salary = salary - 5000
   WHERE employee_id = 1;

   UPDATE Employees
   SET salary = salary + 5000
   WHERE employee_id = 2;

   COMMIT;
   ```

   **Explanation**: This transaction begins with `BEGIN`, reduces `employee_id = 1` salary by 5000, increases `employee_id = 2` salary by 5000, and commits the changes. If an error occurs, a `ROLLBACK` could undo the changes.

