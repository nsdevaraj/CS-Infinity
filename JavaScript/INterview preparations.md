
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

### **7. How would you implement `Promise.all` manually?**

#### **Answer:**

```javascript
function promiseAll(promises) {
  return new Promise((resolve, reject) => {
    const results = [];
    let completed = 0;

    promises.forEach((p, index) => {
      Promise.resolve(p)
        .then(value => {
          results[index] = value;
          completed++;
          if (completed === promises.length) resolve(results);
        })
        .catch(reject);
    });
  });
}
```



### Function Prototypes Polyfills: Popular Q&A

---

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

---

### Promise Polyfills: Popular Q&A

---

### **1. Write a polyfill for `Promise.all`.**

**Answer:**

```javascript
Promise.myAll = function (promises) {
  return new Promise((resolve, reject) => {
    let results = [];
    let completed = 0;

    promises.forEach((promise, index) => {
      Promise.resolve(promise)
        .then((value) => {
          results[index] = value; // Store result in order
          completed++;
          if (completed === promises.length) resolve(results);
        })
        .catch(reject); // Reject immediately if any promise fails
    });
  });
};

// Example:
const p1 = Promise.resolve(1);
const p2 = Promise.resolve(2);
const p3 = Promise.resolve(3);
Promise.myAll([p1, p2, p3]).then(console.log); // [1, 2, 3]
```

---

### **2. Write a polyfill for `Promise.race`.**

**Answer:**

```javascript
Promise.myRace = function (promises) {
  return new Promise((resolve, reject) => {
    promises.forEach((promise) => {
      Promise.resolve(promise).then(resolve).catch(reject); // Resolve/reject with the first settled promise
    });
  });
};

// Example:
const p1 = new Promise((resolve) => setTimeout(resolve, 100, 'First'));
const p2 = new Promise((resolve) => setTimeout(resolve, 200, 'Second'));
Promise.myRace([p1, p2]).then(console.log); // "First"
```

---

### **3. Write a polyfill for `Promise.allSettled`.**

**Answer:**

```javascript
Promise.myAllSettled = function (promises) {
  return new Promise((resolve) => {
    let results = [];
    let completed = 0;

    promises.forEach((promise, index) => {
      Promise.resolve(promise)
        .then((value) => {
          results[index] = { status: 'fulfilled', value };
        })
        .catch((reason) => {
          results[index] = { status: 'rejected', reason };
        })
        .finally(() => {
          completed++;
          if (completed === promises.length) resolve(results);
        });
    });
  });
};

// Example:
const p1 = Promise.resolve(1);
const p2 = Promise.reject('Error');
const p3 = Promise.resolve(3);
Promise.myAllSettled([p1, p2, p3]).then(console.log);
// [
//   { status: 'fulfilled', value: 1 },
//   { status: 'rejected', reason: 'Error' },
//   { status: 'fulfilled', value: 3 }
// ]
```

---

### **4. Implement a simple `Promise` class (Polyfill for `Promise`).**

**Answer:**

```javascript
function MyPromise(executor) {
  let onResolve, onReject, isResolved = false, isRejected = false, value;

  this.then = function (callback) {
    onResolve = callback;
    if (isResolved) onResolve(value);
    return this;
  };

  this.catch = function (callback) {
    onReject = callback;
    if (isRejected) onReject(value);
    return this;
  };

  function resolve(val) {
    isResolved = true;
    value = val;
    if (onResolve) onResolve(value);
  }

  function reject(val) {
    isRejected = true;
    value = val;
    if (onReject) onReject(value);
  }

  executor(resolve, reject);
}

// Example:
const p = new MyPromise((resolve, reject) => {
  setTimeout(() => resolve('Success!'), 1000);
});
p.then(console.log); // "Success!"
```

These polyfills are commonly discussed in interviews to test understanding of JavaScript's core concepts like prototypes and promises.



---

### **8. Explain the difference between `interface` and `type` in TypeScript.**

#### **Answer:**

