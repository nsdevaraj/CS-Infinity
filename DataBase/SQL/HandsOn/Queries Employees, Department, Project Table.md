
$ [[Employees, Department, Project Table]]


### nth Max / Min salary 

### **1. second highest salary from the Employee table.**

```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);
```


```sql

--  maximum salary 
SELECT MAX(salary)
FROM Employee


--  rows other than minimalist salary row
SELECT *
FROM Employee
WHERE salary != (
                  SELECT MIN(salary)
                  FROM Employee
                )

-- second highest salary
SELECT MAX(salary)
FROM Employee
WHERE salary < (
  SELECT MAX(salary)
  FROM Employee
)


-- second highest salary row
SELECT *
FROM Employee
WHERE salary = (
  SELECT MAX(salary)
  FROM Employee
  WHERE salary < (
    SELECT MAX(salary)
    FROM Employee
  )
)

```


to check {
	[[2nd highest]]
}


### **12. Write a query to find the employee who has the minimum salary.**
```sql
SELECT employee_name, salary
FROM Employee
WHERE salary = (SELECT MIN(salary) FROM Employee);
```


### **2. Retrieve all employees who have more than one department assignment 

```sql
SELECT employee_id, COUNT(department_id) AS DepartmentCount
FROM Employee
GROUP BY employee_id
HAVING COUNT(department_id) > 1;
```

### **3. List all employees who have no manager.**
```sql
SELECT employee_id, employee_name
FROM Employee
WHERE manager_id IS NULL;
```

### **4. Write a query to get all the records from `Employee` where the name starts with 'A'.**
```sql
SELECT * 
FROM Employee
WHERE employee_name LIKE 'A%';
```

### **5. Find the total salary paid to employees by department.**
```sql
SELECT department_id, SUM(salary) AS TotalSalary
FROM Employee
GROUP BY department_id;
```

### **6. Retrieve the names of employees who are older than 30 years and work in the 'IT' department.**
```sql

SELECT employee_name
FROM Employee
WHERE age > 30 
  AND department_id = (
    SELECT department_id
    FROM Department
    WHERE department_name = 'IT'
  )
```

### **7. Write a query to get the number of employees in each department.**

```sql

SELECT department_id, COUNT(*) AS NumberOfEmployees
FROM Employee
GROUP BY department_id

```

### **8. Find the employees who are earning more than the average salary.**

```sql
SELECT employee_name, salary
FROM Employee
WHERE salary > (
  SELECT AVG(salary)
  FROM Employee
  )
```

### **9. Get the employees who have the same salary.**

```sql

-- Select employee names and their salaries from the Employee table
SELECT employee_name, salary
FROM Employee
-- Filter the employees whose salary is found in the subquery result
WHERE salary 
IN (
  -- Subquery: Select salaries that are repeated (more than 1 employee has the same salary)
  SELECT salary
  FROM Employee
  -- Group the records by salary, so we can count occurrences of each salary
  GROUP BY salary
  -- Use HAVING to filter groups where the count of employees with the same salary is greater than 1
  HAVING COUNT(*) > 1
)

```


```sql

SELECT *
FROM Employee
GROUP BY salary
HAVING COUNT(*) > 1

-- having condition met with 1st item and returns 1st item.. 
-- or condition check , iterate all items.. but takes only first item , which not valid.. groupBy need aggregation of displaying fields (MySQL and others )
```

### **10. Write a query to find all the departments with more than 5 employees.**

```sql
 SELECT department_id, COUNT(*) as EmployeeCount
 FROM Employee
 GROUP By department_id
 HAVING COUNT(*)>5
```


```sql
 
 SELECT employeeTable.department_id, departmentTable.department_name, COUNT(*) as EmployeeCount
 FROM Employee employeeTable
 JOIN Department departmentTable
 ON employeeTable.department_id = departmentTable.department_id
 GROUP By employeeTable.department_id
 HAVING COUNT(*)>5
 
 
```

---

### **11. Retrieve the names of employees and their corresponding department names.**

```sql
SELECT e.employee_name, d.department_name
FROM Employee e
JOIN Department d ON e.department_id = d.department_id;
```

### **13. Find the number of employees who report directly to each manager.**

```sql
SELECT manager_id, COUNT(*) AS NumberOfReports
FROM Employee
WHERE manager_id IS NOT NULL
GROUP BY manager_id;
```

```sql

SELECT e.manager_id, e2.employee_name, COUNT(*) AS NumberOfReports
FROM Employee e
JOIN Employee e2
ON e.manager_id = e2.manager_id
GROUP By e.manager_id
 
```

### **14. Retrieve the departments that have employees older than 40 years.**

```sql

SELECT DISTINCT d.department_name, COUNT(*) as EmployeeAbove40
FROM Department d
JOIN Employee e 
ON d.department_id = e.department_id
WHERE e.age > 40

```

### **15. Write a query to find the average salary of employees in each department.**

