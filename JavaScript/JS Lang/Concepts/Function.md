

### 1. **Function Basics**

In JavaScript, functions are first-class citizens, meaning they can be:
- Assigned to variables
- Passed as arguments to other functions
- Returned from other functions

**Syntax of Function Declaration**:
```javascript
function add(a, b) {
    return a + b;
}
```

**Syntax of Function Expression**:
```javascript
const add = function(a, b) {
    return a + b;
};
```

**Arrow Functions (ES6)**:
```javascript
const add = (a, b) => a + b;
```

### 2. **Types of Functions in JavaScript**

- **Named Functions**: Defined with a specific name and can be called by that name.
- **Anonymous Functions**: Functions without a name, often used in function expressions or as arguments.
- **Arrow Functions**: Shorter syntax introduced in ES6, with lexical `this` binding (no own `this`).
- **Immediately Invoked Function Expressions (IIFE)**: Functions that execute as soon as they are defined, often used to avoid polluting the global scope.

  ```javascript
  (function() {
      console.log("IIFE executed");
  })();
  ```

### 3. **Higher-Order Functions**

Higher-order functions take other functions as arguments or return them as results. They’re crucial for functional programming in JavaScript.

**Example: `map` and `filter` (both higher-order functions)**:
```javascript
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(num => num * 2);  // [2, 4, 6, 8, 10]
const evens = numbers.filter(num => num % 2 === 0); // [2, 4]
```

**Common Interview Questions on Higher-Order Functions**:
- Explain and demonstrate the use of `.map()`, `.filter()`, and `.reduce()`.
- Write a higher-order function that takes a function and a number, applies the function to the number, and returns the result.

### 4. **Closures and Scoping**

Closures are formed when a function retains access to its lexical scope, even after the outer function finishes execution. This is often used to maintain state, create private variables, or remember variable values over time.

**Example: Counter with Closure**:
```javascript
function createCounter() {
    let count = 0;
    return function() {
        count++;
        return count;
    };
}

const counter = createCounter();
console.log(counter()); // 1
console.log(counter()); // 2
```

**Common Interview Questions on Closures**:
- Describe how closures work and when they’re useful.
- Implement a counter function that remembers its count even after multiple calls.

### 5. **Callback Functions**

A callback function is a function passed as an argument to another function, often used in asynchronous programming (like handling events or fetching data).

**Example of Callback**:
```javascript
function greet(name, callback) {
    console.log(`Hello, ${name}!`);
    callback();
}

greet("Alice", function() {
    console.log("Callback executed!");
});
```

### 6. **`this` Keyword**

In JavaScript, `this` refers to the execution context and can behave differently depending on how a function is invoked.

**Examples of `this` in different contexts**:
- **Method Invocation**: Refers to the object the method is called on.
- **Simple Function Call**: In strict mode, `this` is `undefined`. In non-strict mode, it refers to the global object.
- **Arrow Functions**: Arrow functions don’t have their own `this`; they inherit `this` from the surrounding lexical context.

**Common Interview Question on `this`**:
- Describe how `this` works in JavaScript. How does it differ in arrow functions vs. regular functions?

### 7. **Function Currying**

Currying is transforming a function that takes multiple arguments into a sequence of functions that each take a single argument.

transforms the function of n arguments into n functions of one/fewer arguments


**Example**:
```javascript
function multiply(a) {
    return function(b) {
        return a * b;
    };
}

const double = multiply(2);
console.log(double(5)); // 10
```

### 8. **Function Composition**

Function composition is combining two or more functions to produce a new function, where the output of one function becomes the input of the next.

**Example**:
```javascript
const add5 = (x) => x + 5;
const multiply2 = (x) => x * 2;

const add5ThenMultiply2 = (x) => multiply2(add5(x));
console.log(add5ThenMultiply2(5)); // Output: 20
```

### 9. **Recursion**

A function is recursive if it calls itself until a base condition is met. Recursion is useful for problems like factorials, Fibonacci sequences, and tree traversals.

