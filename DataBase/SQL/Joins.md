

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





