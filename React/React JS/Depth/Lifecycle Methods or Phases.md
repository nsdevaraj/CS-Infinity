
Phases 
1) Mounting - component first created and rendered
2) Updating - update component based on prop(i.e parent prop by default ) or state change
3) Unmounting - component removed from DOM

### **React Class Component Lifecycle Methods**

React class components have several lifecycle methods that control the component's behavior at different stages of its existence.

#### **1. Mounting (Component is being created and inserted into the DOM)**

- **`constructor(props)`**: Called when the component is created. Used to initialize state and bind methods.
- **`static getDerivedStateFromProps(nextProps, nextState)`**: Invoked right before rendering, both on initial mount and on subsequent updates. Returns an object to update the state or `null` to update nothing.
- **`render()`**: The only required method in a class component. Returns the JSX to render to the DOM.
- **`componentDidMount()`**: Called immediately after the component is added to the DOM. Good for initializing network requests, subscriptions, or interacting with the DOM.

#### **2. Updating (Component is being re-rendered due to changes in state or props)**

- **`static getDerivedStateFromProps(nextProps, nextState)`**: Called before every render when props or state change.
- **`shouldComponentUpdate(nextProps, nextState)`**: Determines whether the component should re-render. Returning `false` can optimize performance by preventing unnecessary renders.
- **`render()`**: Re-renders the component based on changes.
- **`getSnapshotBeforeUpdate(prevProps, prevState)`**: Called right before React applies changes to the DOM. It allows you to capture some information (like scroll position) before updates.
- **`componentDidUpdate(prevProps, prevState, snapshot)`**: Called after the component is updated. It’s useful for performing side effects after a render (e.g., fetching data, updating the DOM).

#### **3. Unmounting (Component is being removed from the DOM)**

- **`componentWillUnmount()`**: Called right before the component is removed from the DOM. It’s used for cleanup (e.g., invalidating timers, cancelling network requests, or cleaning up subscriptions).

#### **4. Error Handling**

- **`static getDerivedStateFromError(error)`**: Called when an error is thrown in a descendant component. Can be used to display a fallback UI.
- **`componentDidCatch(error, info)`**: Catches errors in any component below this component in the tree. Allows for logging errors and showing fallback UI.

---

### **React 16.8+ (Functional Components with Hooks)**

With the introduction of hooks in React 16.8, the need for class component lifecycle methods has decreased. Now, you can manage lifecycle events in functional components using hooks.

- **`useState()`**: For managing state.
- **`useEffect()`**: Replaces `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount` for handling side effects. Runs after render and allows cleanup with a return function.

#### **Example of Lifecycle Methods with Hooks:**

```jsx
import React, { useState, useEffect } from 'react';

function MyComponent() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    // ComponentDidMount equivalent
    console.log('Component mounted');
    return () => {
      // ComponentWillUnmount equivalent
      console.log('Component will unmount');
    };
  }, []); // Empty array ensures this effect runs only once

  useEffect(() => {
    // ComponentDidUpdate equivalent
    console.log('Count updated:', count);
  }, [count]); // Effect runs when 'count' changes

  return <div>{count}</div>;
}

export default MyComponent;
```

### **Summary:**

- **Class Components:** Use lifecycle methods for managing component behavior during mounting, updating, unmounting, and error handling.
- **Functional Components:** Use hooks like `useEffect` and `useState` to replicate lifecycle methods in a simpler, more concise way.
