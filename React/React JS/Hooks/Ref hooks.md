

## UseRef
### **Purpose**

The `useRef` hook:

- Provides a way to create a persistent reference to a **DOM element** or a **mutable value**.
- Avoids triggering re-renders when the referenced value changes.

---

### **Key Use Cases**

1. **Accessing DOM Elements**
    
    - Obtain a direct reference to a DOM element for manipulation (e.g., focusing an input field).
2. **Storing Mutable Values**
    
    - Hold values that don’t need to trigger re-renders, such as timers or previous values.
    - Useful for maintaining function references or tracking mutable variables.
    - Keeping a mutable variable that persists for the full lifetime of the component.

---

### **Key Characteristics**

- **No Re-renders**: Updates to the `useRef.current` value do **not** cause the component to re-render.
- **Persistent Reference**: The `useRef` value persists across renders without resetting.
- **Direct DOM Manipulation**: Enables direct access and manipulation of DOM elements.

---

### **Examples**

#### **1. Accessing & Modifing a DOM Element**

```jsx
import React, { useRef } from 'react';

function ColorBox() {
  const boxRef = useRef(null); // Create a ref for the color box

  const changeColor = () => {
    boxRef.current.style.backgroundColor = 'lightblue'; // Change the background color
  };

  return (
    <div>
      <div
        ref={boxRef}
        style={{ width: '100px', height: '100px', backgroundColor: 'red' }}
      />
      <button onClick={changeColor}>Change Color</button>
    </div>
  );
}
```

**Key Points**:
- The `boxRef` is assigned to the div representing the color box.
- The `changeColor` function modifies the style of the DOM element directly.


---

#### **2. Storing Mutable Values**

```jsx
import { useRef, useEffect } from 'react';

function Timer() {
  const timerRef = useRef(null); // Store the timer ID

  useEffect(() => {
    timerRef.current = setInterval(() => {
      console.log('Timer tick'); // Log every second
    }, 1000);

    return () => clearInterval(timerRef.current); // Clear timer on cleanup
  }, []);

  return <h1>Check the console for timer ticks!</h1>;
}
```

- **Key Points**:
    - The `timerRef` persists the interval ID across renders.
    - Using `useRef` prevents unnecessary re-renders when the timer is updated.

---

#### **3. Storing a Function**

```jsx
import { useRef } from 'react';

function MyComponent() {
  const handleClick = useRef(() => {
    console.log('Initial function');
  });

  const updateHandler = () => {
    handleClick.current = () => {
      console.log('Updated function');
    };
  };

  return (
    <div>
      <button onClick={handleClick.current}>Run Function</button>
      <button onClick={updateHandler}>Update Function</button>
    </div>
  );
}
```

- **Key Points**:
    - `useRef` can hold function references, which can be dynamically updated without re-rendering the component.

---

---

### **When to Use `useRef` vs `useState`**

|**Scenario**|**useRef**|**useState**|
|---|---|---|
|Persistent data without triggering re-renders|✅ Ideal|❌ Triggers re-renders unnecessarily|
|Triggering UI updates|❌ Not suitable|✅ Automatically triggers renders|
|Accessing and manipulating DOM elements|✅ Suitable|❌ Not possible|
|Storing dynamic, mutable values|✅ Suitable|❌ Leads to unnecessary re-renders|

---

## UseImperativeHandle


### **Purpose**

The `useImperativeHandle` hook in React is a powerful tool that allows you to customize the value or methods exposed by a child component's `ref` to its parent. It enables a parent component to directly invoke specific methods or access properties of a child component without exposing the entire implementation.

Child to parent communication!



---

### **How It Works**

1. **Arguments:**
    
    - **`ref`**: The `ref` passed from the parent to the child.
    - **`createHandle`**: A function that returns an object containing the properties and methods to expose.
    - **`deps` (Dependencies)**: An optional dependency array that controls when the `createHandle` function is re-evaluated.
2. **Returns:**
    
    - An object containing methods or properties for the parent to use.
