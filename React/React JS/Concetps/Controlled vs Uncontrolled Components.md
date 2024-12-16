

- **What is the difference between controlled and uncontrolled components in React?**
    
    - Controlled components have their state managed by React (via props/state). Uncontrolled components rely on the DOM to manage state using refs.



#### **Controlled Components**:

A **controlled component** is one where React is responsible for managing the component's state. The state is always bound to React state via props, and the component’s behavior is entirely controlled by React.

- **Characteristics**:
    
    - **State Managed by React**: The form data or state is controlled by React and updated via state changes.
    - **Single Source of Truth**: React has complete control over the form input values, and the value is stored in the component's state.
    - **Event Handling**: Updates are handled using React's `setState()` method or the setter function from `useState()`.
- **When to Use**:
    
    - When you need to keep track of form input values, validation, or when the form data should be used elsewhere in the app.
- **Example** (Controlled Component):
    
    ```jsx
    function ControlledInput() {
      const [value, setValue] = useState("");
    
      const handleChange = (e) => {
        setValue(e.target.value);
      };
    
      return (
        <input 
          type="text" 
          value={value}  // Controlled by React state
          onChange={handleChange}
        />
      );
    }
    ```
    

#### **Uncontrolled Components**:

An **uncontrolled component** is one where React does not manage the state of the component. The form element maintains its own internal state, and you typically interact with it using **refs**.

- **Characteristics**:
    
    - **State Managed by DOM**: The form data is not controlled by React. Instead, the DOM itself maintains the state.
    - **Using Refs**: Instead of binding state to React, you access the current value using `ref`.
    - **Less React Overhead**: Often simpler for smaller or static forms where you don't need to manage the state actively.
- **When to Use**:
    
    - When you don't need to manipulate or track form inputs dynamically, or when dealing with legacy code or simple forms.
- **Example** (Uncontrolled Component):
    
    ```jsx
    function UncontrolledInput() {
      const inputRef = useRef();
    
      const handleSubmit = () => {
        alert("Entered value: " + inputRef.current.value);  // Accessing the DOM node's value directly
      };
    
      return (
        <div>
          <input type="text" ref={inputRef} />
          <button onClick={handleSubmit}>Submit</button>
        </div>
      );
    }
    ```
    

---

### **Summary Table**

|**Feature**|**Pure Component**|**Impure Component**|
|---|---|---|
|**Definition**|Renders the same output for the same input.|Output may vary even for the same input.|
|**Side Effects**|No side effects.|May have side effects (e.g., API calls, DOM manipulations).|
|**Performance Optimization**|Can be optimized to avoid unnecessary re-renders (e.g., using `React.PureComponent`).|No built-in optimization for re-renders.|
|**Use Case**|Simple components that don’t depend on external state.|Complex components with external dependencies.|

|**Feature**|**Controlled Component**|**Uncontrolled Component**|
|---|---|---|
|**State Management**|Managed by React state.|Managed by the DOM, accessed via refs.|
|**Data Flow**|Single source of truth (React).|DOM handles its own state.|
|**Performance**|React controls re-rendering based on state changes.|Less React overhead, but no automatic re-rendering when data changes.|
|**Use Case**|Forms or inputs that require validation or need to be controlled programmatically.|Simple forms where you don’t need to track state.|

---

When to use each :

- **Use Controlled Components** when:
    
    - You need to track form data, handle validation, or manage input dynamically.
- **Use Uncontrolled Components** when:
    
    - You don't need to track the value in state, and just need to access it when necessary, often in simpler forms.