**Example: Factorial Calculation**:
```javascript
function factorial(n) {
    if (n === 0) return 1;
    return n * factorial(n - 1);
}

console.log(factorial(5)); // Output: 120
```

**Common Interview Questions on Recursion**:
- Write a recursive function to calculate the Fibonacci sequence.
- How does recursion work, and when is it preferable to iteration?

### 10. **Asynchronous Functions and Promises**

JavaScript functions can be asynchronous, allowing non-blocking code execution. `async`/`await` and `Promises` are commonly used for handling asynchronous code.

**Example of `async`/`await`**:
```javascript
async function fetchData() {
    try {
        const response = await fetch('https://api.example.com/data');
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error("Error fetching data", error);
    }
}
```

**Common Interview Questions on Async Functions**:
- Explain the difference between callbacks, Promises, and `async`/`await`.
- How do you handle errors in asynchronous functions?

### Sample Interview Questions

1. **Explain the difference between function declarations and function expressions.**
   - Function declarations are hoisted, meaning they can be called before they’re defined. Function expressions are not hoisted and are only accessible after they’re defined.

2. **What are arrow functions, and how do they differ from regular functions?**
   - Arrow functions have a shorter syntax and do not have their own `this` context, making them unsuitable as methods in some cases.

3. **Write a function to implement a basic debounce.**
   - Debouncing limits the rate at which a function can fire. A common example is delaying input events to prevent excessive function calls.

4. **How does `bind`, `call`, and `apply` work in JavaScript?**
   - These methods are used to set the `this` context of a function.
   - `call` and `apply` invoke the function immediately, with `call` taking individual arguments and `apply` taking an array.
   - `bind` returns a new function with a permanently bound `this` context.

### Practice Questions

1. **Implement a function that memoizes another function.**
   ```javascript
   function memoize(fn) {
       const cache = {};
       return function(...args) {
           const key = JSON.stringify(args);
           if (cache[key]) return cache[key];
           const result = fn(...args);
           cache[key] = result;
           return result;
       };
   }
   ```

2. **Write a function that uses closures to create a simple counter.**
   ```javascript
   function createCounter() {
       let count = 0;
       return function() {
           count++;
           return count;
       };
   }
   ```

By mastering these concepts, you’ll be well-prepared to handle questions on functions in JavaScript interviews. Let me know if you need deeper insight into any specific area!



---



## Function usage

Here’s a breakdown of the distinctions among `function User() {}`, `var user = User()`, and `var user = new User()` in JavaScript:

### 1. **Function Declaration: `function User() {}`**
- **Definition**: This is a function declaration that defines a function named `User`.
- **Usage**: It can be invoked later as a function or used as a constructor when called with `new`.
- **Example**:
  ```javascript
  function User() {
      this.name = "Alice";
  }
  ```
- **Key Points**:
  - It does not create an instance or execute anything on its own.
  - The `User` function can be used to create multiple instances if invoked with `new`.

### 2. **Function Call: `var user = User()`**
- **Definition**: This calls the `User` function without the `new` keyword.
- **Usage**: The function executes and returns `undefined` unless a return value is specified.
- **Example**:
  ```javascript
  var user = User(); // This calls the User function
  console.log(user); // Outputs: undefined
  ```
- **Key Points**:
  - In this case, `this` inside the `User` function will not refer to a new object. Instead, it refers to the global object (in non-strict mode) or is `undefined` (in strict mode).
  - If the function modifies or accesses `this`, it will not behave as expected because `user` will not be an instance of `User`.

### 3. **Constructor Call: `var user = new User()`**
- **Definition**: This calls the `User` function as a constructor using the `new` keyword.
- **Usage**: It creates a new instance of `User` and assigns it to the variable `user`.
- **Example**:
  ```javascript
  var user = new User(); // This creates a new User instance
  console.log(user.name); // Outputs: Alice
  ```
