

```sql


CREATE TABLE Department (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);


-- Insert data into Department table
INSERT INTO Department (department_id, department_name) VALUES
(1, 'Sales'),
(2, 'Marketing'),
(3, 'IT'),
(4, 'HR'),
(5, 'Finance');


-- SELECT *
-- FROM Department

-- Output:

-- +---------------+-----------------+
-- | department_id | department_name |
-- +---------------+-----------------+
-- |             1 | Sales           |
-- |             2 | Marketing       |
-- |             3 | IT              |
-- |             4 | HR              |
-- |             5 | Finance         |
-- +---------------+-----------------+



CREATE TABLE Employee (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    salary DECIMAL(10, 2),
    department_id INT,
    manager_id INT,
    age INT,
    FOREIGN KEY (department_id) REFERENCES Department(department_id),
    FOREIGN KEY (manager_id) REFERENCES Employee(employee_id)
);



-- Insert data into Employee table
INSERT INTO Employee (employee_id, employee_name, salary, department_id, manager_id, age) VALUES
(1, 'Alice', 6000.00, 1, NULL, 30),
(2, 'Bob', 5000.00, 1, 1, 28),
(3, 'Charlie', 7000.00, 2, NULL, 35),
(4, 'David', 4500.00, 2, 3, 26),
(5, 'Eve', 8000.00, 3, NULL, 40),
(6, 'Frank', 7500.00, 3, 5, 29),
(7, 'Grace', 5500.00, 4, NULL, 50),
(8, 'Hank', 5000.00, 4, 7, 45),
(9, 'Ivy', 9000.00, 5, NULL, 38),
(10, 'Jack', 6500.00, 5, 9, 33),
(11, 'John', 8500.00, 3, NULL, 31),  
(12, 'Lucy', 10000.00, 1, NULL, 34), 
(13, 'George', 5500.00, 4, NULL, 29),
(14, 'Tom', 6000.00, 2, 1, 27),      
(15, 'Nancy', 4000.00, 4, NULL, 26), 
(16, 'Olivia', 8000.00, 1, NULL, 42), 
(17, 'Alice', 7000.00, 3, NULL, 31),  
(18, 'Paul', 5500.00, 1, NULL, 30),  
(19, 'Anna', 6500.00, 2, NULL, 30),   
(20, 'Rachel', 4000.00, 3, NULL, 32), 
(21, 'Jake', 5500.00, 1, NULL, 30);  




-- SELECT *
-- FROM Employee



-- -- Output:

-- -- +-------------+---------------+----------+---------------+------------+------+
-- -- | employee_id | employee_name | salary   | department_id | manager_id | age  |
-- -- +-------------+---------------+----------+---------------+------------+------+
-- -- |           1 | Alice         |  6000.00 |             1 |       NULL |   30 |
-- -- |           2 | Bob           |  5000.00 |             1 |          1 |   28 |
-- -- |           3 | Charlie       |  7000.00 |             2 |       NULL |   35 |
-- -- |           4 | David         |  4500.00 |             2 |          3 |   26 |
-- -- |           5 | Eve           |  8000.00 |             3 |       NULL |   40 |
-- -- |           6 | Frank         |  7500.00 |             3 |          5 |   29 |
-- -- |           7 | Grace         |  5500.00 |             4 |       NULL |   50 |
-- -- |           8 | Hank          |  5000.00 |             4 |          7 |   45 |
-- -- |           9 | Ivy           |  9000.00 |             5 |       NULL |   38 |
-- -- |          10 | Jack          |  6500.00 |             5 |          9 |   33 |
-- -- |          11 | John          |  8500.00 |             3 |       NULL |   31 |
-- -- |          12 | Lucy          | 10000.00 |             1 |       NULL |   34 |
-- -- |          13 | George        |  5500.00 |             4 |       NULL |   29 |
-- -- |          14 | Tom           |  6000.00 |             2 |          1 |   27 |
-- -- |          15 | Nancy         |  4000.00 |             4 |       NULL |   26 |
-- -- |          16 | Olivia        |  8000.00 |             1 |       NULL |   42 |
-- -- |          17 | Alice         |  7000.00 |             3 |       NULL |   31 |
-- -- |          18 | Paul          |  5500.00 |             1 |       NULL |   30 |
-- -- |          19 | Anna          |  6500.00 |             2 |       NULL |   30 |
-- -- |          20 | Rachel        |  4000.00 |             3 |       NULL |   32 |
-- -- |          21 | Jake          |  5500.00 |             1 |       NULL |   30 |
-- -- +-------------+---------------+----------+---------------+------------+------+




CREATE TABLE Project (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    department_id INT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (department_id) REFERENCES Department(department_id)
);

-- Inserting data into Project table
INSERT INTO Project (project_id, project_name, department_id, start_date, end_date) VALUES
(1, 'Project Alpha', 1, '2023-01-15', '2032-06-15'),
(2, 'Project Beta', 2, '2023-03-01', '2023-12-31'),
(3, 'Project Gamma', 3, '2000-04-10', '2013-08-20'),
(4, 'Project Delta', 4, '2023-02-25', '2024-07-01');






-- SELECT *
-- FROM PROJECT


-- -- Output:

-- -- +------------+-----------------+---------------+------------+------------+
-- -- | project_id | project_name    | department_id | start_date | end_date   |
-- -- +------------+-----------------+---------------+------------+------------+
-- -- |          1 | Project Alpha   |             1 | 2023-01-15 | 2023-06-15 |
-- -- |          2 | Project Beta    |             2 | 2023-03-01 | 2023-12-31 |
-- -- |          3 | Project Gamma   |             3 | 2023-04-10 | 2023-08-20 |
-- -- |          4 | Project Delta   |             4 | 2023-02-25 | 2023-07-01 |
-- -- |          5 | Project Epsilon |             5 | 2023-05-01 | 2023-11-15 |
-- -- +------------+-----------------+---------------+------------+------------+

```

