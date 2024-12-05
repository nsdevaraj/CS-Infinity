

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






reffered {

https://www.youtube.com/watch?v=Yh4CrPHVBdE


}
## **Section 3: Joins and Subqueries**


Join: 2 columns only on same type ( logical or illogical join columns based on developer )
To make logically correct -> join will be done with foreign key
### 1. **Joins (Combining Tables)**

   - **Concept**: Joins combine rows from two or more tables based on a related column between them.
   - **Types of Joins**:
     - **INNER JOIN**: Returns rows when there is a match in both tables.
     - **LEFT JOIN** (or **LEFT OUTER JOIN**): Returns all rows from the left table, and matched rows from the right table.
     - **RIGHT JOIN** (or **RIGHT OUTER JOIN**): Returns all rows from the right table, and matched rows from the left table.
     - **FULL JOIN** (or **FULL OUTER JOIN**): Returns rows when there is a match in one of the tables.

   #### **Interview Question 1**: Write a query to retrieve employee names along with their department names, assuming `Employees` and `Departments` tables.

   ```sql
   SELECT e.name, d.department_name
   FROM Employees e
   INNER JOIN Departments d ON e.department_id = d.department_id;
   ```

   **Explanation**: `INNER JOIN` combines `Employees` and `Departments` tables based on matching `department_id` values, and retrieves employee names with their respective department names.

   #### **Interview Question 2**: Retrieve all employees along with their department names, including employees without a department.

   ```sql
   SELECT e.name, d.department_name
   FROM Employees e
   LEFT JOIN Departments d ON e.department_id = d.department_id;
   ```

   **Explanation**: `LEFT JOIN` includes all employees, even those who don’t have a matching department, showing `NULL` for `department_name` where no match is found.

---

### 2. **Self-Joins**

   - **Concept**: A self-join is a join of a table with itself. It’s often used for hierarchical data or comparing rows within the same table.
   - **Use Case**: Finding employees managed by other employees in the same `Employees` table.

   #### **Interview Question 3**: Write a query to list employees along with their manager names, assuming the `Employees` table has a `manager_id` column.

   ```sql
   SELECT e.name AS employee_name, m.name AS manager_name
   FROM Employees e
   LEFT JOIN Employees m ON e.manager_id = m.employee_id;
   ```

   **Explanation**: `LEFT JOIN` is used to join `Employees` to itself, with `e` as the employee and `m` as the manager. This fetches each employee’s manager name.

---



### SQL JOIN Types Explained with Examples

---

#### **1. Primary Key and Foreign Key Relationship**
- **Definition**: 
  - **Primary Key**: Uniquely identifies a row in a table.
  - **Foreign Key**: Establishes a relationship between two tables via shared values.
- **Example**:
  ```sql
  -- Customer table: Primary Key
  CREATE TABLE customer (
      customer_id INT PRIMARY KEY,
      name VARCHAR(100)
  );

  -- Event table: Foreign Key
  CREATE TABLE event (
      event_id INT PRIMARY KEY,
      customer_id INT,
      action VARCHAR(100),
      FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
  );
  ```

### **Common Table Modifications**

#### Create a table for action types and use foreign keys:
```sql
CREATE TABLE action_type (
    action_id INT PRIMARY KEY,
    action_name VARCHAR(100)
);

CREATE TABLE event_v2 (
    event_id INT PRIMARY KEY,
    customer_id INT,
    action_id INT,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (action_id) REFERENCES action_type(action_id)
);
```



---




### **1. Tables and Their Data**

#### **`customer` Table**:
| customer_id | name         |
|-------------|--------------|
| 1           | Alice        |
| 2           | Bob          |
| 3           | Charlie      |

#### **`event` Table**:
| event_id | customer_id | action        |
|----------|-------------|---------------|
| 101      | 1           | Login         |
| 102      | 1           | Purchase      |
| 103      | 2           | View Product  |

#### **`teacher` Table**:
| name       | age |
|------------|-----|
| Mr. Smith  | 30  |
| Ms. Johnson| 40  |

#### **`student` Table**:
| name      | age |
|-----------|-----|
| John Doe  | 20  |
| Jane Smith| 30  |

#### **`action_type` Table**:
| action_id | action_name |
|-----------|-------------|
| 1         | Login       |
| 2         | Purchase    |
| 3         | View Product|

#### **`event_v2` Table**:
| event_id | customer_id | action_id |
|----------|-------------|-----------|
| 201      | 1           | 1         |
| 202      | 1           | 2         |
| 203      | 2           | 3         |



