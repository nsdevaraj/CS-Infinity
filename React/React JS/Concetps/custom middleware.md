
In React, middleware is often associated with state management libraries like **Redux**, but you can also create custom middleware-like logic for scenarios such as logging, error handling, or intercepting requests.

Below are examples of implementing custom middleware logic in **React**.

---

### **1. Custom Middleware with Redux**

If you're using Redux for state management, you can create middleware to intercept actions.

#### **Steps:**

1. Write a function that takes the `store` and `next` middleware in the chain.
2. Process the action before passing it to the next middleware or reducer.

#### **Code Example**

```javascript
const customLoggerMiddleware = (store) => (next) => (action) => {
  console.log("Dispatching action:", action);
  const result = next(action); // Pass to the next middleware or reducer
  console.log("Updated state:", store.getState());
  return result;
};

// Applying the middleware
import { createStore, applyMiddleware } from "redux";
import rootReducer from "./reducers";

const store = createStore(rootReducer, applyMiddleware(customLoggerMiddleware));
```

---

### **2. Custom Middleware in React without Redux**

For React applications not using Redux, you can mimic middleware behavior in your component hierarchy or API requests.

---

#### **Example 1: API Request Interception Middleware**

Create middleware for handling API requests globally, such as logging or token addition.

```javascript
const apiMiddleware = async (request, next) => {
  console.log("Request Started:", request);

  try {
    const response = await next(request);
    console.log("Response Received:", response);
    return response;
  } catch (error) {
    console.error("Request Failed:", error);
    throw error;
  }
};

const fetchWithMiddleware = (url, options) => {
  const next = (req) => fetch(req.url, req.options);
  return apiMiddleware({ url, options }, next);
};

// Usage
fetchWithMiddleware("/api/data", { method: "GET" }).then((data) =>
  console.log(data)
);
```

---

#### **Example 2: Higher-Order Component (HOC) Middleware**

Use an HOC to wrap components with middleware logic.

```javascript
const withLogger = (WrappedComponent) => {
  return (props) => {
    console.log("Props passed to component:", props);
    return <WrappedComponent {...props} />;
  };
};

// Usage
const MyComponent = (props) => <div>Hello, {props.name}</div>;

export default withLogger(MyComponent);
```

---

### **3. Middleware in React Context**

Use middleware-like logic with React's Context API to intercept updates.

#### **Example: Middleware for Context State**

```javascript
import React, { createContext, useReducer } from "react";

const StateContext = createContext();

const loggerMiddleware = (reducer) => {
  return (state, action) => {
    console.log("Previous State:", state);
    console.log("Action:", action);
    const newState = reducer(state, action);
    console.log("New State:", newState);
    return newState;
  };
};

const reducer = (state, action) => {
  switch (action.type) {
    case "INCREMENT":
      return { count: state.count + 1 };
    default:
      return state;
  }
};

const StateProvider = ({ children }) => {
  const [state, dispatch] = useReducer(loggerMiddleware(reducer), { count: 0 });

  return (
    <StateContext.Provider value={{ state, dispatch }}>
      {children}
    </StateContext.Provider>
  );
};

// Usage
const Counter = () => {
  const { state, dispatch } = React.useContext(StateContext);

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: "INCREMENT" })}>Increment</button>
    </div>
  );
};

export const App = () => (
  <StateProvider>
    <Counter />
  </StateProvider>
);
```

---

### **Key Takeaways**

- **With Redux**: Middleware is used to intercept and transform actions between dispatch and reducer.
- **Custom Middleware**:
    - Can be implemented in API request handlers.
    - Can wrap components using HOCs for pre/post logic.
- **React Context Middleware**: Combine `useReducer` with a middleware-like wrapper for managing state transitions.