

### **1. Create a polyfill for `Function.prototype.bind`.**

**Answer:**

```javascript
Function.prototype.myBind = function (context, ...args) {
  const fn = this; // The original function
  return function (...newArgs) {
    return fn.apply(context, [...args, ...newArgs]);
  };
};

// Example:
function greet(greeting) {
  return `${greeting}, ${this.name}`;
}
const user = { name: 'Alice' };
const boundGreet = greet.myBind(user, 'Hello');
console.log(boundGreet()); // "Hello, Alice"
```

---

### **2. Implement a polyfill for `Function.prototype.call`.**

**Answer:**

```javascript
Function.prototype.myCall = function (context, ...args) {
  context = context || globalThis; // Handle null/undefined context
  const fnSymbol = Symbol(); // Create a unique property on the context
  context[fnSymbol] = this; // Assign the function to the context
  const result = context[fnSymbol](...args); // Call the function
  delete context[fnSymbol]; // Clean up
  return result;
};

// Example:
function sayHi(greeting) {
  return `${greeting}, ${this.name}`;
}
const user = { name: 'Bob' };
console.log(sayHi.myCall(user, 'Hi')); // "Hi, Bob"
```

---

### **3. Implement a polyfill for `Function.prototype.apply`.**

**Answer:**

```javascript
Function.prototype.myApply = function (context, args) {
  context = context || globalThis; // Handle null/undefined context
  const fnSymbol = Symbol(); // Create a unique property
  context[fnSymbol] = this; // Assign the function
  const result = args ? context[fnSymbol](...args) : context[fnSymbol](); // Call with args
  delete context[fnSymbol]; // Clean up
  return result;
};

// Example:
function introduce(greeting, punctuation) {
  return `${greeting}, ${this.name}${punctuation}`;
}
const user = { name: 'Charlie' };
console.log(introduce.myApply(user, ['Hello', '!'])); // "Hello, Charlie!"
```


### 5. **`Function.prototype.call`**
The `call` method calls a function with a given `this` value and arguments provided individually.

**Polyfill for `call`:**
```javascript
Function.prototype.myCall = function(context = {}, ...args) {
  context.fn = this;
  const result = context.fn(...args);
  delete context.fn;
  return result;
};
```

### 6. **`Function.prototype.apply`**
The `apply` method calls a function with a given `this` value, and arguments provided as an array.

**Polyfill for `apply`:**
```javascript
Function.prototype.myApply = function(context = {}, args = []) {
  context.fn = this;
  const result = context.fn(...args);
  delete context.fn;
  return result;
};
```

### 7. **`Function.prototype.bind`**
The `bind` method creates a new function that, when called, has its `this` keyword set to the provided value, with a given sequence of arguments preceding any provided when the new function is called.

**Polyfill for `bind`:**
```javascript
Function.prototype.myBind = function(context, ...args) {
  const fn = this;
  return function(...newArgs) {
    return fn.apply(context, [...args, ...newArgs]);
  };
};
```

These polyfills mimic the behavior of the native methods while giving a solid understanding of how higher-order functions and `this` binding work in JavaScript.



