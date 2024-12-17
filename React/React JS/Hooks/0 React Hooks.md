


[React Hooks -  YT (Code Bootcamp) )](https://www.youtube.com/watch?v=LOH1l-MP_9k)


![[Map of Hooks.png]]



[[Introduction]]
[[State management hooks]]
[[Effect Hooks]]
[[Ref hooks]]
[[Performance Hooks]]
[[Context Hooks]]
[[Transition Hooks]]
[[Random Hooks]]

[[Custom Hooks]]


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


  
Hooks: - function gives super power things react  
  
Note: use only in top level of functional component, not work inside function or loops etc  
. (expect custom hooks)  
  
  
• useState - handle reactivity data - state variable to maintain component rerenders  
  
getter, setter = ( default)  
  
  
• useEffect - component life cycle things managed in it...  
  
didMount - compount first time rendered  
didUpdate - updated for some reason  
willUnmount - just before unmounted  
  
  
without dependency - rerender on - mount / state  
is updated  
  
empty dependency - rerender on mount  
List of deps ( state or props) - rerender if any of dependencies changes  
  
return callback func in useEffect - call it when unmount  
  
  
• use Context - things shared data without passing as prop - to reduce prop trilling  
  
  
in top level, create Context and put provider in return with values...  
  
In child renderer - get those values from use Content hook or context.consumer  
  
context updates - context using component rerenders  
  
  
useRef - maintain reference of things , but not rerenders like state variables  
  
Most usecase - grab html element from DOM  
  
  
  
useReducer : like state, but while directly updating given value, it goes to reducer function amd update states  
  
[ state, dispatch] = ( updateFunc, default)  
  
updateFunc ( state, argsPassWhileCalling)  
  
  
Usage : when logics are complex  
  
  
useMemo - cache results of function call - optimise computation for improving Performances  
, so only use for expensive operations - memoize return values..  
  
cost getCount = useMemo ( () => do something, [deps])  
  
  
  
useCallback - memoize entire func ( not only return value)  
  
Creating a func in parent and passing to children as callback, when parent are-renderer, child passing func recreated and which makes rerenders os child, which prevented by this...  
  


[[React JS/Hooks/to check|to check]]