```sql

SELECT department_id, AVG(salary) AS AverageSalary
FROM Employee
GROUP BY department_id;

```


```sql

SELECT d.department_name, AVG(e.salary) as AverageSalary
FROM Department d
JOIN Employee e 
on e.department_id = d.department_id
GROUP By d.department_id

```


### **17. Get the total number of employees in each department and their average salary.**
```sql
SELECT department_id, COUNT(*) AS TotalEmployees, AVG(salary) AS AverageSalary
FROM Employee
GROUP BY department_id;
```

### **18. Write a query to find employees who share the same  name.**

```sql
SELECT employee_name, COUNT(*) 
FROM Employee
GROUP BY employee_name
HAVING COUNT(*) > 1;
```

### **19. Retrieve all employees whose salary is greater than 10% higher than the average salary.**

```sql

SELECT employee_name, salary
FROM Employee
WHERE salary > (
  SELECT 1.1* AVG(salary)
  FROM Employee
  )

```

### **20. Find the employees who are working in 'Sales' or 'Marketing' department and earn more than $5000.**
```sql

SELECT employee_name, salary
FROM Employee
WHERE department_id 
	IN (
      SELECT department_id 
      FROM Department 
      WHERE department_name IN ('Sales', 'Marketing')
    )
	AND salary > 5000;

```


```sql

SELECT e.employee_name, e.salary
FROm Employee e
JOIN Department d
ON e.department_id = d.department_id
WHERE 
	(d.department_name IS 'Sales' OR department_name IS 'Marketing') 
    AND salary > 5000


```

---

### **21. Retrieve the employee with the highest salary in each department.**

```sql
-- highest salary consiting rows in each dept (consider 2 rows of high salary )

SELECT e.department_id, e.employee_name, e.salary
FROM Employee e
WHERE e.salary = (
    SELECT MAX(salary) 
    FROM Employee 
    WHERE department_id = e.department_id
);
```


```sql
-- each department only one highest row ( not consider 2 rows of high salary )

SELECT e.department_id, d.department_name, MAX(e.salary) as HighestSalary
FROM Employee e
JOIN Department d
ON e.department_id = d.department_id
GROUP By e.department_id

```


### **22. Find the employees whose salary is between 5000 and 7000.**
```sql
SELECT employee_name, salary
FROM Employee
WHERE salary BETWEEN 5000 AND 7000;
```

### **23. List the departments that do not have any employees.**


note: not sure about correctness
```sql

SELECT d.department_name
FROM Department d 
JOIN Employee e
ON d.department_id = e.department_id
WHERE e.employee_id is NULL

```


```sql

SELECT *
FROM Department d
WHERE  NOT EXISTS (
  SELECT *
  FROM Employee 
  WHERE d.department_id = department_id
)

```




### **24. Find the manager who manages the most employees.**

```sql
SELECT manager_id, COUNT(*) as EmployeeCount
FROM Employee e1
WHERE manager_id is NOT NULL
GROUP By manager_id
ORDER BY COUNT(*) DESC
LIMIT 1
```


```sql
SELECT  e1.employee_name, COUNT(*) AS employee_count
FROM Employee e1
JOIN Employee e2 ON e1.employee_id = e2.manager_id
GROUP BY e1.manager_id, e1.employee_name
HAVING COUNT(*) = (
    SELECT MAX(employee_count)
    FROM (
        SELECT COUNT(*) AS employee_count
        FROM Employee
        WHERE manager_id IS NOT NULL
        GROUP BY manager_id
    )
);

```

### **25. Retrieve the names of employees who have the same manager.**

note: not sure about correctness
```sql
SELECT e1.employee_name, e2.employee_name AS ManagerEmployeeName
FROM Employee e1
JOIN Employee e2 ON e1.manager_id = e2.employee_id
WHERE e1.manager_id IS NOT NULL;
```


```sql

SELECT e1.employee_name, e2.employee_name as manager_name
FROM Employee e1
JOIn Employee e2
ON e1.manager_id = e2.employee_id
ORDER BY e1.manager_id;

```


### **26. Find the employees who are older than 30 but earn less than the average salary.**

```sql

SELECT employee_name, salary, age
FROM Employee
WHERE 
	age > 30 
	AND (
		SELECT AVG(salary)
	  	FROM Employee
	)

```


### **27. List the departments and the number of employees in each, sorted by the number of employees (in descending order).**


```sql

SELECT d.department_name, COUNT(*) as Employee_Count
FROM Department d
JOIN Employee e
    ON e.department_id = d.department_id
GROUP by d.department_id
ORDER BY COUNT(*) DESC


```


### **28. Retrieve the employees whose names end with 'e'.**
```sql
SELECT employee_name
FROM Employee
WHERE employee_name LIKE '%e';
```


### **30. Get the average age of employees in each department.**
```sql
SELECT department_id, AVG(age) AS AverageAge
FROM Employee
GROUP BY department_id;
```

