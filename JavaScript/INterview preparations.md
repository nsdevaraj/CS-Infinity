
Here are **20 advanced JavaScript (JS) and TypeScript (TS) coding questions** that are commonly asked in interviews for senior software engineers. These cover topics like advanced ES6+ features, functional programming, asynchronous behavior, TypeScript-specific concepts, and more.

---

### **1. Explain the difference between `==` and `===` in JavaScript.**

#### **Answer:**

- `==` compares two values for equality after converting both values to a common type (type coercion).
    - Example: `'5' == 5` is `true`.
- `===` compares two values for equality without type conversion (strict equality).
    - Example: `'5' === 5` is `false`.

Here are some popular hands-on interview questions related to `==` and `===` in JavaScript, along with their answers:

---

### **1. What will be the output of the following code?**

```javascript
console.log(0 == false);
console.log(0 === false);
```

**Answer:**

- `0 == false`: `true` because `==` performs type coercion, and `false` is converted to `0`.
- `0 === false`: `false` because `===` checks for strict equality without type coercion (different types: `number` vs `boolean`).

---

### **2. Compare the following and explain the result:**

```javascript
console.log('' == false);
console.log('' === false);
```

**Answer:**

- `'' == false`: `true` because `==` converts both operands to a common type. Here, `''` is falsy, and `false` is coerced to `0` during comparison.
- `'' === false`: `false` because the types differ (`string` vs `boolean`).

---

### **3. What does the following code output and why?**

```javascript
console.log(null == undefined);
console.log(null === undefined);
```

**Answer:**

- `null == undefined`: `true` because `==` treats `null` and `undefined` as equal in loose equality.
- `null === undefined`: `false` because the types differ (`null` vs `undefined`).

---

### **4. Predict the output:**

```javascript
console.log([1, 2] == "1,2");
console.log([1, 2] === "1,2");
```

**Answer:**

- `[1, 2] == "1,2"`: `true` because `==` coerces the array to a string (`"1,2"`) before comparison.
- `[1, 2] === "1,2"`: `false` because the types differ (`object` vs `string`).

---

### **5. What will this code output?**

```javascript
console.log('true' == true);
console.log('true' === true);
```

**Answer:**

- `'true' == true`: `false` because type coercion converts `true` to `1`, but `'true'` is not converted to a number.
- `'true' === true`: `false` because the types differ (`string` vs `boolean`).

---

### **6. Explain the result of this comparison:**

```javascript
console.log([] == false);
console.log([] === false);
```

**Answer:**

- `[] == false`: `true` because `[]` is coerced to an empty string (`''`), and `'' == false` is `true` (both are falsy values).
- `[] === false`: `false` because the types differ (`object` vs `boolean`).

---

### **7. Determine the result:**

```javascript
console.log(' \t\r\n' == 0);
console.log(' \t\r\n' === 0);
```

**Answer:**

- `' \t\r\n' == 0`: `true` because the string is coerced to `0` (whitespace strings are converted to `0` in loose equality).
- `' \t\r\n' === 0`: `false` because the types differ (`string` vs `number`).

---

### **8. Is the comparison true or false? Explain:**

```javascript
console.log(false == '0');
console.log(false === '0');
```

**Answer:**

- `false == '0'`: `true` because `false` is coerced to `0`, and `'0'` is coerced to `0`.
- `false === '0'`: `false` because the types differ (`boolean` vs `string`).

---

### **9. Analyze this comparison:**

```javascript
console.log(42 == '42');
console.log(42 === '42');
```

**Answer:**

- `42 == '42'`: `true` because `==` coerces `'42'` to a number before comparison.
- `42 === '42'`: `false` because the types differ (`number` vs `string`).

---

### **10. What is the output of the following code?**

```javascript
console.log(NaN == NaN);
console.log(NaN === NaN);
```

**Answer:**

- `NaN == NaN`: `false` because `NaN` is not equal to anything, including itself, even with `==`.
- `NaN === NaN`: `false` for the same reason.