- **Key Points**:
  - When called with `new`, a new object is created, and `this` inside `User` refers to this new object.
  - The function will return the new object unless explicitly stated otherwise (with a return statement returning a different object).

### Summary Table

| **Expression**        | **Definition**                                   | **Behavior**                                               | **Value of `this`**                |
|-----------------------|--------------------------------------------------|------------------------------------------------------------|-------------------------------------|
| `function User() {}`  | Function declaration                             | Defines a function but does not execute it or create an instance. | N/A                                 |
| `var user = User()`   | Function call                                   | Executes the function; returns `undefined` unless specified. | Global object (non-strict) or `undefined` (strict mode) |
| `var user = new User()` | Constructor call                              | Creates a new instance of `User` and assigns it to `user`. | New object (the instance being created) |

### Conclusion
- Use **`function User() {}`** to define a function.
- Use **`var user = User()`** for a regular function call, but be cautious about how `this` is handled.
- Use **`var user = new User()`** to create a new instance of the `User` function, leveraging it as a constructor.



### Summary of Function Usage in JavaScript

In JavaScript, functions can be defined and invoked in different ways, leading to distinct behaviors. Here’s a concise overview of the concepts discussed:

#### 1. Function Declaration: `function User() {}`
- **Purpose**: Defines a function named `User`.
- **Behavior**: Does not create an instance or execute anything by itself.
- **Use**: Can be called later or used as a constructor when paired with `new`.

#### 2. Function Call: `var user = User()`
- **Purpose**: Calls the `User` function without `new`.
- **Behavior**: Executes the function, returning `undefined` unless a return value is specified.
- **Key Points**:
  - The value of `this` refers to the global object (in non-strict mode) or is `undefined` (in strict mode).
  - Does not create an instance of `User`.

#### 3. Constructor Call: `var user = new User()`
- **Purpose**: Invokes the `User` function as a constructor using `new`.
- **Behavior**: Creates a new object instance of `User`.
- **Key Points**:
  - The value of `this` inside `User` refers to the new object being created.
  - If no return statement is specified, the function returns the newly created object.

### Related Concepts for Better Understanding

- **`this` Keyword**:
  - Refers to the context in which a function is executed.
  - Its value changes depending on how a function is invoked (regular call, method call, or constructor call).

- **Constructor Functions**:
  - Functions intended to be used with `new` to create instances.
  - Typically, constructor functions start with an uppercase letter by convention.

- **Classes (ES6)**:
  - A modern syntax for defining constructor functions and prototypes.
  - Example:
    ```javascript
    class User {
        constructor(name) {
            this.name = name;
        }
    }
    const user = new User("Alice");
    ```

- **Object Instantiation**:
  - The process of creating an instance of an object using a constructor function or class.
  - Provides a way to create multiple objects with shared behavior.

### Conclusion
Understanding the distinctions between defining, calling, and constructing functions in JavaScript is crucial for effective programming. Recognizing how the `this` context changes based on invocation helps avoid common pitfalls. The introduction of classes in ES6 provides a more intuitive approach to object-oriented programming in JavaScript.




## call , apply and bind



Certainly! Here’s a concise explanation of `call`, `apply`, `bind`, and their roles in JavaScript, including their purposes and differences.

### 1. `Function.call`
- **Purpose**: Invokes a function with a specified `this` context and allows you to pass individual arguments.
- **Syntax**: `func.call(thisArg, arg1, arg2, ...)`
- **Example**:
  ```javascript
  function greet(greeting) {
      console.log(`${greeting}, ${this.name}`);
  }
  
  const user = { name: 'Alice' };
  greet.call(user, 'Hello'); // Outputs: Hello, Alice
  ```

### 2. `Function.apply`
- **Purpose**: Similar to `call`, but it accepts an array (or array-like object) of arguments.
- **Syntax**: `func.apply(thisArg, [argsArray])`
- **Example**:
  ```javascript
  function greet(greeting) {
      console.log(`${greeting}, ${this.name}`);
  }
  
  const user = { name: 'Alice' };
  greet.apply(user, ['Hi']); // Outputs: Hi, Alice
  ```

