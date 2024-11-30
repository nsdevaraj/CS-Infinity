
Refered {

https://youtu.be/m9yjaTG1-Gg?si=MEdf_WplubY2BH7V

}

### Understanding Node.js Event Loop with Examples

The Node.js event loop is a mechanism that handles asynchronous operations and ensures non-blocking execution. Let's break this down with examples and comments for better understanding:

---

### **JavaScript Basics**

JavaScript is:

1. **Single-threaded**: Executes one task at a time.
2. **Blocking**: A task must complete before moving to the next.
3. **Synchronous by default**: Executes code line by line.

```javascript
// Synchronous Execution
function taskA() {
  console.log("Task A");
}

function taskB() {
  console.log("Task B");
}

taskA();
taskB(); // Output: Task A -> Task B
```

Blocking example:

```javascript
function longTask() {
  const start = Date.now();
  while (Date.now() - start < 5000); // 5-second block
  console.log("Long Task Completed");
}

function shortTask() {
  console.log("Short Task");
}

longTask();
shortTask(); // Output: Long Task Completed -> Short Task (shortTask waits)
```

---

### **Asynchronous Operations**

Node.js uses **libuv** to handle asynchronous tasks like file I/O, timers, and HTTP requests.

#### Example with Callbacks

```javascript
const fs = require("fs");

console.log("Start");

fs.readFile("example.txt", "utf8", (err, data) => {
  if (err) throw err;
  console.log("File Read Complete");
});

console.log("End");

// Output:
// Start
// End
// File Read Complete
```

Here:

1. `console.log("Start")` and `console.log("End")` are synchronous.
2. `fs.readFile` is asynchronous and handled by libuv.

---

### **Event Loop Phases**

The Node.js event loop has several phases:

1. **Timers**: Executes `setTimeout` and `setInterval` callbacks.
2. **Pending Callbacks**: Executes I/O callbacks deferred by timers.
3. **Idle/Prepare**: Internal operations.
4. **Poll**: Fetches new I/O events.
5. **Check**: Executes `setImmediate` callbacks.
6. **Close Callbacks**: Handles close events like `socket.on('close')`.

#### Example of Execution Order

```javascript
setTimeout(() => console.log("Timeout"), 0);
setImmediate(() => console.log("Immediate"));

console.log("Start");

// Output (may vary):
// Start
// Immediate
// Timeout
```

- `setImmediate` often executes before `setTimeout` as it directly queues in the "Check" phase, skipping the "Poll" phase.

---

### **Microtasks**

Microtasks like **Promises** and `process.nextTick` have the highest priority and execute before moving to the next phase.

```javascript
setTimeout(() => console.log("Timeout"), 0);
Promise.resolve().then(() => console.log("Promise"));
process.nextTick(() => console.log("Next Tick"));

console.log("Start");

// Output:
// Start
// Next Tick
// Promise
// Timeout
```

Order of execution:

1. Synchronous code (`Start`).
2. Microtasks (`process.nextTick`, `Promise`).
3. Timers (`setTimeout`).

---

### **Practical Example**

A real-world scenario combining various phases:

```javascript
setTimeout(() => console.log("Timer Phase"), 0);
setImmediate(() => console.log("Check Phase"));

fs.readFile("example.txt", "utf8", () => {
  console.log("Poll Phase");

  setTimeout(() => console.log("Timer Phase (nested)"), 0);
  setImmediate(() => console.log("Check Phase (nested)"));
});

process.nextTick(() => console.log("Next Tick"));
Promise.resolve().then(() => console.log("Promise"));

console.log("Start");

// Expected Output:
// Start
// Next Tick
// Promise
// Timer Phase
// Check Phase
// Poll Phase
// Timer Phase (nested)
// Check Phase (nested)
```

---

### **Key Takeaways**

1. **Synchronous Tasks**: Run first.
2. **Microtasks**: Execute before moving to the next event loop phase.
3. **Timers**: Executed in the Timer phase after Microtasks.
4. **I/O Operations**: Handled in the Poll phase.
5. **SetImmediate**: Executed in the Check phase.
6. **Callbacks**: Only executed when the Call Stack is empty.

Understanding these concepts is crucial to effectively writing non-blocking, performant Node.js applications.



![[Pasted image 20241128051926.png]]