- **Interface**:
    - Primarily used for defining object shapes.
    - Supports inheritance via `extends`.
- **Type**:
    - More flexible; can define unions, intersections, primitives, etc.
    - Cannot be extended like interfaces.

```typescript
interface User {
  name: string;
}
type Status = 'active' | 'inactive';
```

---

### **9. How do you implement memoization in JavaScript?**

#### **Answer:**

```javascript
function memoize(func) {
  const cache = new Map();
  return (...args) => {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const result = func(...args);
    cache.set(key, result);
    return result;
  };
}
// Usage:
const factorial = memoize(n => (n <= 1 ? 1 : n * factorial(n - 1)));
console.log(factorial(5)); // 120
```

---

### **10. How do you handle circular references in JSON?**

#### **Answer:**

```javascript
function safeStringify(obj) {
  const seen = new WeakSet();
  return JSON.stringify(obj, (key, value) => {
    if (typeof value === "object" && value !== null) {
      if (seen.has(value)) return undefined;
      seen.add(value);
    }
    return value;
  });
}
```

---

### **11. What is a generator function, and how do you use it?**

#### **Answer:**

Generator functions allow you to yield multiple values.

```javascript
function* generateSequence() {
  yield 1;
  yield 2;
  yield 3;
}
const generator = generateSequence();
console.log(generator.next()); // { value: 1, done: false }
```

---

### **12. Explain the difference between `null` and `undefined`.**

#### **Answer:**

- `null`: Explicitly represents no value.
- `undefined`: Represents a variable that has been declared but not assigned.

---

### **13. How can you enforce immutability in TypeScript?**

#### **Answer:**

```typescript
type Immutable<T> = {
  readonly [K in keyof T]: Immutable<T[K]>;
};

const user: Immutable<{ name: string }> = { name: "John" };
// user.name = "Doe"; // Error: Cannot assign to 'name' because it is a read-only property.
```

---

### **14. How do you deep clone an object in JavaScript?**

#### **Answer:**

```javascript
const deepClone = obj => JSON.parse(JSON.stringify(obj));
```

---

### **15. How do you detect a memory leak in JavaScript?**

#### **Answer:**

- Use browser developer tools:
    - Monitor heap size in the performance tab.
    - Look for detached DOM elements or retained closures in the profiler.

---

### **16. Write a function to merge two sorted arrays.**

#### **Answer:**

```javascript
function mergeArrays(arr1, arr2) {
  const result = [];
  let i = 0, j = 0;

  while (i < arr1.length && j < arr2.length) {
    result.push(arr1[i] < arr2[j] ? arr1[i++] : arr2[j++]);
  }
  return result.concat(arr1.slice(i)).concat(arr2.slice(j));
}
```

---

### **17. How would you implement a deep comparison function?**

#### **Answer:**

```javascript
function deepEqual(a, b) {
  if (a === b) return true;
  if (typeof a !== 'object' || typeof b !== 'object' || a == null || b == null) return false;

  const keysA = Object.keys(a);
  const keysB = Object.keys(b);

  if (keysA.length !== keysB.length) return false;
  return keysA.every(key => deepEqual(a[key], b[key]));
}
```

---

### **18. Explain the concept of `event loop` in JavaScript.**

#### **Answer:**

The **event loop** processes asynchronous callbacks in JavaScript. It consists of:

1. **Call stack**: Executes synchronous code.
2. **Task queue**: Handles `setTimeout`, I/O, etc.
3. **Microtask queue**: Handles promises, `process.nextTick`.

---

### **19. Write a function to generate Fibonacci numbers.**

#### **Answer:**

```javascript
function* fibonacci() {
  let [a, b] = [0, 1];
  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
}
// Usage:
const fib = fibonacci();
console.log(fib.next().value); // 0
console.log(fib.next().value); // 1
```

---

### **20. How do you type-check a React component with TypeScript?**

#### **Answer:**

```typescript
import React from "react";

type Props = {
  name: string;
};

const MyComponent: React.FC<Props> = ({ name }) => <div>Hello, {name}</div>;

export default MyComponent;
```


