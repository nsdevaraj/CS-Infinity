
[Promises Intro @WebDevSimplified](https://www.youtube.com/watch?v=DHvZLI7Db8E)



### What is a Promise?

A **Promise** in JavaScript is an `object that represents the eventual completion (or failure) of an asynchronous operation and its resulting value`. Promises allow you to write asynchronous code in a more manageable and readable way compared to traditional callback functions.

A **Promise** is a `wrapper for a value that is unknown right now but will resolve in the future`, such as a response from an API call. 

Promises help handle asynchronous operations like API requests, file I/O, or timers, making the code more readable, especially when compared to callbacks.

#### States of a Promise:
1. **Pending**: The initial state, neither fulfilled nor rejected.
2. **Fulfilled**: The operation completed successfully, resulting in a resolved value.
3. **Rejected**: The operation failed, resulting in a reason for the failure (an error).

#### Basic Syntax:
```javascript

let myPromise = new Promise((resolve, reject) => {
    // Asynchronous operation
    if (/* success condition */) {
        resolve("Success value"); // Resolve the promise with a value
    } else {
        reject("Error occurred"); // Reject the promise with an error
    }
});

// Consuming the promise
myPromise
    .then(result => {
        console.log("Success:", result);  // Handles resolved promise
    })
    .catch(error => {
        console.error("Error:", error);  // Handles rejected promise
    })
    .finally(() => {
        console.log("Finally block executed");  // Always runs regardless of success or failure
    });

```


### Applications of Promises

1. **Asynchronous Operations**:
   - Promises are primarily used for handling asynchronous tasks such as API calls, file reading, or any operation that might take time to complete.
   ```javascript
   fetch('https://api.example.com/data')
       .then(response => response.json())
       .then(data => console.log(data))
       .catch(error => console.error('Error:', error));
   ```

2. **Chaining Promises**:
   - Promises can be chained to perform a series of asynchronous operations in sequence. Each `then` returns a new promise, allowing further chaining.
   ```javascript
   fetchData()
       .then(processData)
       .then(displayData)
       .catch(handleError);
   ```

3. **Error Handling**:
   - Promises provide a structured way to handle errors in asynchronous operations through the `catch` method, improving code readability and maintainability.
   ```javascript
   fetchData()
       .then(data => process(data))
       .catch(error => console.error('Error:', error));
   ```

4. **Parallel Execution**:
   - Promises can be used with `Promise.all` to execute multiple asynchronous operations in parallel and handle their results collectively.
   ```javascript
   Promise.all([fetchData1(), fetchData2()])
       .then(([data1, data2]) => {
           console.log('Both data received:', data1, data2);
       })
       .catch(error => console.error('Error in one of the promises:', error));
   ```

5. **Async/Await Syntax**:
   - Promises are the foundation of the `async/await` syntax, which provides a more synchronous-looking way to write asynchronous code, enhancing readability.
   ```javascript
   async function fetchData() {
       try {
           const response = await fetch('https://api.example.com/data');
           const data = await response.json();
           console.log(data);
       } catch (error) {
           console.error('Error:', error);
       }
   }
   ```



Promise code:


### Code 1:

```js
Promise.resolve().then(() => {  
    console.log('resolve');  
});
```

1. **Behavior**:
    
    - `Promise.resolve()` creates a resolved promise immediately.
    - The `.then()` method schedules its callback to run in the **microtask queue** after the current execution context finishes.
2. **Execution**:
    
    - The callback (`console.log('resolve')`) is executed **asynchronously** after the current synchronous code finishes.

---

### Code 2:

```js
const promise1 = new Promise((resolve, reject) => {  
    console.log('resolve');  
});
promise1.then(res => {  
    console.log(res);  
});
```

1. **Behavior**:
    
    - `new Promise()` runs the executor function **immediately**. In this case, it executes the `console.log('resolve')` synchronously.
    - However, the promise is **pending** because `resolve` (or `reject`) is not called.
    - The `.then()` callback is registered but **never executes** because the promise remains in the pending state.
2. **Execution**:
    
    - `console.log('resolve')` runs **synchronously**.
    - The `.then()` callback is never executed because the promise is never resolved.

---

### Key Differences:

|Feature|**Code 1**|**Code 2**|
|---|---|---|
|**Promise Creation**|`Promise.resolve()` creates an already-resolved promise.|`new Promise()` creates a pending promise.|
|**Executor Execution**|No custom executor function runs.|Executor runs immediately.|
|**Resolution**|Promise is resolved immediately.|Promise remains pending (no `resolve()` called).|
|**Then Callback Execution**|Callback in `.then()` is executed as a **microtask**.|Callback in `.then()` is never executed.|
|**Synchronous Logging**|Only `resolve` inside `.then()` is logged asynchronously.|`resolve` inside the executor is logged synchronously.|

---

### Execution Comparison:

#### Code 1:

```js
Promise.resolve().then(() => {  
    console.log('resolve');  
});
console.log('end');
```

**Output**:

```
end
resolve
```

- `Promise.resolve().then(...)` schedules `console.log('resolve')` in the **microtask queue**, which runs after the synchronous code (`console.log('end')`).

---

#### Code 2:

```js
const promise1 = new Promise((resolve, reject) => {  
    console.log('resolve');  
});
promise1.then(res => {  
    console.log(res);  
});
console.log('end');
```

**Output**:

```
resolve
end
```

- `console.log('resolve')` runs **synchronously** inside the executor.
- The `.then()` callback does not run because `resolve()` is never called, so the promise stays in the **pending** state.

---

### Summary:

1. **Code 1** demonstrates the resolution of a promise and the use of the microtask queue to defer the `.then()` callback.
2. **Code 2** shows a pending promise with an executor function that runs synchronously but does not resolve, so the `.then()` callback is never executed.

This difference highlights how promises are either immediately resolved/rejected or stay pending until explicitly resolved/rejected.



to check {

https://www.youtube.com/watch?v=1l4wHWQCCIc

}



### Then in promises

In JavaScript, `.then()` is typically used with **Promises** to handle asynchronous operations, especially when chaining multiple asynchronous tasks. It allows us to specify what should happen once the Promise resolves (success) or rejects (error). Below are common real-time examples where `.then()` is used in callbacks:

### **1. Fetching Data from an API (Using `.then()` with Promises)**

When making asynchronous requests to a server (e.g., fetching weather data), `.then()` is used to handle the resolved response (success) or handle errors.

```javascript
console.log("Fetching weather data...");

function getWeather(city) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const weatherData = { city: city, temperature: 25, condition: "Sunny" };
      resolve(weatherData); // Resolves the Promise with data
    }, 2000);
  });
}

getWeather("London")
  .then(data => {
    console.log(`Weather in ${data.city}: ${data.temperature}°C, ${data.condition}`);
  })
  .catch(error => {
    console.log("Error:", error); // Catching any error
  });
```

### **2. Reading Files Asynchronously (Node.js)**

In Node.js, `.then()` can be used to handle the result of asynchronous file operations, often seen in combination with `fs.promises` API.

```javascript
const fs = require('fs').promises;

fs.readFile('file.txt', 'utf8')
  .then(data => {
    console.log("File content:", data); // Handle successful file read
  })
  .catch(error => {
    console.log("Error reading file:", error); // Handle error
  });
```

### **3. Chaining Multiple Asynchronous Operations**

When you have multiple asynchronous tasks (e.g., multiple API calls), you can chain `.then()` to ensure that each operation occurs after the previous one completes.

```javascript
function fetchUserData(userId) {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve({ id: userId, name: "Alice" });
    }, 1000);
  });
}

function fetchUserPosts(userId) {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve([{ id: 1, content: "Hello World" }, { id: 2, content: "JavaScript is awesome" }]);
    }, 1500);
  });
}

fetchUserData(1)
  .then(user => {
    console.log("User:", user);
    return fetchUserPosts(user.id); // Chain the next promise
  })
  .then(posts => {
    console.log("Posts:", posts);
  })
  .catch(error => {
    console.log("Error:", error);
  });
```

### **4. Handling Timeouts and Delays with `.then()`**

You can use `.then()` with a `setTimeout`-like function to handle asynchronous tasks after a delay.

```javascript
function delay(ms) {
  return new Promise(resolve => {
    setTimeout(resolve, ms);
  });
}

delay(2000)
  .then(() => {
    console.log("Executed after 2 seconds");
  })
  .catch(error => {
    console.log("Error:", error);
  });
```

### **5. Using `.then()` with Fetch API (Network Request)**

The Fetch API returns a **Promise**, which you can handle using `.then()` to process the response data.

```javascript
fetch('https://jsonplaceholder.typicode.com/posts')
  .then(response => response.json())  // Converts the response to JSON
  .then(data => {
    console.log("Fetched posts:", data);
  })
  .catch(error => {
    console.log("Error fetching posts:", error);
  });
```

### **Summary of Use Cases for `.then()` in Callbacks**:

- **API calls**: Handle responses from APIs (e.g., `fetch`).
- **File reading**: Handle asynchronous file operations in Node.js.
- **Chaining multiple asynchronous tasks**: Sequential tasks after each promise resolves.
- **Handling delays**: Use in combination with `setTimeout` or `delay`.
- **Error handling**: Handle errors at any point in the promise chain using `.catch()`.

The `.then()` method is a powerful way to handle asynchronous operations and callbacks in a more readable and maintainable way, avoiding callback hell and providing better control over asynchronous workflows.





### **Chaining Promises**

Promises can be chained using `.then()`. This allows for sequential asynchronous operations, making the code more manageable.

```javascript
const promise1 = new Promise((resolve) => resolve(10));

promise1
  .then((result) => {
    console.log(result);  // 10
    return result * 2;
  })
  .then((result) => {
    console.log(result);  // 20
    return result + 5;
  })
  .then((result) => {
    console.log(result);  // 25
  })
  .catch((error) => {
    console.error("Error:", error);
  });
```

### **Promise.all()**

`Promise.all()` allows you to run multiple promises in parallel and handle their results once all promises have resolved. It returns a single promise that resolves when all the input promises are resolved, or rejects if any of the input promises rejects.

```javascript
const promise1 = new Promise((resolve) => resolve("First"));
const promise2 = new Promise((resolve) => resolve("Second"));
const promise3 = new Promise((resolve) => resolve("Third"));

Promise.all([promise1, promise2, promise3])
  .then((results) => {
    console.log(results);  // ["First", "Second", "Third"]
  })
  .catch((error) => {
    console.log(error);  // Error handling
  });
```

### **Promise.race()**

`Promise.race()` returns a promise that resolves as soon as one of the input promises resolves or rejects. It doesn't wait for all promises to complete, just the first one.

```javascript
const promise1 = new Promise((resolve) => setTimeout(resolve, 1000, "First"));
const promise2 = new Promise((resolve) => setTimeout(resolve, 500, "Second"));

Promise.race([promise1, promise2])
  .then((result) => {
    console.log(result);  // "Second" (since it resolves first)
  });
```

### **Promise.resolve() & Promise.reject()**

- **`Promise.resolve()`** creates a resolved promise with a given value.
- **`Promise.reject()`** creates a rejected promise with a given reason.

```javascript
const resolvedPromise = Promise.resolve("Resolved");
resolvedPromise.then((result) => console.log(result));  // "Resolved"

const rejectedPromise = Promise.reject("Rejected");
rejectedPromise.catch((error) => console.log(error));  // "Rejected"
```

### **Handling Errors with Promises**

Errors in promises can be handled with `.catch()`, which is equivalent to `try/catch` in synchronous code. If any promise in a chain fails, the `.catch()` block catches the error.

```javascript
const faultyPromise = new Promise((_, reject) => reject("An error occurred"));

faultyPromise
  .then(() => {
    console.log("This won't run");
  })
  .catch((error) => {
    console.log(error);  // "An error occurred"
  });
```

### **Async/Await: Syntactic Sugar for Promises**

`async/await` is syntactic sugar over promises, providing a cleaner and more readable way to handle asynchronous code. The `async` keyword is used before a function, and the `await` keyword is used to pause the execution of the function until the promise is resolved.

#### **Example**:

```javascript
async function fetchData() {
  const data = await Promise.resolve("Data fetched");
  console.log(data);  // "Data fetched"
}

fetchData();
```

### **Advantages of Promises**:

1. **Avoid Callback Hell**: Promises offer better structure than nested callbacks, avoiding "callback hell."
2. **Error Handling**: Easier error propagation using `.catch()`.
3. **Chaining**: Promises can be chained for better flow and readability.
4. **Parallel Execution**: Methods like `Promise.all()` allow multiple promises to run in parallel, improving performance.

### **Disadvantages**:

1. **Complexity with Nested Promises**: Though promises avoid callback hell, they can still become difficult to manage when nesting several promises.
2. **Error Propagation**: If not handled properly, errors can still propagate unexpectedly, especially in chained promises.



.then.then => callback ladder... 

