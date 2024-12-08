

Got it! Here are some popular **vanilla JavaScript** interview questions, along with concise answers focusing on **core JavaScript concepts**:

---

### **1. What is the difference between `null` and `undefined`?**

**Answer:**

- `undefined` means a variable has been declared but has not been assigned a value.
- `null` is an assignment value representing no value or an empty object reference.

```javascript
let x; // undefined
let y = null; // explicitly no value
```

---

### **2. What are closures in JavaScript?**

**Answer:**  
A **closure** is a function that "remembers" its lexical scope, even when the function is executed outside that scope.

```javascript
function outer() {
  let counter = 0;
  return function inner() {
    counter++;
    return counter;
  };
}

const count = outer();
console.log(count()); // 1
console.log(count()); // 2
```

---

### **3. How does `this` work in JavaScript?**

**Answer:**

- In **global scope**, `this` refers to the **global object** (in a browser, it’s `window`).
- In a **function**, `this` refers to the object that **calls** the function.
- In **arrow functions**, `this` is **lexically bound** (it refers to the context in which it was created).

```javascript
function regularFunction() {
  console.log(this); // `this` refers to global object (window in browsers)
}

const obj = { name: 'Alice', greet: function() { console.log(this.name); } };
obj.greet(); // "Alice"
```

---

### **4. What is event delegation in JavaScript?**

**Answer:**  
**Event delegation** is a technique where a single event listener is added to a parent element, and it handles events for its child elements through event bubbling.

```javascript
document.querySelector('#parent').addEventListener('click', function(event) {
  if (event.target && event.target.matches('button.className')) {
    console.log('Button clicked!');
  }
});
```

---

### **5. What is the difference between `==` and `===`?**

**Answer:**

- `==` is the **loose equality** operator, which compares values after **type coercion**.
- `===` is the **strict equality** operator, which compares both **value and type** without coercion.

```javascript
console.log(5 == '5'); // true
console.log(5 === '5'); // false
```

---

### **6. What are `let`, `const`, and `var`?**

**Answer:**

- **`var`**: Function-scoped, can be re-declared and updated.
- **`let`**: Block-scoped, can be updated but not re-declared in the same scope.
- **`const`**: Block-scoped, cannot be updated or re-declared, must be initialized during declaration.

```javascript
var a = 10;
let b = 20;
const c = 30;

a = 15; // Works
b = 25; // Works
c = 35; // Error: Assignment to constant variable
```

---

### **7. What is a promise in JavaScript?**

**Answer:**  
A **promise** is an object representing the eventual completion or failure of an asynchronous operation. It can be in one of three states: pending, resolved, or rejected.

```javascript
let promise = new Promise((resolve, reject) => {
  let success = true;
  if (success) {
    resolve('Operation successful');
  } else {
    reject('Operation failed');
  }
});

promise.then(response => console.log(response)).catch(error => console.log(error));
```

---

### **8. What is the difference between `apply()`, `call()`, and `bind()`?**

**Answer:**

- `**call()**`: Immediately invokes a function with a given `this` value and arguments.
- `**apply()**`: Similar to `call()`, but takes arguments as an array.
- `**bind()**`: Returns a new function with a bound `this` value, but does not invoke it immediately.

```javascript
function greet(name) {
  console.log(this.message + ' ' + name);
}

const obj = { message: 'Hello' };
greet.call(obj, 'John'); // Hello John
greet.apply(obj, ['Jane']); // Hello Jane

const boundGreet = greet.bind(obj);
boundGreet('Doe'); // Hello Doe
```

---

### **9. What is the difference between `forEach()`, `map()`, and `filter()`?**

**Answer:**

- **`forEach()`**: Executes a function once for each element in the array, but does not return anything.
- **`map()`**: Creates a new array with the results of calling a function for every array element.
- **`filter()`**: Creates a new array with all elements that pass the test implemented by the provided function.

```javascript
const arr = [1, 2, 3, 4];

// forEach
arr.forEach(item => console.log(item));

// map
const squares = arr.map(item => item * item);

// filter
const evenNumbers = arr.filter(item => item % 2 === 0);
```

---

### **10. What is a "debounce" and "throttle"?**

**Answer:**

- **Debounce**: Limits the rate at which a function is executed, ensuring that it only runs after a delay has passed since the last invocation (useful for search input).
- **Throttle**: Ensures a function is only executed once in a specified period, no matter how many times it is triggered.

```javascript
// Debounce
function debounce(func, wait) {
  let timeout;
  return function(...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func(...args), wait);
  };
}

// Throttle
function throttle(func, wait) {
  let lastTime = 0;
  return function(...args) {
    const now = Date.now();
    if (now - lastTime >= wait) {
      func(...args);
      lastTime = now;
    }
  };
}
```

---

### **11. What is the purpose of the `new` keyword in JavaScript?**

**Answer:**  
The `new` keyword creates a new instance of an object that has a constructor function.

```javascript
function Person(name, age) {
  this.name = name;
  this.age = age;
}

const john = new Person('John', 30); // Creates a new Person object
```

---

### **12. What is the event loop in JavaScript?**

**Answer:**  
The **event loop** is a mechanism that handles asynchronous operations in JavaScript. It allows non-blocking execution by placing tasks (like callbacks, promises) in the **task queue** and executing them in the main execution thread when it's free.

---

### **13. What are template literals?**

**Answer:**  
Template literals are a feature in ES6 that allow multi-line strings and embedding expressions inside strings using `${}`.

```javascript
let name = 'Alice';
let message = `Hello, ${name}! Welcome to JavaScript.`;
console.log(message);
```

---

### **14. What are arrow functions?**

**Answer:**  
Arrow functions are a shorter syntax for writing functions. They do not have their own `this`, so they inherit `this` from the surrounding context.

```javascript
const add = (a, b) => a + b;
```

---

### **15. What is the `fetch` API?**

**Answer:**  
The `fetch` API is used to make HTTP requests and returns a **Promise** that resolves to the response of the request.

```javascript
fetch('https://api.example.com')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.log(error));
```

---

These answers cover key JavaScript concepts, and they should help you demonstrate a strong understanding of vanilla JavaScript during an interview. Let me know if you'd like more!

