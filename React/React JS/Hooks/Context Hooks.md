
https://usehooks-ts.com/

https://usehooks.com/



### **5. Context Hooks**

Context Hooks in React provide a way to share values between components without explicitly passing props through every level of the component tree. The primary hook for this is `useContext`.

---

#### **5.1 `useContext`: Accessing Context Values**

- **What It Does**: `useContext` allows you to consume context values easily in any functional component.
- **Use Case**: Ideal for sharing global data, like themes or authentication status, across the application without prop drilling.

**Example**:
```jsx
import React, { createContext, useContext } from 'react';

// Create a Context for the theme
const ThemeContext = createContext('light'); // Default value is 'light'

function ThemedComponent() {
  const theme = useContext(ThemeContext); // Access the theme value from context

  return <div className={`theme-${theme}`}>Current Theme: {theme}</div>; // Use the theme in the component
}

function App() {
  return (
    <ThemeContext.Provider value="dark"> {/* Provide the 'dark' theme */}
      <ThemedComponent />
    </ThemeContext.Provider>
  );
}

export default App;
```

**Key Points**:
- **Creating Context**: A context is created using `createContext`, which provides a default value.
- **Consuming Context**: `useContext(ThemeContext)` allows the component to access the current theme value from the nearest provider above it.
- The theme can easily be changed by wrapping components in a different `Provider`.

---

#### **5.2 Updating Context Values**

- **What It Does**: Context values can be updated using state management techniques combined with context.
- **Use Case**: Great for managing user preferences or application settings.

**Example**:
```jsx
import React, { createContext, useContext, useState } from 'react';

// Create a Context for the theme
const ThemeContext = createContext();

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light'); // Manage theme state

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}> {/* Provide theme and setter */}
      {children}
    </ThemeContext.Provider>
  );
}

function ThemedComponent() {
  const { theme, setTheme } = useContext(ThemeContext); // Access theme and setter

  return (
    <div className={`theme-${theme}`}>
      Current Theme: {theme}
      <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>Toggle Theme</button>
    </div>
  );
}

function App() {
  return (
    <ThemeProvider>
      <ThemedComponent />
    </ThemeProvider>
  );
}

export default App;
```

**Key Points**:
- **Provider Component**: The `ThemeProvider` manages the theme state and provides both the theme value and the setter function through context.
- **Updating Context**: The button toggles between light and dark themes by calling `setTheme`, demonstrating dynamic context updates.

---

### Summary of Context Hooks:
- **`useContext`**: Enables easy access to context values in any component wrapped within the provider.
- Context Hooks eliminate the need for prop drilling, allowing for cleaner and more manageable code, especially in larger applications.

---

Let me know when you're ready for the next section on **Transition Hooks**!



josh - custom hooks

```js
export function useDebounce<T>(value: T, delay?: number): T {  
  const [debouncedValue, setDebouncedValue] = useState<T>(value);  
  useEffect(() => {  
    const timer = setTimeout(() => setDebouncedValue(value), delay || 500);  
    return () => {  
      clearTimeout(timer);  
    };  
  }, [value, delay]);  
  return debouncedValue;  
}


const debouncedValue = useDebounce<string>(inputValue, delayTimer);


useEffect(() => {  
    if (!isMounted.current) {  
      isMounted.current = true;  
      return;  
    }  
    onChange(debouncedValue);  
  }, [debouncedValue]);
  
```



