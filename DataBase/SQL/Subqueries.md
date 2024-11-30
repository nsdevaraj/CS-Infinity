
### 3. **Subqueries in SELECT, WHERE, and FROM Clauses**

   - **Concept**: Subqueries (or nested queries) are queries within another query. They can be used within `SELECT`, `WHERE`, and `FROM` clauses.
   - **Types**:
     - **Scalar Subquery**: Returns a single value.
     - **Table Subquery**: Returns a set of rows to be used as a temporary table.

   #### **Interview Question 4**: Retrieve employee names along with their department's average salary. Assume `Employees` table has `department_id` and `salary`.

   ```sql
   SELECT name,
          salary,
          (SELECT AVG(salary)
           FROM Employees
           WHERE department_id = e.department_id) AS department_avg_salary
   FROM Employees e;
   ```

   **Explanation**: The subquery calculates the average salary per department and is included as an additional column in the main `SELECT`.

   #### **Interview Question 5**: Write a query to find employees whose salary is higher than the average salary of all employees.

   ```sql
   SELECT name, salary
   FROM Employees
   WHERE salary > (SELECT AVG(salary) FROM Employees);
   ```

   **Explanation**: The subquery `(SELECT AVG(salary) FROM Employees)` calculates the overall average salary, and the main query filters employees with salaries above this average.

---

### 4. **Correlated Subqueries**

   - **Concept**: A correlated subquery references columns from the outer query and is re-evaluated for each row processed by the outer query.
   - **Use Case**: Comparing each row to a dynamically calculated value based on that row’s context.

   #### **Interview Question 6**: Retrieve employees whose salary is higher than the average salary of their department.

   ```sql
   SELECT name, salary, department_id
   FROM Employees e
   WHERE salary > (SELECT AVG(salary)
                   FROM Employees
                   WHERE department_id = e.department_id);
   ```

   **Explanation**: The subquery calculates the average salary per department for each employee’s department, allowing the outer query to filter based on that specific average.

---

### 5. **Subqueries in the FROM Clause (Derived Tables)**

   - **Concept**: Subqueries in the `FROM` clause, also called derived tables, allow intermediate results to be treated as a temporary table.
   - **Use Case**: Useful when multiple aggregations or transformations are needed before the main query processes them.

   #### **Interview Question 7**: Write a query to find the department with the highest average salary.

   ```sql
   SELECT department_id, avg_salary
   FROM (SELECT department_id, AVG(salary) AS avg_salary
         FROM Employees
         GROUP BY department_id) AS dept_avg
   ORDER BY avg_salary DESC
   LIMIT 1;
   ```

   **Explanation**: The inner query calculates the average salary per department, and the outer query selects the department with the highest average.

---

### 6. **Exists vs. IN with Subqueries**

   - **Concept**:
     - **`IN`** checks if a value matches any value in a list or subquery result.
     - **`EXISTS`** checks if a subquery returns any rows, returning `TRUE` if it does.
   - **Difference**: `EXISTS` stops evaluating once a match is found, often making it more efficient in correlated subqueries with large datasets.

   #### **Interview Question 8**: Write a query to retrieve employees who work in departments that have at least one employee with a salary greater than 100,000.

   ```sql
   SELECT name, department_id
   FROM Employees e
   WHERE EXISTS (SELECT 1
                 FROM Employees
                 WHERE department_id = e.department_id
                   AND salary > 100000);
   ```

   **Explanation**: The `EXISTS` subquery checks if there are any employees in each employee’s department earning over 100,000. If the subquery returns any rows, `EXISTS` is `TRUE`, and the employee is included in the result.

?? SELECT 1 ??

---

$ [[Cricket and Cricket Players Table]]
```sql
SELECT Player_Name, Sum(Runs) as Total_Runs
FROM Cricket
JOIN Cricket
-- Not unique table/alias: 'Cricket'
-- ON Cricket.Player_Name = Cricket_Players.Player_Name
ON Cricket.Player_Name = Cricket_Players.Player_Name
WHERE Year != 2021
GROUP BY Player_Name
HAVING Total_Runs > 700 
ORDER BY Total_Runs DESC
LIMIT 3

```

It looks like there are some issues with table aliasing and joins in your query. Specifically, the `Cricket` table is referenced twice without an alias, which causes ambiguity. Also, there's an incorrect join condition between the `Cricket` and `Cricket_Players` tables, assuming the intention is to join these two tables on `Player_Name`.

Let's correct it step by step:

1. **Alias the tables**: When you join the same table twice (or join two different tables), it's necessary to alias them to avoid ambiguity.
2. **Use the correct `JOIN` condition**: If you're trying to join `Cricket` with `Cricket_Players`, make sure the join condition matches the schema.
3. **Fix the aggregate function**: In the `HAVING` clause, you should use `SUM(Runs)` directly since you already alias it as `Total_Runs`.

Here’s the corrected query:

```sql
SELECT cp.Player_Name, SUM(c.Runs) AS Total_Runs
FROM Cricket c
JOIN Cricket_Players cp ON c.Player_Name = cp.Player_Name
WHERE c.Year != 2021
GROUP BY cp.Player_Name
HAVING SUM(c.Runs) > 700
ORDER BY Total_Runs DESC
LIMIT 3;
```

