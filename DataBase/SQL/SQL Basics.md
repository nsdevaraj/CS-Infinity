
### 1. **Data Retrieval (SELECT Queries)**

   - **Concept**: SQL `SELECT` statements are used to retrieve data from a database.
   - **Key Components**:
     - `SELECT` specifies which columns to retrieve.
     - `FROM` specifies the table.
     - `WHERE` filters rows.
     - `ORDER BY` sorts results.
     - `DISTINCT` removes duplicate records.

   #### **Interview Question 1**: Write a query to retrieve all unique job titles from the `Employees` table.

   ```sql
   SELECT DISTINCT job_title FROM Employees;
   ```

   **Explanation**: The `DISTINCT` keyword eliminates duplicate job titles.

   #### **Interview Question 2**: Retrieve the `name` and `salary` of employees, sorted by `salary` in descending order.

   ```sql
   SELECT name, salary FROM Employees
   ORDER BY salary DESC;
   ```

   **Explanation**: The `ORDER BY` clause with `DESC` orders records by salary from highest to lowest.

---

### 2. **Filtering Data (WHERE Clause)**

   - **Concept**: The `WHERE` clause filters records based on specific conditions.
   - **Operators**:
     - Comparison: `=`, `!=`, `>`, `<`, `>=`, `<=`
     - Logical: `AND`, `OR`, `NOT`
     - Pattern Matching: `LIKE`
     - Range: `BETWEEN`, `IN`

   #### **Interview Question 3**: Write a query to find employees whose salary is between 50,000 and 100,000.

   ```sql
   SELECT name, salary FROM Employees
   WHERE salary BETWEEN 50000 AND 100000;
   ```

   **Explanation**: `BETWEEN` checks if `salary` falls in the range 50,000 to 100,000.

   #### **Interview Question 4**: Retrieve all employees whose `name` starts with the letter ‘A’.

   ```sql
   SELECT name FROM Employees
   WHERE name LIKE 'A%';
   ```

   **Explanation**: `LIKE 'A%'` finds all names starting with "A".

---

### 3. **Sorting Results (ORDER BY Clause)**

   - **Concept**: SQL `ORDER BY` sorts the results based on one or more columns, in ascending or descending order.
   - **Default**: Ascending (`ASC`) if no sort order is specified.

   #### **Interview Question 5**: Retrieve employees’ `name` and `salary`, sorted by `name` alphabetically and then by `salary` in ascending order if names are the same.

   ```sql
   SELECT name, salary FROM Employees
   ORDER BY name ASC, salary ASC;
   ```

   **Explanation**: The query first sorts by `name` alphabetically, then by `salary` in ascending order within each `name`.

---

### 4. **Limiting Results (LIMIT Clause)**

   - **Concept**: `LIMIT` restricts the number of records returned.
   - **Usage**: Useful in cases like fetching the top results.

   #### **Interview Question 6**: Write a query to retrieve the top 5 highest-paid employees.

   ```sql
   SELECT name, salary FROM Employees
   ORDER BY salary DESC
   LIMIT 5;
   ```

   **Explanation**: `ORDER BY salary DESC` orders employees by salary in descending order, and `LIMIT 5` returns only the top 5 records.

---

### 5. **Aggregations (COUNT, SUM, AVG, MIN, MAX)**

   - **Concept**: Aggregation functions perform calculations on a set of values, returning a single value.
   - **Common Functions**:
     - `COUNT()`: Counts rows.
     - `SUM()`: Returns the sum of values.
     - `AVG()`: Calculates the average.
     - `MIN()`: Finds the smallest value.
     - `MAX()`: Finds the largest value.

   #### **Interview Question 7**: Write a query to find the total number of employees.

   ```sql
   SELECT COUNT(*) AS total_employees FROM Employees;
   ```

   **Explanation**: `COUNT(*)` counts all rows in the `Employees` table.

   #### **Interview Question 8**: Find the average salary of employees in the `Sales` department.

   ```sql
   SELECT AVG(salary) AS average_salary FROM Employees
   WHERE department = 'Sales';
   ```

   **Explanation**: `AVG(salary)` calculates the average salary for employees in the Sales department.

---


## LIKE


The `LIKE` operator in SQL is used to search for a specified pattern in a column. It's typically used in the `WHERE` clause to filter records based on a pattern matching.

### **LIKE Syntax:**
```sql
SELECT column_names
FROM table_name
WHERE column_name LIKE pattern;
```

### **Wildcards used with LIKE:**
1. **`%`** – Represents **zero or more characters**.
2. **`_`** – Represents **exactly one character**.

### **Examples:**

1. **`LIKE 'A%'`**:  
   Matches all values in the column that start with 'A'.  
   - Example: `'Alice', 'Anna', 'Alex'` (all names starting with 'A').

2. **`LIKE '%A'`**:  
   Matches all values in the column that end with 'A'.  
   - Example: `'Sara', 'Tina', 'Maya'` (all names ending with 'A').

3. **`LIKE '%A%'`**:  
   Matches all values in the column that contain 'A' anywhere in the string.  
   - Example: `'Maya', 'Tina', 'Sara'` (all names containing 'A').

4. **`LIKE 'A_ _%'`**:  
   Matches values that start with 'A' followed by **exactly two characters**, and then any number of additional characters.  
   - Example: `'Anna', 'Amy', 'Alex'` (names starting with 'A' and having two characters after 'A').

---

### **Your Example:**
```sql
SELECT *
FROM Employee
WHERE employee_name LIKE 'A%';
```
This will return all employees whose names **start with the letter 'A'**.

### **Summary:**
- **`%`** is used for multiple characters (including zero characters).
- **`_`** is used for exactly one character.
- **`LIKE`** allows you to match patterns based on partial strings in a column.



foreign keys:

https://www.w3schools.com/sql/sql_foreignkey.asp

https://www.geeksforgeeks.org/how-to-create-a-table-with-a-foreign-key-in-sql/

