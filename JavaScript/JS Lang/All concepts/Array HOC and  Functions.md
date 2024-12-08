


### **Common Array HOCs**

1. **`forEach`**  
    Executes a provided callback function once for each array element.  
    **Key Points**:
    
    - Does not return a value.
    - Primarily used for side effects like logging or modifying external variables.
    
    **Example:**
    
    ```javascript
    const arr = [1, 2, 3];
    arr.forEach(value => console.log(value));
    ```
    

---

2. **`map`**  
    Creates a new array by applying a callback function to each element.  
    **Key Points**:
    
    - Always returns a new array.
    - Ideal for data transformation.
    
    **Example:**
    
    ```javascript
    const arr = [1, 2, 3];
    const squared = arr.map(value => value * value);
    console.log(squared); // [1, 4, 9]
    ```
    

---

3. **`filter`**  
    Creates a new array with elements that pass a given condition.  
    **Key Points**:
    
    - Always returns a subset (or empty array).
    - Does not modify the original array.
    
    **Example:**
    
    ```javascript
    const arr = [1, 2, 3];
    const even = arr.filter(value => value % 2 === 0);
    console.log(even); // [2]
    ```
    

---

4. **`reduce`**  
    Reduces the array to a single value by iteratively applying a callback.  
    **Key Points**:
    
    - Requires an initial accumulator value.
    - Can perform operations like sum, product, or constructing objects.
    
    **Example:**
    
    ```javascript
    const arr = [1, 2, 3];
    const sum = arr.reduce((acc, value) => acc + value, 0);
    console.log(sum); // 6
    ```
    

---

5. **`find`**  
    Returns the first element that satisfies a condition.  
    **Key Points**:
    
    - Returns the element or `undefined` if no match is found.
    
    **Example:**
    
    ```javascript
    const arr = [1, 2, 3];
    const found = arr.find(value => value > 2);
    console.log(found); // 3
    ```
    

---

6. **`some` and `every`**
    
    - **`some`**: Returns `true` if at least one element matches the condition.
    - **`every`**: Returns `true` only if all elements match the condition.
    
    **Example:**
    
    ```javascript
    const arr = [1, 2, 3];
    console.log(arr.some(value => value > 2)); // true
    console.log(arr.every(value => value > 0)); // true
    ```
    

---

7. **`sort`**  
    Sorts the array in place based on a comparator function.  
    **Key Points**:
    
    - Mutates the original array.
    - Defaults to lexicographical order for strings.
    
    **Example:**
    
    ```javascript
    const arr = [3, 1, 2];
    arr.sort((a, b) => a - b); // Ascending order
    console.log(arr); // [1, 2, 3]
    ```
    

---

### **Comparison Table**

|**HOC**|**Returns**|**Use Case**|**Modifies Array?**|
|---|---|---|---|
|`forEach`|`undefined`|Perform side effects.|No|
|`map`|New array|Transform data.|No|
|`filter`|New subset array|Extract elements.|No|
|`reduce`|Single value|Aggregate/accumulate data.|No|
|`find`|First matching element|Find an element.|No|
|`some`|Boolean (`true/false`)|Check if any element matches.|No|
|`every`|Boolean (`true/false`)|Check if all elements match.|No|
|`sort`|Original array (mutated)|Arrange elements in an order.|Yes|

---

### **Key Takeaways**

- Array HOCs make code expressive and readable.
- `map`, `filter`, and `reduce` are the most commonly used.
- Always check if the HOC mutates the array (`sort`) or creates a new one (`map`, `filter`).






### Higher-Order Functions
A higher-order function is defined as a function that either takes one or more functions as arguments or returns a function. Among the 14 methods mentioned, the following are higher-order functions:

1. **forEach()**
2. **map()**
3. **filter()**
4. **reduce()**
5. **some()**
6. **every()**
7. **find()**
8. **findIndex()**

### Non-Higher-Order Functions
The following methods do not take a function as an argument and are not classified as higher-order functions:

9. **includes()**: Checks for the presence of a value.
10. **splice()**: Modifies the array in place.
11. **slice()**: Creates a shallow copy of a portion of the array.
12. **concat()**: Merges two or more arrays.
13. **sort()**: Sorts the elements of an array.
14. **reverse()**: Reverses the order of elements in the array.

### Summary
Only the first eight methods are considered higher-order functions because they involve passing functions as arguments or returning functions. The rest are useful array manipulation methods but do not meet the criteria for higher-order functions.


Yes, there are a few additional higher-order array methods in JavaScript that are useful for various operations. Here are some of the noteworthy ones:

### 9. **Array.includes()**
- **Purpose**: Determines whether an array includes a certain value among its entries.
- **Usage**: Useful for checking if a specific element is present in the array.
- **Returns**: `true` if the value exists, otherwise `false`.
- **Example**:
  ```javascript
  const numbers = [1, 2, 3];
  const hasTwo = numbers.includes(2);
  console.log(hasTwo); // Outputs: true
  ```

### 10. **Array.splice()**
- **Purpose**: Changes the contents of an array by removing or replacing existing elements and/or adding new elements in place.
- **Usage**: Useful for modifying the array directly.
- **Returns**: An array containing the removed elements (if any).
- **Example**:
  ```javascript
  const numbers = [1, 2, 3, 4];
  const removed = numbers.splice(1, 2); // Removes 2 elements starting at index 1
  console.log(numbers); // Outputs: [1, 4]
  console.log(removed); // Outputs: [2, 3]
  ```

