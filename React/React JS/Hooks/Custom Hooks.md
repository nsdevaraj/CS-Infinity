
https://usehooks-ts.com/

https://usehooks.com/


A custom Hook is a JavaScript function whose name starts with 'use' and that may call other Hooks.







### **23. How do you create a custom React hook in TypeScript?**

#### **Answer:**

```typescript
import { useState } from "react";

function useToggle(initialValue: boolean): [boolean, () => void] {
  const [value, setValue] = useState(initialValue);
  const toggle = () => setValue(!value);
  return [value, toggle];
}
// Usage:
const [isVisible, toggleVisibility] = useToggle(false);
```





how react knows its custom hook func and its not!

React differentiates a custom hook from a regular function based on **naming conventions** and **how it's used**. Here's how React knows:

### 1. **Naming Convention:**

- React assumes a function is a **custom hook** if its name starts with the prefix `use`. For example:
    
    ```javascript
    function useMyCustomHook() {
      // Custom hook logic
    }
    ```
    
- This is a convention, but it also plays a critical role. React enforces rules for hooks (like calling them only at the top level of a component or another hook) based on this naming pattern.

### 2. **Rule of Hooks:**

- React uses a static code analysis tool (like ESLint's "Rules of Hooks") to check the following:
    - Hooks (like `useState`, `useEffect`, and custom hooks) must **always** be called:
        - At the top level of a React function component or another custom hook.
        - Never inside loops, conditions, or nested functions.
- By identifying a function that starts with `use`, React enforces these rules and treats it as a hook.

### 3. **Not a Special Syntax or Behavior:**

- There's no magical mechanism in React that distinguishes hooks from regular functions. The `use` prefix and usage context (called in a component or another hook) are what define a custom hook.

### What Happens Without `use`:

- If you don't name your custom hook starting with `use`, React won’t enforce the "Rules of Hooks" on it, and the function will be treated like a regular JavaScript function. This can lead to bugs if the function uses React hooks internally but isn't following the rules.

### Example:

#### Valid Custom Hook:

```javascript
function useCounter() {
  const [count, setCount] = React.useState(0);
  const increment = () => setCount((prev) => prev + 1);
  return { count, increment };
}

// Usage in a component
function CounterComponent() {
  const { count, increment } = useCounter();
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>Increment</button>
    </div>
  );
}
```

#### Regular Function (Not a Hook):

```javascript
function incrementValue(val) {
  return val + 1; // This is just a regular function.
}
```

React only applies the "Rules of Hooks" to functions starting with `use`, ensuring consistent behavior for hooks.



Yes, **Hooks must start with `use`** by convention.

React **enforces this rule** to:

1. **Identify hooks:** React relies on the naming convention (starting with `use`) to distinguish hooks from regular functions.
2. **Enable linting:** ESLint rules (e.g., `react-hooks/rules-of-hooks`) check if hooks follow the correct rules.

---

### **What If a Hook Doesn’t Start with `use`?**

If you write a function that behaves like a hook but doesn't start with `use`, React won't treat it as a hook:

- You’ll lose React's **automatic state and effect tracking**.
- Linting tools won't catch violations of the **Rules of Hooks**.
- You risk breaking the proper execution order of hooks.

---

### **Example:**

#### Invalid Custom Hook (no `use` prefix):

```javascript
function customState(initialValue) {
  return useState(initialValue); // ❌ React won't recognize this as a hook
}

function Example() {
  const [count, setCount] = customState(0); // Unexpected behavior or lint error
}
```

#### Correct Custom Hook:

```javascript
function useCustomState(initialValue) {
  return useState(initialValue); // ✅ React recognizes this as a hook
}

function Example() {
  const [count, setCount] = useCustomState(0); // Works as expected
}
```

---

### **Why Does React Require the `use` Prefix?**

1. It ensures **consistent behavior** when React runs hooks in a predictable order.
2. Tools like **ESLint** can statically analyze and enforce the Rules of Hooks.
3. It’s part of the **React design contract** to keep hooks recognizable and manageable.

🚨 **Bottom line**: If a function doesn’t start with `use`, React won’t treat it as a hook.


https://stackoverflow.com/questions/72851622/why-do-have-to-use-use-before-custom-hook-in-react


---

### **Key Benefits of Custom Hooks**

1. **Reusability**: Extract logic to share across multiple components.
2. **Readability**: Simplify complex components by moving logic to a separate hook.
3. **Testability**: Test hooks independently from components.
4. **Flexibility**: Compose hooks to build powerful, modular functionality.

By leveraging these custom hooks, you can write cleaner, reusable, and more efficient React code.

---



#### 35. **How do you implement a custom hook that shares logic between components?**
**Answer**:
A custom hook allows you to extract reusable logic. Start the hook's name with `use` and encapsulate logic using built-in hooks.

**Example**:
```javascript
import { useState, useEffect } from 'react';

function useFetchData(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(url)
      .then(response => response.json())
      .then(data => {
        setData(data);
        setLoading(false);
      });
  }, [url]);

  return { data, loading };
}

// Usage
function App() {
  const { data, loading } = useFetchData('https://api.example.com/data');

  if (loading) return <div>Loading...</div>;
  return <div>{JSON.stringify(data)}</div>;
}
```

**Concept Explanation**:
Custom hooks encapsulate logic that can be shared across different components, promoting reusability and clean code.

