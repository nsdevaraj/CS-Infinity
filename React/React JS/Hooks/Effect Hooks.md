
### **2. Effect Hooks**

Effect Hooks allow you to perform **side effects** in your functional components. A side effect can be anything that interacts with the outside world, such as data fetching, subscriptions, or manually changing the DOM.

---

#### **2.1 `useEffect`: The Primary Effect Hook**

- **What It Does**: `useEffect` lets you synchronize your component with external systems.
- **How It Works**: You provide a function to `useEffect`, which runs after every render by default. You can control when it runs using a **dependency array**.

**Example**:
```jsx
import React, { useEffect, useState } from 'react';

function ExampleComponent() {
  const [count, setCount] = useState(0);

  // Effect to update document title
  useEffect(() => {
    document.title = `You clicked ${count} times`;
  }, [count]); // Only runs when 'count' changes

  return (
    <div>
      <h1>Count: {count}</h1>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

**Key Points**:
- The effect updates the document title whenever the `count` changes.
- The **dependency array** `[count]` means the effect runs only when `count` changes.
- Without a dependency array, the effect runs after every render.

---

#### **2.2 `useLayoutEffect`: For Synchronous Effects**

- **What It Does**: Similar to `useEffect`, but runs synchronously before the browser paints.
- **Use Case**: Useful for reading layout from the DOM and synchronously re-rendering.

**Example**:
```jsx
import React, { useLayoutEffect, useRef } from 'react';

function LayoutExample() {
  const boxRef = useRef(null);

  // Measure the box's size before rendering
  useLayoutEffect(() => {
    const { width, height } = boxRef.current.getBoundingClientRect();
    console.log(`Width: ${width}, Height: ${height}`);
  });

  return <div ref={boxRef} style={{ width: '200px', height: '100px' }}>Box</div>;
}
```

**Key Points**:
- The layout effect allows you to measure the size of the box before rendering.
- Use this hook when you need to interact with the DOM layout before the user sees the changes.

---

#### **2.3 `useInsertionEffect`: For CSS-in-JS Libraries**

- **What It Does**: Inserts styles before DOM mutations.
- **Use Case**: Primarily used by CSS-in-JS libraries to ensure styles are applied before rendering.

**Example**:
```jsx
import { useInsertionEffect } from 'react';

function StyleInjector() {
  useInsertionEffect(() => {
    // Insert styles dynamically
    const style = document.createElement('style');
    style.textContent = `
      .my-class {
        color: red;
      }
    `;
    document.head.appendChild(style);

    return () => {
      // Cleanup the styles on unmount
      document.head.removeChild(style);
    };
  }, []); // Run once on mount

  return <div className="my-class">Hello, World!</div>;
}
```

**Key Points**:
- Inserts styles before the component mounts to ensure proper styling.
- Cleanup function removes styles when the component unmounts.

---

### Summary of Effect Hooks:
- **`useEffect`**: For managing side effects after rendering. Ideal for data fetching, subscriptions, etc.
- **`useLayoutEffect`**: Synchronous; use for measuring layout before rendering.
- **`useInsertionEffect`**: For libraries that manage styles; ensures CSS is applied before rendering.

---

Let me know when you're ready for the next section on **Ref Hooks**!