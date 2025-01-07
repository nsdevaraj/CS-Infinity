

[EventLoop @LydiaHallie](https://youtu.be/eiC58R16hb8?si=UmxYQViF1uXlgNMB)


### The Event Loop



In JavaScript, code execution is typically **synchronous**—executed line by line.

The event loop is a `mechanism that enables JavaScript to perform non-blocking operations, despite being single-threaded` 

Different operations:
- **I/O operations** (e.g., reading files, network requests).
- **Timers** (e.g., `setTimeout`, `setInterval`).
- **User interactions** (e.g., click events, DOM updates).
- **Promises/microtasks** (e.g., `then`, `async/await`).



The **event loop** is a mechanism that continuously processes and coordinates tasks from the call stack and task queues to ensure non-blocking execution in JavaScript.


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


The **event loop** is a mechanism in JavaScript that:

1. Continuously checks if the **call stack** is empty.
2. If empty, it picks tasks from the **task queues** (like microtask and macro task queues) and moves them to the **call stack** for execution.

### Flow:

1. Execute **synchronous code** first (fills and clears the call stack).
2. Handle **microtasks** (e.g., Promises) next.
3. Then process **macro tasks** (e.g., `setTimeout`, I/O callbacks).

### Key:

- Ensures **non-blocking execution** by coordinating tasks between the **main thread**, **queues**, and **Web APIs**.


### **Event Loop Components**

1. **Call Stack**: Executes synchronous code.
2. **Web APIs**: Handle async operations (e.g., `setTimeout`, `fetch`).
3. **Task Queue**: Holds macrotasks (e.g., `setTimeout` callbacks).
4. **Microtask Queue**: Holds microtasks (e.g., `Promise.then` callbacks).
5. **Event Loop**: Transfers tasks from queues to the call stack once it’s empty.


![[Pasted image 20241206080924.png]]


---

### Tasks

**Tasks** in JavaScript are `units of work queued by the runtime to be executed by the event loop`, categorized as **macrotasks** (e.g., `setTimeout`) and **microtasks** (e.g., Promises).


### **Microtasks vs Macrotasks**


| **Aspect**           | **Microtasks**                                                                                                                                                    | **Macrotasks**                                                                                                                    |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Priority**         | Higher (executed before macrotasks).                                                                                                                              | Lower (executed after microtasks).                                                                                                |
| **Execution Timing** | After the current synchronous code finishes but before the next macrotask. i.e  Executed immediately after the current stack finishes but before any macro tasks. | After all microtasks in the queue are completed. i.e Handled after all microtasks in the current cycle are completed.             |
| **Queue**            | Microtask queue.                                                                                                                                                  | Macrotask queue.                                                                                                                  |
| **Examples**         | - Promises (`.then`, `.catch`, `.finally`) - `MutationObserver` - `queueMicrotask`                                                                                | - Timers `setTimeout`, `setInterval` - I/O operations - DOM UI events (e.g., clicks, rendering) - SetImmeditate (nodejs specific) |
| **Processing Order** | Entire queue processed before macrotasks.                                                                                                                         | FIFO: One task processed per event loop cycle.                                                                                    |
|                      |                                                                                                                                                                   |                                                                                                                                   |

Both **macrotasks** and **microtasks** are handled by the **JavaScript runtime** (e.g., the V8 engine in browsers or Node.js). However:

- **Macrotasks** are typically queued and executed after interacting with **Web APIs** (e.g., `setTimeout`, network requests).
- **Microtasks** are managed by the **JavaScript engine itself**, specifically in the **microtask queue** after the current synchronous code finishes, and they include tasks like **Promise** callbacks.



### Code Example


Simple:

```javascript

console.log('Start')

setTimeout(()=> {
  console.log('Macrotask - setTimeout')
}, 0)

Promise.resolve().then(()=> console.log('Microtask - Promise resolved'))

console.log('End')


/*=> 
Start
End
Microtask - Promise resolved
Macrotask - setTimeout
*/
```


**Execution Order**:
1. "Start" is logged.
2. The `setTimeout` callback is scheduled in the callback queue.
3. The `Promise` resolves and its `.then()` callback is also scheduled.
4. "End" is logged.
5. After the main stack is empty, the event loop checks the callback queue:
   - "Promise resolved" is logged first (microtasks have priority).
   - "Timeout" is logged next.


Advanced:


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

### Flow Explanation:

1. **Synchronous code execution**:
    
    - `console.log("Start")` → Prints **Start**.
    - `console.log("End")` → Prints **End**.
2. **Microtasks**:
    
    - `Promise.resolve().then(...)` is added to the **microtask queue**.
    - **Microtask 2** (`console.log("Microtask 2")`) is executed before macrotasks, so it prints **Microtask 2**.
3. **Macrotasks**:
    
    - `setTimeout()` is added to the **macrotask queue**.
    - Once the microtasks are finished, the event loop processes the **macrotask**.
    - `setTimeout()` callback runs and prints **setTimeout**.
    - Inside the `setTimeout()` callback, another **microtask** (`Promise.resolve().then()`) is queued and then processed.
    - **Microtask 1** (`console.log("Microtask 1")`) prints **Microtask 1**.


---







reffered {

https://www.explainthis.io/en/swe/js-event-loop-questions


}

to check {

https://www.linkedin.com/posts/alina-kulish_event-loop-ugcPost-7281074451302019074-de1s?utm_source=share&utm_medium=member_desktop


}



---

