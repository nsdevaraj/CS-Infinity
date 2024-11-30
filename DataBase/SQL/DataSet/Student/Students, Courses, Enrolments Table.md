
### **Schema Definition**

#### 1. **Students**
| Column Name     | Data Type       | Description                           |
|------------------|----------------|---------------------------------------|
| StudentID        | INT (Primary Key) | Unique ID for each student           |
| Name             | VARCHAR(100)   | Full name of the student              |
| Age              | INT            | Age of the student                    |
| Major            | VARCHAR(50)    | The major field of study              |
| GPA              | DECIMAL(3, 2)  | Grade point average                   |

Decimal(3,2) => 3 digits, out of 3 , 2 are reserved for fractional part


##### Students
| StudentID | Name          | Age | Major        | GPA |
| --------- | ------------- | --- | ------------ | --- |
| 1         | Alice Johnson | 20  | Computer Sci | 3.8 |
| 2         | Bob Smith     | 22  | Mathematics  | 3.4 |
| 3         | Clara Evans   | 21  | Biology      | 3.6 |



#### 2. **Courses**
| Column Name     | Data Type       | Description                           |
|------------------|----------------|---------------------------------------|
| CourseID         | INT (Primary Key) | Unique ID for each course           |
| CourseName       | VARCHAR(100)   | Name of the course                    |
| Department       | VARCHAR(50)    | Department offering the course        |
| Credits          | INT            | Number of credits for the course      |


##### Courses
| CourseID | CourseName      | Department   | Credits |
| -------- | --------------- | ------------ | ------- |
| 101      | Data Structures | Computer Sci | 4       |
| 102      | Linear Algebra  | Mathematics  | 3       |
| 103      | Genetics        | Biology      | 3       |



#### 3. **Enrollments**
| Column Name     | Data Type       | Description                           |
|------------------|----------------|---------------------------------------|
| EnrollmentID     | INT (Primary Key) | Unique enrollment record ID        |
| StudentID        | INT (Foreign Key) | Links to Students(StudentID)       |
| CourseID         | INT (Foreign Key) | Links to Courses(CourseID)         |
| Semester         | VARCHAR(20)    | Semester when enrolled (e.g., "Fall 2024") |
| Grade            | CHAR(2)        | Grade received by the student        |

##### Enrollments
| EnrollmentID | StudentID | CourseID | Semester    | Grade |
| ------------ | --------- | -------- | ----------- | ----- |
| 1001         | 1         | 101      | Fall 2024   | A     |
| 1002         | 2         | 102      | Fall 2024   | B     |
| 1003         | 3         | 103      | Fall 2024   | A     |
| 1004         | 1         | 102      | Spring 2024 | B+    |
| 1005         | 2         | 103      | Spring 2024 | C     |


```sql
-- Create the Courses table
CREATE TABLE Courses (
  id INT PRIMARY KEY,
  name VARCHAR(30) UNIQUE NOT NULL,
  department VARCHAR(30) NOT NULL,
  credits INT NOT NULL
);

-- Insert sample data into Courses
INSERT INTO Courses (id, name, department, credits) VALUES
(101, 'DS', 'CS', 4),
(102, 'Trig', 'Math', 3),
(103, 'Genes', 'Bio', 3),
(104, 'AI', 'CS', 3),
(105, 'Calculus', 'Math', 4),
(106, 'Biochemistry', 'Bio', 3),
(107, 'Statistics', 'Math', 3),
(108, 'Networks', 'CS', 4);


-- Create the Students table
CREATE TABLE Students (
  id INT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  age INT NOT NULL,
  major VARCHAR(30) NOT NULL,
  gpa DECIMAL(3,2) NOT NULL
);

-- Insert sample data into Students
INSERT INTO Students (id, name, age, major, gpa) VALUES
(1, 'Alice Johnson', 20, 'CS', 3.8),
(2, 'Bob Smith', 22, 'Math', 3.4),
(3, 'Clara Evans', 21, 'Bio', 3.6),
(4, 'David Green', 23, 'CS', 3.7),
(5, 'Eva Adams', 21, 'Math', 3.9),
(6, 'Frank Harris', 22, 'Bio', 3.5),
(7, 'Grace Lee', 20, 'CS', 3.6),
(8, 'Henry Carter', 24, 'Math', 3.3);


-- Create the Enrollments table with foreign keys to Students and Courses
CREATE TABLE Enrollments (
  EnrollmentID INT PRIMARY KEY,                
  StudentID INT,                               
  CourseID INT,                                
  Semester VARCHAR(20),                        
  Grade CHAR(2),                               
  FOREIGN KEY (StudentID) REFERENCES Students(id), 
  FOREIGN KEY (CourseID) REFERENCES Courses(id)
);

-- Insert sample data into Enrollments
INSERT INTO Enrollments (EnrollmentID, StudentID, CourseID, Semester, Grade) VALUES
(1, 1, 101, 'Fall 2024', 'A'),  
(2, 2, 102, 'Fall 2024', 'B'),  
(3, 3, 103, 'Spring 2024', 'A'),
(4, 4, 104, 'Spring 2024', 'A'),
(5, 5, 105, 'Fall 2024', 'B'),
(6, 6, 106, 'Spring 2024', 'B'),
(7, 7, 108, 'Fall 2024', 'A'),
(8, 8, 107, 'Spring 2024', 'C'),
(9, 1, 105, 'Spring 2024', 'B'),
(10, 2, 104, 'Fall 2024', 'A'),
(11, 3, 108, 'Fall 2024', 'B'),
(12, 4, 102, 'Spring 2024', 'A'),
(13, 5, 103, 'Spring 2024', 'A');





```




extra:

adding foreign key constraint

```sql

ALTER TABLE Courses
ADD CONSTRAINT fk_department_major
FOREIGN KEY (department) REFERENCES Students(major)
ON DELETE CASCADE;

```