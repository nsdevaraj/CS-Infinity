


### **6. Functions**

- **Definition and Purpose of Functions:**
  - Functions in JavaScript are reusable blocks of code designed to perform a specific task.
  - They are first-class objects, meaning they can be assigned to variables, passed as arguments, and returned from other functions.
  - functions are just objects in js, so that we can used as expressions
  - higher order functions => func with another func as argument or return value
  - func can be nested to form closure, that encapsulate data and logic ... 

- **Types of Functions:**
  - **Function Declaration**: Defines a function with the `function` keyword. It is hoisted, so it can be called before it’s defined.
  - **Function Expression**: Stores a function in a variable; it is not hoisted, so it must be defined before it’s called.
  - **Arrow Functions**: Introduced in ES6, providing a concise syntax. They don’t have their own `this` binding and are often used in callback functions.
  - **Anonymous Functions**: Functions without a name, often used as arguments in higher-order functions.
  - **Immediately Invoked Function Expressions (IIFE)**: Functions that execute immediately after they are defined, used to create isolated scopes.

  ```javascript
  // Function Declaration
  function add(a, b) {
      return a + b;
  }

  // Function Expression
  const multiply = function(a, b) {
      return a * b;
  };

  // Arrow Function
  const subtract = (a, b) => a - b;

  // IIFE
  (function() {
      console.log("IIFE executed!");
  })();
  ```

- **Parameters and Arguments:**
  - Functions can take parameters (placeholders) which are filled by arguments when the function is called.
  - JavaScript doesn’t enforce strict matching of the number of parameters and arguments, meaning extra arguments are ignored, and missing ones are `undefined`.

  ```javascript
  function greet(name = "Guest") { // Default parameter
      return `Hello, ${name}!`;
  }
  ```

- **Rest Parameters and Spread Operator:**
  - **Rest Parameters (`...args`)**: Collects all remaining arguments into an array, allowing functions to accept a variable number of arguments.
  - **Spread Operator (`...`)**: Expands an array or object into individual elements, useful for calling functions with array values.

  ```javascript
  function sum(...numbers) {
      return numbers.reduce((a, b) => a + b, 0);
  }
  console.log(sum(1, 2, 3, 4)); // Output: 10
  ```

- **`this` Keyword in Functions:**
  - In a **regular function**, `this` refers to the object calling the function.
  - In **arrow functions**, `this` is lexically bound, meaning it uses the `this` value from the outer scope where it was defined.
  
  ```javascript
  const person = {
      name: "Alice",
      greet: function() {
          console.log(`Hello, ${this.name}`);
      },
      greetArrow: () => {
          console.log(`Hello, ${this.name}`); // `this` refers to the outer scope, not the `person` object
      }
  };
  person.greet();       // Outputs "Hello, Alice"
  person.greetArrow();  // Outputs "Hello, undefined"
  ```

- **Closures:**
  - A closure occurs when a function retains access to its lexical scope, even after the outer function has completed execution.
  - Closures are commonly used to create **private variables** and **encapsulate functionality**.

  ```javascript
  function counter() {
      let count = 0;
      return function() {
          count++;
          return count;
      };
  }
  const increment = counter();
  console.log(increment()); // Output: 1
  console.log(increment()); // Output: 2
  ```

* noramlly func will be present in call stack and its variables with primitive value will be in stack memory ( short term memory ), but when closure inner func will access the outer func value becoz js will store outer func vairables in heap memory which get persisited between func calls.


- **Higher-Order Functions:**
  - Functions that take other functions as arguments or return functions as results.
  - Common in functional programming and array manipulation methods like `map`, `filter`, and `reduce`.

  ```javascript
  const numbers = [1, 2, 3, 4];
  const doubled = numbers.map(num => num * 2);
  console.log(doubled); // Output: [2, 4, 6, 8]
  ```

- **Function Currying:**
  - Currying is the process of transforming a function with multiple arguments into a series of functions each taking a single argument.
  - Useful for creating specialized functions by partially applying arguments.

  ```javascript
  function multiply(a) {
      return function(b) {
          return a * b;
      };
  }
  const double = multiply(2);
  console.log(double(5)); // Output: 10
  ```

- **Callback Functions:**
  - A function passed as an argument to another function and executed after some operation completes.
  - Commonly used in asynchronous operations like handling events or fetching data.

  ```javascript
  function fetchData(callback) {
      setTimeout(() => {
          callback("Data loaded");
      }, 1000);
  }
  fetchData(data => console.log(data)); // Output: "Data loaded" after 1 second
  ```

