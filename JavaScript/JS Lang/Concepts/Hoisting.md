
### Hoisting in JavaScript

**Definition**: Hoisting is a JavaScript mechanism where variables and function declarations are moved to the top of their containing scope during the compilation phase. This means you can use functions and variables before they are declared in the code.

### How Hoisting Works

1. **Variables**:
   - Only the declaration is hoisted, not the initialization. This means that if you try to access a variable before it has been declared, it will return `undefined`.

   **Example**:
   ```javascript
   console.log(x); // Outputs: undefined
   var x = 5;
   console.log(x); // Outputs: 5
   ```

   In the above code, `var x` is hoisted, but its assignment (`x = 5`) is not. Therefore, the first `console.log` outputs `undefined`.

2. **Functions**:
   - Function declarations are fully hoisted, meaning you can call a function before its declaration.

   **Example**:
   ```javascript
   greet(); // Outputs: "Hello!"

   function greet() {
       console.log("Hello!");
   }
   ```

   Here, the function `greet` can be called before its actual declaration due to hoisting.

3. **Function Expressions**:
   - Function expressions (including arrow functions) are not hoisted in the same way. Only the variable declaration is hoisted, not the function definition.

   **Example**:
   ```javascript
   greet(); // TypeError: greet is not a function

   var greet = function() {
       console.log("Hello!");
   };
   ```

   In this case, attempting to call `greet` before its assignment results in a `TypeError` because `greet` is treated as `undefined` at that point.

### Scope and Hoisting

- **Global Scope**: Variables declared with `var` in the global scope become properties of the global object (`window` in browsers).
- **Function Scope**: Variables declared with `var` inside a function are hoisted to the top of that function's scope.
- **Block Scope**: Variables declared with `let` and `const` are also hoisted but are not initialized. Accessing them before their declaration results in a `ReferenceError` due to the "temporal dead zone."

### Temporal Dead Zone (TDZ)
- The TDZ is the time period from the start of a block until the variable is declared. During this time, any attempt to access the variable results in a `ReferenceError`.

**Example**:
```javascript
console.log(y); // ReferenceError: Cannot access 'y' before initialization
let y = 10;
```

### Summary
- **Hoisting** allows variables and function declarations to be used before they are defined in the code.
- **Variables** declared with `var` are hoisted but initialized to `undefined`, while **function declarations** are fully hoisted.
- **Function expressions** are not hoisted like declarations.
- **`let` and `const`** are also hoisted but cannot be accessed until they are declared, resulting in a temporal dead zone.

Understanding hoisting is crucial for writing predictable and bug-free JavaScript code, particularly when dealing with variable declarations and function calls.



