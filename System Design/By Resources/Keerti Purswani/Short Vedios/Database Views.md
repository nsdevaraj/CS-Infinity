

https://youtu.be/zFYqZgIMTq8?si=OO1TyDilsPRQo0ZW



### Database Views: Key Points

1. **Complexity Reduction**: 
   - Simplifies repeated complex queries for fetching customer orders involving multiple tables (customers, orders, order details).

2. **Definition**: 
   - A view is essentially a complex query stored in the database.

3. **Clean Code**: 
   - Helps make code cleaner and more maintainable by eliminating redundancy.

4. **Virtual Table**: 
   - Acts like a table but is a virtual table, meaning it doesn't store data, just the query.

5. **Query Execution**: 
   - Every time a view is accessed, the underlying query is executed, so execution time remains consistent.

6. **Storing Results**: 
   - To store results instead of executing the query each time, consider using **materialized views**.



### Key Points on Database Views for Job Interviews

1. **Purpose of Views**:
   - Simplify complex queries.
   - Enhance code readability and maintainability.

2. **Types of Views**:
   - **Standard Views**: Virtual tables that execute the underlying query each time.
   - **Materialized Views**: Store the query result, allowing faster access but requiring refresh mechanisms.

3. **Use Cases**:
   - Data abstraction: Hides complexity from users.
   - Security: Restricts access to specific data without exposing the underlying tables.

4. **Performance Considerations**:
   - Views do not store data, so performance can be affected by the complexity of the underlying query.
   - Materialized views can improve performance but need to be refreshed.

5. **Limitations**:
   - Cannot index a view directly; however, indexes can be created on underlying tables.
   - Some operations (like INSERT, UPDATE, DELETE) may be restricted depending on the complexity of the view.

6. **Join Operations**:
   - Views can encapsulate joins, making it easier to work with related data without rewriting the join logic.

7. **SQL Syntax**:
   - Basic syntax: 
     ```sql
     CREATE VIEW view_name AS 
     SELECT column1, column2 
     FROM table_name 
     WHERE condition;
     ```

8. **Common Interview Questions**:
   - Explain the difference between a view and a table.
   - What are materialized views, and when would you use them?
   - How do views affect performance?

### Tips:
- Be prepared to discuss real-world scenarios where you used views.
- Understand when to use views vs. direct queries based on performance and complexity needs.

### Important Points About Database Views for Job Interviews

1. **Definition**: 
   - A view is a virtual table based on the result of a SQL query, used to simplify data access.

2. **Types of Views**:
   - **Standard Views**: Execute the underlying query each time they are accessed.
   - **Materialized Views**: Store the query result physically, allowing for faster access but requiring refresh.

3. **Advantages**:
   - **Simplification**: Encapsulates complex queries for easier access.
   - **Security**: Restricts user access to specific data.
   - **Data Abstraction**: Hides complexity from users, presenting a simplified interface.

4. **Limitations**:
   - Cannot be indexed directly.
   - Updates may be restricted based on view complexity.
   - Performance can be impacted by complex underlying queries.

5. **Creating a View**:
   - Basic syntax:
     ```sql
     CREATE VIEW view_name AS 
     SELECT column1, column2 
     FROM table_name 
     WHERE condition;
     ```

6. **Use Cases**:
   - Reporting: Simplifies queries for reports.
   - Data Sharing: Allows different users to access relevant data without exposing the entire table.

7. **Performance Considerations**:
   - Standard views may slow down with complex queries; consider materialized views for read-heavy applications.

8. **Common Interview Questions**:
   - Differences between views and tables.
   - Use cases for standard vs. materialized views.
   - Situations where you might avoid using views.


### Differences Between Views and Tables

1. **Data Storage**:
   - **Tables**: Physically store data in the database.
   - **Views**: Do not store data; they represent a stored query that fetches data dynamically.

2. **Data Retrieval**:
   - **Tables**: Accessed directly for reading and writing operations.
   - **Views**: Accessed via a query, which can simplify complex data retrieval.

3. **Update Capability**:
   - **Tables**: Directly updatable (insert, update, delete operations).
   - **Views**: Updatable only if certain conditions are met (e.g., based on a single table without complex joins).

4. **Performance**:
   - **Tables**: Access is generally faster since data is stored directly.
   - **Views**: Performance can vary; standard views may be slower due to repeated query execution, while materialized views can be faster but require refresh.

5. **Security**:
   - **Tables**: Can expose all data unless restricted.
   - **Views**: Can restrict access to specific columns or rows, enhancing security.

---

### Use Cases for Standard vs. Materialized Views

1. **Standard Views**:
   - **Use Case**: Ideal for simplifying complex queries in applications where real-time data access is needed.
   - **Example**: A reporting tool that frequently runs the same complex join queries but needs current data from underlying tables.

2. **Materialized Views**:
   - **Use Case**: Best for scenarios requiring high read performance with less frequent updates to the underlying data.
   - **Example**: A dashboard that aggregates sales data where quick access to pre-calculated results is beneficial, but real-time updates are less critical.

---

### Situations Where You Might Avoid Using Views

1. **Performance Concerns**:
   - If the underlying query of a standard view is very complex and involves heavy calculations or joins, it might lead to slow performance.

2. **Data Manipulation Needs**:
   - When you need to perform frequent insert, update, or delete operations, using a view can complicate the process, especially if it's not updatable.

3. **Debugging Issues**:
   - Views can make debugging more difficult since the logic is abstracted away. If you frequently need to troubleshoot queries, directly querying tables may be simpler.

4. **Materialized View Refresh Overhead**:
   - If the underlying data changes frequently and the materialized view requires constant refreshing, the overhead may outweigh the benefits.

5. **Complex Business Logic**:
   - If the logic is too complex to be effectively captured in a view, it may be better handled in application logic or stored procedures.

By considering these points, you can effectively articulate the differences, use cases, and potential drawbacks of using views in a database context during your interview.


### Tips for Interviews:
- Provide concrete examples of when you've used views.
- Understand both the benefits and drawbacks of views in practical scenarios.
