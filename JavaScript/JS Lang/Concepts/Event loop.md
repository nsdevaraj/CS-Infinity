

## Async , Sync and Event loop
### Synchronous vs. Asynchronous Functions

**Synchronous Functions**:
- **Definition**: These functions execute sequentially, blocking the execution of the code until the current function completes. The next line of code will not run until the synchronous function has finished.
- **Example**:
  ```javascript
  function syncFunction() {
      console.log("Start");
      // Simulate a time-consuming task
      for (let i = 0; i < 1e9; i++) {}
      console.log("End");
  }
  syncFunction();
  console.log("This runs after syncFunction.");
  ```
- **Behavior**: In this example, "This runs after syncFunction." will only execute after "End" is logged.

**Asynchronous Functions**:
- **Definition**: These functions allow other code to run while they execute in the background. They do not block the main thread, enabling non-blocking behavior.
- **Example**:
  ```javascript
  function asyncFunction() {
      console.log("Start");
      setTimeout(() => {
          console.log("End");
      }, 1000);
  }
  asyncFunction();
  console.log("This runs before End.");
  ```
- **Behavior**: In this case, "This runs before End." will be logged before "End" because `setTimeout` allows the rest of the code to continue executing.

### The Event Loop

**Definition**: The event loop is a mechanism that enables JavaScript to perform non-blocking I/O operations, despite being single-threaded. It allows asynchronous operations to be executed after the main thread has completed its current task.

**How It Works**:
1. **Call Stack**: This is where the JavaScript engine keeps track of function calls. When a function is invoked, it gets added to the stack, and when it returns, it gets removed.
  
2. **Web APIs**: When an asynchronous function (like `setTimeout`, AJAX requests, etc.) is called, it is handled by the browser's Web APIs. Once the operation completes, it sends a callback function to the **callback queue**.

3. **Callback Queue**: This queue holds all the callback functions that are ready to be executed after the current stack is clear.

4. **Event Loop**: The event loop continuously checks the call stack and the callback queue:
   - If the call stack is empty, it takes the first function from the callback queue and pushes it onto the call stack for execution.

**Visualization**:

```
Call Stack
    |
    |  (executes sync functions)
    V
Event Loop <-- checks if the Call Stack is empty
    |
    |  (moves callbacks from Callback Queue)
    V
Callback Queue
```

### Example of Event Loop in Action

```javascript
console.log("Start");

setTimeout(() => {
    console.log("Timeout");
}, 0);

Promise.resolve().then(() => {
    console.log("Promise resolved");
});

console.log("End");
```

**Execution Order**:
1. "Start" is logged.
2. The `setTimeout` callback is scheduled in the callback queue.
3. The `Promise` resolves and its `.then()` callback is also scheduled.
4. "End" is logged.
5. After the main stack is empty, the event loop checks the callback queue:
   - "Promise resolved" is logged first (microtasks have priority).
   - "Timeout" is logged next.

### Conclusion

Understanding synchronous and asynchronous functions, along with the event loop, is crucial for writing efficient and responsive JavaScript applications. Synchronous functions block execution, while asynchronous functions allow for non-blocking behavior, enabling smoother user experiences. The event loop coordinates the execution of these asynchronous operations, ensuring that JavaScript can handle multiple tasks effectively despite its single-threaded nature.