- **Promises and Async/Await:**
  - **Promises**: Introduced to handle asynchronous operations, providing `then` and `catch` methods for chaining.
  - **Async/Await**: Syntactic sugar over promises, making asynchronous code look synchronous for readability.

  ```javascript
  function getData() {
      return new Promise((resolve, reject) => {
          setTimeout(() => {
              resolve("Data fetched");
          }, 1000);
      });
  }
  
  // Using Promises
  getData().then(data => console.log(data));
  
  // Using Async/Await
  async function fetchData() {
      const data = await getData();
      console.log(data);
  }
  fetchData();
  ```

### Interview Insights:
- Be comfortable explaining **closures** and **lexical scope** as these concepts are frequently asked.
- **Arrow functions** and their behavior with `this` are common interview points, especially in comparison with regular functions.
- Understand **callbacks, promises, and async/await**; interviewers may ask you to refactor code between these.
- **Higher-order functions** like `map`, `filter`, and `reduce` are often tested for their concise, functional approach to array manipulation.


### Functions in JavaScript

1. **Function Declarations and Expressions**
   - **Function Declaration**: A traditional way to define a function, available for use anywhere in its scope due to hoisting.
     - Syntax:
       ```javascript
       function greet() {
         console.log("Hello, World!");
       }
       ```
   - **Function Expression**: A function assigned to a variable, not hoisted, so it can only be used after its definition.
     - Syntax:
       ```javascript
       const greet = function() {
         console.log("Hello, World!");
       };
       ```

2. **Arrow Functions (ES6)**
   - A concise syntax for function expressions. Arrow functions do not have their own `this` context (useful for functional programming and callbacks).
   - Syntax:
     ```javascript
     const greet = () => console.log("Hello, World!");
     ```
   - **Key Differences**:
     - No `this` binding: Arrow functions inherit `this` from their surrounding scope.
     - No `arguments` object: Arrow functions don’t have their own `arguments` object, though it can be accessed through rest parameters.

3. **Higher-Order Functions**
   - Functions that can accept other functions as arguments or return them as outputs. 
   - Example: Array methods like `map`, `filter`, and `reduce`.
     ```javascript
     const numbers = [1, 2, 3];
     const doubled = numbers.map(num => num * 2); // [2, 4, 6]
     ```

4. **Closures**
   - A closure is created when an inner function has access to variables from an outer function, even after the outer function has finished executing. This enables data encapsulation.
   - Example:
     ```javascript
     function makeCounter() {
       let count = 0;
       return function() {
         count++;
         console.log(count);
       };
     }
     const counter = makeCounter();
     counter(); // 1
     counter(); // 2
     ```

5. **The `this` Keyword**
   - `this` refers to the context in which a function is invoked:
     - In global scope, `this` refers to the global object (e.g., `window` in browsers).
     - Inside an object method, `this` refers to the object itself.
     - In arrow functions, `this` is lexically bound (from the outer context).
   - Example:
     ```javascript
     const obj = {
       name: "JavaScript",
       getName() {
         console.log(this.name);
       },
     };
     obj.getName(); // "JavaScript"
     ```

6. **Function Parameters**
   - JavaScript functions are flexible in handling parameters:
     - **Default Parameters**: Assigns a default value if an argument is `undefined`.
       ```javascript
       function greet(name = "Stranger") {
         console.log(`Hello, ${name}!`);
       }
       ```
     - **Rest Parameters**: Gathers all remaining arguments into an array.
       ```javascript
       function add(...nums) {
         return nums.reduce((sum, num) => sum + num, 0);
       }
       add(1, 2, 3); // 6
       ```

7. **Call, Apply, and Bind Methods**
   - `call` and `apply` allow functions to be invoked with a specific `this` context.
     - `call`: Accepts arguments individually.
       ```javascript
       const greet = function(greeting) {
         console.log(`${greeting}, ${this.name}`);
       };
       greet.call({ name: "JavaScript" }, "Hello"); // "Hello, JavaScript"
       ```
     - `apply`: Accepts arguments as an array.
       ```javascript
       greet.apply({ name: "JavaScript" }, ["Hello"]); // "Hello, JavaScript"
       ```
   - `bind`: Creates a new function with a permanently bound `this`.
     ```javascript
     const boundGreet = greet.bind({ name: "JavaScript" });
     boundGreet("Hello"); // "Hello, JavaScript"
     ```

