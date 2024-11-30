
### **5. Control Structures**

- **Conditional Statements:**
  - `if`, `else if`, and `else` control flow based on conditions.
  - **Ternary Operator** provides a shorthand for simple conditions: `condition ? expr1 : expr2`.

  ```javascript
  let score = 85;
  let grade = score > 60 ? "Pass" : "Fail"; // Ternary operator example
  ```

- **Loops:**
  - **`for` loop**: Commonly used for a set number of iterations.
  - **`while` loop**: Continues as long as a condition is true.
  - **`do...while` loop**: Executes at least once before checking the condition.
  - **`for...of` loop**: Iterates over iterable objects (arrays, strings).
  - **`for...in` loop**: Iterates over object properties.

  ```javascript
  // for loop
  for (let i = 0; i < 5; i++) {
      console.log(i); // Outputs numbers 0 to 4
  }

  // while loop
  let count = 3;
  while (count > 0) {
      console.log(count); // Outputs 3, 2, 1
      count--;
  }
  ```
