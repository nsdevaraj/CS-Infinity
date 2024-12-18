

React Hooks are categorized based on their use cases, enabling developers to manage state, side effects, performance optimizations, and reusable logic efficiently.



![[Map of Hooks.png]]




---

### **State Management Hooks**

- **`useState`**: Adds state to functional components.
    
    ```jsx
    const [count, setCount] = useState(0);
    ```
    
- **`useReducer`**: Handles complex state logic with a reducer.
    
    ```jsx
    const [state, dispatch] = useReducer(reducer, initialState);
    ```
    
- **`useSyncExternalStore`**: Synchronizes state with external stores.

---

### **Effect Hooks**

- **`useEffect`**: Handles side effects (e.g., fetching data, DOM updates).
    
    ```jsx
    useEffect(() => { fetchData(); }, [dependency]);
    ```
    
- **`useLayoutEffect`**: Like `useEffect`, but fires after all DOM mutations.
- **`useInsertionEffect`**: For injecting styles before DOM painting (React 18+).

---

### **Ref Hooks**

- **`useRef`**: Creates a reference to DOM elements or mutable values.
    
    ```jsx
    const inputRef = useRef();  
    inputRef.current.focus();
    ```
    
- **`useImperativeHandle`**: Customizes instance values when using `ref`.

---

### **Context Hooks**

- **`useContext`**: Accesses React Context values directly.
    
    ```jsx
    const theme = useContext(ThemeContext);
    ```
    

---

### **Performance Hooks**

- **`useMemo`**: Memoizes values to prevent unnecessary computations.
    
    ```jsx
    const result = useMemo(() => expensiveCalculation(), [dependencies]);
    ```
    
- **`useCallback`**: Memoizes functions to avoid recreating them unnecessarily.
    
    ```jsx
    const handleClick = useCallback(() => doSomething(), [dependency]);
    ```
    

---

### **Transition Hooks** (React 18+)

- **`useTransition`**: Defers state updates to prioritize UI responsiveness.
- **`useDeferredValue`**: Defers a value update to optimize performance.

---

### **Random Hooks**

- **`useDebugValue`**: Adds custom labels to React DevTools for debugging.
- **`useId`**: Generates unique IDs for accessibility and server-side rendering.

---

### **React 19 Hooks** (Upcoming Features)

- **`useFormStatus`**: Manages form status in concurrent rendering.
- **`useFormState`**: Handles form state more efficiently.
- **`useOptimistic`**: Optimistically updates the UI for faster interactions.
- **`use`**: Suspends a component until a promise resolves.

---

### **Key Notes**

1. Hooks **must be called at the top level** of functional components.
2. Custom hooks (`useCustomHook`) allow you to encapsulate and reuse stateful logic.
3. Use hooks like `useMemo` and `useCallback` only when **performance optimization** is necessary.


---


### **1. How React Identifies Hooks vs Normal Functions**

React identifies **Hooks** (e.g., `useState`, `useEffect`) because:

- They **start with the word "use"** (e.g., `useSomething`).
- Hooks are part of React's **internal implementation** and must follow **specific rules**.

**Example:**

```javascript
function useCustomHook() {
  const [value, setValue] = useState(0); // Valid Hook
}
```

React **recognizes** `useState` because it adheres to the naming convention and is part of the React library.

---

### **2. What Happens if Hooks Are Not at the Top Level**

Hooks **must be called at the top level** of a component or a custom Hook:

- **Top-level** means no conditional statements, loops, or nested functions.

If violated:

1. React cannot **preserve the Hook's state** across renders.
2. It may lead to **unexpected behavior** or errors.

**Invalid Example:**

```javascript
function Component() {
  if (true) {
    const [count, setCount] = useState(0); // ❌ This will break React's rules
  }
}
```

React **relies on the order of Hooks** being consistent across renders. Breaking this rule disrupts the Hook execution sequence.

**Valid Example:**

```javascript
function Component() {
  const [count, setCount] = useState(0); // ✅ Top-level
  return <div>{count}</div>;
}
```

---

### **Key Takeaways**

1. **Hooks vs Normal Functions**: Hooks start with "use" and follow React's internal API.
2. **Top-Level Rule**: Hooks must always be called in the same order and at the top level to ensure React can manage their state properly. 🚀



\
#### 33. **What are React hooks rules, and why are they important?**
**Answer**:
React hooks have specific rules that ensure consistent behavior:
1. **Only call hooks at the top level**: Do not call hooks inside loops, conditions, or nested functions. This ensures that hooks are called in the same order each time a component renders.
2. **Only call hooks from React functions**: Hooks should only be called within React functional components or custom hooks.

**Why they are important**:
Following these rules prevents unpredictable behavior and ensures that React can track hooks properly, maintaining their state between renders.

**Concept Explanation**:
These rules help React’s hook mechanism remain predictable and error-free, avoiding issues with state management and component behavior.

