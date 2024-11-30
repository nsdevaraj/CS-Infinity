

Here’s a crisp breakdown of MongoDB’s **CRUD Operations** and **Aggregation Framework**, along with example code and potential interview questions with answers.

---

### 1. CRUD Operations (Create, Read, Update, Delete)

#### Basic CRUD Operations in MongoDB

1. **Create** - Inserts data into a collection.
   ```javascript
   db.collection.insertOne({ name: "Alice", age: 25 });
   db.collection.insertMany([{ name: "Bob", age: 30 }, { name: "Charlie", age: 35 }]);
   ```

2. **Read** - Retrieves data from a collection.
   ```javascript
   db.collection.find({ age: { $gte: 30 } });  // Finds documents where age >= 30
   db.collection.findOne({ name: "Alice" });   // Finds one document with name "Alice"
   ```

3. **Update** - Modifies existing data in a collection.
   ```javascript
   db.collection.updateOne({ name: "Alice" }, { $set: { age: 26 } });
   db.collection.updateMany({ age: { $gte: 30 } }, { $inc: { age: 1 } });
   ```

4. **Delete** - Removes data from a collection.
   ```javascript
   db.collection.deleteOne({ name: "Alice" });
   db.collection.deleteMany({ age: { $gte: 30 } });
   ```

#### Aggregation Framework

The Aggregation Framework in MongoDB processes data records and returns computed results. It's especially useful for handling complex queries like data transformations and analysis.

**Example Aggregation Pipeline**
```javascript
db.collection.aggregate([
   { $match: { age: { $gte: 25 } } },                // Stage 1: Filter documents where age >= 25
   { $group: { _id: "$age", count: { $sum: 1 } } },  // Stage 2: Group by 'age' and count occurrences
   { $sort: { count: -1 } }                          // Stage 3: Sort by count in descending order
]);
```

---

### Common Interview Questions and Answers

#### Q1. **Explain the difference between `insertOne()` and `insertMany()` in MongoDB.**
   - `insertOne()` inserts a single document into a collection, 
   - while `insertMany()` inserts multiple documents at once. 
   - `insertMany()` is generally more efficient for batch inserts, as it reduces the number of calls to the database.

#### Q2. **How would you update multiple documents at once in MongoDB?**
   - To update multiple documents, you use the `updateMany()` method. For example:
     ```javascript
     db.collection.updateMany({ age: { $gte: 30 } }, { $inc: { age: 1 } });
     ```
     This command increments the `age` field by 1 for all documents where `age` is 30 or more.

#### Q3. **What is the purpose of the Aggregation Framework in MongoDB?**
   - The Aggregation Framework is used to perform complex data processing and transformation operations on collections. 
   - It allows you to filter, group, sort, and project data in stages using pipelines, which is efficient for operations like reporting, analysis, and data restructuring.

#### Q4. **How does `find()` differ from `findOne()`?**
   - `find()` returns a cursor to all documents that match a query, allowing for iterative access to multiple results. 
   - In contrast, `findOne()` returns only the first document that matches the query criteria.

#### Q5. **Can you explain the `$match` and `$group` stages in an aggregation pipeline?**
   - **Answer**: 
     - **$match**: Filters documents based on specified conditions, similar to the `find()` method. Only documents that meet the criteria move to the next pipeline stage.
     - **$group**: Groups documents by a specified key and performs operations like `sum`, `average`, `count`, etc., on grouped data.