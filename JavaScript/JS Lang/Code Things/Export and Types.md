
### **1. Types of Export**

- **Named Exports**: Export multiple values by name.
- **Default Exports**: Export a single value as the default.

---

### **2. Syntax Examples**

#### **Named Export**

```javascript
export const add = (a, b) => a + b;
export const subtract = (a, b) => a - b;

// Import
import { add, subtract } from './math.js';
```

#### **Default Export**

```javascript
export default function multiply(a, b) {
  return a * b;
}

// Import
import multiply from './math.js';
```

---

### **3. Rules for `export`**

- **Named Exports**:
    - Multiple named exports allowed in a file.
    - Use `{}` to import specific names.
- **Default Export**:
    - Only one default export allowed per file.
    - Name can differ during import.

---

### **4. Mixing Named and Default**

```javascript
export const divide = (a, b) => a / b;
export default function add(a, b) {
  return a + b;
}

// Import
import add, { divide } from './math.js';
```

---

### **5. Re-exporting**

Re-export values from another module.

```javascript
export { add, subtract } from './math.js';
```

---

### **6. Dynamic Import**

Imports modules dynamically, useful for lazy loading.

```javascript
const module = await import('./math.js');
console.log(module.add(2, 3));
```

---


### **1. Difference Between Named and Default Exports**

|**Named Export**|**Default Export**|
|---|---|
|Can export multiple values.|Exports a single value.|
|Imported using `{}` with the exact name.|Imported without `{}`, any name can be used.|
|Example: `export const value = 42;`|Example: `export default value;`|

---

### **2. Using `export` with Classes, Objects, or Functions**

- **Class**
    
    ```javascript
    export class MyClass {
      greet() { console.log("Hello!"); }
    }
    ```
    
- **Object**
    
    ```javascript
    export const config = { env: "production", version: "1.0" };
    ```
    
- **Function**
    
    ```javascript
    export function greet() { console.log("Hello World!"); }
    ```
    

---

### **3. Error When Importing Without an `export`**

- **Scenario:** Trying to import a variable or function that was not exported.
- **Error:** `Uncaught SyntaxError: The requested module does not provide an export named 'example'.`
- **Solution:** Ensure the module explicitly exports the value.

---

### **4. Importing Everything Using `import * as`**

- **Syntax:**
    
    ```javascript
    import * as utils from './math.js';
    console.log(utils.add(2, 3)); // Access exports via namespace
    ```
    
- **Use Case:** Useful when working with multiple exports but want a single namespace.

### **Behavior of `import * as`**

1. **Named Exports**
    
    - All named exports are included under the namespace object (`utils` in this case).
2. **Default Export**
    
    - The default export is not included as part of the namespace object. To access it, you need a separate default import.

---

### **Example with Named and Default Exports**

#### `math.js`

```javascript
export const add = (a, b) => a + b; // Named export
export const subtract = (a, b) => a - b; // Named export
export default function multiply(a, b) { // Default export
  return a * b;
}
```

#### Importing

```javascript
import * as utils from './math.js'; // Namespace for named exports
import multiply from './math.js';   // Separate import for default export

console.log(utils.add(2, 3));       // Access named export: 5
console.log(utils.subtract(5, 2));  // Access named export: 3
console.log(multiply(2, 3));        // Access default export: 6
```

### **Key Notes**

- **`import * as`** is for gathering named exports.
- Default exports must be imported separately, as they are not part of the namespace object.