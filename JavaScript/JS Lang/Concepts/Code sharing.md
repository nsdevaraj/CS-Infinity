
## Sharing JS code


Code sharing between files in JavaScript can be accomplished through various methods, depending on the environment (like Node.js or the browser) and the module system being used. Here are some of the common techniques:

### 1. **Using Modules (ES6 Import/Export)**

In modern JavaScript, the ES6 module system allows you to export functions, objects, or variables from one file and import them into another.

**Example:**

**File: `math.js`**
```javascript
export const add = (a, b) => a + b;
export const subtract = (a, b) => a - b;
```

**File: `app.js`**
```javascript
import { add, subtract } from './math.js';

console.log(add(2, 3));       // Output: 5
console.log(subtract(5, 2));  // Output: 3
```

### 2. **CommonJS Modules (Node.js)**

In Node.js, the CommonJS module system is widely used. You use `module.exports` to export and `require()` to import modules.

**Example:**

**File: `math.js`**
```javascript
const add = (a, b) => a + b;
const subtract = (a, b) => a - b;

module.exports = { add, subtract };
```

**File: `app.js`**
```javascript
const { add, subtract } = require('./math');

console.log(add(2, 3));       // Output: 5
console.log(subtract(5, 2));  // Output: 3
```

### 3. **Using `<script>` Tags in HTML (for Browser)**

In web development, you can share code between JavaScript files by including them in your HTML file using `<script>` tags. However, this approach is less modular than using ES6 or CommonJS modules.

**Example:**

**HTML File: `index.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="math.js"></script>
    <script src="app.js"></script>
</head>
<body>
    <script>
        console.log(add(2, 3)); // Output: 5 (assuming `add` is defined in math.js)
    </script>
</body>
</html>
```

### 4. **Bundlers (e.g., Webpack, Parcel)**

For larger applications, you may want to use a module bundler to manage dependencies and bundle files for production. Bundlers allow you to write modular code using ES6 imports/exports or CommonJS and handle the complexities of loading modules in the browser.

**Example:**
```javascript
// Using Webpack to bundle your JavaScript files
```

### 5. **Dynamic Imports**

You can dynamically import modules using the `import()` function, which allows you to load modules conditionally or on demand.

**Example:**

```javascript
async function loadMathModule() {
    const math = await import('./math.js');
    console.log(math.add(2, 3)); // Output: 5
}

loadMathModule();
```

### Conclusion

Sharing code between files in JavaScript can be done using various methods, with ES6 modules and CommonJS being the most popular in modern development. Bundlers and dynamic imports further enhance the modularity and flexibility of your code, making it easier to manage dependencies and optimize performance. Understanding these techniques is crucial for writing maintainable and scalable applications.


