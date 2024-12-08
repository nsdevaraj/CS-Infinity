
### **Various Ways to Loop an Array in JavaScript**

1. **`for` Loop**:  
    Traditional approach for indexed iteration.
    
    ```javascript
    const arr = [1, 2, 3];
    for (let i = 0; i < arr.length; i++) {
      console.log(arr[i]);
    }
    ```
    

---

2. **`for...of` Loop**:  (es6+)
    Iterates over array values directly.
    
    ```javascript
    const arr = [1, 2, 3];
    for (const value of arr) {
      console.log(value);
    }
    ```
    

---

7. **`while` Loop**:  
    Iterates with manual control of index.
    
    ```javascript
    const arr = [1, 2, 3];
    let i = 0;
    while (i < arr.length) {
      console.log(arr[i]);
      i++;
    }
    ```
    

---

8. **`do...while` Loop**:  
    Executes at least once, regardless of condition.
    
    ```javascript
    const arr = [1, 2, 3];
    let i = 0;
    do {
      console.log(arr[i]);
      i++;
    } while (i < arr.length);
    ```
    



* can also use higher order functions.. 

---

### **Summary Table**

| **Method**        | **Description**                               | **Use Case**                       | **Mutates Array?** |
| ----------------- | --------------------------------------------- | ---------------------------------- | ------------------ |
| `for` Loop        | Iterates using indices.                       | Precise control over loop logic.   | No                 |
| `for...of`        | Iterates over array values.                   | Simplified value iteration.        | No                 |
| `while` Loop      | Iterates with a manual condition.             | Dynamic condition-based iteration. | No                 |
| `do...while` Loop | Ensures at least one iteration.               | Guaranteed initial execution.      | No                 |



### **Array Higher-Order Functions (HOCs) in JavaScript**

Array Higher-Order Functions (HOCs) are methods that operate on arrays and take a callback function as an argument to process array elements. These functions abstract common iteration patterns, making the code more expressive and concise.

---



### **`for...in` vs `for...of` in JavaScript**

|**Aspect**|**`for...in`**|**`for...of`**|
|---|---|---|
|**Purpose**|Iterates over enumerable **keys (properties)** of an object (including arrays).|Iterates over **values** of an iterable (arrays, strings, etc.).|
|**Iterates Over**|Keys (property names).|Values (array elements, string characters, etc.).|
|**Use Case**|Best for objects.|Best for iterables (arrays, strings, maps, etc.).|
|**Output**|Returns the keys/indexes as strings.|Returns the actual value of each element.|
|**Can Iterate Arrays?**|Yes, but returns indices as strings (not ideal).|Yes, iterates array elements.|
|**Suitable for Objects?**|Yes.|No, throws error if object is not iterable.|
|**Includes Inherited Properties?**|Yes.|No, iterates only over the actual iterable.|

---

### **Detailed Examples**

1. **`for...in` Example** (Objects and Arrays):
    
    ```javascript
    const obj = { a: 1, b: 2 };
    for (let key in obj) {
      console.log(key, obj[key]); // Logs keys (a, b) and values (1, 2)
    }
    
    const arr = [10, 20, 30];
    for (let index in arr) {
      console.log(index); // Logs "0", "1", "2" (as strings)
      console.log(arr[index]); // Logs 10, 20, 30
    }
    ```
    
2. **`for...of` Example** (Arrays and Strings):
    
    ```javascript
    const arr = [10, 20, 30];
    for (let value of arr) {
      console.log(value); // Logs 10, 20, 30
    }
    
    const str = 'hello';
    for (let char of str) {
      console.log(char); // Logs h, e, l, l, o
    }
    ```
    
3. **Inherited Properties**:
    
    ```javascript
    Object.prototype.extra = 'inherited';
    const obj = { a: 1 };
    for (let key in obj) {
      console.log(key); // Logs "a" and "extra" (inherited property)
    }
    for (let value of Object.keys(obj)) {
      console.log(value); // Logs "a" only (ignores inherited properties)
    }
    ```
    

---

### **Key Differences**

|**Feature**|**`for...in`**|**`for...of`**|
|---|---|---|
|Iterates Properties/Keys|Yes|No|
|Iterates Values|No|Yes|
|Suitable for Arrays|No (keys as strings)|Yes|
|Suitable for Objects|Yes|No (objects are not iterable by default)|

---

### **When to Use**

- **Use `for...in`**: For iterating over object properties.
- **Use `for...of`**: For iterating over iterable data structures like arrays, strings, and maps.


![[Pasted image 20241208162524.png]]

