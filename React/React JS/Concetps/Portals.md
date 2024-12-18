

### **React Portals: Rendering Outside the Root DOM Node**

**What Are React Portals?** React Portals provide a way to render children into a DOM node that exists outside the DOM hierarchy of the parent component.

---

### **Key Features**

1. **Separation of Concerns**: Allows components to be visually and structurally separated from the rest of the app while maintaining React's event bubbling.
2. **Event Propagation**: Events triggered within the portal propagate as if they occurred in the component tree, following React's bubbling mechanism.
3. **Common Use Cases**:
    - Modals/Dialogs
    - Tooltips
    - Popovers
    - Overlays

---

### **How It Works**

React Portals are created using the `ReactDOM.createPortal` method, which takes two arguments:

1. **Child**: The React component or JSX to render.
2. **Container**: The DOM element where the child should be rendered.

---

### **Code Example: Modal with Portals**

```jsx
import React from 'react';
import ReactDOM from 'react-dom';

const Modal = ({ isOpen, onClose, children }) => {
  if (!isOpen) return null; // Don't render if modal is not open

  return ReactDOM.createPortal(
    <div style={modalStyles}>
      <div style={modalContentStyles}>
        <button onClick={onClose} style={closeButtonStyles}>
          Close
        </button>
        {children}
      </div>
    </div>,
    document.getElementById('portal-root') // Render outside the main app root
  );
};

const App = () => {
  const [isModalOpen, setIsModalOpen] = React.useState(false);

  return (
    <div>
      <h1>React Portals Example</h1>
      <button onClick={() => setIsModalOpen(true)}>Open Modal</button>
      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)}>
        <h2>Modal Content</h2>
        <p>This is rendered using React Portals!</p>
      </Modal>
    </div>
  );
};

// Example styles
const modalStyles = {
  position: 'fixed',
  top: 0,
  left: 0,
  width: '100%',
  height: '100%',
  backgroundColor: 'rgba(0,0,0,0.5)',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
};

const modalContentStyles = {
  backgroundColor: '#fff',
  padding: '20px',
  borderRadius: '8px',
  maxWidth: '500px',
  width: '100%',
};

const closeButtonStyles = {
  backgroundColor: '#f44336',
  color: '#fff',
  border: 'none',
  padding: '8px 12px',
  cursor: 'pointer',
  float: 'right',
};

export default App;
```

### **Steps to Set Up**

1. Add an additional `div` with an ID (e.g., `portal-root`) to your `index.html` file:
    
    ```html
    <div id="portal-root"></div>
    ```
    
2. Use `ReactDOM.createPortal` to render content into this `div`.

---

### **Key Considerations**

- **Styling**: Ensure proper styling for the portal content since it’s outside the main app tree.
- **Accessibility**: Manage focus trapping and keyboard navigation for modals rendered via portals.
- **Event Bubbling**: React handles event bubbling seamlessly, so events inside the portal bubble up through the React tree as expected.

---

### **Advantages**

- **Flexibility**: Render components anywhere in the DOM while keeping them logically inside the React component tree.
- **Clean Structure**: Ideal for UI elements that must appear at a higher DOM level without disrupting parent styles.

React Portals are powerful tools for creating advanced UI components like modals, tooltips, and overlays, while maintaining React’s declarative nature.