---

![[Pasted image 20241118090501.png]]


---


#### **2. INNER JOIN**
- **Use Case**: Fetch rows where there is a match in both tables.
- default join , just JOIN means inner join
- **Example**:
  ```sql
  SELECT customer.name, event.action
  FROM customer
  INNER JOIN event ON customer.customer_id = event.customer_id;
  ```


**Output**:
| name   | action       |
|--------|--------------|
| Alice  | Login        |
| Alice  | Purchase     |
| Bob    | View Product |



![[Pasted image 20241118085855.png]]



---

#### **3. LEFT JOIN**
- **Use Case**: Fetch all rows from the left table and matched rows from the right table. For non-matching rows, NULLs are used.
- **Example**:
  ```sql
  SELECT customer.name, event.action
  FROM customer
  LEFT JOIN event ON customer.customer_id = event.customer_id;

  
  ```



**Output**:
| name    | action       |
|---------|--------------|
| Alice   | Login        |
| Alice   | Purchase     |
| Bob     | View Product |
| Charlie | NULL         |


![[Pasted image 20241118085937.png]]





---

#### **4. RIGHT JOIN**
- **Use Case**: Fetch all rows from the right table and matched rows from the left table. For non-matching rows, NULLs are used.
- rarest one since any right join can be rewritten left join
- Usecase: combine data across multiple table
- **Example**:
  ```sql
  SELECT event.action, customer.name
  FROM event
  RIGHT JOIN customer ON customer.customer_id = event.customer_id;
  ```



**Output**:
| action       | name     |
|--------------|----------|
| Login        | Alice    |
| Purchase     | Alice    |
| View Product | Bob      |
| NULL         | Charlie  |



![[Pasted image 20241118090020.png]]



![[Pasted image 20241118090102.png]]




---

#### **5. FULL / OUTER JOIN**
- **Use Case**: Fetch all rows from both tables. For non-matching rows, NULLs are used.
- combination of left and right join
- **Example**:
  ```sql
  SELECT teacher.name AS teacher_name, student.name AS student_name
  FROM teacher
  FULL OUTER JOIN student ON teacher.age = student.age;
  ```


**Output**:
| teacher_name | student_name |
|--------------|--------------|
| Mr. Smith    | Jane Smith   |
| Ms. Johnson  | NULL         |
| NULL         | John Doe     |



![[Pasted image 20241118090159.png]]



---

#### **6. UNION**
- **Use Case**: Combine two tables into one by stacking rows. Deduplicates the results.
- stack data from 2 datasets as single table
- ignore duplicate
- **Example**:
  ```sql
  SELECT name FROM teacher
  UNION
  SELECT name FROM student;
  ```


**Output**:
| name          |
|---------------|
| Mr. Smith     |
| Ms. Johnson   |
| John Doe      |
| Jane Smith    |


---

#### **7. UNION ALL**
- **Use Case**: Combine two tables into one by stacking rows. Does not deduplicate the results.
- same like union, but include duplicate
- **Example**:
  ```sql
  SELECT name FROM teacher
  UNION ALL
  SELECT name FROM student;
  ```


**Output**:
| name          |
|---------------|
| Mr. Smith     |
| Ms. Johnson   |
| John Doe      |
| Jane Smith    |

---

#### **8. CROSS JOIN**
- **Use Case**: Combines every row of the first table with every row of the second table.
- for each row in one table is mapped with other table's row
- **Example**:
  ```sql
  SELECT teacher.name AS teacher_name, student.name AS student_name
  FROM teacher
  CROSS JOIN student;
  ```



**Output**:
| teacher_name | student_name |
|--------------|--------------|
| Mr. Smith    | John Doe     |
| Mr. Smith    | Jane Smith   |
| Ms. Johnson  | John Doe     |
| Ms. Johnson  | Jane Smith   |


![[Pasted image 20241118090352.png]]


---



#### **2.8 LEFT JOIN with `event_v2`**
```sql
SELECT customer.name, action_type.action_name
FROM customer
LEFT JOIN event_v2 ON customer.customer_id = event_v2.customer_id
LEFT JOIN action_type ON event_v2.action_id = action_type.action_id;
```

**Output**:
| name    | action_name  |
|---------|--------------|
| Alice   | Login        |
| Alice   | Purchase     |
| Bob     | View Product |
| Charlie | NULL         |





