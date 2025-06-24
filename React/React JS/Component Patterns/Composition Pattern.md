
Here’s a **crisp yet in-depth guide** to the **React Composition Pattern** — one of the most powerful and idiomatic ways to build flexible, reusable components.

---

## 🧱 What is Composition in React?

**Composition** means building UIs by combining smaller components together — like Lego blocks.

Instead of hardcoding structure or behavior, components receive other components (or content) via **props** — especially `children` — and **compose** them internally.

> 🧠 “Prefer composition over inheritance” — a core React principle.

---

## 🧩 Why Use Composition?

✅ Increases **flexibility**  
✅ Promotes **reusability**  
✅ Keeps components **decoupled**  
✅ Simplifies **testing**  
✅ Supports **customization** without duplication

---

## ✨ Core Composition Patterns

### 1. **Children as Content**

Let parent components inject children into reusable wrappers.

```tsx
const Card = ({ children }) => (
  <div className="card">{children}</div>
);

<Card>
  <h2>Title</h2>
  <p>Body content here.</p>
</Card>
```

---

### 2. **Slot Pattern (Named Composition)**

Pass multiple renderable props (slots) for specific positions.

```tsx
const Modal = ({ header, footer, children }) => (
  <div className="modal">
    <div className="header">{header}</div>
    <div className="body">{children}</div>
    <div className="footer">{footer}</div>
  </div>
);

<Modal
  header={<h1>Title</h1>}
  footer={<button>Close</button>}
>
  <p>Modal content here</p>
</Modal>
```

➡️ More scalable than `children` alone for complex layouts.

---

### 3. **Function as Child (Render Props)**

Pass a **function** as a child that gets called with dynamic values.

```tsx
const MouseTracker = ({ children }) => {
  const [pos, setPos] = useState({ x: 0, y: 0 });
  return (
    <div onMouseMove={e => setPos({ x: e.clientX, y: e.clientY })}>
      {children(pos)}
    </div>
  );
}

<MouseTracker>
  {({ x, y }) => <p>Mouse at {x}, {y}</p>}
</MouseTracker>
```

🔁 Enables behavior sharing across components.

---

### 4. **Component Injection**

Let consumers pass components to use internally.

```tsx
const List = ({ items, renderItem }) => (
  <ul>
    {items.map((item, i) => (
      <li key={i}>{renderItem(item)}</li>
    ))}
  </ul>
);

<List
  items={['A', 'B', 'C']}
  renderItem={item => <strong>{item}</strong>}
/>
```

🧠 Think of `renderItem` as a customizable slot for a loop.

---

### 5. **Compound Components**

Use context to build a set of components that work together.

```tsx
const TabsContext = React.createContext();

const Tabs = ({ children, value, onChange }) => (
  <TabsContext.Provider value={{ value, onChange }}>
    {children}
  </TabsContext.Provider>
);

const Tab = ({ value, children }) => {
  const ctx = useContext(TabsContext);
  const active = ctx.value === value;
  return (
    <button onClick={() => ctx.onChange(value)} className={active ? 'active' : ''}>
      {children}
    </button>
  );
};

<Tabs value="a" onChange={v => console.log(v)}>
  <Tab value="a">Tab A</Tab>
  <Tab value="b">Tab B</Tab>
</Tabs>
```

🧩 Allows building flexible component APIs (like headless UI libraries).

---

## 🧠 When to Use Composition

✅ When you want consumers to **inject behavior or content**  
✅ When components need to **stay flexible**  
✅ To avoid **prop drilling** and over-configuration  
✅ When logic needs to be **shared** but rendered differently

---

## 🚫 Avoid When...

- The structure is fixed and won’t vary
    
- Simpler props are enough
    
- Overusing context/slots may lead to complexity
    

---

## 🧾 Summary

|Pattern|Use for|
|---|---|
|`children`|Simple content injection|
|Named slots|Structured layouts (modals, cards)|
|Render props|Dynamic behavior injection|
|Component injection|Customizable render logic (lists, forms)|
|Compound components|Groups with shared state/context|

---

## 🔚 Final Thought

> Composition isn’t just a pattern — it’s the React way.  
> Embrace it to build reusable, declarative, and elegant UI systems.