3. **Requires `forwardRef`:**
    
    - The child component must use `forwardRef` to allow the parent to pass a `ref` down to it. (in react19, don't need forwardRef wrapper I guess.. )

---

### **Key Use Cases**

1. **Exposing Controlled Actions:**
    
    - Expose specific methods (e.g., focus, validation, scroll-to) of a child component for the parent to call.
2. **Encapsulation:**
    
    - Keeps internal implementation details of the child component hidden while exposing only what is necessary.
3. **Optimized Reusability:**
    
    - Enables reusable and customizable child components with clear and intentional API exposure.

---

### **Simple Example: Custom Input Focus**

```jsx
import React, { useImperativeHandle, forwardRef, useRef } from 'react';

// Child Component
const CustomInput = forwardRef((props, ref) => {
  const inputRef = useRef();

  useImperativeHandle(ref, () => ({
    focus: () => inputRef.current.focus(), // Expose focus method
    clear: () => (inputRef.current.value = ""), // Expose clear method
  }));

  return <input ref={inputRef} type="text" placeholder="Type something..." />;
});

// Parent Component
function Parent() {
  const inputRef = useRef();

  return (
    <div>
      <CustomInput ref={inputRef} />
      <button onClick={() => inputRef.current.focus()}>Focus Input</button>
      <button onClick={() => inputRef.current.clear()}>Clear Input</button>
    </div>
  );
}
```

**Key Points:**

- The parent can directly invoke `focus` or `clear` methods on the child.
- The child encapsulates the logic, exposing only the required methods.

---

### **Real-World Example: Collapsible Panel**

In complex UI components like a collapsible panel or accordion, `useImperativeHandle` allows a parent to control the expanded/collapsed state or trigger animations programmatically.

```jsx
import React, { useImperativeHandle, forwardRef, useRef, useState } from 'react';

// Collapsible Panel Component
const CollapsiblePanel = forwardRef((props, ref) => {
  const [isOpen, setIsOpen] = useState(false);
  const panelRef = useRef();

  useImperativeHandle(ref, () => ({
    toggle: () => setIsOpen((prev) => !prev),
    expand: () => setIsOpen(true),
    collapse: () => setIsOpen(false),
  }));

  return (
    <div>
      <button onClick={() => setIsOpen((prev) => !prev)}>
        {isOpen ? "Collapse" : "Expand"}
      </button>
      {isOpen && (
        <div ref={panelRef} style={{ padding: "10px", border: "1px solid black" }}>
          <p>This is the content of the panel.</p>
        </div>
      )}
    </div>
  );
});

// Parent Component
function App() {
  const panelRef = useRef();

  return (
    <div>
      <CollapsiblePanel ref={panelRef} />
      <button onClick={() => panelRef.current.expand()}>Expand Programmatically</button>
      <button onClick={() => panelRef.current.collapse()}>Collapse Programmatically</button>
    </div>
  );
}
```

**Key Points:**

- The parent can control the state of the collapsible panel using methods exposed by `useImperativeHandle`.
- Encapsulation ensures the internal implementation remains hidden.

---

### **Real-World Example: Form Validation**

`useImperativeHandle` can help expose form validation logic from a child form component to the parent.

```jsx
import React, { useImperativeHandle, forwardRef, useRef } from 'react';

// Form Component
const Form = forwardRef((props, ref) => {
  const nameRef = useRef();
  const emailRef = useRef();

  const validate = () => {
    const errors = {};
    if (!nameRef.current.value) {
      errors.name = "Name is required";
    }
    if (!emailRef.current.value.includes("@")) {
      errors.email = "Email is invalid";
    }
    return errors;
  };

  useImperativeHandle(ref, () => ({
    submit: () => {
      const errors = validate();
      if (Object.keys(errors).length === 0) {
        alert("Form submitted successfully!");
      } else {
        alert(JSON.stringify(errors));
      }
    },
  }));

  return (
    <div>
      <input ref={nameRef} placeholder="Name" />
      <input ref={emailRef} placeholder="Email" />
    </div>
  );
});

// Parent Component
function App() {
  const formRef = useRef();

  return (
    <div>
      <Form ref={formRef} />
      <button onClick={() => formRef.current.submit()}>Submit Form</button>
    </div>
  );
}
```

**Key Points:**

- The parent can trigger validation and submission logic without directly accessing or managing the form’s internal state.
- The form component remains reusable and self-contained.

---

### **Alternatives to `useImperativeHandle`**

Before reaching for `useImperativeHandle`, consider alternative patterns:

1. **Props and Callbacks**:  
    Pass a callback function from the parent to the child. The child can invoke this function when required.
2. **Context API**:  
    Share state and methods across deeply nested components without props drilling.
3. **State Lifting**:  
    Lift the child’s state up to the parent and manage it centrally.

---

### **Key Considerations**

- **Use Sparingly**: Overusing `useImperativeHandle` can lead to tightly coupled components, breaking React’s unidirectional data flow.
- **Focus on Encapsulation**: Expose only the minimal set of methods or properties that the parent needs to interact with.
- **Avoid Overcomplicating**: If simple state or props management can solve the problem, prefer those over `useImperativeHandle`.

---

### **Summary**

- The `useRef` hook is a powerful tool for interacting with DOM elements or managing mutable values. It avoids unnecessary re-renders, making it an excellent choice for performance-critical applications.
- Use `useImperativeHandle` and `forwardRef` for advanced use cases involving parent-child communication.


---

