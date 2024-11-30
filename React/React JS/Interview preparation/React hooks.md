
### **Section 4: React Hooks**

React hooks are a powerful addition introduced in React 16.8. 
They allow functional components to use state and other React features without writing class components.


**What are React hooks? Name a few commonly used hooks.**

- Hooks allow you to use state and lifecycle features in functional components. Common hooks:
    - `useState`: Manage state.
    - `useEffect`: Handle side effects.
    - `useContext`: Access context values.

**How would you optimize a React application?**

- Use memoization (`React.memo`, `useMemo`).
- Avoid unnecessary renders using `useCallback`.
- Code-split using React.lazy and Suspense.

---

#### 16. **What are React hooks, and why were they introduced?**
**Answer**:
React hooks are functions that let you use state and other React features in functional components. They were introduced to eliminate the need for class components, simplifying component structures and improving code readability.

**Main reasons for introduction**:
- **Reusability**: Makes it easier to reuse stateful logic across components.
- **Simplification**: Reduces the complexity of components by using functions instead of classes.
- **Cleaner code**: Provides a more concise and declarative way to write components.

**Example**:
```javascript
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

**Concept Explanation**:
Hooks allow for side effects, state management, and accessing the lifecycle of a component within functional components, streamlining development and making code easier to understand and maintain.

---

#### 17. **What is `useState`, and how do you use it?**
**Answer**:
`useState` is a hook that allows you to add state to functional components. It returns an array with two elements: the current state and a function to update that state.

**Example**:
```javascript
import React, { useState } from 'react';

function Toggle() {
  const [isOn, setIsOn] = useState(false);

  return (
    <button onClick={() => setIsOn(!isOn)}>
      {isOn ? 'ON' : 'OFF'}
    </button>
  );
}
```

**Concept Explanation**:
`useState` can be initialized with a default value and provides an easy way to update the state, causing the component to re-render when the state changes.

---

#### 18. **What is `useEffect`, and how does it work?**
**Answer**:
`useEffect` is a hook used to perform side effects in functional components. It runs after the component renders and can be configured to run:
- **After every render**
- **Only on mount** (using an empty dependency array)
- **When specific values change** (using a dependency array with values)

**Example**:
```javascript
import React, { useEffect, useState } from 'react';

function DataFetcher() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('https://api.example.com/data')
      .then((response) => response.json())
      .then((result) => setData(result));
  }, []); // Runs only once on mount

  return <div>{data ? JSON.stringify(data) : 'Loading...'}</div>;
}
```

**Concept Explanation**:
`useEffect` combines the behaviors of `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount` into one function. Cleanup logic can be returned inside `useEffect` to handle unmounting or updates.

---

#### 19. **What are dependency arrays in `useEffect`, and how do they work?**
**Answer**:
The dependency array in `useEffect` determines when the effect should be re-run:
- **Empty array (`[]`)**: The effect runs only once on mount.
- **Array with dependencies (`[dep1, dep2]`)**: The effect runs when any dependency changes.
- **No array**: The effect runs after every render.

**Example**:
```javascript
useEffect(() => {
  console.log('Runs only once on mount');
}, []);

useEffect(() => {
  console.log('Runs when `count` changes');
}, [count]);
```

**Concept Explanation**:
By controlling the dependency array, you can optimize performance and avoid unnecessary side effects. If dependencies aren't managed correctly, it can lead to infinite loops or missed updates.

---

#### 20. **What is `useRef`, and how is it different from `useState`?**
**Answer**:
`useRef` is a hook that returns a mutable ref object whose `.current` property persists across renders. It does not trigger a re-render when updated, unlike `useState`.

**Use cases**:
- **Accessing DOM elements**: To directly manipulate a DOM element.
- **Storing mutable values**: To hold mutable values that don’t trigger re-renders.

**Example**:
```javascript
import React, { useRef, useEffect } from 'react';

function InputFocus() {
  const inputRef = useRef(null);

  useEffect(() => {
    inputRef.current.focus(); // Automatically focuses the input on mount
  }, []);

  return <input ref={inputRef} />;
}
```

**Concept Explanation**:
`useRef` is ideal for persisting values between renders without causing re-renders. It’s commonly used for focusing inputs or holding values such as timers or previous states.




to check {

Read.memo => how optmizes the things.. 


}