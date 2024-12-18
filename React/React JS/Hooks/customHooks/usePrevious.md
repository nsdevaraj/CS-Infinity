

### **3. usePrevious: Track Previous State or Props**

```jsx
import { useRef, useEffect } from 'react';

/**
 * Custom hook to get the previous value of a state or prop.
 * @param {any} value - The current value.
 * @returns {any} The previous value.
 */
export function usePrevious(value) {
  const ref = useRef();

  useEffect(() => {
    ref.current = value;
  }, [value]);

  return ref.current;
}

// Example usage
function Counter() {
  const [count, setCount] = useState(0);
  const previousCount = usePrevious(count);

  return (
    <div>
      <p>Current: {count}, Previous: {previousCount}</p>
      <button onClick={() => setCount((prev) => prev + 1)}>Increment</button>
    </div>
  );
}
```
