

### 10. **Error Handling and Debugging**
   - **Error Types**: Understand the difference between operational errors and programmer errors.
   - **Logging**: Familiarize yourself with logging frameworks like Winston or Morgan.
   - **Debugging Tools**: Learn to debug with built-in tools like `console.log`, the `debug` module, and using `node --inspect` for in-depth debugging.

   - **Common Questions:**
     - How do you handle exceptions in Node.js?
     - What are some best practices for logging in a production Node.js application?



### 9. **Error Handling**
   - **Explanation**: Error handling in Node.js is crucial for building robust applications. Errors can occur due to invalid input, network issues, or other unexpected conditions.
   - **Key Points**:
     - Common error-handling patterns include try/catch blocks for synchronous code and `.catch` methods or `try/catch` with async/await for asynchronous code.
     - Using callbacks or error-first patterns in Node.js can help manage errors effectively.

   **Interview Question**: *How do you handle errors in async functions in Node.js?*
   - **Example Answer**:
     ```javascript
     async function fetchData() {
       try {
         const data = await someAsyncOperation();
         console.log(data);
       } catch (error) {
         console.error('Error:', error);
       }
     }
     ```
     In this example, `try/catch` handles errors in async/await syntax. If `someAsyncOperation` throws an error, it’s caught in the `catch` block, allowing us to handle it gracefully.

---

### Exceptions handing

* for sync code - use try/catch block
* for async code - use callback func or Promises with catch.. 



