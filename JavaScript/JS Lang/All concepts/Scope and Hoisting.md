
### **7. Scope and Hoisting**

- **Scope**:
  - Scope determines the accessibility of variables, objects, and functions in different parts of code.
  - **Types of Scope in JavaScript**:
    - **Global Scope**: Variables declared outside any function or block are in the global scope and accessible from anywhere in the code.
    - **Function Scope**: Variables declared within a function are local to that function and cannot be accessed outside.
    - **Block Scope**: Variables declared with `let` and `const` within a block `{}` are block-scoped, meaning they are accessible only within that specific block. `var`, however, is function-scoped and ignores block-level scope.

  ```javascript
  let x = 10; // Global scope

  function example() {
      let y = 20; // Function scope
      if (true) {
          let z = 30; // Block scope
          console.log(x, y, z); // 10, 20, 30
      }
      console.log(x, y); // 10, 20
      // console.log(z); // Error: z is not defined
  }
  example();
  ```

- **Lexical Scope**:
  - the scope of a variable is determined by its location in the source code.
  - Inner functions have access to variables defined in their outer functions, creating closures.

  ```javascript
  function outer() {
      const name = "Alice";
      function inner() {
          console.log(name); // Accesses variable from outer scope
      }
      inner();
  }
  outer(); // Output: Alice
  ```

- **Hoisting**:
  - Hoisting is JavaScript’s default behavior of moving declarations to the top of their containing scope during the compilation phase.
  - **Variable Hoisting**:
    - Variables declared with `var` are hoisted to the top of their function scope with an initial value of `undefined`.
    - `let` and `const` are also hoisted, but they remain uninitialized in a "temporal dead zone" from the start of the block until the line where they are defined, throwing a `ReferenceError` if accessed before their declaration.

    ```javascript
    console.log(a); // Output: undefined (due to `var` hoisting)
    var a = 10;

    // console.log(b); // Uncaught ReferenceError (due to `let` hoisting)
    let b = 20;
    ```

  - **Function Hoisting**:
    - **Function Declarations**: Entire function declarations are hoisted, meaning they can be called before they are defined.
    - **Function Expressions and Arrow Functions**: Only the variable name is hoisted, not the function body. Attempting to call the function before declaration will result in an error.

    ```javascript
    // Function declaration (hoisted)
    sayHello(); // Output: Hello, World!
    function sayHello() {
        console.log("Hello, World!");
    }

    // Function expression (not hoisted)
    // greet(); // Uncaught TypeError: greet is not a function
    const greet = function() {
        console.log("Hi!");
    };
    ```

### Interview Insights:
- Be able to explain the difference between **var**, **let**, and **const** in terms of scoping and hoisting.
- Understanding **lexical scope** is essential, especially how it relates to closures.
- Know how **temporal dead zone** works for `let` and `const` to handle common errors involving uninitialized variables.
- Interviewers may test your understanding by asking you to predict outputs for code examples that leverage hoisting or test your understanding of scope chaining.




### Scoping


Scoping in JavaScript defines the accessibility of variables and functions at different parts of the code. 
It determines where a variable or function is accessible and helps prevent naming collisions.

### 1. **Global Scope**
   - Variables defined in the global scope are accessible from anywhere in the code.
   - Any variable declared outside a function or block is globally scoped.
   - In the browser, global variables are properties of the `window` object (e.g., `window.variableName`).

   ```javascript
   var globalVar = "I am global";

   function example() {
       console.log(globalVar); // Accessible here
   }

   console.log(globalVar); // Accessible here too
   ```

### 2. **Function Scope**
   - Variables declared with `var` within a function are scoped to that function.
   - These variables cannot be accessed outside the function.

   ```javascript
   function myFunction() {
       var functionScopedVar = "I am scoped to myFunction";
       console.log(functionScopedVar); // Accessible within the function
   }

   myFunction();
   console.log(functionScopedVar); // Error: functionScopedVar is not defined
   ```

### 3. **Block Scope**
   - Variables declared with `let` and `const` are block-scoped, meaning they are only accessible within the block `{ ... }` where they were declared (e.g., within an `if` or `for` loop).
   - This is different from `var`, which ignores block scope and is only limited by function or global scope.

   ```javascript
   if (true) {
       let blockScopedVar = "I am block scoped";
       const anotherBlockScopedVar = "Me too!";
       console.log(blockScopedVar); // Accessible here
   }

   console.log(blockScopedVar); // Error: blockScopedVar is not defined
   ```

