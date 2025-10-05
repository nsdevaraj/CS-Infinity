
React offers several powerful **component design patterns** that help you write clean, reusable, and scalable UIs. Below is a **comprehensive list** of the **most common patterns**, explained **crisp and in depth**, with **when to use** and **trade-offs**.

2
## 🧩 1. **Presentational and Container Pattern**

**Also Known As:** Smart vs. Dumb components

### 📦 What It Is:

- **Presentational** components only handle **UI and props**
    
- **Container** components handle **data fetching, state, and logic**
    

### 🧠 Why:

- Separates concerns — makes components reusable and testable
    
- Keeps logic out of UI layers
    

### 🧱 Example:

```tsx
// Presentational
const UserList = ({ users }) => (
  <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>
);

// Container
const UserListContainer = () => {
  const [users, setUsers] = useState([]);
  useEffect(() => fetchUsers().then(setUsers), []);
  return <UserList users={users} />;
};
```

### ✅ Use When:

- You want **separation of logic and UI**
    
- Multiple components consume **same data logic**
    

---

## 🔁 2. **Higher-Order Components (HOC)**

**Also Known As:** `withX` pattern

### 📦 What It Is:

A function that **takes a component and returns a new component**, injecting props or behavior.

### 🧠 Why:

- Share logic between unrelated components
    

### 🧱 Example:

```tsx
function withLogger(WrappedComponent) {
  return function (props) {
    useEffect(() => console.log(props), [props]);
    return <WrappedComponent {...props} />;
  };
}
```

### ✅ Use When:

- Logic needs to be reused across components
    
- You want a **decorator-like** pattern
    

### ❌ Avoid If:

- You're using hooks (prefer custom hooks)
    
- It causes wrapper hell (nesting)
    

---

## 🔗 3. **Render Props**

### 📦 What It Is:

Pass a **function as a child** that receives dynamic values.

### 🧠 Why:

- Share logic flexibly
    
- Decouple logic from rendering
    

### 🧱 Example:

```tsx
const MouseTracker = ({ children }) => {
  const [pos, setPos] = useState({ x: 0, y: 0 });
  return <div onMouseMove={e => setPos({ x: e.clientX, y: e.clientY })}>
    {children(pos)}
  </div>;
};

<MouseTracker>
  {({ x, y }) => <p>Mouse at {x}, {y}</p>}
</MouseTracker>
```

### ✅ Use When:

- You want a **flexible logic + rendering contract**
    

### ❌ Avoid If:

- It introduces deeply nested trees
    

---

## 🧱 4. **Compound Components**

### 📦 What It Is:

Multiple components work together, often using shared context.

### 🧠 Why:

- Allow multiple parts to collaborate (like `Tabs`, `Accordion`, `Form`)
    
- Great for **headless or UI libraries**
    

### 🧱 Example:

```tsx
<Tabs>
  <Tabs.Tab>Tab A</Tabs.Tab>
  <Tabs.Panel>Content A</Tabs.Panel>
</Tabs>
```

🔄 These use React Context internally to share state.

### ✅ Use When:

- Subcomponents must work in coordination
    

---

## 🧼 5. **Controlled vs Uncontrolled Components**

### 📦 What It Is:

- **Controlled:** Parent holds the state via props
    
- **Uncontrolled:** Internal state is managed with refs or `defaultValue`
    

### 🧱 Example:

```tsx
// Controlled
<input value={value} onChange={e => setValue(e.target.value)} />

// Uncontrolled
<input defaultValue="initial" ref={inputRef} />
```

### ✅ Use When:

- Controlled: for **forms, validation, controlled behavior**
    
- Uncontrolled: for **performance** or simple form cases
    

---

## 🧳 6. **Custom Hooks**

### 📦 What It Is:

Extract **reusable logic** (state, side effects) into reusable functions that start with `use`

### 🧠 Why:

- Cleaner than HOCs or render props
    
- Composable
    

### 🧱 Example:

```tsx
function useToggle(initial = false) {
  const [value, setValue] = useState(initial);
  const toggle = () => setValue(v => !v);
  return [value, toggle];
}
```

### ✅ Use When:

- Logic is repeated across components (e.g., form handling, API calls)
    

---

## 🧮 7. **Slot/Named Children Pattern**

### 📦 What It Is:

Named props are used to pass subcontent (not just `children`)

### 🧱 Example:

```tsx
const Modal = ({ header, footer, children }) => (
  <>
    <div>{header}</div>
    <div>{children}</div>
    <div>{footer}</div>
  </>
);
```

### ✅ Use When:

- Your component needs **structured layout injection**
    

---

## 🧭 8. **State Reducer Pattern**

### 📦 What It Is:

Expose internal state logic to parent via a reducer function

### 🧠 Why:

- Give consumers control over component behavior
    

### 🧱 Example:

```tsx
function useToggleWithReducer(reducer, initial = false) {
  const [state, dispatch] = useReducer(reducer, initial);
  return [state, () => dispatch({ type: 'toggle' })];
}
```

### ✅ Use When:

- You build reusable components needing **external logic control**
    

---

## 🧩 9. **Static Property Composition** (aka Namespace)

```tsx
<Dropdown>
  <Dropdown.Trigger />
  <Dropdown.Menu />
</Dropdown>
```

Implemented by assigning child components as static props of the parent. Great for scoping and discoverability.

---

## Summary Table

|Pattern|Use Case|Tooling Needed|
|---|---|---|
|Presentational + Container|Separate UI from logic|None|
|HOC|Inject behavior into components|Functions|
|Render Props|Share logic with flexible UI|Functions|
|Compound Components|Multiple parts working together|React Context|
|Controlled/Uncontrolled|Input and form management|useState, refs|
|Custom Hooks|Reusable logic across components|Functions|
|Slot Pattern|Named layout composition|JSX props|
|State Reducer|Exposing internal state control|useReducer|
|Static Property Composition|Scoped API via `Component.SubComponent`|Static props|

---

## 🧠 Final Thought

> Great React architecture is less about picking one pattern — it's about using **the right pattern for the right problem**.



