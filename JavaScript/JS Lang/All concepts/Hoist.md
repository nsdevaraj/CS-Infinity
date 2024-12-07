

Hoisting is JavaScript's default behavior of `moving declarations to the top of their containing scope during compilation`. It applies to both variables and functions.

note: no hoist for  func expression (including arrow func) and blockscoped variable not intialized 

---

#### **1. Variable Hoisting**

- **`var`:** Variables declared with `var` are hoisted to the top of their function or global scope and initialized to `undefined`.
- **`let` and `const`:** These are also hoisted but remain uninitialized and are in the "Temporal Dead Zone" (TDZ) until their declaration is encountered.

---

**Example with `var`:**

```javascript
console.log(x); // Output: undefined (hoisted)
var x = 10;
console.log(x); // Output: 10
```

**Example with `let` and `const`:**

```javascript
console.log(y); // ReferenceError: Cannot access 'y' before initialization
let y = 20;
```

---

#### **2. Function Hoisting**

- **Function Declarations**: Entire function declarations are hoisted, meaning they can be called before their definition.
- **Function Expressions and Arrow Functions**: Only the variable name is hoisted, not the function body. Calling these before declaration results in an error.

---

**Function Declaration Example:**

```javascript
sayHello(); // Output: Hello!

function sayHello() {
    console.log("Hello!");
}
```

**Function Expression Example:**

```javascript
console.log(greet); // Output: undefined
var greet = function () {
    console.log("Hi!");
};
greet(); // Output: Hi!
```

---

#### **3. Temporal Dead Zone (TDZ)**

The TDZ is the time between the start of a block and the declaration of a `let` or `const` variable. During this time, accessing the variable results in a `ReferenceError`.

Example:

```javascript
{
    // Accessing 'x' here results in a ReferenceError
    let x = 10; // TDZ ends here
    console.log(x); // Output: 10
}
```

---

### **Common Hoisting Pitfalls**

**1. Variable Overwriting in Functions:**  
Variables declared as `var` inside a function can be overwritten by a function declaration with the same name.

```javascript
function example() {
    console.log(hoistedVar); // Output: undefined (var is hoisted)
    var hoistedVar = "I am a variable";

    function hoistedVar() {
        return "I am a function";
    }

    return hoistedVar; // TypeError: hoistedVar is not a function
}

example();
```

---

**2. Function Hoisting in Nested Scopes:**  
When multiple function declarations with the same name exist in a scope, the last declaration takes precedence.

```javascript
function foo() {
    function bar() {
        return 8;
    }
    return bar();

    function bar() {
        return 3;
    }
}

console.log(foo()); // Output: 3 (last definition takes precedence)
```

---
Best practice:

- Use `const` by default and `let` when reassignment is needed. Reserve `var` for legacy code.

---


[[Hoisting]]

