
### 🚫 Why JavaScript Sucks

- **No Type Safety** – Dynamically typed, so type bugs show up at runtime.
- **Weird Type Coercion** – Confusing behavior like:

    ```js
    [] + {} // "[object Object]"
    null == undefined // true
    ```

- **Runtime Errors** – No warnings when accessing `undefined`:

    ```js
    let x;
    x.foo; // 💥 TypeError
    ```

- **Poor IDE Support** – Without types, autocomplete and refactoring are unreliable in large projects.


---

### ✅ Why TypeScript Is Better

- **Static Typing** – Catches bugs before runtime.
- **Great IDE Support** – Autocomplete, real-time type checking, and safe refactoring.


---

### ⚠️ But TypeScript Also Sucks

- **False Sense of Safety** – Types vanish at runtime. Still JS under the hood.
    
    ```ts
    const user = JSON.parse('{}') as { name: string };
    user.name.toUpperCase(); // 💥 Runtime error
    ```
    
- **Complexity Overhead** – Setup (tsconfig, types), compile steps, and steep learning curve for advanced types.


---

TypeScript emerged to fix JavaScript’s shortcomings - like lack of type safety and tooling- but at the same time, JavaScript itself has been evolving and fixing many of its own issues in parallel.

---
Before implementing anything, it's crucial to first decide:
- **What does JavaScript execute after compilation?**
- **What does TypeScript offer that JavaScript lacks

---