### 3. `Function.bind`
- **Purpose**: Returns a new function with a specified `this` context and allows you to pre-set some arguments. It does not invoke the function immediately.
- **Syntax**: `const newFunc = func.bind(thisArg, arg1, arg2, ...)`
- **Example**:
  ```javascript
  function greet(greeting) {
      console.log(`${greeting}, ${this.name}`);
  }
  
  const user = { name: 'Alice' };
  const greetUser = greet.bind(user);
  greetUser('Hey'); // Outputs: Hey, Alice
  ```

### Key Differences

| Feature                  | `call`                             | `apply`                            | `bind`                              |
|--------------------------|------------------------------------|-----------------------------------|-------------------------------------|
| **Invocation**           | Invokes the function immediately    | Invokes the function immediately   | Returns a new function; does not invoke immediately |
| **Argument Passing**     | Individual arguments                | Single array of arguments          | Pre-binds arguments for later use   |
| **Return Value**         | Returns the result of the invoked function | Returns the result of the invoked function | Returns a new function               |

### Use Cases
- **`call`**: Use when you want to invoke a function immediately with a specific `this` context and known arguments.
- **`apply`**: Use when you want to invoke a function immediately but have the arguments in an array format.
- **`bind`**: Use when you want to create a new function that can be called later with a specific `this` context and pre-defined arguments.

### Summary
- `call`, `apply`, and `bind` are powerful methods for controlling the `this` context in JavaScript functions.
- They help manage function invocation and argument passing in a flexible way, facilitating functional programming patterns and event handling.





IIFE => for intializing thigs..



### Func  defining



Func declaration or function definition or funciton statement

Func expression -> store func inside a vairable


Func declaration and expression - both same, but expression just assigned to a variable 



```js


// func delcarion 
funciton square(num){
    return num * num;
}

// func expression - with anonlymous func
const square2 = function(num){
    return num * num
}


```

anonymous func:
- func without no name
- 



First class func 


To organize this extensive course content, I'll break down the key JavaScript interview topics into sections, with explanations and code snippets where needed. Here’s **Section 1**, which covers:

- Function Declarations vs. Function Expressions
- Anonymous Functions
- First-Class Functions
- IIFE (Immediately Invoked Function Expressions)

---

### 1. Function Declarations vs. Function Expressions

**Definition**:
- A **Function Declaration** defines a named function and can be used before it’s defined due to hoisting.
- A **Function Expression** assigns an anonymous function to a variable and is not hoisted.

```javascript
// Function Declaration
function square(num) {
  return num * num;
}
console.log(square(5)); // Output: 25

// Function Expression
const squareExpr = function(num) {
  return num * num;
};
console.log(squareExpr(5)); // Output: 25
```

---

### 2. Anonymous Functions

**Definition**:
An **Anonymous Function** is a function without a name, often assigned to variables or used as arguments to other functions.

```javascript
// Assigned to a variable
const greet = function() {
  console.log("Hello!");
};
greet(); // Output: Hello!

// Used as a callback
setTimeout(function() {
  console.log("Anonymous callback function executed!");
}, 1000);
```

---

### 3. First-Class Functions

**Definition**:
In JavaScript, **First-Class Functions** mean that functions are treated as variables. 
They can be passed as arguments to other functions, returned as values, or assigned to variables. and it also can be manipulated.

**Example**:

```javascript
// Passing function as an argument
function greetUser(name) {
  console.log("Hello, " + name);
}

function executeGreeting(greetFunction, name) {
  greetFunction(name);
}
executeGreeting(greetUser, "Alice"); // Output: Hello, Alice

// Returning a function from another function
function createMultiplier(multiplier) {
  return function(num) {
    return num * multiplier;
  };
}
const double = createMultiplier(2);
console.log(double(5)); // Output: 10
```