### 11. **Array.slice()**
- **Purpose**: Returns a shallow copy of a portion of an array into a new array object.
- **Usage**: Useful for creating subarrays without modifying the original.
- **Returns**: A new array with the sliced elements.
- **Example**:
  ```javascript
  const numbers = [1, 2, 3, 4];
  const sliced = numbers.slice(1, 3); // Returns elements from index 1 to 3 (excluding 3)
  console.log(sliced); // Outputs: [2, 3]
  ```

### 12. **Array.concat()**
- **Purpose**: Merges two or more arrays into a new array.
- **Usage**: Useful for combining arrays.
- **Returns**: A new array that is the combination of the original arrays.
- **Example**:
  ```javascript
  const numbers1 = [1, 2];
  const numbers2 = [3, 4];
  const combined = numbers1.concat(numbers2);
  console.log(combined); // Outputs: [1, 2, 3, 4]
  ```

### 13. **Array.sort()**
- **Purpose**: Sorts the elements of an array in place and returns the sorted array.
- **Usage**: Useful for ordering elements.
- **Returns**: The sorted array.
- **Example**:
  ```javascript
  const numbers = [3, 1, 4, 2];
  numbers.sort(); // Sorts in place (alphabetical by default)
  console.log(numbers); // Outputs: [1, 2, 3, 4]
  ```

### 14. **Array.reverse()**
- **Purpose**: Reverses the elements of an array in place.
- **Usage**: Useful for reversing the order of elements.
- **Returns**: The reversed array.
- **Example**:
  ```javascript
  const numbers = [1, 2, 3];
  numbers.reverse();
  console.log(numbers); // Outputs: [3, 2, 1]
  ```

### Summary
These additional methods enhance the functionality of arrays in JavaScript, allowing for greater manipulation and analysis. They provide essential tools for everyday programming tasks, making data handling more intuitive and efficient. Understanding and using these higher-order functions effectively can greatly improve your coding practices.



### **All Array Methods in JavaScript (Crisp)**

#### **Mutating Methods**

These methods modify the original array.

|**Method**|**Description**|**Example**|
|---|---|---|
|`push()`|Adds elements to the end of an array.|`arr.push(4);`|
|`pop()`|Removes the last element from an array.|`arr.pop();`|
|`unshift()`|Adds elements to the beginning of an array.|`arr.unshift(0);`|
|`shift()`|Removes the first element from an array.|`arr.shift();`|
|`splice()`|Adds/removes elements at a specific index.|`arr.splice(1, 1, 4);`|
|`sort()`|Sorts elements in place (default is lexicographical order).|`arr.sort((a, b) => a - b);`|
|`reverse()`|Reverses the array in place.|`arr.reverse();`|
|`fill()`|Fills all or part of an array with a static value.|`arr.fill(0, 1, 3);`|
|`copyWithin()`|Copies part of an array to another location within the same array.|`arr.copyWithin(1, 3);`|

---

#### **Non-Mutating Methods**

These methods do not modify the original array and often return a new one.

|**Method**|**Description**|**Example**|
|---|---|---|
|`concat()`|Combines two or more arrays into a new array.|`arr.concat([4, 5]);`|
|`slice()`|Extracts a portion of the array into a new array.|`arr.slice(1, 3);`|
|`map()`|Creates a new array by applying a function to each element.|`arr.map(x => x * 2);`|
|`filter()`|Creates a new array with elements that pass a condition.|`arr.filter(x => x > 2);`|
|`reduce()`|Reduces the array to a single value using a function.|`arr.reduce((a, b) => a + b, 0);`|
|`reduceRight()`|Similar to `reduce` but iterates from right to left.|`arr.reduceRight((a, b) => a - b);`|
|`flat()`|Flattens nested arrays to the specified depth.|`[[1], [2]].flat();`|
|`flatMap()`|Maps and flattens the array in one step.|`arr.flatMap(x => [x, x * 2]);`|
|`join()`|Joins all array elements into a string.|`arr.join('-');`|
|`includes()`|Checks if an array contains a specific value.|`arr.includes(2);`|
|`indexOf()`|Returns the first index of a value, or `-1` if not found.|`arr.indexOf(3);`|
|`lastIndexOf()`|Returns the last index of a value, or `-1` if not found.|`arr.lastIndexOf(3);`|
|`every()`|Checks if all elements pass a test.|`arr.every(x => x > 0);`|
|`some()`|Checks if at least one element passes a test.|`arr.some(x => x > 2);`|
|`find()`|Returns the first element that satisfies a condition.|`arr.find(x => x > 2);`|
|`findIndex()`|Returns the index of the first element that satisfies a condition.|`arr.findIndex(x => x > 2);`|
|`keys()`|Returns an iterator for the array's keys (indices).|`for (let key of arr.keys());`|
|`values()`|Returns an iterator for the array's values.|`for (let value of arr.values());`|
|`entries()`|Returns an iterator for key-value pairs in the array.|`for (let [i, v] of arr.entries());`|
|`toString()`|Converts the array to a string.|`arr.toString();`|
|`toLocaleString()`|Converts array elements to a locale-sensitive string.|`arr.toLocaleString();`|

---

#### **ES6+ Additions**

|**Method**|**Description**|**Example**|
|---|---|---|
|`from()`|Creates an array from an iterable or array-like object.|`Array.from('123');`|
|`of()`|Creates a new array from arguments.|`Array.of(1, 2, 3);`|

---

### **Key Takeaways**

1. **Mutating methods** change the original array (`push`, `pop`, `sort`).
2. **Non-mutating methods** return new arrays or values (`map`, `filter`, `slice`).
3. Choose the method based on whether you want to preserve the original array.


