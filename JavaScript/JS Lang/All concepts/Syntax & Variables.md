
### **4. Basic Syntax and Variables**

* use camelCase
* dynamically typed, no datatype needed while writing code ( loosely typed )
* a variable can contain any type of data on runtime 
* any value other than primitive type are object type
* semicolons are optional, js parser will put at end of line if you missed automatically

- **Variable Declarations:** Three keywords for variable declarations:
  - **`let`**: Block-scoped, can be reassigned.
  - **`const`**: Block-scoped, cannot be reassigned.
  - **`var`**: Function-scoped (hoisted), generally avoided in modern JavaScript due to scoping issues.

  ```javascript
  let count = 10;       // `let` allows reassignment
  const pi = 3.14;      // `const` cannot be reassigned
  var username = "JS";  // `var` is function-scoped and hoisted
  ```

- **Data Types in JavaScript:**
  - **Primitive Types(7)**: `Number`, `String`, `Boolean`, `null`, `undefined`, `Symbol`, `BigInt`.
  - **Reference Types**: Objects, Arrays, and Functions.
  
  ```javascript
  let age = 25;              // Number
  let name = "Alice";        // String
  let isAdmin = true;        // Boolean
  let data = { key: "value" }; // Object
  ```

* undefined is default value for any variable
* null represent empty for any vairable

- **Type Checking and Conversion:**
  - `typeof` operator checks the data type.
  - JavaScript allows implicit type coercion (e.g., combining numbers and strings).

  ```javascript
  console.log(typeof 10);          // "number"
  console.log("5" + 5);            // "55" (string concatenation)
  ```



Intialization done:

```ts

const ary1 :number = [], ary2:number[];
```
