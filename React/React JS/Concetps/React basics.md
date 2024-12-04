
### **Section 1: React Basics**


#### 1. **What is React, and why is it popular?**
**Answer**:
React is an open-source JavaScript library developed by Facebook for building fast, interactive user interfaces, primarily for single-page applications (SPAs). It is popular due to its:
- **Component-based architecture**: Encourages reusability and modular development.
- **Virtual DOM**: Improves performance by updating only parts of the real DOM that need changes.
- **Ease of integration**: Can be used alongside other frameworks or libraries.

**Concept Explanation**:
React's main strength lies in its declarative approach, which makes the code more predictable and easier to debug. This approach is different from imperative programming, where you explicitly tell the program how to perform operations.

---

#### 2. **What is JSX, and why is it used in React?**
**Answer**:
JSX (JavaScript XML) is a syntax extension for JavaScript that allows developers to write HTML elements directly in JavaScript code. It is used because:
- It makes the code more readable and helps visualize the UI structure.
- Transpiles into `React.createElement()` calls, which creates React elements.

**Example**:
```javascript
const element = <h1>Hello, world!</h1>;
// Transpiles to:
const element = React.createElement('h1', null, 'Hello, world!');
```

**Concept Explanation**:
JSX is not mandatory but is widely used in React projects because it combines the logic and markup, making code more cohesive and easier to understand.

---

#### 3. **What are React components?**
**Answer**:
React components are the building blocks of any React application. They can be classified into:
- **Functional components**: Simple JavaScript functions that return JSX.
- **Class components**: More feature-rich and used for stateful logic (prior to hooks).

**Example**:
Functional Component:
```javascript
function Greeting() {
  return <h1>Hello, world!</h1>;
}
```

Class Component:
```javascript
class Greeting extends React.Component {
  render() {
    return <h1>Hello, world!</h1>;
  }
}
```

**Concept Explanation**:
Components help in building UIs by breaking down the application into reusable pieces. Functional components are now preferred due to the introduction of hooks, making them powerful enough to handle state and side effects.

---

#### 4. **What are props in React?**
**Answer**:
Props (short for "properties") are read-only inputs passed from a parent component to a child component. They enable data transfer and make components dynamic.

**Example**:
```javascript
function Welcome(props) {
  return <h1>Hello, {props.name}!</h1>;
}

// Usage:
<Welcome name="John" />
```

**Concept Explanation**:
Props are immutable, which means a child component should never modify them. This ensures a unidirectional data flow, keeping data predictable and easier to manage.

---

#### 5. **What is the difference between a controlled and an uncontrolled component in React?**
**Answer**:
- **Controlled components**: Components whose form data is handled by React state. They give React full control over the input elements.
- **Uncontrolled components**: Form data is managed by the DOM itself, and refs are used to access the value.

**Example** (Controlled):
```javascript
function ControlledInput() {
  const [value, setValue] = React.useState('');
  return (
    <input value={value} onChange={(e) => setValue(e.target.value)} />
  );
}
```

**Example** (Uncontrolled):
```javascript
function UncontrolledInput() {
  const inputRef = React.useRef(null);
  return (
    <input ref={inputRef} />
  );
}
```

**Concept Explanation**:
Controlled components are generally preferred for better data handling and validation, whereas uncontrolled components can be useful when direct manipulation of the DOM is needed.**





