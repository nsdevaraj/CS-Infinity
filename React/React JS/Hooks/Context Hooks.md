

### **5. Context Hooks**

Context Hooks in React provide a way to share values between components without explicitly passing props through every level of the component tree. The primary hook for this is `useContext`.

---
### **What is `useContext`?**

- **Purpose**:
    - Simplifies sharing data or state across components without passing props manually through multiple levels of the component tree (i.e., eliminates "prop drilling").
    - Works in conjunction with React's Context API to provide global data access to any component within the context tree.

---

### **How It Works**

1. **Create a Context**:
    
    - Use `React.createContext()` to create a context object. This object holds the data or state to be shared.
2. **Provide the Context**:
    
    - Wrap the relevant parts of your component tree with the `Provider` component from the context object. The `Provider` supplies the context value.
3. **Consume the Context**:
    
    - Use the `useContext` hook within any component that needs access to the shared data. Pass the context object as an argument to `useContext`.

---


```jsx
import React , { useState, createContext, useContext  } from 'react';

 const ContextName = createContext( 'initial');
const SubComp = () => {
    const value = useContext(ContextName);
    return <div>{value}</div>;
}

export default function App() {

    const [text, setText] = useState('Hi');

    const doToggleContext = () => {

        setText((prev) => {
            if(prev == 'Hi') {
                return 'Bye';
            }else{
                return 'Hi';
            }
        })
        
    }
    
    return(<div>
    <ContextName.Provider value = {text}>
    <SubComp />
    </ContextName.Provider>
        <button onClick={doToggleContext}>
            {'toggle'}
        </button>
    </div>);
}

```

note: when 2 files.. export and import ContextName...

---

### **Key Features**

1. **Global State Sharing**:
    
    - Makes global data like user information, theme, or language settings accessible across multiple components.
2. **No Prop Drilling**:
    
    - Avoids passing props down through intermediate components that don’t use the data, improving maintainability.
3. **Dynamic Updates**:
    
    - When the context value changes, all components consuming it automatically re-render with the updated value. i.e. **only components that use `useContext` or `Context.Consumer`** will automatically re-render with the updated value.

---

### **Advanced Example: Dynamic Theme Toggle**

#### Creating a Context with Dynamic State

```jsx
import React, { createContext, useContext, useState } from 'react';

// Create Context
const ThemeContext = createContext();

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');

  const toggleTheme = () => setTheme((prev) => (prev === 'light' ? 'dark' : 'light'));

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

function ThemedComponent() {
  const { theme, toggleTheme } = useContext(ThemeContext); // Access theme and toggle function

  return (
    <div className={`theme-${theme}`}>
      <p>Current Theme: {theme}</p>
      <button onClick={toggleTheme}>Toggle Theme</button>
    </div>
  );
}

function App() {
  return (
    <ThemeProvider>
      <ThemedComponent />
    </ThemeProvider>
  );
}

export default App;
```

**Key Highlights**:

- The `ThemeProvider` manages state (`theme`) and exposes a method (`toggleTheme`) via context.
- Any component consuming the context can read and update the shared state.

---

### **Real-World Use Cases**

1. **Authentication**:
    
    - Share authentication state (e.g., `isAuthenticated`, `user`) across the app.
    
    ```jsx
    const AuthContext = createContext();
    
    function AuthProvider({ children }) {
      const [user, setUser] = useState(null);
      return (
        <AuthContext.Provider value={{ user, setUser }}>
          {children}
        </AuthContext.Provider>
      );
    }
    ```
    
2. **Themes and Preferences**:
    
    - Dynamically switch themes, languages, or layout preferences globally.
3. **Global Notifications**:
    
    - Share a global message or alert system throughout the app.
4. **E-commerce Cart**:
    
    - Manage a shopping cart's state and provide it to any component that needs to display or update cart details.

---

### **Considerations When Using `useContext`**

1. **Performance Concerns**:
    
    - **Issue**: When the context value changes, all consuming components re-render.
    - **Solution**: Use memoization (`React.memo`) or split contexts to minimize unnecessary re-renders.
    
    ```jsx
    const ThemeContext = createContext();
    const AuthContext = createContext(); // Separate context for authentication
    ```
    
2. **Overuse of Context**:
    
    - Avoid using context for every piece of state. For local state, prefer `useState` or `useReducer`.
    - Use context primarily for **global state** shared across many components.
3. **Complex State Management**:
    
    - For highly dynamic or nested state, consider external libraries like Redux, Zustand, or MobX instead of solely relying on context.
4. **Debugging**:
    
    - Debugging context changes can be challenging, as it doesn’t provide detailed insight into what triggered re-renders.

---

### **Alternatives to Context API**

