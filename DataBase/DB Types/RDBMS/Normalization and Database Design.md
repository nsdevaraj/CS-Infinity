

## Section 3: Normalization and Database Design

### 3.1 Database Design Principles
Good database design is essential for performance, scalability, and data integrity in a relational database. Core principles include:

#### Key Concepts:
- **Entity-Relationship Modeling (ER Modeling)**: A diagram-based design technique to model entities (tables) and relationships (connections) in a database.
- **Avoiding Redundancy**: Minimizes duplicate data to prevent data anomalies.
- **Ensuring Data Integrity**: Maintains accuracy and consistency across tables using constraints (e.g., primary keys, foreign keys).
- **Scalability**: Structures the database for ease of scaling up when data or user load increases.

#### Related Interview Questions:
- **Q1. What is ER modeling in database design, and why is it used?**
  - *Answer*: ER modeling visualizes entities and relationships, serving as a blueprint for designing relational databases.

- **Q2. Why is reducing redundancy important in database design?**
  - *Answer*: Reducing redundancy saves storage, improves query performance, and prevents anomalies during updates.

---

### 3.2 Normalization
* Normalization -  the process of organizing data to minimize redundancy and improve data integrity.
* It involves breaking down tables based on a series of rules, called normal forms.

#### Normal Forms:
1. **First Normal Form (1NF)**:
   - Eliminates repeating groups by ensuring each cell holds a single value.
   - Example: Separate multiple phone numbers into distinct rows if stored in a single cell.

2. **Second Normal Form (2NF)**:
   - Achieved if the table is in 1NF and all non-key attributes depend on the entire primary key (i.e., no partial dependency).
   - Applies to tables with composite keys, requiring every attribute to depend on all parts of the key.

3. **Third Normal Form (3NF)**:
   - Achieved if the table is in 2NF and all attributes depend only on the primary key (i.e., no transitive dependency).
   - Removes attributes that depend on other non-key attributes.

4. **Boyce-Codd Normal Form (BCNF)**:
   - Stricter version of 3NF; requires every determinant to be a candidate key.

#### Related Interview Questions:
- **Q3. What is normalization, and why is it essential in database design?**
  - *Answer*: Normalization reduces redundancy and dependency, leading to efficient data management and minimizing data anomalies.

- **Q4. Explain the difference between 1NF and 2NF.**
  - *Answer*: 1NF ensures each cell contains atomic (single) values, while 2NF (if composite key exists) ensures every non-key attribute depends on the entire primary key.

- **Q5. What is the purpose of BCNF, and how does it differ from 3NF?**
  - *Answer*: BCNF is a stricter form of 3NF where every determinant must be a candidate key, ensuring even stronger data integrity.

---

### 3.3 Denormalization
* Denormalization is the process of combining tables or adding redundant data to optimize read-heavy operations. 
* It’s often used when high performance is prioritized over strict data integrity.

#### Key Concepts:
- **Benefits**: Improves read performance by reducing the number of joins.
- **Trade-offs**: Increases storage requirements and may lead to data anomalies during updates.
- **When Used**: Common in read-heavy applications like data warehouses where data consistency is not updated frequently.

#### Related Interview Questions:
- **Q6. What is denormalization, and when is it applied?**
  - *Answer*: Denormalization adds redundancy to improve read performance, often used in scenarios like data warehousing.

- **Q7. What are the potential downsides of denormalization?**
  - *Answer*: Increased storage use and potential data anomalies (inconsistencies) due to redundant data across tables.

---

### 3.4 Keys and Constraints in Database Design
Keys and constraints are essential for enforcing data integrity and relationships between tables.

#### Key Concepts:
- **Primary Key**: Unique identifier for each row in a table, ensuring uniqueness.
- **Foreign Key**: Field that links to a primary key in another table, establishing relationships.
- **Unique Constraint**: Ensures that all values in a column or set of columns are unique.
- **Check Constraint**: Ensures data in a column meets specific criteria.
- **Not Null Constraint**: Ensures a column cannot have NULL values.

#### Related Interview Questions:
- **Q8. Explain the importance of primary and foreign keys in relational database design.**
  - *Answer*: Primary keys uniquely identify records, and foreign keys enforce relationships, maintaining referential integrity across tables.

- **Q9. What is a unique constraint, and how does it differ from a primary key?**
  - *Answer*: A unique constraint enforces uniqueness for a column, while a primary key also identifies records uniquely and is the main identifier.

---

### 3.5 Indexes in Database Design
Indexes are data structures that improve the speed of data retrieval operations on database tables. 

#### Key Concepts:
- **Types of Indexes**:
  - **Primary Index**: Automatically created on primary keys.
  - **Unique Index**: Prevents duplicate values in indexed columns.
  - **Composite Index**: Built on multiple columns to optimize queries involving multiple fields.
  - **Full-Text Index**: Used for fast text search, especially in large text columns.
- **Trade-offs**:
  - **Advantages**: Enhances query performance by reducing data retrieval time.
  - **Disadvantages**: Increases storage space and can slow down data modification operations.

#### Related Interview Questions:
- **Q10. What is an index in a database, and why is it used?**
  - *Answer*: An index speeds up data retrieval by allowing quicker access to rows in a table, essential for performance optimization.

- **Q11. What is a composite index, and when would you use one?**
  - *Answer*: A composite index is based on multiple columns, useful when queries often filter or sort by multiple fields together.

---

### 3.6 Relationships Between Tables
Relationships define how tables are linked and interact in a relational database. 

#### Types of Relationships:
1. **One-to-One (1:1)**:
   - One record in a table relates to one and only one record in another table.
   - Example: Person and Passport tables.

2. **One-to-Many (1:N)**:
   - One record in a table relates to multiple records in another table.
   - Example: Customer and Orders tables.

3. **Many-to-Many (M:N)**:
   - Records in one table relate to multiple records in another, often resolved with a junction (bridge) table.
   - Example: Students and Courses tables with an Enrollment junction table.

#### Related Interview Questions:
- **Q12. Explain the difference between one-to-many and many-to-many relationships.**
  - *Answer*: In one-to-many, a record in one table relates to multiple in another, while many-to-many allows multiple relationships across both tables, typically resolved by a junction table.

- **Q13. What is the purpose of a junction table in a many-to-many relationship?**
  - *Answer*: A junction table helps represent many-to-many relationships by linking the primary keys of the two related tables, effectively breaking them into one-to-many relationships.

---

### 3.7 Entity Integrity and Referential Integrity
These integrity rules maintain data accuracy and reliability across a database.

#### Key Concepts:
- **Entity Integrity**: Ensures each entity (row) is unique and identifiable, usually enforced by primary keys.
- **Referential Integrity**: Ensures consistency between related tables, typically enforced by foreign keys.

#### Related Interview Questions:
- **Q14. What is entity integrity, and how is it maintained in a relational database?**
  - *Answer*: Entity integrity ensures each row is unique, maintained by having a primary key for each table.

- **Q15. What is referential integrity, and how does it relate to foreign keys?**
  - *Answer*: Referential integrity ensures that foreign key values match primary key values in related tables, preventing orphaned records and ensuring data consistency.

---
