
```js
console.log("A");

setTimeout(() => {
  console.log("B");
}, 0);

console.log("C");

setTimeout(() => {
  console.log("D");
}, 0);

console.log("E");

/*=>
A
C
E
B
D

*/
```


```js

function asyncOperation(msg, delay, callback) {
  setTimeout(() => {
    console.log(msg);
    callback();
  }, delay);
}

console.log("Start");

asyncOperation("Step 1", 1000, () => {
  asyncOperation("Step 2", 500, () => {
    asyncOperation("Step 3", 200, () => {
      console.log("Done");
    });
  });
});

console.log("End");


/*
Start
End
Step 1
Step 2
Step 3
Done

*/
```



Here are some **hard coding interview questions** focused on **callback functions**. Each question is accompanied by **crisp code** and expected **output**.

### **1. Implement `map` Function Using Callback**

**Question**: Write a custom `map` function that mimics the built-in `Array.prototype.map` method using callbacks.

#### **Code**:

```javascript
function customMap(arr, callback) {
  let result = [];
  for (let i = 0; i < arr.length; i++) {
    result.push(callback(arr[i], i, arr));
  }
  return result;
}

const arr = [1, 2, 3, 4];
const doubled = customMap(arr, (item) => item * 2);
console.log(doubled);
```

#### **Output**:

```
[2, 4, 6, 8]
```

---

### **2. Implement `setTimeout` Without Using `setTimeout`**

**Question**: Write a function that simulates `setTimeout` behavior using callbacks.

#### **Code**:

```javascript
function customSetTimeout(callback, delay) {
  const start = Date.now();
  function check() {
    if (Date.now() - start >= delay) {
      callback();
    } else {
      requestAnimationFrame(check);
    }
  }
  requestAnimationFrame(check);
}

customSetTimeout(() => {
  console.log("Executed after 2 seconds");
}, 2000);
```

#### **Output** (after 2 seconds):

```
Executed after 2 seconds
```

---

### **3. Implement `filter` Function Using Callback**

**Question**: Write a custom `filter` function that mimics the built-in `Array.prototype.filter` method using callbacks.

#### **Code**:

```javascript
function customFilter(arr, callback) {
  let result = [];
  for (let i = 0; i < arr.length; i++) {
    if (callback(arr[i], i, arr)) {
      result.push(arr[i]);
    }
  }
  return result;
}

const arr = [1, 2, 3, 4, 5];
const evenNumbers = customFilter(arr, (item) => item % 2 === 0);
console.log(evenNumbers);
```

#### **Output**:

```
[2, 4]
```

---

### **4. Chaining Multiple Asynchronous Operations**

**Question**: Given multiple asynchronous operations using `setTimeout`, chain them in the correct order using callbacks.

#### **Code**:

```javascript
function first(callback) {
  setTimeout(() => {
    console.log("First operation");
    callback();
  }, 1000);
}

function second(callback) {
  setTimeout(() => {
    console.log("Second operation");
    callback();
  }, 500);
}

function third(callback) {
  setTimeout(() => {
    console.log("Third operation");
    callback();
  }, 300);
}

first(() => {
  second(() => {
    third(() => {
      console.log("All operations completed");
    });
  });
});
```

#### **Output** (in sequence):

```
First operation
Second operation
Third operation
All operations completed
```

---

### **5. Debouncing Function with Callback**

**Question**: Implement a debounce function that ensures the provided callback is only called after a specified time period has passed without any new invocations.

#### **Code**:

```javascript
function debounce(callback, delay) {
  let timer;
  return function(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => {
      callback(...args);
    }, delay);
  };
}

const debouncedLog = debounce(() => {
  console.log("Debounced function executed");
}, 1000);

debouncedLog();
debouncedLog();
debouncedLog();  // Only one log will occur after 1 second
```

#### **Output** (after 1 second):

```
Debounced function executed
```

---

### **6. Asynchronous Data Fetching with Callback (Simulating API call)**

**Question**: Simulate an API call that uses a callback function to return the result after a delay.

#### **Code**:

```javascript
function fetchData(callback) {
  setTimeout(() => {
    const data = { name: "John Doe", age: 30 };
    callback(data);
  }, 1500);
}

fetchData((data) => {
  console.log(`Name: ${data.name}, Age: ${data.age}`);
});
```

#### **Output** (after 1.5 seconds):

```
Name: John Doe, Age: 30
```

---

### **7. Recursive Callback Example**

**Question**: Write a recursive function using a callback to sum up all numbers in an array.

#### **Code**:

```javascript
function sumArray(arr, callback, index = 0, sum = 0) {
  if (index === arr.length) {
    callback(sum);
    return;
  }
  sum += arr[index];
  sumArray(arr, callback, index + 1, sum);
}

sumArray([1, 2, 3, 4], (result) => {
  console.log("Total sum:", result);
});
```

#### **Output**:

```
Total sum: 10
```

---

### **8. Error Handling in Callback**

**Question**: Write a function that simulates a process where the callback is called with an error if something goes wrong.

#### **Code**:

```javascript
function processData(callback) {
  const error = false;  // Set to true to simulate error
  if (error) {
    callback("Error occurred", null);
  } else {
    callback(null, "Data processed successfully");
  }
}

processData((err, result) => {
  if (err) {
    console.log(err);
  } else {
    console.log(result);
  }
});
```

#### **Output**:

```
Data processed successfully
```

---

These questions focus on **callbacks** and cover a range of concepts such as **asynchronous programming**, **error handling**, **recursive callbacks**, **debouncing**, and more, making them useful for interviews.