---

### 4. IIFE (Immediately Invoked Function Expression)

**Definition**:
An **IIFE** is a function that is defined and immediately executed. It’s useful for creating isolated scopes and avoiding global variable pollution.

**Syntax**:

```javascript
(function() {
  console.log("IIFE executed immediately!");
})(); // Output: IIFE executed immediately!

// IIFE with parameters
(function(num) {
  console.log("Square:", num * num);
})(5); // Output: Square: 25



(function (x){
    return (function (y){
        // search and get x in parent's scope ( closure )
        console.log(x);
    })(2);
})(1) //=> 1

```

---



### Funciton scopes:

Here’s **Section 2**, covering:

- Scopes
- Closures
- Lexical Scope
- Block Scope using `let` and `const`

Each concept includes explanations and examples.

---

### 1. Scopes

**Definition**:
In JavaScript, **Scope** determines the accessibility of variables. There are mainly three types of scopes:

- **Global Scope**: Variables declared outside any function have global scope and are accessible anywhere.
- **Function Scope**: Variables declared within a function are scoped to that function.
- **Block Scope**: Variables declared within a block (`{}`) using `let` or `const` are block-scoped and cannot be accessed outside the block.

**Example**:

```javascript
// Global scope
let globalVar = "I am global";

function checkScope() {
  // Function scope
  let funcVar = "I am in function scope";
  console.log(globalVar);  // Accessible: Output -> I am global
  console.log(funcVar);    // Accessible: Output -> I am in function scope
}
checkScope();
console.log(globalVar);     // Accessible: Output -> I am global
// console.log(funcVar);    // Error: funcVar is not defined
```

---

### 2. Closures

**Definition**:
A **Closure** is a function that remembers its outer scope even after the outer function has finished executing. Closures are powerful for creating private variables and encapsulating state.

**Example**:

```javascript
function outerFunction() {
  let count = 0;
  // innerFunction is a closure that has access to `count`
  function innerFunction() {
    count++;
    console.log("Count:", count);
  }
  return innerFunction;
}

const counter = outerFunction();
counter(); // Output: Count: 1
counter(); // Output: Count: 2
```

In this example, `innerFunction` has access to `count`, even though `outerFunction` has completed execution.

---

### 3. Lexical Scope

**Definition**:
**Lexical Scope** (also known as Static Scope) means that the scope of a variable is determined by its position in the source code. Functions in JavaScript have access to variables defined in their outer lexical environment.

**Example**:

```javascript
function outer() {
  let outerVar = "I'm from outer";

  function inner() {
    console.log(outerVar); // Accesses outerVar due to lexical scoping
  }

  inner(); // Output: I'm from outer
}
outer();
```

Here, `inner` has access to `outerVar` because of lexical scoping: the `inner` function can "see" the variables defined in the `outer` function.

---

### 4. Block Scope using `let` and `const`

**Definition**:
JavaScript introduced block-scoping with the `let` and `const` keywords, where variables declared within a block `{}` are only accessible inside that block.

**Example**:

```javascript
if (true) {
  let blockVar = "I'm block scoped!";
  console.log(blockVar); // Output: I'm block scoped!
}
// console.log(blockVar); // Error: blockVar is not defined

// Using `const` for constants with block scope
for (let i = 0; i < 3; i++) {
  const constantVal = i * 2;
  console.log(constantVal); // Outputs: 0, 2, 4
}
// console.log(i);          // Error: i is not defined
```

The variables `blockVar` and `i` are accessible only within their respective blocks due to block scoping.

---

This concludes Section 2. Let me know when you’re ready for **Section 3**, which will cover **Asynchronous JavaScript** concepts.

Here’s **Section 2**, covering:

- Scopes
- Closures
- Lexical Scope
- Block Scope using `let` and `const`

Each concept includes explanations and examples.

---

### 1. Scopes

