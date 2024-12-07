
Scope determines the `accessibility of variables, functions, and objects in different parts of the code`. JavaScript has the following types of scope:

`context in which variable/func is declared and accessed`


---

**a. Global Scope**

- Variables declared outside any function or block are in the global scope and can be accessed from anywhere.
- In browsers, global variables become properties of the `window` object.

Example:

```javascript
var globalVar = "I am global";

function example() {
    console.log(globalVar); // Accessible here
}

example();
console.log(globalVar); // Accessible here too
```

---

**b. Function Scope** (Local scope)

- Variables declared with `var` inside a function are accessible only within that function.

Example:

```javascript
function myFunction() {
    var functionScopedVar = "I am scoped to myFunction";
    console.log(functionScopedVar); // Accessible within the function
}

myFunction();
console.log(functionScopedVar); // Error: functionScopedVar is not defined
```

---

**c. Block Scope** (Local scope)

- Variables declared with `let` and `const` are block-scoped, meaning they are accessible only within the block `{}` where they are declared.

Example:

```javascript
if (true) {
    let blockScopedVar = "I am block scoped";
    const anotherBlockScopedVar = "Me too!";
    console.log(blockScopedVar); // Accessible here
}

console.log(blockScopedVar); // Error: blockScopedVar is not defined
```

---

**d. Lexical Scope**(or Static Scope)

- JavaScript uses lexical scoping, meaning a function's `scope is determined by its location within the code during writing, not during execution`.
- Lexical scope means the scope of a variable is determined by its position in the source code.
- Functions have access to variables in their outer scope, even after the outer function has executed (**closures**).

Example:

```javascript
function outerFunction() {
    let outerVar = "Outer Scope";

    function innerFunction() {
        console.log(outerVar); // Accessing outer function's variable
    }

    innerFunction();
}

outerFunction(); // Output: Outer Scope
```

- **Closures** are functions that "remember" their lexical scope even after they are executed.
   - When a function returns another function, the returned function retains access to the variables from its parent scope, creating a closure.
   
---


| **Scope Type** | **Block-scoped** | **Hoisting** | **Global Object Attachment** | **Re-declaration Allowed  | **Re-assignment Allowed** | **Temporal Dead Zone (TDZ)** |
| -------------- | ---------------- | ------------ | ---------------------------- | ------------------------- | ------------------------- | ---------------------------- |
| **var**        | Function-scoped  | Yes          | Yes (`window` in browsers)   | **Yes**                   | Yes                       | No                           |
| **let**        | Block-scoped     | Yes          | No                           | **No**                    | Yes                       | Yes                          |
| **const**      | Block-scoped     | Yes          | No                           | **No**                    | No (must initialize)      | Yes                          |

---



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


---


#### **2. Scope Chaining**

When JavaScript `tries to access a variable, it starts with the current scope and works outward to parent scopes until it finds the variable`.

Example:

```javascript
let globalVar = "Global";

function parent() {
    let parentVar = "Parent";

    function child() {
        let childVar = "Child";
        console.log(globalVar, parentVar, childVar); // Global, Parent, Child
    }

    child();
}

parent();
```

---

3. **Best Practices**:
    
    - Declare variables and functions at the top of their scope for clarity.


---

### **Global Scope with `var`, `let`, and `const`**

1. **`var`**:
    
    - When a variable is declared with `var` at the top level (outside any function or block), it becomes a property of the **global object** (e.g., `window` in browsers).
    - Example:
    
    ```javascript
    var globalVar = "I am global";
    console.log(window.globalVar); // Accessible as a property of the global window object
    ```
    
2. **`let` and `const`**:
    
    - When you declare a variable with `let` or `const` at the top level, it is still in the **global scope**, but **it does NOT become a property of the global object**.
    - This means they are in the **global lexical environment** but do **not** attach to the `window` object.

### Example Demonstration:

```javascript
var globalVar = "var global";
let globalLet = "let global";
const globalConst = "const global";

console.log(window.globalVar); // "var global"
console.log(window.globalLet); // undefined
console.log(window.globalConst); // undefined
```

### **Why the Difference?**

This distinction exists because `let` and `const` were introduced in ES6 (ECMAScript 2015) with **block-scoping** and stricter handling to avoid polluting the global object, unlike `var`.

So:

- **`var` creates a global property on the global object**.
- **`let` and `const` respect block scoping and avoid attaching to `window`.**

This behavior makes your code less error-prone and prevents unintended global access.

---



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


---

```js
var a = 1;  
function b() {  
   a = 10;  
   return;  
   function a() {}  
}  
b();  
console.log(a);//o:  1
```


```js
function foo(){  
   function bar() {  
     return 3;  
   }  
   return bar();  
   function bar() {  
     return 8;  
   }  
}  
console.log(foo());//o: 8
```


```js


function example () {
  var x = 1
  let y = 2
  const z = 3
  
  // const x = 10
  //: SyntaxError: Identifier 'x' has already been declared
  
  if(true){
    var x = 4
    let y = 5
    
    console.log(x,y,z) //=> 4 5 3
  }
  
  
    console.log(x,y,z) //=> 4 2 3
    
    x = 7
    y = 8
    // z = 9 // TypeError: Assignment to constant variable.
}


example()

```