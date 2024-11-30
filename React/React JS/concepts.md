
### **React Overview & Introduction**

#### React Basics

- **Release & Use Case**: React was first released by Facebook in **2011** to build dynamic and interactive UIs. It's known for its **component-based architecture** and efficient **Virtual DOM** system.
- **React vs Other Frameworks**: Unlike **Angular** (complete framework) or **Vue**, React is a library mainly for building UIs.
- **Component-Based Architecture**: Components in React are like **building blocks** of the UI. Each component can be created and managed individually, allowing modular and reusable code.
  
#### DOM Management

- **Vanilla JS DOM vs React's Virtual DOM**:
  - Traditional DOM updates are costly as changes reflect directly on the **real DOM**.
  - React manages a **Virtual DOM**—a lightweight in-memory representation of the DOM. Changes are first reflected in the virtual DOM, and only the differences (diffs) between the real and virtual DOM are updated, enhancing performance.

#### Setting Up React

- **Initial Setup**:
  - React can be set up using tools like **Create React App** or **Vite** (faster with a smaller bundle size).
  - The **`index.html`** file serves as the **entry point** and links the main **`main.tsx`** file where the **App component** is rendered.
  - **TypeScript (`.ts`)** is used for utility/service files, and **`.tsx`** for React components.

#### React Components

- **Component Types**: 
  - **Class Components** (older) and **Function Components** (modern and preferred).
  - Naming convention: **PascalCase** for components, **camelCase** for other variables.

- **JSX**: 
  - React uses **JSX (JavaScript XML)**, which looks like writing **HTML in JavaScript**, but it’s JavaScript creating DOM elements.
  - JSX allows for dynamicity: We can conditionally render content, manage lists, and handle user events.
  
- **Virtual DOM**: React’s **React DOM** package works with the browser’s DOM to ensure changes in components reflect efficiently in the browser, based on the diffing algorithm.

#### Key Concepts

- **Single Component Return**: In JSX, we can return only **one parent component**. Empty fragments (`<> </>`) or `<Fragment></Fragment>` can be used to wrap multiple elements.
  
- **Conditional Rendering**:
  - Common technique: `condition && <Component />`.
  - Simplifies logic by only rendering components based on a condition.
  
- **CSS in JSX**: Attributes are written in **camelCase** (e.g., `backgroundColor` instead of `background-color`). Also, **class** is written as `className`.

---

### **React Hooks**

**Hooks** are functions that allow function components to access state and other React features. They should only be called at the **top level** of a function component (not inside loops, conditions, etc.).

#### Key Hooks

1. **`useState`**: Manages **state** in a functional component.
   - Example: 
     ```tsx
     const [count, setCount] = useState(0);
     ```

2. **`useEffect`**: Handles **side effects** in a component, such as data fetching, subscriptions, or manually changing the DOM.
   - Example: 
     ```tsx
     useEffect(() => {
       document.title = `You clicked ${count} times`;
     }, [count]); // Only re-run the effect if count changes
     ```

3. **`useContext`**: Accesses **context** without needing to pass props through every level.
   - Example:
     ```tsx
     const value = useContext(SomeContext);
     ```

4. **`useRef`**: Persists a **mutable reference** between renders without causing a re-render.
   - Example: 
     ```tsx
     const inputRef = useRef(null);
     inputRef.current.focus();
     ```

5. **`useReducer`**: An alternative to `useState` for managing **more complex state logic** (similar to Redux).
   - Example: 
     ```tsx
     const [state, dispatch] = useReducer(reducer, initialState);
     ```

6. **`useMemo`**: Memoizes **expensive calculations** to avoid recomputation unless dependencies change.
   - Example:
     ```tsx
     const expensiveResult = useMemo(() => computeExpensiveValue(a, b), [a, b]);
     ```

7. **`useCallback`**: Memoizes functions to prevent unnecessary re-creations and re-renders.
   - Example:
     ```tsx
     const handleClick = useCallback(() => {
       console.log('Clicked!');
     }, []);
     ```

---

### **Memoization in JavaScript**

Memoization is an optimization technique where the result of expensive function calls is cached and returned when the same inputs occur again.

- **Fibonacci Example**:
  ```js
  const fibonacci = (n, memo = {}) => {
    if (n <= 1) return n;
    if (n in memo) return memo[n];
    return memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
  };
  ```

- **Resources**:
  - [Memoization in Fibonacci](https://medium.com/codex/fibonacci-sequence-javascript-recursion-memoization-74d997900ff8)
  


### **Links & References**

- **React Documentation**: 
  - [React Overview](https://www.w3schools.com/REACT/react_overview.asp)
  - [React Hooks](https://www.w3schools.com/REACT/react_hooks.asp)
  - [JSX in React](https://www.w3schools.com/react/react_jsx.asp)
  
- **Memoization**:
  - [Fibonacci Memoization](https://medium.com/codex/fibonacci-sequence-javascript-recursion-memoization-74d997900ff8)

- **Hooks Overview**:
  - [React Hooks Overview](https://www.youtube.com/watch?v=TNhaISOUy6Q)

This structured breakdown covers all your key points while providing useful links and comparisons for easy reference and learning!