---

### **21. How do you implement currying in JavaScript?**

#### **Answer:**

```javascript
function curry(func) {
  return function curried(...args) {
    if (args.length >= func.length) {
      return func(...args);
    } else {
      return (...nextArgs) => curried(...args, ...nextArgs);
    }
  };
}
// Usage:
const sum = (a, b, c) => a + b + c;
const curriedSum = curry(sum);
console.log(curriedSum(1)(2)(3)); // 6
```


### Popular JavaScript Currying Interview Questions with Answers

---

### **1. What is currying in JavaScript?**

**Answer:** Currying is a technique where a function with multiple arguments is transformed into a sequence of functions, each taking a single argument.

**Example:**

```javascript
function multiply(a) {
  return function (b) {
    return a * b;
  };
}
const multiplyBy2 = multiply(2);
console.log(multiplyBy2(5)); // 10
console.log(multiply(3)(4)); // 12
```

---

### **2. Implement a function that converts a normal function to a curried function.**

**Answer:**

```javascript
function curry(func) {
  return function curried(...args) {
    if (args.length >= func.length) {
      return func.apply(this, args); // Invoke the function if all arguments are supplied
    } else {
      return function (...nextArgs) {
        return curried.apply(this, args.concat(nextArgs)); // Keep collecting arguments
      };
    }
  };
}

// Example:
function sum(a, b, c) {
  return a + b + c;
}
const curriedSum = curry(sum);
console.log(curriedSum(1)(2)(3)); // 6
console.log(curriedSum(1, 2)(3)); // 6
```

---

### **3. How can currying be used to create reusable functions?**

**Answer:** Currying allows partial application of arguments, creating specialized versions of a function.

**Example:**

```javascript
function calculate(operation) {
  return function (a) {
    return function (b) {
      if (operation === 'add') return a + b;
      if (operation === 'multiply') return a * b;
    };
  };
}

const add = calculate('add');
const multiply = calculate('multiply');

console.log(add(5)(3)); // 8
console.log(multiply(5)(3)); // 15
```

---

### **4. Create a curried version of a function to filter an array.**

**Answer:**

```javascript
const filter = (criteria) => (array) => array.filter(criteria);

// Example:
const isEven = (num) => num % 2 === 0;
const filterEvens = filter(isEven);

console.log(filterEvens([1, 2, 3, 4, 5])); // [2, 4]
```

---

### **5. Write a curried function for logging with different prefixes.**

**Answer:**

```javascript
const logger = (prefix) => (message) => console.log(`${prefix}: ${message}`);

// Example:
const errorLogger = logger('Error');
const infoLogger = logger('Info');

errorLogger('Something went wrong!'); // "Error: Something went wrong!"
infoLogger('All systems operational.'); // "Info: All systems operational."
```

---

### **6. Convert a curried function back to a normal function.**

**Answer:**

```javascript
function uncurry(curried) {
  return function (...args) {
    return args.reduce((fn, arg) => fn(arg), curried);
  };
}

// Example:
const curriedSum = (a) => (b) => (c) => a + b + c;
const normalSum = uncurry(curriedSum);

console.log(normalSum(1, 2, 3)); // 6
```

---

### **7. Write a function that sums an indefinite number of arguments using currying.**

**Answer:**

```javascript
function sum(a) {
  return function (b) {
    if (b !== undefined) {
      return sum(a + b);
    }
    return a;
  };
}

// Example:
console.log(sum(1)(2)(3)()); // 6
console.log(sum(4)(5)());    // 9
```

---

### **8. Explain the difference between partial application and currying.**

**Answer:**

- **Currying**: Transforms a function into nested functions, each taking one argument at a time.
- **Partial Application**: Pre-fixes some arguments of a function, creating a new function with fewer parameters.

**Example:**

```javascript
// Currying:
const curriedAdd = (a) => (b) => a + b;
console.log(curriedAdd(1)(2)); // 3

// Partial Application:
const add = (a, b) => a + b;
const add5 = add.bind(null, 5);
console.log(add5(3)); // 8
```

