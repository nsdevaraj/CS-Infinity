

### **4. useDebounce: Debounce Input for Optimized Performance**

```jsx
import { useState, useEffect } from 'react';

/**
 * Custom hook to debounce a value.
 * @param {any} value - The value to debounce.
 * @param {number} delay - Delay in milliseconds.
 * @returns {any} Debounced value.
 */
export function useDebounce(value, delay) {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);

  return debouncedValue;
}

// Example usage
function Search() {
  const [query, setQuery] = useState('');
  const debouncedQuery = useDebounce(query, 500);

  useEffect(() => {
    if (debouncedQuery) {
      console.log(`Searching for: ${debouncedQuery}`);
    }
  }, [debouncedQuery]);

  return <input onChange={(e) => setQuery(e.target.value)} placeholder="Search..." />;
}
```

---
