
### Key Points
- JavaScript modules allow code sharing across files.
- Use `export` to expose functions and `import` to bring them into another file.

### Code Example
Module example:

**module.js**
```javascript
export const greet = (name) => {
    return `Hello, ${name}!`;
};
```

**main.js**
```javascript
import { greet } from './module.js';

console.log(greet('Alice'));
```

### Explanation
- The `greet` function is exported from `module.js` and imported into `main.js`.



As your JavaScript code grows, you can use **modules** to share code between files. By default, code in a module is private to that file. To export functions for use elsewhere, you can create a default export.

#### Example of Module Export/Import

**In `math.js`:**
```javascript
export const add = (a, b) => a + b;
export const subtract = (a, b) => a - b;

// Default export
const multiply = (a, b) => a * b;
export default multiply;
```

**In `app.js`:**
```javascript
import multiply, { add, subtract } from './math.js';

console.log(add(2, 3)); // 5
console.log(subtract(5, 2)); // 3
console.log(multiply(2, 3)); // 6
```


* by default all module things are private.. 

