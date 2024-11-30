
### **Section 2: React State and Lifecycle**

\State and lifecycle concepts are crucial for creating dynamic and responsive applications.

---

#### 6. **What is state in React?**
**Answer**:
State is an object in React components that holds dynamic data and determines the behavior of the component. Unlike props, state is mutable and managed within the component itself.

**Example**:
```javascript
function Counter() {
  const [count, setCount] = React.useState(0);
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

**Concept Explanation**:
State allows components to create interactive and dynamic UIs. It triggers a re-render of the component whenever it is updated.

---

#### 7. **What are lifecycle methods in React class components?**
**Answer**:
Lifecycle methods are special methods in React class components that allow you to run code at specific points in a component’s lifecycle:
- **Mounting**: `componentDidMount()`
- **Updating**: `componentDidUpdate()`
- **Unmounting**: `componentWillUnmount()`

**Example**:
```javascript
class ExampleComponent extends React.Component {
  componentDidMount() {
    console.log('Component mounted');
  }

  componentDidUpdate() {
    console.log('Component updated');
  }

  componentWillUnmount() {
    console.log('Component will unmount');
  }

  render() {
    return <div>Example Component</div>;
  }
}
```

**Concept Explanation**:
These methods help perform side effects such as fetching data, setting up subscriptions, or cleaning up resources when the component is unmounted.

---

#### 8. **What is `useEffect`, and how does it relate to lifecycle methods?**
**Answer**:
`useEffect` is a React hook that allows you to perform side effects in functional components. It can mimic the behavior of lifecycle methods such as `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount`.

**Example**:
```javascript
function ExampleComponent() {
  React.useEffect(() => {
    console.log('Component mounted or updated');

    return () => {
      console.log('Cleanup on unmount');
    };
  }, []); // Empty dependency array ensures it runs once like `componentDidMount`
}
```

**Concept Explanation**:
`useEffect` runs after the component renders, allowing you to handle side effects efficiently. Adding a dependency array lets you control when it runs and how to clean up effects when the component unmounts.

---

#### 9. **What is the difference between `componentDidMount` and `useEffect` with an empty dependency array?**
**Answer**:
- **`componentDidMount`**: Runs once after the initial render in class components.
- **`useEffect` with an empty array**: Mimics `componentDidMount` in functional components by running only once when the component mounts.

**Concept Explanation**:
`useEffect` provides more flexibility because you can use it for multiple side effects and control them via the dependency array, making it a more powerful tool than class lifecycle methods.

---

#### 10. **How can you fetch data on component mount using hooks?**
**Answer**:
You can use `useEffect` to fetch data when a component mounts by placing the fetch logic inside the `useEffect` and using an empty dependency array.

**Example**:
```javascript
function DataFetchingComponent() {
  const [data, setData] = React.useState(null);

  React.useEffect(() => {
    fetch('https://api.example.com/data')
      .then((response) => response.json())
      .then((data) => setData(data))
      .catch((error) => console.error('Error fetching data:', error));
  }, []); // Runs only once on mount

  return <div>{data ? JSON.stringify(data) : 'Loading...'}</div>;
}
```

**Concept Explanation**:
Placing the fetch call inside `useEffect` ensures the data is fetched after the component mounts. The empty dependency array ensures that it only runs once, similar to `componentDidMount`.











