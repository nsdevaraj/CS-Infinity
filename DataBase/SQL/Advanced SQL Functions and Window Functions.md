



## **Section 4: Advanced SQL Functions and Window Functions**

### 1. **String Functions**

   - **Concept**: SQL provides functions to manipulate text data, such as `CONCAT`, `SUBSTRING`, `UPPER`, `LOWER`, `REPLACE`, and `LENGTH`.
   - **Usage**: Often used to clean, format, or combine string data within queries.

   #### **Interview Question 1**: Write a query to retrieve the first three characters of each employee’s name in uppercase.

   ```sql
   SELECT UPPER(SUBSTRING(name, 1, 3)) AS short_name
   FROM Employees;
   ```

   **Explanation**: `SUBSTRING(name, 1, 3)` extracts the first three characters, and `UPPER()` converts them to uppercase.

   #### **Interview Question 2**: Combine each employee’s first and last names into a single column called `full_name`.

   ```sql
   SELECT CONCAT(first_name, ' ', last_name) AS full_name
   FROM Employees;
   ```

   **Explanation**: `CONCAT` joins `first_name` and `last_name` with a space to form a full name.

---

### 2. **Date and Time Functions**

   - **Concept**: SQL includes functions for working with dates and times, like `NOW`, `DATEADD`, `DATEDIFF`, `YEAR`, `MONTH`, and `DAY`.
   - **Usage**: These functions help perform operations like calculating age, finding elapsed time, or extracting parts of a date.

   #### **Interview Question 3**: Write a query to calculate each employee’s years of service, assuming the `hire_date` column.

   ```sql
   SELECT name,
          YEAR(CURDATE()) - YEAR(hire_date) AS years_of_service
   FROM Employees;
   ```

   **Explanation**: `YEAR(CURDATE()) - YEAR(hire_date)` calculates the difference in years from the current date to the hire date.

   #### **Interview Question 4**: Retrieve employees who have been with the company for over 10 years.

   ```sql
   SELECT name, hire_date
   FROM Employees
   WHERE DATEDIFF(CURDATE(), hire_date) > 3650;
   ```

   **Explanation**: `DATEDIFF(CURDATE(), hire_date)` calculates the number of days between the current date and the hire date; dividing by 3650 (~10 years) filters for employees with over 10 years of service.

---

### 3. **Mathematical Functions**

   - **Concept**: SQL offers mathematical functions for calculations, including `ROUND`, `FLOOR`, `CEIL`, `ABS`, `POWER`, and `MOD`.
   - **Usage**: These functions are used in financial or statistical calculations, for rounding values, or other numeric operations.

   #### **Interview Question 5**: Write a query to find the salary rounded to the nearest thousand for each employee.

   ```sql
   SELECT name, ROUND(salary, -3) AS rounded_salary
   FROM Employees;
   ```

   **Explanation**: `ROUND(salary, -3)` rounds the salary to the nearest thousand.

---

### 4. **Window Functions**

   - **Concept**: Window functions operate on a set of rows related to the current row, without grouping rows into a single result. Common window functions include `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`, `LEAD`, and `LAG`.
   - **Usage**: Useful for calculating rankings, cumulative sums, running totals, or moving averages.

   #### **Interview Question 6**: Write a query to assign a row number to each employee within each department, ordered by salary.

   ```sql
   SELECT name, department, salary,
          ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC) AS row_num
   FROM Employees;
   ```

   **Explanation**: `ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC)` assigns a unique row number within each department based on salary.

   #### **Interview Question 7**: Retrieve the top two highest-paid employees from each department.

   ```sql
   SELECT name, department, salary
   FROM (
       SELECT name, department, salary,
              RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS salary_rank
       FROM Employees
   ) AS ranked_salaries
   WHERE salary_rank <= 2;
   ```

   **Explanation**: `RANK() OVER(PARTITION BY department ORDER BY salary DESC)` ranks employees by salary within each department, and the outer query filters for the top two.

---

### 5. **Aggregations with Window Functions (SUM, AVG)**

   - **Concept**: Aggregation functions combined with window functions (like `SUM`, `AVG`, `MIN`, and `MAX`) calculate cumulative metrics without collapsing rows.
   - **Use Case**: Running totals, cumulative averages, and sliding window analytics.

   #### **Interview Question 8**: Write a query to calculate the running total of salaries for each employee, ordered by hire date.

   ```sql
   SELECT name, hire_date, salary,
          SUM(salary) OVER(ORDER BY hire_date) AS running_total
   FROM Employees
   ORDER BY hire_date;
   ```

   **Explanation**: `SUM(salary) OVER(ORDER BY hire_date)` calculates the cumulative total of salaries, ordered by hire date, providing a running total as each row is processed.

   #### **Interview Question 9**: Retrieve each employee’s salary and the average salary of their department.

   ```sql
   SELECT name, department, salary,
          AVG(salary) OVER(PARTITION BY department) AS department_avg_salary
   FROM Employees;
   ```

   **Explanation**: `AVG(salary) OVER(PARTITION BY department)` computes the average salary for each department and lists it alongside each employee’s salary.

---