### Key Changes:
1. **Aliased `Cricket` as `c`** and `Cricket_Players` as `cp`.
2. **Join condition**: Corrected to `c.Player_Name = cp.Player_Name`.
3. **Sum aggregation**: Directly used `SUM(c.Runs)` in the `HAVING` clause instead of using the alias `Total_Runs` in the `HAVING` condition.
   
This should fix the issues and give you the top 3 players with total runs greater than 700 (excluding 2021).

**Sum aggregation**: Directly used `SUM(c.Runs)` in the `HAVING` clause instead of using the alias `Total_Runs` in the `HAVING` condition. why its needed ?

Great question! Let's dive into why **you can't use the alias `Total_Runs` directly in the `HAVING` clause** and why it's necessary to use `SUM(c.Runs)`.

### SQL Execution Order:

SQL queries are processed in a specific order (called the **logical query processing order**). When you write a query, the steps are roughly as follows:

1. **FROM** and **JOIN** clauses: First, SQL figures out what tables you're working with and how to combine them (if there's a join).
2. **WHERE** clause: Filters rows based on conditions.
3. **GROUP BY** clause: Groups the data (if applicable) based on certain columns.
4. **SELECT** clause: Calculates and selects the columns, including aggregate functions like `SUM()`, `COUNT()`, etc.
5. **HAVING** clause: Filters groups based on aggregate functions.
6. **ORDER BY** clause: Sorts the final result.
7. **LIMIT** clause: Limits the number of rows returned.

### Problem with Using Aliases in the `HAVING` Clause:

- **Aliases in the `SELECT` clause are created after the `HAVING` clause is processed**. This means the `HAVING` clause runs **before** the `SELECT` clause is fully processed, which includes creating any aliases you define in the `SELECT` clause.

- **The `HAVING` clause is used to filter groups** (after `GROUP BY`), and it can only reference things that are already available in the aggregation phase—i.e., raw column names or aggregate functions (like `SUM()`, `COUNT()`, etc.) at that point.

### Why Can't You Use `Total_Runs` Directly in `HAVING`?

In your original query, you have this alias in the `SELECT` clause:

```sql
SELECT cp.Player_Name, SUM(c.Runs) AS Total_Runs
```

The alias `Total_Runs` is defined **after** the aggregation phase. But the `HAVING` clause operates **before** the final result is formed, which means it cannot access the alias `Total_Runs`.

So, if you try to use it like this:

```sql
HAVING Total_Runs > 700
```

SQL won’t know what `Total_Runs` refers to at that stage because it hasn't been "calculated" yet.

### Correct Approach:

Instead of referring to the alias in the `HAVING` clause, you can directly use the aggregate function that defines it:

```sql
HAVING SUM(c.Runs) > 700
```

This works because **`SUM(c.Runs)`** is evaluated during the aggregation phase, which happens before the `HAVING` clause filters the results.

### Summary:

- **The `HAVING` clause filters the results after the `GROUP BY`** and **before the `SELECT` clause**, so you can only use columns or aggregate functions that are already part of the grouping and aggregation.
- Since the alias `Total_Runs` is created in the `SELECT` clause, it's **not available** to the `HAVING` clause, so you need to use the original aggregate function (`SUM(c.Runs)`) directly in `HAVING`.

Hope this clears it up! Let me know if you need more explanation or examples.

```sql


SELECT *
FROM Cricket c
JOIN Cricket_Players cp ON c.Player_Name = cp.Player_Name

-- Output:

-- +------+--------------+------+-------+-----------+--------------+
-- | Year | Player_Name  | Runs | Balls | Player_ID | Player_Name  |
-- +------+--------------+------+-------+-----------+--------------+
-- | 2023 | Virat Kohli  |  480 |   455 |         1 | Virat Kohli  |
-- | 2022 | Virat Kohli  |  356 |   346 |         1 | Virat Kohli  |
-- | 2021 | Shubman Gill |  620 |   615 |         2 | Shubman Gill |
-- | 2023 | Shubman Gill |  450 |   400 |         2 | Shubman Gill |
-- | 2023 | Rohit Sharma |  500 |   348 |         3 | Rohit Sharma |
-- | 2023 | Rohit Sharma |  450 |   440 |         3 | Rohit Sharma |
-- +------+--------------+------+-------+-----------+--------------+




```


```sql


SELECT Player_Name
FROM Cricket c
JOIN Cricket_Players cp ON c.Player_Name = cp.Player_Name
--=> error : Column 'Player_Name' in field list is ambiguous


```

```sql



SELECT cp.Player_Name, c.Player_Name
FROM Cricket c
JOIN Cricket_Players cp ON c.Player_Name = cp.Player_Name

-- Output:

-- +--------------+--------------+
-- | Player_Name  | Player_Name  |
-- +--------------+--------------+
-- | Virat Kohli  | Virat Kohli  |
-- | Virat Kohli  | Virat Kohli  |
-- | Shubman Gill | Shubman Gill |
-- | Shubman Gill | Shubman Gill |
-- | Rohit Sharma | Rohit Sharma |
-- | Rohit Sharma | Rohit Sharma |
-- +--------------+--------------+


```