---

These questions cover various nuances of `==` and `===` in JavaScript, commonly tested in interviews to assess understanding of type coercion and strict equality.

---

### **2. How would you implement a debounce function?**

#### **Answer:**

```javascript
function debounce(func, delay) {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func(...args), delay);
  };
}
// Usage:
const log = debounce(() => console.log('Hello'), 300);
log(); // Call multiple times; logs only once after 300ms.
```


  

```js

const debounce = (callBackFun, delay) => {

	let timeOutId;
	
	return (...args) => {
		console.log(args)
		clearTimeout(timeOutId)
		timeOutId = setTimeout(()=> callBackFun(...args), delay)
	
	}

}

const log = debounce((name) => console.log(`Hello ${name}`), 300);

log('Jeeva');
log('Saravanan');

  

/*
[ 'Jeeva' ]
[ 'Saravanan' ]
Hello Saravanan
*/

```

---

### **3. What is the difference between `var`, `let`, and `const`?**

#### **Answer:**

- `var`: Function-scoped, can be redeclared, hoisted.
- `let`: Block-scoped, cannot be redeclared in the same scope, not hoisted.
- `const`: Block-scoped, must be initialized, immutable references (value may still be mutable).



Here are popular interview-style questions with code examples on the differences between `var`, `let`, and `const`:

---

### **1. What will the following code output? Explain why.**

```javascript
console.log(a); 
var a = 5;
console.log(a);
```

**Answer:**

- `console.log(a)`: Outputs `undefined` because `var` is hoisted to the top of its scope but not initialized.
- `console.log(a)`: Outputs `5` because `a` has now been assigned a value.

---

### **2. Predict the output:**

```javascript
console.log(b); 
let b = 10;
console.log(b);
```

**Answer:**

- `console.log(b)`: Throws a `ReferenceError` because `let` is not hoisted in the same way as `var`. It's in a "temporal dead zone" until the declaration is encountered.

---

### **3. Can you reassign or redeclare variables declared with `var`, `let`, or `const`?**

```javascript
var x = 1;
var x = 2; // valid

let y = 1;
let y = 2; // Error: Identifier 'y' has already been declared

const z = 1;
z = 2; // Error: Assignment to constant variable
```

**Answer:**

- `var`: Can be redeclared and reassigned.
- `let`: Cannot be redeclared in the same scope but can be reassigned.
- `const`: Cannot be reassigned or redeclared.

---

### **4. What will be the output of this code?**

```javascript
function test() {
  if (true) {
    var x = 1;
    let y = 2;
    const z = 3;
  }
  console.log(x);
  console.log(y);
  console.log(z);
}
test();
```

**Answer:**

- `console.log(x)`: Outputs `1` because `var` is function-scoped.
- `console.log(y)`: Throws a `ReferenceError` because `let` is block-scoped.
- `console.log(z)`: Throws a `ReferenceError` because `const` is block-scoped.

---

### **5. Is the following code valid? If not, why?**

```javascript
const arr = [1, 2, 3];
arr.push(4); 
console.log(arr);
arr = [5, 6, 7];
```

**Answer:**

- `arr.push(4)`: Valid. The contents of the array can be modified because `const` prevents reassigning the reference, not the value.
- `arr = [5, 6, 7]`: Throws a `TypeError` because `const` variables cannot be reassigned.

---

### **6. Explain the output:**

```javascript
var x = 10;
if (true) {
  var x = 20;
}
console.log(x);
```

**Answer:**

- Outputs `20` because `var` is function-scoped, and redeclaring `x` inside the `if` block affects the `x` outside.

---

### **7. How does `let` behave differently than `var` in loops?**

```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 1000);
}

for (let j = 0; j < 3; j++) {
  setTimeout(() => console.log(j), 1000);
}
```

**Answer:**

- `var`: Prints `3` three times because `var` is function-scoped and the same `i` is shared across all iterations.
- `let`: Prints `0`, `1`, and `2` because `let` is block-scoped, creating a new `j` for each iteration.

