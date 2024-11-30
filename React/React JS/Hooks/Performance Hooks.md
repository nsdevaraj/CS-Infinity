

### **4. Performance Hooks**

Performance Hooks in React are designed to optimize the performance of your applications, particularly for expensive computations and to prevent unnecessary re-renders. The primary hooks in this category are **`useMemo`** and **`useCallback`**.

---

#### **4.1 `useMemo`: Memoizing Expensive Calculations**

- **What It Does**: `useMemo` caches the result of a computation and recalculates it only when one of its dependencies changes.
- **Use Case**: Ideal for optimizing performance when performing expensive calculations or rendering large lists.

**Example**:
```jsx
import React, { useMemo, useState } from 'react';

function ExpensiveComputation({ number }) {
  const computeExpensiveValue = (num) => {
    // Simulate an expensive calculation
    console.log('Calculating...');
    return num * 2; // Example calculation
  };

  // Memoize the result of the expensive calculation
  const memoizedValue = useMemo(() => computeExpensiveValue(number), [number]);

  return <h1>Computed Value: {memoizedValue}</h1>;
}

function App() {
  const [count, setCount] = useState(1);

  return (
    <div>
      <ExpensiveComputation number={count} />
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

**Key Points**:
- The function `computeExpensiveValue` simulates an expensive calculation.
- The result is memoized, so it only recalculates when the `number` prop changes.
- Console logs "Calculating..." only when necessary, reducing unnecessary calculations.

---

#### **4.2 `useCallback`: Memoizing Callback Functions**

- **What It Does**: `useCallback` memoizes a function, returning a stable reference that only changes if its dependencies change.
- **Use Case**: Useful when passing callback functions to child components to prevent unnecessary re-renders.

**Example**:
```jsx
import React, { useState, useCallback } from 'react';

function Button({ onClick, label }) {
  console.log(`Rendering ${label}`);
  return <button onClick={onClick}>{label}</button>;
}

function App() {
  const [count, setCount] = useState(0);

  // Use useCallback to memoize the increment function
  const increment = useCallback(() => {
    setCount((prevCount) => prevCount + 1);
  }, []); // Dependencies array is empty, function never changes

  return (
    <div>
      <h1>Count: {count}</h1>
      <Button onClick={increment} label="Increment" />
    </div>
  );
}
```

**Key Points**:
- The `increment` function is memoized using `useCallback`.
- This prevents the `Button` component from re-rendering unless the dependencies change.
- The console logs “Rendering Increment” only when the button component mounts or the `increment` function reference changes.

---

### Summary of Performance Hooks:
- **`useMemo`**: Caches the result of an expensive calculation, re-computing it only when dependencies change.
- **`useCallback`**: Memoizes callback functions to maintain stable references and prevent unnecessary re-renders of child components.

---

Let me know when you're ready for the next section on **Context Hooks**!