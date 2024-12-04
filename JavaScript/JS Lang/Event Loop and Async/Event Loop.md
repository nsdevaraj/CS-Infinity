

[EventLoop @LydiaHallie](https://youtu.be/eiC58R16hb8?si=UmxYQViF1uXlgNMB)


### Synchronous vs. Asynchronous Functions

**Synchronous Functions**:
- These functions execute sequentially, blocking the execution of the code until the current function completes. The next line of code will not run until the synchronous function has finished.
- Execute line-by-line; block further execution until complete.
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


	// => Start, End, This run after syncFunction

  ```




**Asynchronous Functions**:
- **Definition**: These functions allow other code to run while they execute in the background. They do not block the main thread, enabling non-blocking behavior.
-  Execute tasks in the background without blocking the main thread.
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
	// => Start, This runs before End, End
  ```



### The Event Loop


In JavaScript, code execution is typically **synchronous**—executed line by line.

The event loop is a mechanism that enables JavaScript to perform non-blocking I/O operations, despite being single-threaded. 

 The **Event Loop** allows JavaScript to perform asynchronous operations, letting the main application continue running while waiting for some tasks to complete.

It allows asynchronous operations to be executed after the main thread has completed its current task.

- The event loop allows asynchronous execution using a separate thread pool.
- This enables multitasking on modern websites with a single main thread.


**How It Works**:
1. **Call Stack**: This is where the JavaScript engine keeps track of function calls. When a function is invoked, it gets added to the stack, and when it returns, it gets removed.
  
2. **Web APIs**: When an asynchronous function (like `setTimeout`, AJAX requests, etc.) is called, it is handled by the browser's Web APIs. Once the operation completes, it sends a callback function to the **callback queue** i.e task queue.

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



### **Event Loop Components**

1. **Call Stack**: Executes synchronous code.
2. **Web APIs**: Handle async operations (e.g., `setTimeout`, `fetch`).
3. **Task Queue**: Holds macrotasks (e.g., `setTimeout` callbacks).
4. **Microtask Queue**: Holds microtasks (e.g., `Promise.then` callbacks).
5. **Event Loop**: Transfers tasks from queues to the call stack once it’s empty.

---

### **Microtasks vs Macrotasks**

### **Macro Task Queue**

- Includes callbacks from:
    - `setTimeout`
    - `setInterval`
    - `setImmediate` (Node.js)
    - DOM events (e.g., `click`, `load`)
    - I/O operations
- Lower priority than microtasks.
- Handled after all microtasks in the current cycle are completed.

---

### **Micro Task Queue**

- Includes:
    - Callbacks from `Promise.then` or `catch`
    - `MutationObserver`
    - `queueMicrotask`
- Higher priority than macro tasks.
- Executed immediately after the current stack finishes but before any macro tasks.



---

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


---
#### Example: Using `setTimeout`

The `setTimeout` function demonstrates how asynchronous code works. It accepts a callback function that gets executed after a specified delay.

```javascript
console.log("Start");

setTimeout(() => {
    console.log("Timeout executed");
}, 2000); // Executes after 2 seconds

console.log("End");
```

**Output:**
```
Start
End
Timeout executed
```


---


### The Event Loop - Interview Preparation Topics

1. **Definition and Purpose**
   - Understand what the event loop is and its role in JavaScript's concurrency model.
   - Recognize how it enables non-blocking I/O operations.

2. **Execution Context**
   - Explain the call stack and how it relates to the event loop.
   - Distinguish between synchronous and asynchronous execution.

3. **Web APIs**
   - Describe how web APIs (like `setTimeout`, `fetch`, etc.) interact with the event loop.
   - Understand how callbacks are scheduled in the event loop.

4. **Task Queue vs. Microtask Queue**
   - Differentiate between the task queue (for callbacks) and the microtask queue (for promises).
   - Explain the priority of microtasks over tasks in the event loop.

5. **Event Loop Phases**
   - Break down the phases of the event loop: 
     - **Microtask Queue**: Process microtasks first (promises, mutation observer).
     - **Task Queue**: Process macrotasks (setTimeout, setInterval).
   - Illustrate how the event loop continuously cycles through these phases.

6. **Common Patterns and Examples**
   - Provide code snippets that demonstrate how the event loop works, including:
     - Nested callbacks (callback hell).
     - Using Promises and `async/await`.
     - Set intervals and timeouts.

7. **Implications on Performance**
   - Discuss how the event loop affects performance and responsiveness in web applications.
   - Address potential pitfalls, such as long-running synchronous code blocking the event loop.

8. **Debugging Tools**
   - Identify tools available for analyzing the event loop and asynchronous operations (e.g., Chrome DevTools).
   - Understand how to use the Performance tab to investigate bottlenecks.

9. **Best Practices**
   - Discuss best practices for managing asynchronous code to maintain performance and readability (e.g., avoiding callback hell, using `async/await`).

10. **Real-World Applications**
    - Explain scenarios where the event loop is critical, such as handling user interactions in web applications or server requests in Node.js.







reffered {

https://www.explainthis.io/en/swe/js-event-loop-questions


}



---

### **Execution Example**

```js
console.log("Start");

setTimeout(() => console.log("Timeout"), 0);

Promise.resolve().then(() => console.log("Promise"));

console.log("End");
```

**Output**:  
`Start` → `End` → `Promise` → `Timeout`.

---

### **Advanced Example**

```js
console.log("Start");

setTimeout(() => {
  console.log("Timeout 1");
  Promise.resolve().then(() => console.log("Microtask 1"));
}, 0);

Promise.resolve().then(() => {
  console.log("Microtask 2");
});

console.log("End");
```

**Output**:  
`Start` → `End` → `Microtask 2` → `Timeout 1` → `Microtask 1`.

---