---

### **8. What will this code output?**

```javascript
let a = 5;
{
  let a = 10;
  console.log(a);
}
console.log(a);
```

**Answer:**

- `console.log(a)` inside the block: Outputs `10` because `let` is block-scoped and a new `a` is declared in the block.
- `console.log(a)` outside the block: Outputs `5` because the outer `a` is unaffected.

---

### **9. Why does this code throw an error?**

```javascript
console.log(x);
let x = 100;
```

**Answer:**

- Throws a `ReferenceError` because `x` is in the "temporal dead zone" and cannot be accessed before its declaration when using `let`.

---

### **10. Explain the behavior of `const` in this code:**

```javascript
const obj = { name: 'Jeeva' };
obj.age = 25;
console.log(obj);
obj = { city: 'Chennai' };
```

**Answer:**

- `obj.age = 25`: Valid because the contents of an object declared with `const` can be modified.
- `obj = { city: 'Chennai' }`: Throws a `TypeError` because `const` prevents reassigning the reference.

---

These questions test the nuances of `var`, `let`, and `const` in JavaScript, showcasing their differences in scoping, hoisting, reassignment, and block-level behavior.


---

### **4. Write a function to flatten a deeply nested array.**

#### **Answer:**

```javascript
function flattenArray(arr) {
  return arr.reduce((acc, val) => 
    Array.isArray(val) ? acc.concat(flattenArray(val)) : acc.concat(val), []);
}
// Example:
flattenArray([1, [2, [3, 4]], 5]); // [1, 2, 3, 4, 5]
```


```js
function flattenArray(arr, depth = 1) {
  return arr.reduce((acc, val) => {
    if (Array.isArray(val) && depth > 0) {
      return acc.concat(flattenArray(val, depth - 1)); // Recursive call reducing depth
    } else {
      return acc.concat(val);
    }
  }, []);
}

// Example:
console.log(flattenArray([1, [2, [3, [4, 5]]], 6], 1)); // [1, 2, [3, [4, 5]], 6]
console.log(flattenArray([1, [2, [3, [4, 5]]], 6], 2)); // [1, 2, 3, [4, 5], 6]
console.log(flattenArray([1, [2, [3, [4, 5]]], 6], Infinity)); // [1, 2, 3, 4, 5, 6]

```


---

### **5. How do you ensure TypeScript type safety when fetching data from an API?**

#### **Answer:**

```typescript
type User = {
  id: number;
  name: string;
  email: string;
};

async function fetchUserData(url: string): Promise<User> {
  const response = await fetch(url);
  const data: unknown = await response.json();
  if (isUser(data)) return data;
  throw new Error("Invalid data format");
}

function isUser(data: any): data is User {
  return typeof data.id === 'number' && typeof data.name === 'string' && typeof data.email === 'string';
}
```

---

### **6. What are the differences between `apply`, `call`, and `bind`?**

#### **Answer:**

- `call`: Invokes a function with a specific `this` value and arguments passed one by one.
- `apply`: Invokes a function with a specific `this` value and arguments passed as an array.
- `bind`: Returns a new function with a specific `this` value.

```javascript
function greet(greeting) {
  return `${greeting}, ${this.name}`;
}
const user = { name: 'Alice' };
console.log(greet.call(user, 'Hello')); // "Hello, Alice"
console.log(greet.apply(user, ['Hi'])); // "Hi, Alice"
const boundGreet = greet.bind(user);
console.log(boundGreet('Hey')); // "Hey, Alice"
```


### Popular Interview Questions on `apply`, `call`, and `bind`

---

### **1. What is the difference between `call` and `apply`?**

**Answer:**

- `call`: Pass arguments individually.
- `apply`: Pass arguments as an array.

```javascript
function sum(a, b) {
  return a + b;
}
console.log(sum.call(null, 1, 2)); // 3
console.log(sum.apply(null, [1, 2])); // 3
```

---

### **2. Can you create a custom implementation of `bind`?**