### 4. **Lexical Scope (or Static Scope)**
   - JavaScript uses lexical scoping, meaning a function's scope is determined by its location within the code during writing, not during execution.
   - Inner functions have access to variables declared in their outer functions, even after the outer function has finished executing (this is due to **closures**).

   ```javascript
   function outerFunction() {
       let outerVar = "I am from outer";

       function innerFunction() {
           console.log(outerVar); // Accessing outer function's variable
       }

       innerFunction();
   }

   outerFunction();
   ```

### 5. **Hoisting and Scope**
   - **Hoisting** is JavaScript's default behavior of moving declarations to the top of their scope (not initializations).
   - Variables declared with `var` are hoisted to the top of their function scope, but `let` and `const` are hoisted to the top of their block scope with a "temporal dead zone" (TDZ), meaning they cannot be accessed until the line where they are declared.

   ```javascript
   function hoistingExample() {
       console.log(hoistedVar); // Undefined (var is hoisted)
       var hoistedVar = "I am hoisted";

       // console.log(notHoistedLet); // Error: notHoistedLet is not defined
       let notHoistedLet = "I am not hoisted";
   }

   hoistingExample();
   ```

### 6. **Closures and Scope**
   - **Closures** are functions that "remember" their lexical scope even after they are executed.
   - When a function returns another function, the returned function retains access to the variables from its parent scope, creating a closure.

   ```javascript
   function closureExample() {
       let count = 0;
       return function increment() {
           count++;
           console.log(count);
       };
   }

   const counter = closureExample();
   counter(); // 1
   counter(); // 2
   ```

### 7. **The `this` Keyword and Scope**
   - In JavaScript, `this` refers to the context in which a function is executed.
   - The value of `this` can vary depending on where the function is defined and how it’s called. 
   - In the global scope, `this` refers to the `window` object in the browser. 
   - Inside an object method, `this` refers to the object itself.

   ```javascript
   const obj = {
       value: 42,
       showValue() {
           console.log(this.value); // Refers to obj's value property
       }
   };

   obj.showValue(); // 42
   ```

### Summary of Scoping Rules

1. **Global Scope**: Variables are accessible everywhere.
2. **Function Scope**: Variables declared with `var` inside a function are only accessible within that function.
3. **Block Scope**: Variables declared with `let` and `const` inside `{ }` are only accessible within that block.
4. **Lexical Scope**: Inner functions can access variables from their outer function scopes.
5. **Hoisting** affects scoping by bringing declarations to the top of their respective scopes.
6. **Closures** capture the lexical scope of a function for later use.

### Practical Tips
- Use `let` and `const` to ensure block-scoping and avoid unintended errors from `var`’s function scope.
- Be mindful of closures when returning functions, as they retain access to outer variables.
- Remember that hoisting may make variables accessible before their declaration, but it’s best practice to declare variables at the top of their scope to avoid confusion.


### Hoisting

Hoisting in JavaScript is a behavior where variable and function declarations are "moved" to the top of their scope during the compilation phase. 
This allows you to use variables and functions before they are declared in the code. However, only the declarations are hoisted, not the initializations (or assignments).

### Key Concepts of Hoisting

1. **Function Declarations Are Fully Hoisted**
   - Function declarations are fully hoisted, meaning both the function name and its implementation are moved to the top of their scope.
   - This allows you to call a function before it appears in the code.

   ```javascript
   greet(); // Outputs: "Hello!"

   function greet() {
       console.log("Hello!");
   }
   ```

2. **Variable Declarations Are Hoisted, But Not Their Initializations**
   - Variable declarations (using `var`, `let`, or `const`) are hoisted to the top of their scope, but only `var` declarations are assigned a default value of `undefined` during hoisting.
   - `let` and `const` variables are hoisted to the top but remain in a "Temporal Dead Zone" (TDZ) until their actual line of code is executed. Accessing them before their declaration will throw a `ReferenceError`.

   ```javascript
   console.log(myVar); // Outputs: undefined (because of var hoisting)
   var myVar = "Hello, world!";
   console.log(myVar); // Outputs: "Hello, world!"
   ```

   ```javascript
   console.log(myLetVar); // ReferenceError: Cannot access 'myLetVar' before initialization
   let myLetVar = "Hello!";
   ```

### Hoisting Examples by Declaration Type