---

### **9. Implement a curried function for string formatting.**

**Answer:**

```javascript
function format(prefix) {
  return function (suffix) {
    return function (message) {
      return `${prefix}${message}${suffix}`;
    };
  };
}

// Example:
const withBrackets = format('[')(']');
console.log(withBrackets('Hello')); // "[Hello]"
```

---

### **10. How can currying help in React or functional programming?**

**Answer:** Currying simplifies passing configurations or arguments incrementally.

**Example:**

```javascript
const connect = (mapState) => (mapDispatch) => (Component) => {
  // Hypothetical connect logic
  return function (props) {
    return `<Connected ${Component} />`;
  };
};

const mapStateToProps = (state) => state.user;
const mapDispatchToProps = (dispatch) => ({ login: () => dispatch('LOGIN') });

const connectedComponent = connect(mapStateToProps)(mapDispatchToProps)('MyComponent');
console.log(connectedComponent); // "<Connected MyComponent />"
```

---

These questions test foundational concepts and practical applications of currying in JavaScript, making them relevant for interviews.



#### Currying 

```js

const sum = (a,b,c) => a+b+c


const wrapCurry = (func) => {
    return function curried(...args){
        if(args.length === func.length){
            return func(...args)
        }else{
            return (...nextArgs) => curried(...args, ...nextArgs);
        }
    }
}

const wrapCurry2 = (func) => {
    return function curried(...args){
        if(args.length === func.length){
            return () => func(...args)
        }else{
            return (...nextArgs) => curried(...args, ...nextArgs);
        }
    }
}

const currySum3 = (arg1) => {
    return function (arg2) {
        if(arg2 === undefined){
            return arg1
        }else{
            return currySum3(arg1+arg2)
        }
    }
}

const unWrapCurry = (func) => {
    return function (...args) {
        return args.reduce((fn,arg)=> fn(arg), func)
    } 
}

console.log(sum(1,2,3))
const currySum = wrapCurry(sum)
console.log(currySum(1)(2)(3))

const currySum2 = wrapCurry2(sum)
console.log(currySum2(1)(2)(3)())

console.log(currySum3(1)(2)(3)())

const unWrapCurrySum = unWrapCurry(currySum)
console.log(unWrapCurrySum(1,2,3))



```


---

### **22. What is the difference between `map`, `forEach`, and `reduce`?**

#### **Answer:**

- **`map`**: Returns a new array with the result of applying a function to each element.
- **`forEach`**: Executes a function on each element but doesn’t return anything.
- **`reduce`**: Aggregates array elements into a single value.

---

### **23. How do you create a custom React hook in TypeScript?**

#### **Answer:**

```typescript
import { useState } from "react";

function useToggle(initialValue: boolean): [boolean, () => void] {
  const [value, setValue] = useState(initialValue);
  const toggle = () => setValue(!value);
  return [value, toggle];
}
// Usage:
const [isVisible, toggleVisibility] = useToggle(false);
```

---

### **24. Write a function to find the longest substring without repeating characters.**

#### **Answer:**

```javascript
function longestSubstring(s) {
  let set = new Set(), maxLen = 0, left = 0;

  for (let right = 0; right < s.length; right++) {
    while (set.has(s[right])) set.delete(s[left++]);
    set.add(s[right]);
    maxLen = Math.max(maxLen, right - left + 1);
  }

  return maxLen;
}
// Example:
console.log(longestSubstring("abcabcbb")); // 3
```

---

### **25. How would you implement a singleton in JavaScript?**

#### **Answer:**

```javascript
class Singleton {
  constructor() {
    if (Singleton.instance) return Singleton.instance;
    Singleton.instance = this;
  }
}
// Usage:
const instance1 = new Singleton();
const instance2 = new Singleton();
console.log(instance1 === instance2); // true
```

---

### **26. How can you handle optional chaining in TypeScript?**

#### **Answer:**

