

### **2. useLocalStorage: Manage State with Local Storage**

```jsx
import { useState } from 'react';

/**
 * Custom hook to sync state with local storage.
 * @param {string} key - Local storage key.
 * @param {any} initialValue - Initial value.
 * @returns {Array} [storedValue, setValue]
 */
export function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch {
      return initialValue;
    }
  });

  const setValue = (value) => {
    try {
      setStoredValue(value);
      window.localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      console.error('Error saving to localStorage', error);
    }
  };

  return [storedValue, setValue];
}

// Example usage
function App() {
  const [name, setName] = useLocalStorage('name', 'Guest');

  return (
    <div>
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Enter your name" />
      <p>Hello, {name}!</p>
    </div>
  );
}
```
