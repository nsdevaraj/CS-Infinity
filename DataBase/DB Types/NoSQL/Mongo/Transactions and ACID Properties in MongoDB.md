

### 5. Transactions and ACID Properties in MongoDB

MongoDB provides **multi-document transactions** that allow for **ACID (Atomicity, Consistency, Isolation, Durability)** compliance, enabling reliable and consistent operations across multiple documents and collections.

#### ACID Properties in MongoDB

1. **Atomicity**: All operations in a transaction are treated as a single unit. If any operation fails, the entire transaction is rolled back, ensuring no partial updates.
2. **Consistency**: Transactions move the database from one valid state to another, maintaining schema rules and constraints.
3. **Isolation**: Changes made in a transaction are isolated from other operations until the transaction is committed. MongoDB uses a form of snapshot isolation.
4. **Durability**: Once a transaction is committed, changes are permanently stored, even in case of a failure.

---

#### Multi-Document Transactions

- **Syntax**:
  ```javascript
  const session = db.getMongo().startSession();
  session.startTransaction();

  try {
      const coll1 = session.getDatabase("myDB").collection("accounts");
      const coll2 = session.getDatabase("myDB").collection("logs");

      coll1.updateOne({ _id: 1 }, { $inc: { balance: -100 } }, { session });
      coll2.insertOne({ accountId: 1, amount: -100, date: new Date() }, { session });

      session.commitTransaction();  // Commit all changes if successful
  } catch (error) {
      session.abortTransaction();  // Roll back all changes on error
  } finally {
      session.endSession();
  }
  ```

- **Limitations**:
  - Transactions incur overhead and may reduce performance, so use them sparingly.
  - Transactions are supported only on **replica sets** and **sharded clusters** (for MongoDB 4.2+).

---

### Interview Questions and Answers

**Q1. What is a transaction in MongoDB, and why is it important?**  
- **Answer**: A transaction in MongoDB allows multiple operations across multiple documents or collections to be executed as a single, atomic unit. This is important for applications requiring data consistency and reliability, as it ensures either all changes are applied, or none are.

**Q2. Explain the ACID properties MongoDB supports with transactions.**  
- **Answer**: MongoDB’s transactions are ACID-compliant:
  - **Atomicity** ensures all or nothing behavior for transaction operations.
  - **Consistency** maintains data integrity rules.
  - **Isolation** keeps changes invisible to other operations until the transaction completes.
  - **Durability** makes committed changes permanent.

**Q3. Can you use transactions in MongoDB on sharded clusters?**  
- **Answer**: Yes, as of MongoDB 4.2, transactions are supported on sharded clusters. This enables multi-document transactions across distributed collections, with certain limitations.

**Q4. When would you avoid using transactions in MongoDB?**  
- **Answer**: Transactions should be used sparingly due to their performance overhead. Avoid transactions when operations can be completed within a single document using atomic operations or when strict ACID guarantees are not required.

**Q5. How do you start and end a transaction in MongoDB?**  
- **Answer**: To start a transaction, initiate a session and call `startTransaction()`. Perform all operations within the transaction, then call `commitTransaction()` to save changes or `abortTransaction()` to roll back changes if an error occurs.







