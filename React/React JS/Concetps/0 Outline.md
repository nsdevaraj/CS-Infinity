


[[React roadmap]]

[[History]]

[[React code]]

[[React/React JS/Concetps/Overview]]


[[Virtual DOM]]
[[Templating]]
[[Components]]



[[Props]]




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


[[phases of react]]



[[Strict mode]]
[[Rerender]]

[[debug]]



[[custom middleware]]


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




watching {
https://youtu.be/wIyHSOugGGw
}


to watch. {

https://www.youtube.com/watch?v=4AXQgOcL1mo


}

 
Extra :  
  
Swallow copy vs deep copy  
100 concepts in js  
  

to check:
js engine and js environment whole
indexed collections , mapped collections, weaksets and things!.. => how memory
js => JIT or interpreter





