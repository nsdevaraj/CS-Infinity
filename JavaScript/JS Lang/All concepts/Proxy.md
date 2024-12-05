


### **39. Explain the use of `Proxy` in JavaScript.**

#### **Answer:**

- A `Proxy` allows you to intercept and customize operations on objects.

```javascript
const obj = { a: 1 };
const proxy = new Proxy(obj, {
  get(target, prop) {
    return prop in target ? target[prop] : 'Default';
  }
});
console.log(proxy.a); // 1
console.log(proxy.b); // "Default"
```




### Proxy in JavaScript: An Overview

The `Proxy` object in JavaScript enables you to create a "proxy" for another object. It allows you to intercept and redefine fundamental operations for the target object, such as reading, writing, and deleting properties. Proxies are widely used for tasks like validation, logging, data binding, and lazy initialization.

---

### **Definition**

```javascript
const proxy = new Proxy(target, handler);
```

- **`target`**: The original object (can be any object, array, or function) to wrap with the proxy.
- **`handler`**: An object containing traps (interceptable operations like `get`, `set`, etc.) that define custom behaviors.

---

### **Key Traps**

Here are the most common traps and their uses:

1. **`get`**: Intercept property access.
    
    ```javascript
    const obj = { name: "John", age: 30 };
    const proxy = new Proxy(obj, {
        get(target, property) {
            console.log(`Getting property '${property}'`);
            return target[property];
        }
    });
    
    console.log(proxy.name); // Logs: "Getting property 'name'" and returns "John"
    ```
    
2. **`set`**: Intercept property assignments.
    
    ```javascript
    const proxy = new Proxy({}, {
        set(target, property, value) {
            console.log(`Setting property '${property}' to '${value}'`);
            target[property] = value;
            return true; // Must return true to indicate success
        }
    });
    
    proxy.age = 25; // Logs: "Setting property 'age' to '25'"
    ```
    
3. **`has`**: Intercept `in` operator.
    
    ```javascript
    const proxy = new Proxy({ name: "John" }, {
        has(target, property) {
            console.log(`Checking if property '${property}' exists`);
            return property in target;
        }
    });
    
    console.log('name' in proxy); // Logs: "Checking if property 'name' exists" and returns true
    ```
    
4. **`deleteProperty`**: Intercept `delete` operator.
    
    ```javascript
    const proxy = new Proxy({ name: "John" }, {
        deleteProperty(target, property) {
            console.log(`Deleting property '${property}'`);
            delete target[property];
            return true;
        }
    });
    
    delete proxy.name; // Logs: "Deleting property 'name'"
    ```
    
5. **`apply`**: Intercept function calls (for function targets).
    
    ```javascript
    const sum = (a, b) => a + b;
    const proxy = new Proxy(sum, {
        apply(target, thisArg, args) {
            console.log(`Called with arguments: ${args}`);
            return target(...args);
        }
    });
    
    console.log(proxy(3, 5)); // Logs: "Called with arguments: 3,5" and returns 8
    ```
    
6. **`construct`**: Intercept `new` operator (for function targets).
    
    ```javascript
    class User {
        constructor(name) {
            this.name = name;
        }
    }
    
    const ProxyUser = new Proxy(User, {
        construct(target, args) {
            console.log(`Creating new instance with arguments: ${args}`);
            return new target(...args);
        }
    });
    
    const user = new ProxyUser("Alice"); // Logs: "Creating new instance with arguments: Alice"
    ```
    

---

### **Use Cases in Interviews**

1. **Validation**: Ensure property assignments meet certain criteria.
    
    ```javascript
    const user = {};
    const proxy = new Proxy(user, {
        set(target, property, value) {
            if (property === 'age' && (typeof value !== 'number' || value <= 0)) {
                throw new Error("Invalid age");
            }
            target[property] = value;
            return true;
        }
    });
    
    proxy.age = 25; // Works
    // proxy.age = -5; // Throws "Invalid age"
    ```
    
2. **Logging**: Debug property accesses and modifications.
    
    ```javascript
    const obj = { name: "John" };
    const proxy = new Proxy(obj, {
        get(target, property) {
            console.log(`Accessed property: ${property}`);
            return target[property];
        },
        set(target, property, value) {
            console.log(`Changed property: ${property} to ${value}`);
            target[property] = value;
            return true;
        }
    });
    
    proxy.name; // Logs: Accessed property: name
    proxy.name = "Doe"; // Logs: Changed property: name to Doe
    ```
    
3. **Default Values**: Provide default values for undefined properties.
    
    ```javascript
    const defaultHandler = {
        get(target, property) {
            return property in target ? target[property] : `Default value for ${property}`;
        }
    };
    
    const obj = { name: "Alice" };
    const proxy = new Proxy(obj, defaultHandler);
    
    console.log(proxy.name); // "Alice"
    console.log(proxy.age); // "Default value for age"
    ```
    
4. **Data Binding**: Useful for reactive frameworks.
    
    ```javascript
    const data = { value: 10 };
    const proxy = new Proxy(data, {
        set(target, property, value) {
            console.log(`Data updated: ${property} = ${value}`);
            target[property] = value;
            return true;
        }
    });
    
    proxy.value = 20; // Logs: Data updated: value = 20
    ```
    
5. **Immutable Object**: Prevent modifications.
    
    ```javascript
    const obj = { name: "Immutable" };
    const proxy = new Proxy(obj, {
        set() {
            throw new Error("Cannot modify immutable object");
        },
        deleteProperty() {
            throw new Error("Cannot delete properties");
        }
    });
    
    // proxy.name = "New"; // Throws "Cannot modify immutable object"
    // delete proxy.name; // Throws "Cannot delete properties"
    ```
    

---

### **Tips for Interviews**

1. **Highlight Use Cases**: Be ready to explain how proxies are used in real-world scenarios like frameworks (e.g., Vue.js reactive system) or middleware design.
    
2. **Demonstrate Understanding**: Show a good grasp of traps and their practical applications.
    
3. **Write Clean Code**: Structure examples clearly and avoid unnecessary complexity.
    

By mastering these patterns and traps, you'll stand out in interviews when discussing or coding with proxies.

