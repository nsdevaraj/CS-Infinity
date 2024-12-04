
#### DOM Management

- **Vanilla JS DOM vs React's Virtual DOM**:
  - Traditional DOM updates are costly as changes reflect directly on the **real DOM**. => repainting flow retriggers more.. 
  - React manages a **Virtual DOM**—a lightweight in-memory representation of the DOM. Changes are first reflected in the virtual DOM, and only the differences (diffs) between the real and virtual DOM are updated, enhancing performance.

#### React Components
# React Component
* Everything is a component in React
* 2 Types of components
    - Class Based Components - OLD ( lifecycle methods )
    - Function Based Components - NEW ( v16.4 have hooks to support lifecycle method and other actions )
    -  Naming convention: **PascalCase** for components, **camelCase** for other variables.


- **JSX**: 
  - React uses **JSX (JavaScript XML)**, which looks like writing **HTML in JavaScript**, but it’s JavaScript creating DOM elements.
  - JSX allows for dynamicity: We can conditionally render content, manage lists, and handle user events.
  
---

# Why react?

- It can be applied to the existing project since its library, not framework which need to applied on whole project

• React library vs other frameworks like Angular, Vue  