```typescript
type User = {
  profile?: {
    address?: {
      city: string;
    };
  };
};

const user: User = {};
const city = user.profile?.address?.city; // undefined
```

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

### **33. Write a TypeScript function that accepts a tuple and swaps its elements.**

#### **Answer:**

```typescript
function swap<T, U>(tuple: [T, U]): [U, T] {
  return [tuple[1], tuple[0]];
}
// Usage:
const result = swap([1, 'a']); // ['a', 1]
```

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

### **35. Explain how `async` and `await` work in JavaScript.**

#### **Answer:**

- **`async`**: Declares a function that returns a `Promise`.
- **`await`**: Pauses the execution of an `async` function until the `Promise` is resolved or rejected.

---

### **36. How do you implement a custom error class in TypeScript?**

#### **Answer:**

```typescript
class CustomError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "CustomError";
  }
}
```

---

### **37. How do you use Generics in TypeScript?**

#### **Answer:**

```typescript
function identity<T>(arg: T): T {
  return arg;
}
// Usage:
const output = identity<string>("Hello"); // "Hello"
```

---

### **38. Write a function to calculate the factorial of a number using recursion.**

#### **Answer:**

```javascript
function factorial(n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}
console.log(factorial(5)); // 120
```

---

### **39. Explain the use of `Proxy` in JavaScript.**

#### **Answer:**

- A `Proxy` allows you to intercept and customize operations on objects.

```javascript
const obj = { a: 1 };
const proxy = new Proxy(obj, {
  get(target, prop) {
    return prop in target ? target[prop] : 'Default';
  }
});
console.log(proxy.a); // 1
console.log(proxy.b); // "Default"
```

---

### **40. Write a TypeScript utility type to extract the return type of a function.**

#### **Answer:**

```typescript
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;
// Usage:
const example = () => 42;
type ExampleReturnType = ReturnType<typeof example>; // number
```

---

These questions explore deep JS/TS concepts, practical use cases, and performance-oriented challenges. They can test problem-solving and debugging skills, essential for senior software engineers.



Here are the **next 20 advanced JavaScript and TypeScript coding questions**, continuing with a focus on senior-level expertise, covering areas like advanced functional programming, optimization, TypeScript utilities, and real-world scenarios.

---

### **41. How would you implement a function to deeply merge two objects?**

#### **Answer:**

```javascript
function deepMerge(target, source) {
  for (const key of Object.keys(source)) {
    if (source[key] instanceof Object) {
      target[key] = deepMerge(target[key] || {}, source[key]);
    } else {
      target[key] = source[key];
    }
  }
  return target;
}
// Usage:
const obj1 = { a: { b: 1 } };
const obj2 = { a: { c: 2 } };
console.log(deepMerge(obj1, obj2)); // { a: { b: 1, c: 2 } }
```

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

### **44. How would you implement a function to shuffle an array?**

#### **Answer:**

```javascript
function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}
// Usage:
console.log(shuffleArray([1, 2, 3, 4, 5]));
```

---

### **45. Explain the difference between `Array.prototype.map` and `Array.prototype.filter`.**

#### **Answer:**

- `map`: Transforms each element of an array and returns a new array.
- `filter`: Filters elements based on a condition and returns a new array.

---

### **46. How do you type a React `useReducer` hook in TypeScript?**

#### **Answer:**

```typescript
type State = { count: number };
type Action = { type: 'increment' | 'decrement' };

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case 'increment': return { count: state.count + 1 };
    case 'decrement': return { count: state.count - 1 };
    default: return state;
  }
}
// Usage:
const [state, dispatch] = useReducer(reducer, { count: 0 });
```

---

### **47. Write a function to perform binary search on a sorted array.**

#### **Answer:**

```javascript
function binarySearch(arr, target) {
  let left = 0, right = arr.length - 1;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (arr[mid] === target) return mid;
    if (arr[mid] < target) left = mid + 1;
    else right = mid - 1;
  }
  return -1;
}
// Usage:
console.log(binarySearch([1, 2, 3, 4, 5], 3)); // 2
```

