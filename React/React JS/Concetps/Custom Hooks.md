

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