**Answer:**

```javascript
Function.prototype.myBind = function (context, ...args) {
  const fn = this;
  return function (...newArgs) {
    return fn.apply(context, [...args, ...newArgs]);
  };
};

// Example
function greet(greeting, ending) {
  return `${greeting}, ${this.name} ${ending}`;
}
const user = { name: 'Jeeva' };
const boundGreet = greet.myBind(user, 'Hello');
console.log(boundGreet('!')); // "Hello, Jeeva !"
```

---

### **3. What will this code output?**

```javascript
const obj = {
  name: 'John',
  greet: function () {
    console.log(`Hello, ${this.name}`);
  },
};
const newObj = { name: 'Jane' };
obj.greet.call(newObj);
```

**Answer:**

- Outputs: `Hello, Jane` because `call` changes the context (`this`) to `newObj`.

---

### **4. How can `apply` be used for array manipulation?**

**Answer:** Use `apply` to pass array elements as arguments:

```javascript
const numbers = [1, 2, 3, 4, 5];
const max = Math.max.apply(null, numbers); // 5
console.log(max);
```

---

### **5. What happens when `bind` is used multiple times?**

**Answer:**

- Each call to `bind` creates a new bound function with a fixed `this` value.
- Subsequent bindings won't override the previous one.

```javascript
function show() {
  return this.name;
}
const user1 = { name: 'Alice' };
const user2 = { name: 'Bob' };

const boundShow = show.bind(user1);
const doubleBoundShow = boundShow.bind(user2);

console.log(boundShow()); // "Alice"
console.log(doubleBoundShow()); // "Alice"
```

---

### **6. What will this code output?**

```javascript
const person = {
  name: 'Eve',
  greet: function (msg) {
    return `${msg}, ${this.name}`;
  },
};
const fn = person.greet;
console.log(fn('Hi'));
console.log(fn.call(person, 'Hi'));
console.log(fn.bind(person)('Hi'));
```

**Answer:**

1. `fn('Hi')`: `Hi, undefined` because `this` defaults to `undefined` (strict mode).
2. `fn.call(person, 'Hi')`: `Hi, Eve` because `call` sets `this` to `person`.
3. `fn.bind(person)('Hi')`: `Hi, Eve` because `bind` creates a new function with `this` bound to `person`.

---

### **7. Can you borrow methods from other objects using `call`?**

**Answer:** Yes, `call` can borrow methods:

```javascript
const obj = { name: 'Sam' };
function greet() {
  return `Hello, ${this.name}`;
}
console.log(greet.call(obj)); // "Hello, Sam"
```

---

### **8. Can you combine `bind` with `setTimeout`?**

**Answer:**

```javascript
const obj = { name: 'Tom' };
function sayHi() {
  console.log(`Hi, ${this.name}`);
}
setTimeout(sayHi.bind(obj), 1000); // "Hi, Tom"
```

---

### **9. Explain the output of this code:**

```javascript
const obj = { value: 5 };
function printValue(addition) {
  return this.value + addition;
}
const boundFunc = printValue.bind(obj, 10);
console.log(boundFunc()); 
```

**Answer:**

- Outputs: `15` because `bind` fixes `this` to `obj` and sets the first argument (`addition`) to `10`.

---

### **10. How can `apply` be used to invoke a constructor?**

**Answer:**

```javascript
function Person(name, age) {
  this.name = name;
  this.age = age;
}
const details = ['Alice', 25];
const person = {};
Person.apply(person, details);
console.log(person); // { name: 'Alice', age: 25 }
```

---

These questions cover practical use cases and nuances of `apply`, `call`, and `bind`, often explored in interviews to evaluate JavaScript skills.



---



### Function Prototypes Polyfills: Popular Q&A

---

---

### Promise Polyfills: Popular Q&A

---

---

---


---

---


---

### **18. Explain the concept of `event loop` in JavaScript.**

#### **Answer:**

The **event loop** processes asynchronous callbacks in JavaScript. It consists of:

1. **Call stack**: Executes synchronous code.
2. **Task queue**: Handles `setTimeout`, I/O, etc.
3. **Microtask queue**: Handles promises, `process.nextTick`.

---

---


---

---

### **27. Write a function to implement an LRU Cache.**

#### **Answer:**

```javascript
class LRUCache {
  constructor(capacity) {
    this.capacity = capacity;
    this.cache = new Map();
  }

  get(key) {
    if (!this.cache.has(key)) return -1;
    const value = this.cache.get(key);
    this.cache.delete(key);
    this.cache.set(key, value);
    return value;
  }

  put(key, value) {
    if (this.cache.has(key)) this.cache.delete(key);
    this.cache.set(key, value);
    if (this.cache.size > this.capacity) this.cache.delete(this.cache.keys().next().value);
  }
}
// Usage:
const cache = new LRUCache(2);
cache.put(1, 1);
cache.put(2, 2);
cache.get(1); // 1
cache.put(3, 3); // Evicts key 2
```

---

### **28. Explain how you’d handle dynamic imports in JavaScript.**

#### **Answer:**

```javascript
async function loadModule() {
  const { default: module } = await import('./module.js');
  module();
}
// Usage:
loadModule();
```

---

### **29. How do you detect and handle prototype pollution?**

#### **Answer:**

- Avoid assigning user input to objects like `Object.prototype` or `Array.prototype`.
- Use libraries like `lodash` with safeguards against prototype pollution.
- Example:

```javascript
const safeObject = Object.create(null);
```

---

### **30. Write a debounce function with TypeScript types.**

#### **Answer:**

```typescript
function debounce<T extends (...args: any[]) => void>(func: T, delay: number): T {
  let timeoutId: NodeJS.Timeout;
  return ((...args: Parameters<T>) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func(...args), delay);
  }) as T;
}
```

---

### **31. How do you prevent memory leaks in event listeners?**

#### **Answer:**

- Use `removeEventListener` in cleanup functions (e.g., React `useEffect` cleanup).
- Use `WeakMap` or `WeakSet` for weak references.

---

### **32. How do you handle circular dependencies in TypeScript?**

#### **Answer:**

- Use interfaces or `type` aliases for decoupling.
- Split modules to avoid circular imports.

---

---

### **34. Write a throttle function in JavaScript.**

#### **Answer:**

```javascript
function throttle(func, limit) {
  let inThrottle;
  return (...args) => {
    if (!inThrottle) {
      func(...args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}
// Usage:
const throttledFunc = throttle(() => console.log('Throttled'), 1000);
```

---

---

---

---


---

---

---



---

### **42. What is the difference between `setTimeout` and `setImmediate`?**

#### **Answer:**

- `setTimeout`: Executes a function after a specified delay.
- `setImmediate`: Executes a function after the current event loop cycle (Node.js-specific).

```javascript
setTimeout(() => console.log('timeout'), 0);
setImmediate(() => console.log('immediate'));
```

---

### **43. How do you implement a basic event emitter in JavaScript?**

#### **Answer:**

```javascript
class EventEmitter {
  constructor() {
    this.events = {};
  }

  on(event, listener) {
    if (!this.events[event]) this.events[event] = [];
    this.events[event].push(listener);
  }

  emit(event, ...args) {
    if (this.events[event]) this.events[event].forEach(listener => listener(...args));
  }
}
// Usage:
const emitter = new EventEmitter();
emitter.on('data', data => console.log(data));
emitter.emit('data', 'Hello World');
```


---

### **52. How do you implement a throttling function in TypeScript?**

#### **Answer:**

```typescript
function throttle<T extends (...args: any[]) => void>(func: T, limit: number): T {
  let lastFunc: NodeJS.Timeout;
  let lastTime: number = 0;
  return ((...args: Parameters<T>) => {
    const now = Date.now();
    if (now - lastTime >= limit) {
      func(...args);
      lastTime = now;
    }
  }) as T;
}
```

---