**Definition**:
In JavaScript, **Scope** determines the accessibility of variables. There are mainly three types of scopes:

- **Global Scope**: Variables declared outside any function have global scope and are accessible anywhere.
- **Function Scope**: Variables declared within a function are scoped to that function.
- **Block Scope**: Variables declared within a block (`{}`) using `let` or `const` are block-scoped and cannot be accessed outside the block.

**Example**:

```javascript
// Global scope
let globalVar = "I am global";

function checkScope() {
  // Function scope
  let funcVar = "I am in function scope";
  console.log(globalVar);  // Accessible: Output -> I am global
  console.log(funcVar);    // Accessible: Output -> I am in function scope
}
checkScope();
console.log(globalVar);     // Accessible: Output -> I am global
// console.log(funcVar);    // Error: funcVar is not defined
```



```js

var num1 = 20, num2 = 3, name = 'Roadside Coder'

function multiple(){
    // takes from globals
    return num1*num2
}

console.log(multiple()) //=> 60

function getScore(){
    var num1 = 10, num2 = 5

    function add(params) {
        // name takes from global
        // num1 and num2 takes from local
        return `${name} scored ${num1+num2}`
    }
    return add()
}

console.log(getScore())//=> Roadside Coder scored 15


```

---

### 2. Closures

**Definition**:
A **Closure** is a function that remembers its outer scope even after the outer function has finished executing. Closures are powerful for creating private variables and encapsulating state.

**Example**:

```javascript
function outerFunction() {
  let count = 0;
  // innerFunction is a closure that has access to `count`
  function innerFunction() {
    count++;
    console.log("Count:", count);
  }
  return innerFunction;
}

const counter = outerFunction();
counter(); // Output: Count: 1
counter(); // Output: Count: 2
```

In this example, `innerFunction` has access to `count`, even though `outerFunction` has completed execution.

---

### 3. Lexical Scope

**Definition**:
**Lexical Scope** (also known as Static Scope) means that the scope of a variable is determined by its position in the source code. Functions in JavaScript have access to variables defined in their outer lexical environment.

**Example**:

```javascript
function outer() {
  let outerVar = "I'm from outer";

  function inner() {
    console.log(outerVar); // Accesses outerVar due to lexical scoping
  }

  inner(); // Output: I'm from outer
}
outer();
```

Here, `inner` has access to `outerVar` because of lexical scoping: the `inner` function can "see" the variables defined in the `outer` function.

---

### 4. Block Scope using `let` and `const`

**Definition**:
JavaScript introduced block-scoping with the `let` and `const` keywords, where variables declared within a block `{}` are only accessible inside that block.

**Example**:

```javascript
if (true) {
  let blockVar = "I'm block scoped!";
  console.log(blockVar); // Output: I'm block scoped!
}
// console.log(blockVar); // Error: blockVar is not defined

// Using `const` for constants with block scope
for (let i = 0; i < 3; i++) {
  const constantVal = i * 2;
  console.log(constantVal); // Outputs: 0, 2, 4
}
// console.log(i);          // Error: i is not defined
```

The variables `blockVar` and `i` are accessible only within their respective blocks due to block scoping.

---

This concludes Section 2. Let me know when you’re ready for **Section 3**, which will cover **Asynchronous JavaScript** concepts.


```js




// both runs on callStack itself, so no difference
for (var i=0;i<3;i++){
    console.log('var', i)
}
for (let i=0;i<3;i++){
    console.log('let',i)
}

// var is func scope, so value increase will reflect and have shadow
for (var i=0;i<3;i++){
    setTimeout(()=>{
        console.log('setVar',i)
    }, 100)
}

// let is block scope, so value don't have shadow
for (let i=0;i<3;i++){
    setTimeout(()=>{
        console.log('setLet',i)
    }, 100)
}

/*
var 0
var 1
var 2
let 0
let 1
let 2
setVar 3
setVar 3
setVar 3
setLet 0
setLet 1
setLet 2
*/


```



