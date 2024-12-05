

## Section 2: SQL Basics and Querying

### 2.1 SQL Overview
SQL (Structured Query Language) is a standard language for managing and querying data in relational databases. It allows users to create, retrieve, update, and delete data (often abbreviated as CRUD operations).

#### SQL Commands Categories:
DDL defines structures, DML manipulates data, DCL manages permissions, and TCL controls transactions.
1. **DDL (Data Definition Language)**: Commands for defining database structure.
   - Examples: `CREATE`, `ALTER`, `DROP`, `TRUNCATE`
   
2. **DML (Data Manipulation Language)**: Commands for data manipulation within tables.
   - Examples: `INSERT`, `UPDATE`, `DELETE`, `SELECT`
   
3. **DCL (Data Control Language)**: Commands for managing permissions.
   - Examples: `GRANT`, `REVOKE`
   
4. **TCL (Transaction Control Language)**: Commands for transaction management.
   - Examples: `COMMIT`, `ROLLBACK`, `SAVEPOINT`

#### Related Interview Questions:
- **Q1. What is SQL, and why is it important in relational databases?**
  - *Answer*: SQL is the standard language for managing data in relational databases, enabling efficient data retrieval, manipulation, and structural control.


---

### 2.2 Basic SQL Queries
SQL queries are used to retrieve data from relational databases, with the `SELECT` statement being the most commonly used.

#### Key Concepts:
- **SELECT**: Retrieves specified columns from one or more tables.
- **WHERE**: Filters rows based on conditions.
- **ORDER BY**: Sorts the result set based on specified columns (ascending or descending).
- **LIMIT**: Restricts the number of returned rows.

#### Example:
```sql
SELECT first_name, last_name
FROM Employees
WHERE department = 'Sales'
ORDER BY last_name ASC
LIMIT 10;
```

#### Related Interview Questions:
- **Q3. Write an SQL query to retrieve the names of employees in the Sales department, ordered by last name.**
  - *Answer*:
    ```sql
    SELECT first_name, last_name
    FROM Employees
    WHERE department = 'Sales'
    ORDER BY last_name;
    ```

- **Q4. How do you retrieve only the top 5 records from a query result?**
  - *Answer*: Use `LIMIT 5` at the end of the query.

---

### 2.3 Filtering and Aggregation
SQL supports filtering with the `WHERE` clause and various aggregation functions to summarize data.

#### Key Concepts:
- **WHERE**: Filters data based on a condition.
- **Aggregate Functions**:
  - **COUNT()**: Counts the number of records.
  - **SUM()**: Calculates the total of a numeric column.
  - **AVG()**: Calculates the average value.
  - **MAX()/MIN()**: Finds the maximum or minimum value.

#### Example:
```sql
SELECT department, COUNT(*) AS employee_count, AVG(salary) AS avg_salary
FROM Employees
WHERE salary > 50000
GROUP BY department;
```

#### Related Interview Questions:
- **Q5. Write a query to count the number of employees in each department.**
  - *Answer*:
    ```sql
    SELECT department, COUNT(*) AS employee_count
    FROM Employees
    GROUP BY department;
    ```

- **Q6. What’s the difference between WHERE and HAVING in SQL?**
  - *Answer*: `WHERE` filters rows before aggregation, and `HAVING` filters rows after aggregation.


---

### 2.5 Subqueries
A subquery is a query nested inside another query. It can be used within `SELECT`, `WHERE`, or `FROM` clauses.

#### Key Concepts:
- **Single-row Subquery**: Returns a single row; often used with operators like `=` or `>`.
- **Multi-row Subquery**: Returns multiple rows; used with operators like `IN` or `ANY`.
- **Correlated Subquery**: A subquery that references a column from the outer query.

#### Example:
```sql
SELECT emp_name
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees);
```

#### Related Interview Questions:
- **Q9. What is a subquery, and how is it used?**
  - *Answer*: A subquery is a query within another query, used to provide data for the main query’s filtering or selection.

- **Q10. Write a query to find employees whose salary is above the average salary.**
  - *Answer*:
    ```sql
    SELECT emp_name
    FROM Employees
    WHERE salary > (SELECT AVG(salary) FROM Employees);
    ```

---

### 2.6 Grouping and Aggregation with GROUP BY
`GROUP BY` groups rows sharing a specific column’s value, often used with aggregate functions for summarizing data.

#### Key Concepts:
- **GROUP BY**: Groups rows for each unique value in specified columns.
- **HAVING**: Filters groups based on an aggregate condition, applied after aggregation.

#### Example:
```sql
SELECT department, AVG(salary) AS avg_salary
FROM Employees
GROUP BY department
HAVING AVG(salary) > 60000;
```

#### Related Interview Questions:
- **Q11. What is the purpose of GROUP BY in SQL?**
  - *Answer*: `GROUP BY` groups records by one or more columns, often used with aggregate functions to summarize data.

- **Q12. Write a query to find departments with an average salary above $60,000.**
  - *Answer*:
    ```sql
    SELECT department, AVG(salary) AS avg_salary
    FROM Employees
    GROUP BY department
    HAVING AVG(salary) > 60000;
    ```

---

### 2.7 Using CASE Statements
The `CASE` statement allows conditional logic in SQL, providing control over the output of query results.

#### Key Concepts:
- **CASE**: Acts as a conditional expression, similar to if-else logic in programming.
- Syntax:
  ```sql
  SELECT emp_name,
         CASE
             WHEN salary > 70000 THEN 'High'
             WHEN salary BETWEEN 50000 AND 70000 THEN 'Medium'
             ELSE 'Low'
         END AS salary_category
  FROM Employees;
  ```

#### Related Interview Questions:
- **Q13. What is a CASE statement in SQL, and how is it used?**
  - *Answer*: A CASE statement provides conditional logic in SQL, allowing different outputs based on specified conditions.

- **Q14. Write a query to categorize employees based on salary as 'High', 'Medium', or 'Low'.**
  - *Answer*:
    ```sql
    SELECT emp_name,
           CASE
               WHEN salary > 70000 THEN 'High'
               WHEN salary BETWEEN 50000 AND 70000 THEN 'Medium'
               ELSE 'Low'
           END AS salary_category
    FROM Employees;
    ```

---

