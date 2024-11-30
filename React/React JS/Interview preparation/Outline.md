

[[React basics]]


[[React State and Lifecycle]]
[[Props and State Management]]
[[React hooks]]
[[React Lifecycle and Hooks Integration]]
[[State Management and Context API]]

[[controlled vs uncontrolled]]

[[Error Boundary]]


[[React Performance Optimization]]


[[React Router and Navigation]]


[[Order of Exec]]



hoc

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



to check {

https://akcoding.medium.com/react-hooks-interview-questions-24d39464a49e

https://www.scholarhat.com/tutorial/react

}






Error Bounder - hook workings full flow
