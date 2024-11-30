

## Section 4: Transactions and Concurrency Control

### 4.1 Transaction Basics
A transaction in a database is a sequence of operations that are executed as a single unit. Transactions ensure data consistency, isolation, and durability.

#### Key Concepts:

- **Transaction Lifecycle**: 
  - **BEGIN**: Start a transaction.
  - **COMMIT**: Save changes to the database.
  - **ROLLBACK**: Undo the transaction if there is an error.

#### Related Interview Questions:
- **Q1. What are ACID properties in a database transaction?**
  - *Answer*: ACID properties are Atomicity (all-or-nothing operations), Consistency (ensures data validity), Isolation (independence of transactions), and Durability (permanence of committed changes).

- **Q2. What happens when a transaction is rolled back?**
  - *Answer*: A rollback undoes all changes made during the transaction, restoring the database to its previous consistent state.

---

### 4.2 Transaction Isolation Levels
Transaction isolation levels define the visibility of one transaction’s changes to other concurrent transactions. The SQL standard defines four levels of isolation:

#### Isolation Levels:
1. **READ UNCOMMITTED**: Allows dirty reads (reading uncommitted data).
2. **READ COMMITTED**: Guarantees no dirty reads, but non-repeatable reads are possible (a value may change between reads).
3. **REPEATABLE READ**: Prevents dirty reads and non-repeatable reads, but phantom reads may still occur (new rows might appear in a subsequent query).
4. **SERIALIZABLE**: Provides the highest isolation, ensuring complete transaction independence but at a performance cost.

#### Related Interview Questions:
- **Q3. Explain the difference between READ COMMITTED and SERIALIZABLE isolation levels.**
  - *Answer*: `READ COMMITTED` allows non-repeatable reads (data can change during the transaction), while `SERIALIZABLE` ensures complete isolation, preventing all types of concurrency anomalies (like dirty reads, non-repeatable reads, and phantom reads).

- **Q4. What is a dirty read, and which isolation level allows it?**
  - *Answer*: A dirty read occurs when a transaction reads uncommitted changes from another transaction. It is allowed in the `READ UNCOMMITTED` isolation level.

---

### 4.3 Concurrency Control
Concurrency control ensures that multiple transactions accessing the database simultaneously do not lead to inconsistencies.

#### Key Concepts:
- **Locking Mechanisms**:
  - **Shared Locks**: Allow multiple transactions to read but not write to the locked resource.
  - **Exclusive Locks**: Prevent other transactions from reading or writing to the locked resource.
  
- **Deadlock**: A situation where two or more transactions are waiting for each other to release resources, causing them to be stuck in a cycle.

- **Optimistic vs Pessimistic Locking**:
  - **Pessimistic Locking**: Transactions lock the resources they use to prevent other transactions from accessing them.
  - **Optimistic Locking**: Transactions assume no conflict and proceed, checking for conflicts only at the time of commit.

#### Related Interview Questions:
- **Q5. What is the purpose of locking in databases?**
  - *Answer*: Locking ensures data integrity by preventing multiple transactions from conflicting when accessing the same data simultaneously.

- **Q6. What is deadlock, and how can it be prevented?**
  - *Answer*: Deadlock occurs when transactions wait for each other to release resources. It can be prevented by using timeout mechanisms, deadlock detection algorithms, or careful resource ordering.

- **Q7. What is the difference between optimistic and pessimistic locking?**
  - *Answer*: Pessimistic locking locks the resource for the entire transaction duration, preventing others from accessing it. Optimistic locking allows transactions to proceed assuming no conflict, checking for conflicts only before commit.


{

to check 

deadlock detection algorithm

}

---

### 4.4 Commit and Rollback Operations
**COMMIT** and **ROLLBACK** are essential transaction control operations.

#### Key Concepts:
- **COMMIT**: Saves the changes made during the transaction permanently in the database.
- **ROLLBACK**: Undoes all changes made by the transaction, returning the database to its state before the transaction started.

#### Related Interview Questions:
- **Q8. What happens when a transaction is committed?**
  - *Answer*: When a transaction is committed, all changes made during the transaction are permanently saved to the database.

- **Q9. How does a rollback work in a database?**
  - *Answer*: A rollback undoes all the operations performed in the current transaction, restoring the database to its state before the transaction started.

---

### 4.5 Locking and Lock Granularity
Locks control access to resources (data) in a database. The granularity of locks determines the level of data (row, table, etc.) that is locked.

#### Key Concepts:
- **Row-Level Locks**: Lock only the specific row being accessed, allowing other transactions to access other rows in the same table.
- **Table-Level Locks**: Lock the entire table, preventing other transactions from accessing any rows within the table.
- **Page-Level Locks**: Lock a group of rows that are stored together in a page, typically used in storage systems for performance optimization.

#### Related Interview Questions:
- **Q10. What is the difference between row-level locking and table-level locking?**
  - *Answer*: Row-level locking locks individual rows, allowing other transactions to access different rows in the same table, while table-level locking locks the entire table, blocking access to all rows.

- **Q11. What are the advantages of using row-level locks over table-level locks?**
  - *Answer*: Row-level locks allow greater concurrency since multiple transactions can access different rows in the same table simultaneously, while table-level locks block access to all rows, reducing concurrency.

---

### 4.6 Isolation and Transaction Anomalies
Transaction anomalies occur when multiple transactions interact in ways that violate the ACID properties. Common anomalies include:

#### Key Concepts:
- **Dirty Read**: A transaction reads data that another transaction has modified but not yet committed.
- **Non-Repeatable Read**: A transaction reads the same data twice, and the value changes between the two reads due to another transaction's modifications.
- **Phantom Read**: A transaction reads a set of rows based on a condition, but other transactions insert or delete rows that match the condition during the transaction.

#### Related Interview Questions:
- **Q12. What is a dirty read, and which isolation level allows it?**
  - *Answer*: A dirty read occurs when a transaction reads uncommitted changes from another transaction. It is allowed in the `READ UNCOMMITTED` isolation level.

- **Q13. What is a phantom read, and which isolation level prevents it?**
  - *Answer*: A phantom read happens when new rows are inserted or deleted by another transaction that affect the result set of a query. The `SERIALIZABLE` isolation level prevents phantom reads.

---

### 4.7 Transactions in SQL
Transactions are managed in SQL using the commands **BEGIN**, **COMMIT**, and **ROLLBACK**.

#### Key Concepts:
- **BEGIN**: Starts a new transaction.
- **COMMIT**: Saves all changes made during the transaction.
- **ROLLBACK**: Reverts changes made during the transaction to maintain consistency.

#### Related Interview Questions:
- **Q14. How do you start, commit, and rollback a transaction in SQL?**
  - *Answer*:
    ```sql
    BEGIN; -- Start transaction
    -- SQL operations
    COMMIT; -- Commit transaction (make changes permanent)
    -- Or ROLLBACK; -- Undo transaction if needed
    ```

- **Q15. Can a transaction be rolled back after it has been committed?**
  - *Answer*: No, once a transaction is committed, the changes are permanent, and it cannot be rolled back.

---