|**Tool**|**Use Case**|**When to Use**|
|---|---|---|
|**`useState`**|Component-local state|For simple and isolated state management.|
|**`useReducer`**|Complex component state|When managing related states or actions in a single component.|
|**Redux**|Centralized state for large-scale apps|For highly dynamic or interdependent global state across many components.|
|**Zustand**|Minimalistic state management|A lightweight alternative for managing shared or global state with better performance than context.|
|**React Query**|Server state management (e.g., API calls, caching)|When dealing with remote data fetching and caching.|

---

### **Best Practices for Using `useContext`**

1. **Combine with State Hooks**:
    
    - Manage state locally within providers using `useState` or `useReducer` and expose it through context.
2. **Optimize Context Updates**:
    
    - Split contexts if different pieces of state change independently to reduce unnecessary re-renders.
3. **Memoize Context Values**:
    
    - Use `useMemo` to prevent re-creating the value object unless necessary:
        
        ```jsx
        const contextValue = useMemo(() => ({ theme, toggleTheme }), [theme]);
        ```
        
4. **Avoid Deeply Nested Providers**:
    
    - Use tools like `recompose` or `provider pattern` wrappers to avoid deeply nested provider trees.

---

### **Comparison with Prop Drilling**

|**Feature**|**Prop Drilling**|**Context + `useContext`**|
|---|---|---|
|Ease of Use|Tedious in large hierarchies|Straightforward, as data is directly accessible.|
|Maintainability|Difficult to manage as the component tree grows|Cleaner and scalable for large applications.|
|Performance|Efficient for static props|Efficient, but requires care to prevent re-renders.|
|Debugging|Easier to trace props|Debugging context updates can be challenging.|

---

### **Summary**

The `useContext` hook is a powerful tool for sharing global data within React apps. By removing the need for prop drilling, it simplifies the structure of your components.

However, it comes with performance trade-offs, and overusing it for every state can lead to unnecessary complexity. Use `useContext` for truly **global state** like themes, authentication, or settings, and combine it with state management best practices for optimal results.




---



### **Section 10: State Management and Context API**

This section covers important concepts related to managing and sharing state across components using Context API and state management strategies in React applications.

---

#### 46. **What is the React Context API, and when would you use it?**
**Answer**:
The **React Context API** is a feature that allows you to manage and share state across the component tree without having to pass props manually through every level of the component hierarchy.

**Example**:
```javascript
import React, { useState, useContext, createContext } from 'react';

const MyContext = createContext();

function App() {
  const [user, setUser] = useState('John');

  return (
    <MyContext.Provider value={{ user, setUser }}>
      <ChildComponent />
    </MyContext.Provider>
  );
}

function ChildComponent() {
  const { user, setUser } = useContext(MyContext);
  
  return (
    <div>
      <h1>{user}</h1>
      <button onClick={() => setUser('Jane')}>Change User</button>
    </div>
  );
}
```

**Concept Explanation**:
Context API provides a way to pass data through the component tree without prop-drilling. It is ideal for sharing global state such as themes, authentication, and user data.

---

#### 47. **What are the limitations of the React Context API?**
**Answer**:
- **Performance issues**: If a value in the context changes, it triggers a re-render for all consumers of that context, which can be a performance bottleneck if not used carefully.
- **Not ideal for complex state management**: For large or deeply nested applications, using Context API alone might lead to more complexity and less scalability, especially for handling more intricate states.

**Concept Explanation**:
While Context API is useful for simple global states, when your application grows or requires more advanced features (like actions and reducers), a state management library like Redux or Zustand might be more appropriate.


---

#### 49. **What are the advantages of using Redux for state management in React?**
**Answer**:
- **Centralized State Management**: Redux stores the application state in a global store, making it accessible across components without passing props.
- **Predictable State**: The state is immutable, and changes happen in a predictable way through actions and reducers.
- **Middleware Support**: Redux has middleware support (e.g., `redux-thunk` or `redux-saga`) for handling asynchronous actions. `redux-persist` -> to persist store values even refresh of page.. 
- **DevTools**: Redux DevTools allow easy debugging, inspecting actions, and tracking state changes.

**Example**:
```javascript
// Action
const increment = () => ({
  type: 'INCREMENT',
});

// Reducer
const counterReducer = (state = { count: 0 }, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    default:
      return state;
  }
};
```

**Concept Explanation**:
Redux provides a robust solution for managing complex or large-scale applications, particularly when the state has to be shared across multiple components or when the application involves complex logic like asynchronous data fetching.

---

#### 50. **How does the `useReducer` hook relate to Redux?**
**Answer**:
The `useReducer` hook is similar to Redux in that it allows you to manage state using a **reducer** function. However, `useReducer` is used within a single component, whereas Redux manages state globally for the entire application.

**Example**:
```javascript
import React, { useReducer } from 'react';

function counterReducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    default:
      return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(counterReducer, { count: 0 });

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>Increment</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>Decrement</button>
    </div>
  );
}
```

**Concept Explanation**:
`useReducer` provides a way to manage state with more complex logic than `useState`. It mimics the Redux pattern on a smaller scale, making it ideal for localized component state with more advanced state transitions.
