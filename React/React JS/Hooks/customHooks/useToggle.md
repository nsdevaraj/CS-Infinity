

### **6. useToggle: Manage Boolean State**

```jsx
import { useState } from 'react';

/**
 * Custom hook to toggle a boolean value.
 * @param {boolean} initialValue - Initial value.
 * @returns {Array} [value, toggle]
 */
export function useToggle(initialValue = false) {
  const [value, setValue] = useState(initialValue);

  const toggle = () => setValue((prev) => !prev);

  return [value, toggle];
}

// Example usage
function App() {
  const [isVisible, toggleVisibility] = useToggle();

  return (
    <div>
      <button onClick={toggleVisibility}>
        {isVisible ? 'Hide' : 'Show'}
      </button>
      {isVisible && <p>Now you see me!</p>}
    </div>
  );
}
```
