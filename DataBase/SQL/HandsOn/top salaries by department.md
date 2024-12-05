


To find the top 3 highest salaries of employees in each department, you can use a **Common Table Expression (CTE)** with the `ROW_NUMBER()` window function in SQL. Here's how you can do it:

### Query:

```sql
WITH RankedSalaries AS (
    SELECT 
        department_id,
        employee_id,
        salary,
        ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank
    FROM 
        employee
)
SELECT 
    department_id,
    employee_id,
    salary
FROM 
    RankedSalaries
WHERE 
    rank <= 3
ORDER BY 
    department_id, rank;
```

### Explanation:

1. **CTE `RankedSalaries`**:
    
    - The `ROW_NUMBER()` function assigns a unique rank to each employee within a department (`PARTITION BY department_id`), ordered by their salary in descending order (`ORDER BY salary DESC`).
2. **Filtering with `rank <= 3`**:
    
    - This retrieves only the top 3 employees in terms of salary for each department.
3. **Output**:
    
    - The result displays the department ID, employee ID, and salary for the top 3 employees in each department.

### Example:

If your `employee` table has the following data:

|employee_id|department_id|salary|
|---|---|---|
|1|10|5000|
|2|10|6000|
|3|10|5500|
|4|20|8000|
|5|20|7000|
|6|20|7500|
|7|30|4000|
|8|30|4500|

The query will return:

|department_id|employee_id|salary|
|---|---|---|
|10|2|6000|
|10|3|5500|
|10|1|5000|
|20|4|8000|
|20|6|7500|
|20|5|7000|
|30|8|4500|
|30|7|4000|

OTher soln:

Yes, you can achieve this using **`IN`** and subqueries, although using window functions (as shown previously) is more efficient. Here's how to find the top 3 salaries per department using **subqueries**:

### Query:

```sql
SELECT 
    e.department_id,
    e.employee_id,
    e.salary
FROM 
    employee e
WHERE 
    e.salary IN (
        SELECT DISTINCT TOP 3 sub.salary
        FROM employee sub
        WHERE sub.department_id = e.department_id
        ORDER BY sub.salary DESC
    )
ORDER BY 
    e.department_id, e.salary DESC;
```

### Explanation:

1. **Inner Subquery**:
    
    - For each department, the subquery selects the top 3 distinct salaries by ordering salaries in descending order for that department.
    - The `WHERE sub.department_id = e.department_id` ensures the subquery is restricted to the current department being processed in the outer query.
2. **`IN` Clause**:
    
    - The outer query filters employees whose salaries are among the top 3 for their department.
3. **Ordering**:
    
    - The result is ordered by `department_id` and `salary` for better readability.

### Notes:

- `TOP 3` syntax is used in SQL Server. If you're using MySQL or PostgreSQL, the approach might differ slightly.
- The `DISTINCT` in the subquery ensures only unique salaries are considered in case of ties.

### Caveat:

If multiple employees have the same salary (ties), this query might include more than 3 employees per department. To avoid this, window functions (`ROW_NUMBER()`, `RANK()`, or `DENSE_RANK()`) are preferred.