---

### **48. How can you define a generic interface in TypeScript?**

#### **Answer:**

```typescript
interface ApiResponse<T> {
  data: T;
  status: number;
}

const response: ApiResponse<string> = { data: "Hello", status: 200 };
```

---

### **49. Write a function to check if two binary trees are identical.**

#### **Answer:**

```javascript
function areIdenticalTrees(tree1, tree2) {
  if (!tree1 && !tree2) return true;
  if (!tree1 || !tree2 || tree1.value !== tree2.value) return false;
  return areIdenticalTrees(tree1.left, tree2.left) && areIdenticalTrees(tree1.right, tree2.right);
}
```

---

### **50. Explain the difference between `weakMap` and `Map`.**

#### **Answer:**

- **`Map`**:
    - Stores key-value pairs.
    - Keys can be of any type and are strongly referenced.
- **`WeakMap`**:
    - Only allows objects as keys.
    - Keys are weakly referenced, enabling garbage collection.

---

### **51. How do you create a utility type to make all properties optional in TypeScript?**

#### **Answer:**

```typescript
type Partial<T> = {
  [K in keyof T]?: T[K];
};

type User = { id: number; name: string };
type OptionalUser = Partial<User>;
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

### **53. Explain the difference between `useState` and `useRef` in React.**

#### **Answer:**

- **`useState`**: Used to store and update a component’s state. Causes re-renders when updated.
- **`useRef`**: Holds a mutable value that doesn’t trigger re-renders when changed.

---

### **54. How would you implement a queue data structure in JavaScript?**

#### **Answer:**

```javascript
class Queue {
  constructor() {
    this.items = [];
  }
  enqueue(item) { this.items.push(item); }
  dequeue() { return this.items.shift(); }
  isEmpty() { return this.items.length === 0; }
}
```

---

### **55. Write a function to perform a deep freeze on an object.**

#### **Answer:**

```javascript
function deepFreeze(obj) {
  Object.freeze(obj);
  Object.keys(obj).forEach(key => {
    if (typeof obj[key] === 'object' && obj[key] !== null) {
      deepFreeze(obj[key]);
    }
  });
  return obj;
}
```

---

### **56. How would you implement a custom middleware in Redux?**

#### **Answer:**

```javascript
const loggerMiddleware = store => next => action => {
  console.log('Dispatching:', action);
  const result = next(action);
  console.log('Next state:', store.getState());
  return result;
};
```

---

### **57. Write a function to implement quicksort.**

#### **Answer:**

```javascript
function quickSort(arr) {
  if (arr.length <= 1) return arr;
  const pivot = arr[arr.length - 1];
  const left = arr.filter(x => x < pivot);
  const right = arr.filter(x => x > pivot);
  return [...quickSort(left), pivot, ...quickSort(right)];
}
```

---

### **58. How do you handle infinite scrolling in React?**

#### **Answer:**

- Use `IntersectionObserver` or listen to scroll events.
- Example:

```javascript
useEffect(() => {
  const handleScroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
      loadMoreData();
    }
  };
  window.addEventListener('scroll', handleScroll);
  return () => window.removeEventListener('scroll', handleScroll);
}, []);
```

---

### **59. Explain the difference between `export default` and `export`.**

#### **Answer:**

- **`export`**: Named export; allows multiple exports from a file.
- **`export default`**: Default export; allows one export per file, imported without curly braces.

---

### **60. How do you implement the observer pattern in JavaScript?**

#### **Answer:**

```javascript
class Observer {
  constructor() {
    this.subscribers = [];
  }
  subscribe(fn) { this.subscribers.push(fn); }
  notify(data) { this.subscribers.forEach(fn => fn(data)); }
}
// Usage:
const observer = new Observer();
observer.subscribe(data => console.log('Received:', data));
observer.notify('Hello World!');
```

---

These questions build further on advanced JavaScript and TypeScript skills, exploring patterns, utilities, and functional programming techniques frequently used in senior-level projects.