#### 1. `var` Hoisting
   - Variables declared with `var` are hoisted with an initial value of `undefined`.

   ```javascript
   console.log(num); // Outputs: undefined
   var num = 5;
   console.log(num); // Outputs: 5
   ```

   This is because `var num;` is hoisted to the top, but `num = 5;` stays in place:

   ```javascript
   var num;
   console.log(num); // undefined
   num = 5;
   console.log(num); // 5
   ```

#### 2. `let` and `const` Hoisting
   - `let` and `const` declarations are hoisted, but they are not initialized and are kept in a "Temporal Dead Zone" (TDZ) from the start of the block until the declaration is encountered. Attempting to access them before declaration will throw an error.

   ```javascript
   console.log(x); // ReferenceError: Cannot access 'x' before initialization
   let x = 10;

   console.log(y); // ReferenceError: Cannot access 'y' before initialization
   const y = 20;
   ```

#### 3. Function Declaration Hoisting
   - Function declarations are fully hoisted, so you can call a function before it appears in the code.

   ```javascript
   sayHello(); // Outputs: "Hello!"

   function sayHello() {
       console.log("Hello!");
   }
   ```

#### 4. Function Expression Hoisting
   - Function expressions (assigned to variables) are **not** hoisted in the same way as function declarations.
   - If a function expression uses `var`, the variable is hoisted with an initial value of `undefined`, but the function itself is not available until after the assignment.
   - If a function expression uses `let` or `const`, it will result in a `ReferenceError` if accessed before initialization.

   ```javascript
   console.log(greet); // undefined
   var greet = function () {
       console.log("Hello!");
   };
   greet(); // Outputs: "Hello!"
   ```

   - With `let` or `const`, trying to access the function before declaration will throw an error.

   ```javascript
   console.log(greet); // ReferenceError: Cannot access 'greet' before initialization
   const greet = function () {
       console.log("Hello!");
   };
   ```

### Temporal Dead Zone (TDZ)
   - The Temporal Dead Zone (TDZ) is a concept that applies to `let` and `const` variables.
   - It’s the time between the start of a scope and the point where the variable is declared, during which the variable is in a "dead" state.
   - Attempting to access a variable in its TDZ will result in a `ReferenceError`.

   ```javascript
   function example() {
       console.log(value); // ReferenceError: Cannot access 'value' before initialization
       let value = 42;
   }

   example();
   ```

### Summary of Hoisting Rules

1. **`var`**: Variables declared with `var` are hoisted and initialized with `undefined`. They can be used before they are declared, though they will have a value of `undefined` until initialized.
2. **`let` and `const`**: These are hoisted to the top of their scope but are not initialized, causing a `ReferenceError` if accessed before their declaration.
3. **Function Declarations**: Function declarations are fully hoisted, so they can be called before they appear in the code.
4. **Function Expressions**: These behave like variables. If they use `var`, they are hoisted as `undefined`, and if they use `let` or `const`, they are in a TDZ until initialization.

### Practical Tips to Avoid Hoisting Pitfalls

- **Use `let` and `const`** instead of `var` to avoid issues with accidental hoisting and TDZ errors.
- **Declare variables at the beginning of their scope** to make code more readable and avoid accidental `undefined` values.
- **Declare functions before using them** unless you specifically want to rely on hoisting.




Scope chaining:
first check vairable in current scope , 
then not found go to uppper level and check...





![[Pasted image 20241106083345.png]]



```js
// var a = 1;  
// function b() {  
//   a = 10;  
//   return;  
//   function a() {}  
// }  
// b();  
// console.log(a);//o:  1

```


```js
// function foo(){  
//   function bar() {  
//     return 3;  
//   }  
//   return bar();  
//   function bar() {  
//     return 8;  
//   }  
// }  
// alert(foo());//o: 8

```


```js

HOISTING:


// function parent() {  
//   var hoisted = "I'm a variable";  
//   function hoisted() {  
//     return "I'm a function";  
//   }  
//   return hoisted();  
// }  
// console.log(parent());// o: TypeError: hoisted is not a function// alert(foo());  
// function foo() {  
//   var bar = function() { return 3;  };  
//   return bar();  
//   var bar = function() {  
//     return 8;  
//   };  
// }  
// //o: 3// var myVar = 'foo';  
// (function()  
//  {  
//   console.log('Original value was: ' + myVar);  
//   var myVar = 'bar';  
//   console.log('New value is: ' + myVar);  
// })();// /*  
// o:  
// "Original value was: undefined"  
// "New value is: bar"  
// */

```