8. **Asynchronous Functions and Promises**
   - JavaScript functions can handle asynchronous operations using `async` and `await`.
   - `async` functions return a Promise, while `await` pauses execution until the promise resolves.
     ```javascript
     async function fetchData() {
       const response = await fetch("https://api.example.com/data");
       const data = await response.json();
       console.log(data);
     }
     fetchData();
     ```

9. **Interview Insights**
   - **Closures**: Frequently asked topic; be prepared to discuss how closures work and their real-world use cases, such as data encapsulation.
   - **Higher-Order Functions**: Understand how functions can act as arguments and return values, with examples like `map`, `filter`, and `reduce`.
   - **Arrow Functions and `this`**: Be ready to explain the differences between traditional functions and arrow functions, particularly their impact on `this` context.
   - **Async/Await vs. Promises**: Be comfortable with async programming patterns and how to handle promises with async/await.



### Pass by Value and Reference

1. **Understanding Pass by Value**
   - JavaScript passes primitive types (e.g., `number`, `string`, `boolean`, `undefined`, `null`, `symbol`, and `bigint`) **by value**. 
   - When passing a primitive type to a function, JavaScript copies the value, so changes inside the function do not affect the original variable.

   ```javascript
   function changeValue(val) {
       val = 10;
   }

   let num = 5;
   changeValue(num);
   console.log(num); // Output: 5
   ```

2. **Understanding Pass by Reference**
   - Non-primitive types (i.e., `object`, `array`, `function`) are **passed by reference**. Instead of copying the value, JavaScript passes a reference to the object, allowing modifications within the function to reflect outside it.

   ```javascript
   function changeProperty(obj) {
       obj.name = 'JavaScript';
   }

   let language = { name: 'Python' };
   changeProperty(language);
   console.log(language.name); // Output: 'JavaScript'
   ```

3. **Implications in Interviews**
   - **Primitive Immutability**: Highlight the immutability of primitives in functions.
   - **Object Mutability**: Discuss mutability of objects in pass-by-reference.
   - **Use Cases**: Pass-by-reference can be beneficial in modifying shared resources, while pass-by-value ensures variable isolation.

Let me know if you'd like the next section.


### Functions in JavaScript

1. **Function Declaration**
   - A function can be defined using a function declaration. It creates a named function.
   - Syntax:
     ```javascript
     function functionName(parameters) {
         // function body
     }
     ```

   ```javascript
   function greet(name) {
       return `Hello, ${name}!`;
   }

   console.log(greet('Alice')); // Output: Hello, Alice!
   ```

2. **Function Expression**
   - Functions can also be defined using function expressions, which can be anonymous (without a name) or named.
   - Syntax:
     ```javascript
     const functionName = function(parameters) {
         // function body
     };
     ```

   ```javascript
   const add = function(a, b) {
       return a + b;
   };

   console.log(add(2, 3)); // Output: 5
   ```

3. **Arrow Functions**
   - Introduced in ES6, arrow functions provide a more concise syntax and do not have their own `this` context.
   - Syntax:
     ```javascript
     const functionName = (parameters) => {
         // function body
     };
     ```

   ```javascript
   const multiply = (a, b) => a * b;

   console.log(multiply(3, 4)); // Output: 12
   ```

4. **Function Parameters**
   - JavaScript allows default parameters, rest parameters, and destructuring of parameters.
   - Default Parameters:
     ```javascript
     function multiply(a, b = 1) {
         return a * b;
     }

     console.log(multiply(5)); // Output: 5
     ```

   - Rest Parameters:
     ```javascript
     function sum(...numbers) {
         return numbers.reduce((acc, curr) => acc + curr, 0);
     }

     console.log(sum(1, 2, 3, 4)); // Output: 10
     ```

   - Destructuring Parameters:
     ```javascript
     function display({ name, age }) {
         console.log(`Name: ${name}, Age: ${age}`);
     }

     display({ name: 'Bob', age: 30 }); // Output: Name: Bob, Age: 30
     ```

5. **Returning Values**
   - Functions can return values using the `return` statement.
   - If no return statement is specified, the function returns `undefined`.

   ```javascript
   function subtract(a, b) {
       return a - b;
   }

   console.log(subtract(10, 5)); // Output: 5
   ```

6. **Implications in Interviews**
   - **Function Scope**: Understand how functions create their own scope.
   - **`this` Context**: Be aware of how `this` works in regular and arrow functions.
   - **Higher-Order Functions**: Know about functions that take other functions as arguments or return them.
   - **Callback Functions**: Be prepared to explain how callback functions work and their common use cases.

Let me know if you'd like the next section.