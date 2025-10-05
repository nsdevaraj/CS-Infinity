
 _"Static Property Composition"_** or **"Component Namespace Pattern"** — it's not always formally named in docs, but it's widely used and very powerful in React.

---

## 🧱 What is `Component.SubComponent`?

It’s a composition pattern where subcomponents are exposed as **static properties** on a parent component:

```tsx
<MyComponent>
  <MyComponent.Header>Header content</MyComponent.Header>
  <MyComponent.Body>Body content</MyComponent.Body>
</MyComponent>
```

Instead of importing all parts separately:

```tsx
import { Header, Body } from './MyComponentParts';
```

You use:

```tsx
import { MyComponent } from './MyComponent';
<MyComponent.Header />
```

---

## ✅ Why Use It?

- **Namespacing**: Groups related components logically
    
- **Improved DX**: Discoverable via auto-complete (e.g. `MyComponent.`)
    
- **Cleaner Imports**: Reduces import clutter
    
- **Scoped Context**: Easier to share context internally if needed
    

---

## 🛠️ How It Works (Implementation)

```tsx
// MyComponent.tsx
const Header = ({ children }) => <div className="header">{children}</div>;
const Body = ({ children }) => <div className="body">{children}</div>;

const MyComponent = ({ children }) => (
  <div className="wrapper">{children}</div>
);

MyComponent.Header = Header;
MyComponent.Body = Body;

export { MyComponent };
```

Now use it like:

```tsx
<MyComponent>
  <MyComponent.Header>Header</MyComponent.Header>
  <MyComponent.Body>Body</MyComponent.Body>
</MyComponent>
```

---

## 🧩 When to Use This Pattern

- For **modular UI components** (e.g., `Modal`, `Tabs`, `Card`, `Form`)
    
- When you want to **encapsulate a component API** in a clean, discoverable way
    
- When subcomponents are **useless outside** their parent
    
- When you want to **avoid prop drilling** using context internally
    

---

## 🧠 Benefits

|Feature|Why it helps|
|---|---|
|🔒 Encapsulation|Subcomponents tied closely to parent logic|
|🧼 Clean API|Looks like a DSL (Domain-Specific Language)|
|🤝 Better UX for devs|Auto-suggest via `.` in IDEs|

---

## 🚫 Watch Out For

- Static properties aren't as friendly to **tree-shaking** (but this is rarely critical).
    
- Can get confusing if **subcomponent logic is reused elsewhere** (consider separating if needed).
    
- IDEs may not always auto-type static assignments unless you're using TypeScript carefully.
    

---

## 🧾 Bonus: TypeScript Example

```ts
type MyComponentType = React.FC & {
  Header: React.FC;
  Body: React.FC;
};

const MyComponent = (({ children }) => (
  <div>{children}</div>
)) as MyComponentType;

MyComponent.Header = ({ children }) => <header>{children}</header>;
MyComponent.Body = ({ children }) => <section>{children}</section>;

export default MyComponent;
```

---

## 🧪 Real-World Examples

- 🧱 **Ant Design**: `Form.Item`, `Layout.Sider`
    
- 💬 **Chakra UI**: `Tabs.TabList`, `Tabs.TabPanel`
    
- 🧩 **Headless UI**: Grouped UI logic via namespaces
    

---

## 🧠 Summary

|Term|Also Known As|
|---|---|
|`Component.Sub`|Static Property Composition|
||Component Namespace Pattern|
||Compound API via static members|

> Use this pattern to create intuitive, modular APIs that scale — especially when building design systems or reusable component libraries.

---
