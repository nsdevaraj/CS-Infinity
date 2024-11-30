

## Section 2: SQL Basics and Querying

### 2.1 SQL Overview
SQL (Structured Query Language) is a standard language for managing and querying data in relational databases. It allows users to create, retrieve, update, and delete data (often abbreviated as CRUD operations).

#### SQL Commands Categories:
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

- **Q2. Explain the difference between DDL, DML, DCL, and TCL in SQL.**
  - *Answer*: DDL defines structures, DML manipulates data, DCL manages permissions, and TCL controls transactions.

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

### 2.4 Joins in SQL
Joins combine rows from two or more tables based on a related column between them. Common types of joins include:

#### Types of Joins:
- **INNER JOIN**: Returns rows with matching values in both tables.
- **LEFT JOIN (LEFT OUTER JOIN)**: Returns all rows from the left table and matching rows from the right table.
- **RIGHT JOIN (RIGHT OUTER JOIN)**: Returns all rows from the right table and matching rows from the left table.
- **FULL JOIN (FULL OUTER/CROSS JOIN)**: Returns all rows when there’s a match in either table.


#### Example:
```sql
SELECT Employees.emp_name, Departments.dept_name
FROM Employees
INNER JOIN Departments ON Employees.dept_id = Departments.dept_id;
```

#### Related Interview Questions:
- **Q7. Explain the difference between INNER JOIN and LEFT JOIN.**
  - *Answer*: INNER JOIN returns only matching rows, while LEFT JOIN returns all rows from the left table with matching rows from the right.

- **Q8. Write a query to retrieve employee names along with their department names, even if some employees don’t belong to a department.**
  - *Answer*:
    ```sql
    SELECT Employees.emp_name, Departments.dept_name
    FROM Employees
    LEFT JOIN Departments ON Employees.dept_id = Departments.dept_id;
    ```




### Different Types of Joins in SQL

SQL joins are used to combine records from two or more tables based on a related column between them. Here’s a brief explanation of each type of join, followed by examples.

---

### 1. **INNER JOIN**
The `INNER JOIN` returns records that have matching values in both tables. Non-matching rows are excluded.

**Example:**

```sql
SELECT Students.StudentID, Students.Name, Enrollments.CourseID
FROM Students
INNER JOIN Enrollments ON Students.StudentID = Enrollments.StudentID;
```

**Explanation**: Retrieves the `StudentID`, `Name`, and `CourseID` for students who have enrolled in a course.

---

### 2. **LEFT JOIN (or LEFT OUTER JOIN)**
The `LEFT JOIN` returns all records from the left table and the matching records from the right table. If there’s no match, `NULL` is returned for the right table’s columns.

**Example:**

```sql
SELECT Students.StudentID, Students.Name, Enrollments.CourseID
FROM Students
LEFT JOIN Enrollments ON Students.StudentID = Enrollments.StudentID;
```

**Explanation**: Retrieves all students, even if they haven’t enrolled in any course (those will have `NULL` for `CourseID`).

---

### 3. **RIGHT JOIN (or RIGHT OUTER JOIN)**
The `RIGHT JOIN` returns all records from the right table and the matching records from the left table. If there’s no match, `NULL` is returned for the left table’s columns.

**Example:**

```sql
SELECT Students.StudentID, Students.Name, Enrollments.CourseID
FROM Students
RIGHT JOIN Enrollments ON Students.StudentID = Enrollments.StudentID;
```

**Explanation**: Retrieves all enrollments, even if some enrollments do not match a student in the `Students` table (those will have `NULL` for student details).

---

### 4. **FULL JOIN (or FULL OUTER JOIN)**
The `FULL JOIN` returns all records when there is a match in either left (Students) or right (Enrollments) table. Non-matching rows from both sides will have `NULL` in columns of the non-matching table.

**Example:**

```sql
SELECT Students.StudentID, Students.Name, Enrollments.CourseID
FROM Students
FULL JOIN Enrollments ON Students.StudentID = Enrollments.StudentID;
```

**Explanation**: Retrieves all students and all enrollments, showing `NULL` for students who haven't enrolled in any course and for courses that have no enrolled students.

---

### 5. **CROSS JOIN**
The `CROSS JOIN` returns the Cartesian product of both tables, i.e., it returns all possible combinations of rows between the two tables.

**Example:**

```sql
SELECT Students.Name, Courses.CourseName
FROM Students
CROSS JOIN Courses;
```

**Explanation**: Combines every student with every course, which may result in a large number of records.

---

### 6. **SELF JOIN**
A `SELF JOIN` is a join where a table is joined with itself. This is useful for hierarchical data.

**Example:**

```sql
SELECT e.EmployeeID, e.Name, m.Name AS ManagerName
FROM Employees e
LEFT JOIN Employees m ON e.ManagerID = m.EmployeeID;
```

**Explanation**: Retrieves a list of employees with their manager's name by joining the `Employees` table with itself.

---

### Interview Perspective Questions and Answers

---

**Q1: What is the difference between `INNER JOIN` and `OUTER JOIN`?**

**A1**: 
- **INNER JOIN** returns only the rows with matching values in both tables.
- **OUTER JOIN** returns all rows from one table and the matching rows from the other. If there's no match, `NULL` is returned for the non-matching table's columns. There are three types of outer joins: **LEFT OUTER JOIN**, **RIGHT OUTER JOIN**, and **FULL OUTER JOIN**.

---

**Q2: What happens when we perform a `CROSS JOIN`?**

**A2**: A `CROSS JOIN` produces the Cartesian product of two tables. It returns every combination of rows between the two tables. This can result in a large number of rows, so it should be used cautiously.

---

**Q3: Can you have multiple `JOIN` clauses in a single query?**

**A3**: Yes, you can perform multiple `JOIN` operations in a single query. Each join operation can join additional tables. It’s important to manage the order of joins and use appropriate conditions to avoid creating Cartesian products unintentionally.

---

**Q4: When would you use a `SELF JOIN`?**

**A4**: A `SELF JOIN` is used when you need to join a table with itself. Common use cases include hierarchical data (e.g., employees and managers), or finding relationships between records in the same table.

---

**Q5: What is a "NULL" in SQL joins, and how does it affect queries?**

**A5**: `NULL` represents the absence of a value. In joins, it appears when there is no matching record in one of the tables. In outer joins (`LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN`), `NULL` is used to fill in missing values for non-matching rows.

---

**Q6: What is the difference between `LEFT JOIN` and `RIGHT JOIN`?**

**A6**: 
- **LEFT JOIN** returns all rows from the left table, and matching rows from the right table. Non-matching rows from the right table are filled with `NULL`.
- **RIGHT JOIN** returns all rows from the right table, and matching rows from the left table. Non-matching rows from the left table are filled with `NULL`.

---

![[Pasted image 20241110180756.png]]



![[Pasted image 20241110181013.png]]



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

