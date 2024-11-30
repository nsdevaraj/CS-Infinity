
## Section 1: Basics of DBMS and Database Models

### 1.1 Database Management System (DBMS)
* software that enables efficient creation, access, management, and manipulation of data in databases.
* It ensures data consistency, integrity, and security while supporting multiple users.

#### Key Concepts:
- **Data Independence**: Separation of data from applications, making structural changes easier.
- **Data Integrity**: Ensures data accuracy and consistency.
- **Data Security**: Protects data through authentication, authorization, and encryption.
- **Concurrency Control**: Manages simultaneous data access, preventing conflicts.
- **Recovery Management**: Ensures data restoration after system failures.

#### Related Interview Questions:
- **Q1. What is DBMS, and how does it differ from a file system?**
  - *Answer*: DBMS is structured for organized data management, supporting features like concurrent access, data integrity, and reduced redundancy, unlike a traditional file system.

- **Q2. What are some essential features of a DBMS?**
  - *Answer*: Data independence, data integrity, data security, concurrency control, and recovery management.

- **Q3. What are some real-world applications of DBMS?**
  - *Answer*: Banking systems, airline reservations, telecommunications, and hospital management systems.

---

### 1.2 Data Models
Data models define the framework for structuring, storing, and accessing data in a DBMS. They provide an abstraction for how data is organized.

#### Types of Data Models:
1. **Hierarchical Model**:
   - Organizes data in a tree-like structure.
   - Each parent has multiple children, but each child has only one parent.
   - Example: File directories.

2. **Network Model**:
   - Organizes data as a graph, allowing more complex many-to-many relationships.
   - Example: Telecommunications networks.

3. **Relational Model**:
   - Stores data in tables (relations), where each row represents a record and each column represents an attribute.
   - Uses primary keys and foreign keys to define relationships between tables.
   - Example: Business applications and transactional databases.

4. **Object-Oriented Model**:
   - Data is represented as objects, suitable for handling complex data like multimedia.
   - Example: Scientific databases and applications requiring complex data structures.

#### Related Interview Questions:
- **Q4. Describe the main types of data models in DBMS and their use cases.**
  - *Answer*: Hierarchical (tree structure), Network (complex relationships), Relational (tables and keys), Object-Oriented (object representation).

- **Q5. What is the difference between the hierarchical and network data models?**
  - *Answer*: Hierarchical uses a tree structure (one-to-many), while network supports many-to-many relationships using a graph structure.

- **Q6. Why is the relational model widely used?**
  - *Answer*: Its flexibility, support for complex queries, and structured data management through SQL make it suitable for many business applications.

---

### 1.3 Relational Database Concepts
Relational databases, based on the relational model, are widely used due to their structured organization and SQL support.

#### Core Concepts:
- **Tables**: Primary structure for storing data; each table represents an entity.
- **Attributes**: Columns in a table; each represents a specific field.
- **Primary Key**: Unique identifier for each record in a table.
- **Foreign Key**: Field that creates a link between tables, enforcing referential integrity.
- **SQL (Structured Query Language)**: Standard language for querying and managing relational databases.

#### Related Interview Questions:
- **Q7. What is a primary key, and why is it essential in relational databases?**
  - *Answer*: It uniquely identifies records in a table, supporting data integrity and enabling relationships with foreign keys in other tables.

- **Q8. Explain the difference between a primary key and a foreign key.**
  - *Answer*: A primary key uniquely identifies records within a table, while a foreign key links records in one table to records in another.

- **Q9. What is referential integrity, and how is it maintained?**
  - *Answer*: Referential integrity ensures foreign key values correspond to existing records in the referenced table, maintained through foreign key constraints.

- **Q10. Write a SQL query to create two related tables with primary and foreign keys.**

```sql
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL
);

CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);
```




---

### 1.4 ACID Properties
ACID properties are essential for ensuring reliable transaction processing in databases. These properties are crucial in any multi-user database system.

1. **Atomicity**: Transactions are all-or-nothing; if one part fails, the entire transaction fails.
2. **Consistency**: Guarantees that a transaction moves the database from one valid state to another.
3. **Isolation**: Ensures that transactions do not interfere with each other.
4. **Durability**: Once a transaction is committed, changes are permanent even in case of failures.

#### Related Interview Questions:
- **Q11. Explain the ACID properties of a DBMS.**
  - *Answer*: Atomicity (all-or-nothing transactions), Consistency (valid states), Isolation (independent transactions), Durability (permanent changes).

- **Q12. Why are ACID properties important in a database system?**
  - *Answer*: They ensure reliable, consistent, and error-free transaction processing, which is crucial in systems where data integrity is critical.

---

### 1.5 Keys in Relational Databases
Keys are fundamental in relational databases, enabling data retrieval, integrity, and relationships between tables.

### Types of Keys

1. **Primary Key**: Uniquely identifies each record in a table. There can only be one primary key per table.
   - Example: In a `Students` table, `StudentID` can be a primary key.

2. **Foreign Key**: Establishes a link between tables by referencing the primary key in another table. It enforces referential integrity.
   - Example: A `CourseEnrollments` table may have a `StudentID` that references the `Students` table.

3. **Candidate Key**: Any column or combination of columns that can qualify as a unique identifier for rows in a table. There can be multiple candidate keys, but only one can be the primary key.
   - Example: In a `Students` table, `StudentID` and `Email` could both serve as candidate keys.

4. **Alternate Key**: A candidate key that is not selected as the primary key.
   - Example: In the `Students` table, if `StudentID` is the primary key, `Email` would be an alternate key.

5. **Composite Key**: A key that consists of two or more columns to uniquely identify a record.
   - Example: In a `CourseEnrollments` table, a combination of `StudentID` and `CourseID` might form a composite key.

6. **Super Key**: A set of one or more columns (attributes) that can uniquely identify a record. Super keys include primary, candidate, and composite keys.

#### Related Interview Questions:
- **Q13. What is a candidate key, and how does it differ from a primary key?**
  - *Answer*: Both can uniquely identify records, but there can be multiple candidate keys in a table, from which one is chosen as the primary key.

- **Q14. What is a composite key, and when would you use it?**
  - *Answer*: A composite key consists of multiple attributes to uniquely identify records, used when no single attribute can serve as a unique identifier.

- **Q15. How does a foreign key enforce referential integrity?**
  - *Answer*: A foreign key links to a primary key in another table, ensuring that relationships remain consistent by restricting foreign key values to valid primary key entries.


In relational database management systems (RDBMS), several types of keys are used to maintain data integrity, establish relationships, and ensure efficient data retrieval. Here’s a quick explanation of each key type, followed by an example using a **Mermaid diagram**.

