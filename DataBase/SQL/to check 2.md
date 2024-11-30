

If you’re preparing for MySQL interview questions that might come up in an interview for a company like "Tacnique," here are some key topics and example questions that can help guide your preparation:

### Core MySQL Questions:
1. **Basic SQL Syntax**
   - What is the difference between `DELETE`, `TRUNCATE`, and `DROP`?
   - How do you write a query to find duplicate rows in a table?

2. **Joins and Subqueries**
   - Explain the difference between `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and `FULL JOIN`.
   - How would you use a subquery in a `SELECT` statement?
   - Write a query to fetch all users who haven't placed any orders.

3. **Indexes and Optimization**
   - What are indexes in MySQL, and how do they improve query performance?
   - What is the difference between a clustered index and a non-clustered index?
   - How would you optimize a slow query?

4. **Data Types and Constraints**
   - What are the different data types in MySQL, and when should each be used?
   - Explain the concept of `FOREIGN KEY` and how it enforces referential integrity.
   - What are `CHECK` constraints, and how are they used in MySQL?

5. **Stored Procedures and Functions**
   - What is the difference between a stored procedure and a function?
   - How do you create a stored procedure to calculate the total sales for a given date range?

6. **Transactions and ACID Properties**
   - What are the ACID properties of a transaction?
   - How do you implement a transaction in MySQL, and why is it useful?
   - What does the `ROLLBACK` command do, and when would you use it?

7. **Views**
   - What is a view in MySQL, and what are its advantages?
   - Can you modify data through a view? Explain with examples.

8. **Triggers**
   - What is a trigger, and how is it used in MySQL?
   - Write a trigger that logs any `UPDATE` operation on a specific table.

9. **Replication and Backup**
   - How does MySQL replication work, and what are the different types?
   - What is the process to create a backup of a database in MySQL?

10. **Performance Tuning**
    - What are the common strategies for MySQL performance tuning?
    - How do you use `EXPLAIN` to understand and optimize query performance?

### Practical Coding Exercises:
1. **Write SQL to return the 2nd highest salary from an `employees` table.**
2. **Create a query to find the top 3 products by sales amount in a `sales` table.**
3. **Generate a report showing the monthly revenue split by regions from a given `orders` table.**
4. **Design a schema to represent a library system with `books`, `authors`, and `borrowed_books` tables.**

Would you like a deeper dive into any of these questions or additional examples?



Here are some SQL questions that might be asked in a Tacnique interview, focusing on practical and conceptual knowledge:

### Example SQL Query Questions:
1. **Finding Duplicates**
   - Write a query to find duplicate records in a table based on a specific column.
   - How would you delete duplicate rows but keep one instance?

2. **Aggregation and Grouping**
   - Write a query to calculate the total sales per region from a `sales` table.
   - How do you find the maximum salary in each department?

3. **Complex Joins**
   - How would you write a query to retrieve data from multiple tables using different types of joins?
   - Given two tables, `employees` and `departments`, write a query to list employees without an assigned department.

4. **Nested Queries**
   - What is a correlated subquery, and when would you use one?
   - Write a query to find the employees who earn more than the average salary in their department.

5. **Ranking and Window Functions**
   - Write a query using `ROW_NUMBER()` to assign a unique number to each record within a department ordered by salary.
   - What is the difference between `RANK()` and `DENSE_RANK()`?

6. **Date and Time Functions**
   - How do you extract the year from a `date` column?
   - Write a query to find all orders placed in the last 30 days.

7. **Conditional Logic**
   - Use `CASE` in a query to categorize employees based on their salaries.
   - Write a query that updates a table's status column based on specific conditions.

8. **Data Modification**
   - Write a query to update the email domain for all users in a `users` table.
   - How do you safely delete data from a table that matches specific conditions?

9. **Schema Design Questions**
   - Design a schema for an e-commerce application with tables for `users`, `products`, `orders`, and `order_details`.
   - What normalization level would you choose for a table to avoid redundancy but maintain performance?

10. **Optimization and Indexing**
    - Explain when to use an index and its impact on `SELECT`, `INSERT`, `UPDATE`, and `DELETE` operations.
    - How would you identify and optimize a slow-running query using `EXPLAIN`?

11. **Common Table Expressions (CTEs)**
    - Write a recursive CTE to display a hierarchical employee structure (manager-subordinate relationship).
    - When would you choose a CTE over a subquery?

Would you like detailed answers or solutions to any specific type of question?



Here are the answers to the SQL questions provided earlier:

### Answers to Example SQL Questions:

1. **Finding Duplicates**
   - **Find duplicate records:**
     ```sql
     SELECT column_name, COUNT(*)
     FROM table_name
     GROUP BY column_name
     HAVING COUNT(*) > 1;
     ```
   - **Delete duplicates but keep one:**
     ```sql
     DELETE FROM table_name
     WHERE id NOT IN (
       SELECT MIN(id)
       FROM table_name
       GROUP BY column_name
     );
     ```

2. **Aggregation and Grouping**
   - **Total sales per region:**
     ```sql
     SELECT region, SUM(sales_amount) AS total_sales
     FROM sales
     GROUP BY region;
     ```
   - **Max salary per department:**
     ```sql
     SELECT department_id, MAX(salary) AS max_salary
     FROM employees
     GROUP BY department_id;
     ```

3. **Complex Joins**
   - **Join multiple tables:**
     ```sql
     SELECT e.employee_name, d.department_name
     FROM employees e
     INNER JOIN departments d ON e.department_id = d.id;
     ```
   - **Employees without an assigned department:**
     ```sql
     SELECT e.employee_name
     FROM employees e
     LEFT JOIN departments d ON e.department_id = d.id
     WHERE d.id IS NULL;
     ```

4. **Nested Queries**
   - **Correlated subquery:**
     ```sql
     SELECT employee_name
     FROM employees e
     WHERE salary > (
       SELECT AVG(salary)
       FROM employees e2
       WHERE e.department_id = e2.department_id
     );
     ```

5. **Ranking and Window Functions**
   - **`ROW_NUMBER()` query:**
     ```sql
     SELECT employee_name, department_id, salary,
            ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank
     FROM employees;
     ```
   - **Difference between `RANK()` and `DENSE_RANK()`:**
     - `RANK()` leaves gaps in the ranking sequence if there are ties.
     - `DENSE_RANK()` does not leave gaps and continues the sequence without skipping.

6. **Date and Time Functions**
   - **Extract year from a date:**
     ```sql
     SELECT EXTRACT(YEAR FROM order_date) AS order_year
     FROM orders;
     ```
   - **Orders placed in the last 30 days:**
     ```sql
     SELECT *
     FROM orders
     WHERE order_date >= NOW() - INTERVAL 30 DAY;
     ```

7. **Conditional Logic**
   - **Categorize employees by salary:**
     ```sql
     SELECT employee_name, salary,
            CASE
              WHEN salary > 100000 THEN 'High'
              WHEN salary BETWEEN 50000 AND 100000 THEN 'Medium'
              ELSE 'Low'
            END AS salary_category
     FROM employees;
     ```
   - **Update status column:**
     ```sql
     UPDATE orders
     SET status = CASE
                   WHEN delivery_date IS NOT NULL THEN 'Delivered'
                   ELSE 'Pending'
                 END;
     ```

8. **Data Modification**
   - **Update email domain:**
     ```sql
     UPDATE users
     SET email = REPLACE(email, '@old_domain.com', '@new_domain.com');
     ```
   - **Safely delete data:**
     ```sql
     DELETE FROM users
     WHERE last_login < NOW() - INTERVAL 1 YEAR;
     ```

9. **Schema Design Questions**
   - **Design schema for an e-commerce application:**
     - `users`: `id`, `name`, `email`, `password`
     - `products`: `id`, `name`, `description`, `price`
     - `orders`: `id`, `user_id`, `order_date`, `status`
     - `order_details`: `id`, `order_id`, `product_id`, `quantity`, `price`
   - **Normalization choice:** Start with 3rd Normal Form (3NF) to reduce redundancy, but denormalize where performance is critical (e.g., report tables).

10. **Optimization and Indexing**
    - **When to use an index:** Use indexes for columns that are frequently used in `WHERE`, `JOIN`, `ORDER BY`, or `GROUP BY` clauses. Be cautious with `INSERT`/`UPDATE` performance as indexes can slow down these operations.
    - **Use `EXPLAIN` to optimize:**
      ```sql
      EXPLAIN SELECT * FROM orders WHERE order_date >= '2024-01-01';
      ```

11. **Common Table Expressions (CTEs)**
    - **Recursive CTE for hierarchical structure:**
      ```sql
      WITH RECURSIVE employee_hierarchy AS (
        SELECT id, name, manager_id
        FROM employees
        WHERE manager_id IS NULL
        UNION ALL
        SELECT e.id, e.name, e.manager_id
        FROM employees e
        INNER JOIN employee_hierarchy eh ON e.manager_id = eh.id
      )
      SELECT * FROM employee_hierarchy;
      ```
    - **CTE vs. subquery:** CTEs are preferred when you need to reuse the result or make the query more readable.

Would you like further explanations or practice on any of these topics?


