

### **1. Basic Implementation with `useState`**

This approach uses a single state variable to manage the counter.

```jsx
import React, { useState } from "react";

const Counter = () => {
  const [count, setCount] = useState(0);
  const maxLimit = 10;
  const minLimit = 0;

  const increment = () => {
    if (count < maxLimit) setCount(count + 1);
  };

  const decrement = () => {
    if (count > minLimit) setCount(count - 1);
  };

  const reset = () => setCount(0);

  return (
    <div>
      <h1>Counter: {count}</h1>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
      <button onClick={reset}>Reset</button>
    </div>
  );
};

export default Counter;
```

---

### **2. Using `useReducer` for State Management**

This approach uses the `useReducer` hook for more structured state management.

```jsx
import React, { useReducer } from "react";

const initialState = 0;
const maxLimit = 10;
const minLimit = 0;

const reducer = (state, action) => {
  switch (action.type) {
    case "INCREMENT":
      return state < maxLimit ? state + 1 : state;
    case "DECREMENT":
      return state > minLimit ? state - 1 : state;
    case "RESET":
      return initialState;
    default:
      return state;
  }
};

const Counter = () => {
  const [count, dispatch] = useReducer(reducer, initialState);

  return (
    <div>
      <h1>Counter: {count}</h1>
      <button onClick={() => dispatch({ type: "INCREMENT" })}>Increment</button>
      <button onClick={() => dispatch({ type: "DECREMENT" })}>Decrement</button>
      <button onClick={() => dispatch({ type: "RESET" })}>Reset</button>
    </div>
  );
};

export default Counter;
```

---

### **3. Controlled Inputs for Custom Limits**

This approach allows users to set their own min/max limits.

```jsx
import React, { useState } from "react";

const Counter = () => {
  const [count, setCount] = useState(0);
  const [limits, setLimits] = useState({ min: 0, max: 10 });

  const increment = () => {
    if (count < limits.max) setCount(count + 1);
  };

  const decrement = () => {
    if (count > limits.min) setCount(count - 1);
  };

  const reset = () => setCount(0);

  const handleLimitChange = (e) => {
    const { name, value } = e.target;
    setLimits((prev) => ({ ...prev, [name]: parseInt(value) || 0 }));
  };

  return (
    <div>
      <h1>Counter: {count}</h1>
      <div>
        <label>
          Min Limit: <input type="number" name="min" onChange={handleLimitChange} />
        </label>
        <label>
          Max Limit: <input type="number" name="max" onChange={handleLimitChange} />
        </label>
      </div>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
      <button onClick={reset}>Reset</button>
    </div>
  );
};

export default Counter;
```

---

### **4. Using Custom Hooks for Reusability**

This approach extracts the counter logic into a reusable custom hook.

```jsx
import React, { useState } from "react";

const useCounter = (initialValue = 0, min = 0, max = 10) => {
  const [count, setCount] = useState(initialValue);

  const increment = () => setCount((prev) => (prev < max ? prev + 1 : prev));
  const decrement = () => setCount((prev) => (prev > min ? prev - 1 : prev));
  const reset = () => setCount(initialValue);

  return { count, increment, decrement, reset };
};

const Counter = () => {
  const { count, increment, decrement, reset } = useCounter(0, 0, 10);

  return (
    <div>
      <h1>Counter: {count}</h1>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
      <button onClick={reset}>Reset</button>
    </div>
  );
};

export default Counter;
```

---

### **5. Using Context for Global State**

This approach uses Context API to share the counter state across components.

```jsx
import React, { createContext, useContext, useState } from "react";

const CounterContext = createContext();

const CounterProvider = ({ children }) => {
  const [count, setCount] = useState(0);
  const maxLimit = 10;
  const minLimit = 0;

  const increment = () => setCount((prev) => (prev < maxLimit ? prev + 1 : prev));
  const decrement = () => setCount((prev) => (prev > minLimit ? prev - 1 : prev));
  const reset = () => setCount(0);

  return (
    <CounterContext.Provider value={{ count, increment, decrement, reset }}>
      {children}
    </CounterContext.Provider>
  );
};

const CounterDisplay = () => {
  const { count } = useContext(CounterContext);
  return <h1>Counter: {count}</h1>;
};

const CounterControls = () => {
  const { increment, decrement, reset } = useContext(CounterContext);
  return (
    <div>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
      <button onClick={reset}>Reset</button>
    </div>
  );
};

const CounterApp = () => (
  <CounterProvider>
    <CounterDisplay />
    <CounterControls />
  </CounterProvider>
);

export default CounterApp;
```

---
