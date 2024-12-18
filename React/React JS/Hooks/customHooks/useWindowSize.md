

### **5. useWindowSize: Track Window Dimensions**

```jsx
import { useState, useEffect } from 'react';

/**
 * Custom hook to track the window's dimensions.
 * @returns {Object} { width, height }
 */
export function useWindowSize() {
  const [size, setSize] = useState({
    width: window.innerWidth,
    height: window.innerHeight,
  });

  useEffect(() => {
    const handleResize = () => {
      setSize({
        width: window.innerWidth,
        height: window.innerHeight,
      });
    };

    window.addEventListener('resize', handleResize);
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  return size;
}

// Example usage
function App() {
  const { width, height } = useWindowSize();

  return (
    <p>
      Window size: {width} x {height}
    </p>
  );
}
```
