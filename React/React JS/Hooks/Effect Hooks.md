

Effect Hooks enable side effects (external things outside react mostly webapis ) in React functional components. Side effects include data fetching, DOM manipulation, subscriptions, or styling changes.

---

### **1. useEffect**

**Purpose**: Handles **asynchronous** side effects after the component renders.  
**Use Cases**:

- Fetching data from APIs
- Subscribing to events (e.g., WebSocket)
- Updating the DOM (e.g., changing `document.title`)
- Cleaning up resources (e.g., event listeners, timers)

**When It Runs**:

- By default, runs **after every render**.
- Controlled by a **dependency array**:
    - `[]`: Runs **once** after the initial render.
    - `[deps]`: Runs when specified dependencies change.

---

**Example**:

```jsx
import React, { useState, useEffect } from 'react';

function ExampleComponent() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    // Side effect: Update document title
    document.title = `You clicked ${count} times`;

    // Optional cleanup
    return () => console.log('Cleanup on unmount or count change');
  }, [count]); // Runs only when 'count' changes

  return (
    <button onClick={() => setCount(count + 1)}>Click Me</button>
  );
}
```


### **Behavior of Cleanup with Dependencies**

When a `useEffect` has a **non-empty dependency array**, the cleanup function works like this:

1. **Before the next effect runs:**  
    If one of the dependencies changes, React first **runs the cleanup function** for the previous effect **before running the new effect**.
    
2. **On unmount:**  
    When the component is unmounted, React runs the cleanup function **one final time**.


---

## **useEffect Lifecycle Comparisons**

|**Class Component**|**useEffect Equivalent**|**Description**|
|---|---|---|
|`componentDidMount`|`useEffect(() => { ... }, [])`|Runs **once after the initial render**.|
|`componentDidUpdate`|`useEffect(() => { ... }, [deps])`|Runs when specified **dependencies change**.|
|`componentWillUnmount`|`useEffect(() => { return cleanup }, [])`|Runs cleanup logic **before unmounting**.|

---

### **1. Equivalent of `componentDidMount`**

- Runs **once** after the component mounts.
- Achieved by passing an **empty dependency array**.

```jsx
useEffect(() => {
  console.log("Component mounted");
}, []); // Empty array: runs once after the initial render
```

---

### **2. Equivalent of `componentDidUpdate`**

- Runs when specified **dependencies** change.
- Achieved by including dependencies in the dependency array.

```jsx
useEffect(() => {
  console.log("Component updated due to count change");
}, [count]); // Runs when 'count' changes
```

---

### **3. Equivalent of `componentWillUnmount`**

- Runs cleanup logic when the component unmounts.
- Achieved by returning a **cleanup function** from `useEffect`.

```jsx
useEffect(() => {
  console.log("Effect setup");

  return () => {
    console.log("Component will unmount - cleanup");
  };
}, []); // Runs cleanup on unmount
```


### **When Cleanup Matters**

You'd typically use cleanup for:

- **Removing event listeners** to prevent memory leaks.
- **Canceling network requests** to avoid unnecessary operations.
- **Cleaning up timers** like `setTimeout` or `setInterval`.


---

### **Combined Example**

Here's an example that demonstrates all three:

```jsx
import React, { useState, useEffect } from "react";

function LifecycleExample() {
  const [count, setCount] = useState(0);

  // componentDidMount equivalent
  useEffect(() => {
    console.log("Component mounted");

    // componentWillUnmount equivalent
    return () => {
      console.log("Component will unmount");
    };
  }, []);

  // componentDidUpdate equivalent
  useEffect(() => {
    console.log(`Count updated to: ${count}`);
  }, [count]);

  return (
    <div>
      <h1>Count: {count}</h1>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

export default LifecycleExample;
```



```jsx
import React , { useState, useEffect  } from 'react';

export default function App() {

    const [ timer, setTimer ] = useState(0);

    
    const [active, setActiive] = useState(false);

    useEffect(()=>{

        const intervalId = setInterval(()=> {
            if(active){
                setTimer(prev => prev+1);
            }
        }, 1000)


        return () => {
            clearInterval(intervalId);
        }
    },[active])
    
    const toggleActive = () => {
        setActiive(prev => !prev);
    }

    return(
        <>

            {`Time:  ${timer}`}

            <button onClick={toggleActive} >
                {`Toggle to ${active ? 'in-active': 'active' }`}
            </button>
           </>
    );
}

```



---

### **2. useLayoutEffect**

**Purpose**: Runs **synchronously** **after DOM mutations** but **before the browser paints** the screen.  
**Use Cases**:

- Measuring layout or DOM elements (e.g., size, position).
- Making **synchronous DOM updates** to avoid flickering.

**When It Runs**:

- After all DOM changes, **before browser paint**.

⚠️ **Caution**: Blocks rendering until the effect completes—use sparingly.

---

**Example**:

```jsx
import React, { useRef, useLayoutEffect } from 'react';

function LayoutEffectExample() {
  const boxRef = useRef(null);

  useLayoutEffect(() => {
    const { width, height } = boxRef.current.getBoundingClientRect();
    console.log(`Width: ${width}, Height: ${height}`);
  }, []); // Runs once after the component mounts

  return (
    <div ref={boxRef} style={{ width: '200px', height: '100px' }}>
      Measure Me!
    </div>
  );
}
```


