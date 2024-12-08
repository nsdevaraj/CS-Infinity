
### **1. What will this code output?**

```javascript
const obj = {
  name: 'Alice',
  greet: function () {
    const sayHello = () => console.log(this.name);
    sayHello();
  },
};
obj.greet();
```

**Answer:**  
`Alice`  
**Explanation:** Arrow functions inherit `this` from their lexical scope. Here, `sayHello` is defined within `greet`, and `this` inside `greet` refers to `obj`.

---

### **2. What will this code output?**

```javascript
const obj = {
  name: 'Alice',
  greet() {
    function sayHello() {
      console.log(this.name);
    }
    sayHello();
  },
};
obj.greet();
```

**Answer:**  
`undefined` (or error in strict mode)  
**Explanation:** `sayHello` is a regular function, and `this` in regular functions defaults to the global object (`window` or `undefined` in strict mode).

**Fix:** Use `bind`, `call`, or an arrow function:

```javascript
const obj = {
  name: 'Alice',
  greet() {
    const sayHello = () => console.log(this.name); // Arrow function
    sayHello();
  },
};
obj.greet(); // Alice
```

---

### **3. Explain the output.**

```javascript
const obj1 = {
  name: 'Alice',
  greet() {
    console.log(this.name);
  },
};
const obj2 = { name: 'Bob' };
const greet = obj1.greet;
greet();
```

**Answer:**  
`undefined` (or error in strict mode)  
**Explanation:** The method `greet` is assigned to a variable and called as a regular function. `this` loses its reference to `obj1` and defaults to the global object.

**Fix:** Use `bind`:

```javascript
const boundGreet = obj1.greet.bind(obj1);
boundGreet(); // Alice
```

---

### **4. What is the output?**

```javascript
const obj = {
  count: 0,
  increment() {
    function step() {
      this.count++;
    }
    step();
  },
};
obj.increment();
console.log(obj.count);
```

**Answer:**  
`TypeError: Cannot read property 'count' of undefined` (or NaN in non-strict mode)  
**Explanation:** `step` is a regular function, so `this` does not refer to `obj`.

**Fix:** Use an arrow function or `bind`:

```javascript
increment() {
  const step = () => {
    this.count++;
  };
  step();
}
```

---

### **5. What's the difference between `call`, `apply`, and `bind`?**

- **`call`**: Invokes a function immediately with a specified `this` and arguments.
- **`apply`**: Same as `call`, but arguments are passed as an array.
- **`bind`**: Returns a new function with `this` permanently bound.

**Example:**

```javascript
function showName(age, city) {
  console.log(`${this.name}, ${age}, ${city}`);
}
const obj = { name: 'Alice' };
showName.call(obj, 25, 'NY'); // Alice, 25, NY
showName.apply(obj, [25, 'NY']); // Alice, 25, NY
const boundShow = showName.bind(obj);
boundShow(25, 'NY'); // Alice, 25, NY
```

---

### **6. Predict the output.**

```javascript
const obj = {
  name: 'Alice',
  greet: () => console.log(this.name),
};
obj.greet();
```

**Answer:**  
`undefined`  
**Explanation:** Arrow functions do not bind `this`; they inherit it from the enclosing lexical context. Here, the context is the global scope.

---

### **7. How does `this` work with event listeners?**

```javascript
const button = document.querySelector('button');
button.addEventListener('click', function () {
  console.log(this);
});
```

**Answer:**  
Logs the button element.  
**Explanation:** In regular functions, `this` refers to the element that triggered the event.

For arrow functions:

```javascript
button.addEventListener('click', () => {
  console.log(this);
});
// Logs the surrounding context, typically the global object or undefined in strict mode.
```

---

### **8. Tricky Binding Example**

```javascript
const obj = {
  name: 'Alice',
  greet() {
    console.log(this.name);
    const nested = function () {
      console.log(this.name);
    };
    nested.call(this); // Explicit binding
  },
};
obj.greet();
```

**Answer:**  
`Alice`  
`Alice`  
**Explanation:** The first `this.name` refers to `obj`. For the `nested` function, `.call(this)` ensures `this` remains bound to `obj`.

---

![[Pasted image 20241208130427.png]]



---

### **Interview Tip:**

- Practice nested scenarios involving multiple contexts of `this`.
- Know how to debug and explain issues related to loss of `this`.
- Be prepared to explain `this` in classes, promises, and event handling contexts.
