


5. **Async/Await**
   - `async` and `await` are `syntactic sugar built on top of promises, providing a more readable way to handle asynchronous code`
   ```javascript
   async function fetchDataAsync() {
       const data = await fetchDataPromise; // Waits for the promise to resolve
       console.log(data); // Output: Data received
   }

   fetchDataAsync();
   ```




### **In-Depth Guide to `async/await` in JavaScript**

`async/await` is a modern syntax in JavaScript (introduced in ES2017/ES8) for writing asynchronous code. It simplifies working with promises by allowing developers to write asynchronous code that looks synchronous.

---

### **What Are `async` and `await`?**

1. **`async` Function**:
    
    - Declares a function as asynchronous.
    - It implicitly returns a `Promise`.
    - Any value returned by the `async` function is automatically wrapped in a resolved promise.
    
    ```javascript
    async function example() {
      return 'Hello';
    }
    
    example().then(console.log); // Output: "Hello"
    ```
    
2. **`await` Keyword**:
    
    - Can only be used inside an `async` function.
    - Pauses the execution of the `async` function until the promise is resolved or rejected.
    - Makes asynchronous code appear synchronous.
    
    ```javascript
    async function example() {
      const result = await Promise.resolve('Hello');
      console.log(result); // Output: "Hello"
    }
    
    example();
    ```
    

---

### **How It Works**

The `async/await` syntax works on top of promises and leverages the **event loop** for asynchronous execution. Here’s the flow:

1. `async` functions return a promise.
2. `await` pauses the function execution until the awaited promise resolves or rejects.
3. The rest of the function continues execution after the `await`.

---

### **Examples**

#### 1. Fetching Data with `async/await`

```javascript
async function fetchData() {
  const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
  const data = await response.json();
  console.log(data);
}

fetchData();
// Output: { userId: 1, id: 1, title: '...', completed: false }
```


In the provided code, the two `await` statements are necessary because they handle two **different asynchronous operations**:

### **1. `await fetch(...)`**

The `fetch` function is used to send an HTTP request to the specified URL. This operation is asynchronous because it involves network communication, and it returns a `Promise`.

Using `await` here ensures that the code waits for the promise returned by `fetch` to resolve, which happens when the HTTP response is received. The resolved value is a `Response` object containing details of the HTTP response.

```javascript
const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
```

---

### **2. `await response.json()`**

The `response.json()` method reads the body of the HTTP response and parses it as JSON. This is also an asynchronous operation because parsing the body (especially for large payloads) is a non-blocking task.

Using `await` here ensures the code waits for the promise returned by `response.json()` to resolve, which happens when the parsing is complete. The resolved value is the actual JSON data.

```javascript
const data = await response.json();
```

---

### **Why Can't We Use a Single `await`?**

Each `await` is tied to a distinct asynchronous operation:

1. The first `await` ensures the HTTP response is received.
2. The second `await` ensures the response body is fully read and parsed.

If you skip the second `await`, you would get a `Promise` instead of the parsed JSON data.

---

### **Alternative Example Without `await`**

Here’s how the same code would look with `.then()` instead of `await`:

```javascript
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then((response) => response.json())
  .then((data) => console.log(data));
```

This chaining shows that each step (`fetch` and `response.json()`) is a separate asynchronous operation.

---

### **Summary**

The two `await` statements handle:

1. **Fetching the HTTP response** (network operation).
2. **Parsing the response body as JSON** (processing the response).

Each is asynchronous and requires its own `await` to ensure sequential execution.


---

#### 2. Handling Errors with `try...catch`

Errors in `async` functions can be caught using `try...catch`.

```javascript
async function fetchDataWithError() {
  try {
    const response = await fetch('https://invalid-url');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

fetchDataWithError();
// Output: "Error: Failed to fetch"
```

---

#### 3. Sequential Execution

Using `await`, you can ensure tasks execute in sequence.

```javascript
const task = (id, time) =>
  new Promise((resolve) => setTimeout(() => resolve(`Task ${id}`), time));

async function runTasks() {
  const task1 = await task(1, 1000);
  console.log(task1);

  const task2 = await task(2, 500);
  console.log(task2);

  const task3 = await task(3, 300);
  console.log(task3);
}

runTasks();
// Output:
// Task 1
// Task 2
// Task 3
```

---

#### 4. Parallel Execution with `Promise.all`

For independent tasks, you can run them concurrently using `Promise.all`.

```javascript
const task = (id, time) =>
  new Promise((resolve) => setTimeout(() => resolve(`Task ${id}`), time));

async function runTasksParallel() {
  const results = await Promise.all([
    task(1, 1000),
    task(2, 500),
    task(3, 300),
  ]);
  console.log(results);
}

runTasksParallel();
// Output: [ 'Task 1', 'Task 2', 'Task 3' ]
```

---

### **Key Points to Remember**

1. **Synchronous-Looking Code**:
    
    - `await` makes asynchronous code appear synchronous, improving readability.
2. **Error Handling**:
    
    - Always use `try...catch` or `.catch()` to handle errors in `async` functions.
3. **Sequential vs. Parallel**:
    
    - Use `await` for sequential execution.
    - Use `Promise.all` for parallel execution.
4. **Rules**:
    
    - `await` can only be used inside `async` functions.
    - If `await` is used on a non-promise value, it resolves immediately.

---

### **Benefits of `async/await`**

- Improves code readability by avoiding `.then()` chaining.
- Easier debugging since stack traces are more straightforward.
- Works seamlessly with existing `Promise`-based APIs.

---

### **Comparison: `async/await` vs. Promises**

|Feature|Promises|`async/await`|
|---|---|---|
|Syntax Complexity|Chained `.then()` callbacks|Synchronous-like|
|Readability|Harder for nested promises|Clean and easy to follow|
|Error Handling|`.catch()`|`try...catch`|
|Execution Flow|Explicit chaining|Sequential, natural flow|

---

### **Conclusion**

`async/await` simplifies asynchronous programming in JavaScript. It’s built on promises, making code easier to write, read, and debug. Use it for handling asynchronous tasks like API calls, file operations, or any non-blocking task.


