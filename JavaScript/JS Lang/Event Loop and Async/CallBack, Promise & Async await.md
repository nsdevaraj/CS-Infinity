


## 2. Callback Functions

### Key Points
- Callback functions are executed later in the event loop.
- Overuse of callbacks can lead to "callback hell".

### Code Example
Example of nested callbacks:

```javascript
getData((data) => {
    processData(data, (processed) => {
        saveData(processed, (result) => {
            console.log("Data saved:", result);
        });
    });
});
```

### Explanation
- This code shows how deeply nested callbacks can lead to less readable code, known as "callback hell".


### 3. Callbacks and Callback Hell

While callback functions are common, excessive nesting can lead to **callback hell**, making code hard to read and maintain.

```javascript
// Callback Hell Example
getData((data) => {
    processData(data, (processedData) => {
        saveData(processedData, (result) => {
            console.log("Data saved:", result);
        });
    });
});
```

---

### 4. Promises

A **Promise** is a wrapper for a value that is unknown right now but will resolve in the future, such as a response from an API call. 

#### Creating and Using Promises

```javascript
const fetchData = new Promise((resolve, reject) => {
    const success = true; // Change to false to simulate an error
    if (success) {
        resolve("Data fetched successfully!");
    } else {
        reject("Error fetching data.");
    }
});

fetchData
    .then(result => console.log(result))
    .catch(error => console.error(error));
```


.then.then => callback ladder... 


---

### 5. Async/Await

You can define an `async` function that automatically returns a promise. Inside, you can use the `await` keyword to pause execution until the promise resolves.



### **35. Explain how `async` and `await` work in JavaScript.**

#### **Answer:**

- **`async`**: Declares a function that returns a `Promise`.
- **`await`**: Pauses the execution of an `async` function until the `Promise` is resolved or rejected.



#### Example of Async/Await

```javascript
const getData = async () => {
    try {
        const data = await fetchData; // Waiting for the promise to resolve
        console.log(data);
    } catch (error) {
        console.error(error);
    }
};

getData();
```



## 3. Promises

### Key Points
- A promise is a wrapper for a value that will be available in the future.
- It can resolve (success) or reject (error).
- Promises provide methods like `.then()` and `.catch()` for handling outcomes.

### Code Example
Using promises:

```javascript
const fetchData = () => {
    return new Promise((resolve, reject) => {
        // Simulate a successful API call
        setTimeout(() => {
            resolve("Data fetched successfully!");
        }, 1000);
    });
};

fetchData()
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
```

### Explanation
- This code simulates an asynchronous operation with a promise that resolves after 1 second.

---

## 4. Async/Await

### Key Points
- Async functions return a promise and allow use of `await` to pause execution until a promise resolves.
- Error handling can be done with try/catch blocks.

### Code Example
Using async/await:

```javascript
const fetchDataAsync = async () => {
    try {
        const data = await fetchData();
        console.log(data);
    } catch (error) {
        console.error("Error:", error);
    }
};

fetchDataAsync();
```

### Explanation
- This function fetches data asynchronously and handles errors using a try/catch block, improving readability.



{
to check:
callback then.. 
promise .. reject , resolve.. then ladder with catch and finally
async, await -> async give promise, await resolve unwrap it .. with try catch.. 
}