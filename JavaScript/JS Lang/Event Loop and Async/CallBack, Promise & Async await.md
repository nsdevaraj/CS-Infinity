



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

promise .. reject , resolve.. then ladder with catch and finally
async, await -> async give promise, await resolve unwrap it .. with try catch.. 
}