```jsx
import React, { useState, useLayoutEffect, useRef } from 'react';

function CenteredPopup() {
  const popupRef = useRef();
  const [centerStyles, setCenterStyles] = useState({ top: 0, left: 0 });

  useLayoutEffect(() => {
    if (popupRef.current) {
      const { offsetWidth, offsetHeight } = popupRef.current;
      setCenterStyles({
        top: (window.innerHeight - offsetHeight) / 2,
        left: (window.innerWidth - offsetWidth) / 2,
      });
    }
  }, [popupRef]);

  return (
    <div>
      <div
        ref={popupRef}
        style={{
          position: 'absolute',
          top: `${centerStyles.top}px`,
          left: `${centerStyles.left}px`,
          width: '200px',
          height: '100px',
          background: 'lightblue',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          border: '1px solid blue',
        }}
      >
        Centered Popup
      </div>
    </div>
  );
}

export default CenteredPopup;

```

---

### **3. useInsertionEffect**

**Purpose**: Runs **synchronously** to insert styles **before DOM mutations**.  
**Use Case**: Specifically for **CSS-in-JS libraries** to prevent style glitches.

**When It Runs**:

- Before any DOM updates happen (to ensure styles are applied first).

⚠️ **Important**:

- Rarely needed for application code.
- Typically used by libraries managing styles.

---

**Example**:

```jsx
import React, { useInsertionEffect } from 'react';

function StyleExample() {
  useInsertionEffect(() => {
    const style = document.createElement('style');
    style.textContent = `.dynamic-style { color: blue; }`;
    document.head.appendChild(style);

    return () => document.head.removeChild(style); // Cleanup
  }, []); // Run once when mounted

  return <div className="dynamic-style">Styled Text</div>;
}
```

---

## **Comparison Table**

| **Hook**             | **Runs**                                                                      | **Use Case**                          |
| -------------------- | ----------------------------------------------------------------------------- | ------------------------------------- |
| `useEffect`          | Asynchronously **after rendering**v i.e after dom mutations and painting done | Data fetching, subscriptions, cleanup |
| `useLayoutEffect`    | **Synchronously after DOM mutations before paint**                            | Measure/adjust layout, avoid flicker  |
| `useInsertionEffect` | **Before DOM mutations**                                                      | Style insertion (CSS-in-JS libraries) |

---

### **Summary**

- **`useEffect`**: Standard hook for side effects after rendering (async).
- **`useLayoutEffect`**: Synchronous effects for layout tasks (use carefully).
- **`useInsertionEffect`**: Specialized for style management (rarely needed).

---



#### 32. **What is the difference between `useEffect` and `useLayoutEffect`, and when would you use one over the other?**
**Answer**:
- **`useEffect`**: Runs asynchronously after the DOM has been updated. It’s suitable for side effects that do not need to block the browser’s painting (e.g., data fetching).
- **`useLayoutEffect`**: Runs synchronously after the DOM mutations but before the browser paints. Use this when you need to make DOM measurements or update the layout before the user sees any changes.

**Example**:
```javascript
useEffect(() => {
  console.log('useEffect runs after the render');
});

useLayoutEffect(() => {
  console.log('useLayoutEffect runs before the render is painted');
});
```

**Concept Explanation**:
Choose `useLayoutEffect` when updates to the DOM need to happen before the browser paints, ensuring the UI reflects any changes immediately. For most use cases, `useEffect` is sufficient and avoids blocking render cycles.


---


#### 52. **What is the `useEffect` hook, and how does it work?**
**Answer**:
`useEffect` is a hook that runs side effects in function components. It is similar to lifecycle methods like `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount` combined.

**Example**:
```javascript
import { useEffect, useState } from 'react';

function MyComponent() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    console.log('Component mounted or updated');

    return () => {
      console.log('Cleanup before unmounting or when dependencies change');
    };
  }, [count]);

  return <button onClick={() => setCount(count + 1)}>Increment</button>;
}
```

**Concept Explanation**:
`useEffect` allows you to perform side effects (e.g., data fetching, subscriptions, or DOM manipulation) in functional components. The second argument (`[]`) controls when the effect runs: on mount, on updates, or on unmount.


---

#### 54. **How does `useEffect` handle cleanup, and when is it necessary?**
**Answer**:
`useEffect` can return a cleanup function, which runs when the component unmounts or before the effect is re-run (if dependencies change).

**Example**:
```javascript
useEffect(() => {
  const timer = setInterval(() => {
    console.log('Timer running');
  }, 1000);

  // Cleanup function
  return () => clearInterval(timer);
}, []);
```

**Concept Explanation**:
Cleanup is crucial for preventing memory leaks, such as clearing timers, canceling subscriptions, or aborting fetch requests. React automatically calls the cleanup function when the component unmounts or when the dependencies of the `useEffect` change.

---

#### 55. **What is the `useLayoutEffect` hook, and how does it differ from `useEffect`?**
**Answer**:
`useLayoutEffect` is similar to `useEffect`, but it is triggered synchronously after all DOM mutations, meaning it runs **before** the browser has painted the screen. This makes it suitable for tasks like measuring the DOM, manipulating layout, or reading layout properties.

**Example**:
```javascript
import { useLayoutEffect, useState } from 'react';

function MyComponent() {
  const [width, setWidth] = useState(0);

  useLayoutEffect(() => {
    setWidth(window.innerWidth);
  }, []); // Runs synchronously after DOM updates

  return <div>Window width: {width}</div>;
}
```

**Concept Explanation**:
`useLayoutEffect` ensures that the DOM changes happen before the browser paints, preventing flicker or layout shifts. Use `useEffect` for most side effects, but `useLayoutEffect` is appropriate for cases where the timing of updates relative to the paint is critical.