---

2. **List all employees who are not assigned to any project (i.e., do not appear in the `Project` table).**



```sql

SELECT * 
FROM Employee e 
WHERE e.employee_id NOT IN ( 
	SELECT e1.employee_id 
	FROM Employee e1 
	JOIN Project p ON e1.department_id = p.department_id 
	WHERE p.project_id IS NOT NULL 
	)

```


Your original query is incorrect because it checks department-level project assignments, not individual employee project assignments.

**When This Query Is Correct**:

- If the assumption is that **all employees in a department with any project are considered assigned to a project**, then the query works perfectly fine for finding employees who **are not part of any department with a project**.
- In this case, the absence of a project in a department means no employee from that department is assigned to a project.

**When This Query May Have Limitations**:

If you eventually modify your schema to allow **individual project assignments** for employees (e.g., through a separate `employee_project` junction table), the query would no longer be accurate. The logic would break if employees were assigned to specific projects within their department
- **For your current use case**, where project assignments are based on the department, your query **will work fine** for finding employees **not assigned to any project** (as long as the assignment is indeed department-based).
- However, this would **not scale well** in case of a more granular project assignment model (i.e., individual employees being assigned to specific projects).



**Right ans**

```sql

SELECT e.employee_id, e.employee_name 
FROM Employee e 
LEFT JOIN Project p 
	ON e.department_id = p.department_id 
WHERE p.project_id IS NULL;

```


5. **Find the names of employees who report to a manager in the `Marketing` department.**

```sql


SELECT e.employee_name, e.manager_id, e2.employee_name as Manager_Name
FROM Employee e
JOIN Employee e2
	ON e.manager_id = e2.employee_id
WHERE e.department_id = (
  SELECT d.department_id
  FROM Department d
  WHERE d.department_name = 'Marketing'
  ) AND e.manager_id IS NOT NULL



```


```sql
SELECT e.employee_name
FROM Employee e
JOIN Department d ON e.department_id = d.department_id
WHERE e.manager_id IN (
    SELECT manager_id
    FROM Employee
    WHERE department_id = 2  -- Marketing department
    AND manager_id IS NULL   -- These are the managers (top-level managers in the Marketing department)
);

```




6. **List the managers who manage more than one employees and their corresponding employee count.**

```sql
SELECT e.manager_id, e2.employee_name AS Manager_Name, COUNT(*) AS Employee_Count
FROM Employee e
JOIN Employee e2 ON e.manager_id = e2.employee_id
GROUP BY e.manager_id, e2.employee_name
HAVING COUNT(*) > 1;
```


7. **Retrieve the names of employees who are not managers (i.e., their `employee_id` is not found in the `manager_id` column).**


```sql

SELECT employee_name
FROM Employee
WHERE employee_id NOT IN (
  SELECT manager_id
  FROM Employee
  WHERE manager_id IS NOT NULL
)


```


Note:

- From a **performance perspective**, using `DISTINCT` might introduce a small overhead, as it will need to sort and remove duplicates in the subquery. But in most cases, if you're only working with a small to medium-sized dataset, the difference in performance between using `DISTINCT` and not using it is negligible.
- If you are certain that the `manager_id` column has no duplicates (because you are using a **foreign key** referencing the `employee_id` in the same table), you might skip `DISTINCT`. But typically, it's good practice to use `DISTINCT` to avoid any potential duplication of data in the subquery.


9. **Retrieve the project names and the department names where the project’s end date is before today's date.**


```sql

SELECT p.project_name, d.department_name
FROM Project p
JOIN Department d ON p.department_id = d.department_id
WHERE p.end_date < CAST(GETDATE() AS DATE);

```

### Explanation:

- **`GETDATE()`**: This function returns the current date and time.
- **`CAST(GETDATE() AS DATE)`**: We cast `GETDATE()` to just the date part (without the time) to compare it with the `end_date` in the `Project` table.
- **`p.end_date < CAST(GETDATE() AS DATE)`**: This condition ensures that only projects with an `end_date` before today's date are selected.



2. **For each department, find the oldest employee and their salary.**


```sql

SELECT d.department_name, e.employee_name, e.age, e.salary
FROM Employee e 
JOIN Department d ON e.department_id = d.department_id
WHERE e.age = (
	SELECT MAX(e2.age)
  	FROM Employee e2
  	WHERE e2.department_id = d.department_id
)

```


```sql

SELECT e.department_id, e.employee_name, e.salary, e.age
FROM Employee e
WHERE (e.age, e.department_id) IN (
    SELECT MAX(age), department_id
    FROM Employee
    GROUP BY department_id
);

```


```sql

SELECT e.department_id, e.employee_name, e.salary, e.age
FROM Employee e
JOIN (
    SELECT department_id, MAX(age) AS max_age
    FROM Employee
    GROUP BY department_id
) subquery
ON e.department_id = subquery.department_id
AND e.age = subquery.max_age;


```



---
