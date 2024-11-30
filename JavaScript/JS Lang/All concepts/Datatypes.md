


### datatypes


In JavaScript, **data types** can be categorized into **primitive types** and **non-primitive types (also known as reference types)**.

### 1. **Primitive Data Types**
Primitive data types are immutable (their values cannot be changed after they're created), and they are directly assigned to variables. They include:

1. **Number**:
   - Represents both integer and floating-point numbers.
   - Example: `let age = 25;`, `let temperature = 98.6;`

2. **String**:
   - Represents a sequence of characters (text).
   - Strings can be enclosed in single quotes (`'...'`), double quotes (`"..."`), or backticks (`` `...` ``).
   - Example: `let name = "John";`, `let greeting = 'Hello, world!';`

3. **Boolean**:
   - Represents one of two values: `true` or `false`.
   - Example: `let isActive = true;`, `let isDone = false;`

4. **Undefined**:
   - A variable that has been declared but has not been assigned a value is automatically given the value `undefined`.
   - Example: `let x;` (x is undefined).

5. **Null**:
   - Represents the intentional absence of any object value. It is a special value that is not equivalent to `undefined`.
   - Example: `let person = null;`

6. **Symbol** (ES6):
   - Represents a unique, immutable value that can be used as an identifier for object properties.
   - Example: `let sym = Symbol('description');`

7. **BigInt** (ES11/ES2020):
   - Represents large integers that cannot be represented by the regular `Number` type.
   - Example: `let bigIntValue = 1234567890123456789012345678901234567890n;`

### 2. **Non-Primitive Data Types (Reference Types)**
Reference types are objects that store references to their values, and they can be modified after they're created. They include:

1. **Object**:
   - Represents a collection of key-value pairs, where keys are strings (or Symbols) and values can be any data type (including other objects).
   - Example: 
     ```javascript
     let person = {
       name: "Alice",
       age: 30
     };
     ```

2. **Array** (a type of Object):
   - A special kind of object used for storing ordered collections of data (indexed by integers).
   - Example:
     ```javascript
     let numbers = [1, 2, 3, 4];
     ```

3. **Function** (a type of Object):
   - Functions in JavaScript are also objects, and they are callable blocks of code.
   - Example:
     ```javascript
     function greet(name) {
       return `Hello, ${name}!`;
     }
     ```

4. **Date**:
   - Represents date and time in JavaScript.
   - Example:
     ```javascript
     let currentDate = new Date();
     ```

5. **RegExp** (Regular Expression):
   - Represents a pattern used for matching character combinations in strings.
   - Example:
     ```javascript
     let regex = /hello/i; // case-insensitive "hello" pattern
     ```

### Summary Table:

| **Data Type**   | **Category**       | **Description**                                          | **Example**                               |
|-----------------|--------------------|----------------------------------------------------------|-------------------------------------------|
| **Number**      | Primitive          | Numeric values (integers, floats)                        | `let x = 42;`                             |
| **String**      | Primitive          | Sequence of characters (text)                            | `let name = "Alice";`                     |
| **Boolean**     | Primitive          | `true` or `false`                                        | `let isActive = true;`                    |
| **Undefined**   | Primitive          | Variable declared but not assigned a value               | `let x;`                                  |
| **Null**        | Primitive          | Represents the intentional absence of any object value   | `let person = null;`                      |
| **Symbol**      | Primitive (ES6)    | Represents a unique identifier                           | `let sym = Symbol('description');`        |
| **BigInt**      | Primitive (ES2020) | Represents large integers                                | `let bigIntValue = 123n;`                 |
| **Object**      | Non-Primitive      | Collection of key-value pairs                            | `let obj = { name: "Alice" };`            |
| **Array**       | Non-Primitive      | Ordered collection of values                             | `let arr = [1, 2, 3];`                    |
| **Function**    | Non-Primitive      | A block of code that can be called                       | `let greet = (name) => 'Hello ' + name;`  |
| **Date**        | Non-Primitive      | Represents date and time                                 | `let today = new Date();`                 |
| **RegExp**      | Non-Primitive      | Represents a regular expression pattern                  | `let pattern = /abc/i;`                   |

### Type Conversion:
JavaScript allows you to convert between different types using functions like:
- **String()**: Converts a value to a string.
- **Number()**: Converts a value to a number.
- **Boolean()**: Converts a value to a boolean.

Example of type conversion:
```javascript
let str = "123";
let num = Number(str); // converts "123" to 123
let booleanValue = Boolean(0); // converts 0 to false
```

### Conclusion:
Understanding JavaScript data types is crucial for writing efficient, bug-free code. Primitive types are simple and immutable, while reference types (like objects and arrays) offer more complexity and flexibility.




to check {


NaN

isNaN



}
