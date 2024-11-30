

### 1. Debounce
**Debounce** limits the rate at which a function is executed. It ensures that a function is only called once after a specified delay has passed since the last call. This is useful for cases like waiting for a user to stop typing before sending a request.Here’s a simple debounce implementation:```javascript  
function debounce(func, delay) {  
  let timeoutId;  
  return function (...args) {  
    clearTimeout(timeoutId);  
    timeoutId = setTimeout(() => func.apply(this, args), delay);  
  };  
}// Usage example:  
const debouncedFunction = debounce(() => console.log("Debounced!"), 1000);  
window.addEventListener("resize", debouncedFunction);  
```- **Explanation**: Each time the function is invoked, `clearTimeout` cancels any pending timeout. If no further calls are made before `delay` milliseconds pass, the function will execute.### 2. Throttle**Throttle** limits the execution of a function to once every specified time interval, regardless of how often it is triggered. This is useful in cases where you want a function to run at regular intervals, like scrolling or resizing events.Here’s a simple throttle implementation:```javascript  
function throttle(func, interval) {  
  let lastTime = 0;  
  return function (...args) {  
    const now = Date.now();  
    if (now - lastTime >= interval) {  
      lastTime = now;  
      func.apply(this, args);  
    }  
  };  
}// Usage example:  
const throttledFunction = throttle(() => console.log("Throttled!"), 1000);  
window.addEventListener("scroll", throttledFunction);  
```- **Explanation**: The `throttle` function checks if the specified `interval` has passed since the last call. If it has, the function is executed, and the `lastTime` is updated. If not, the function is ignored until the interval has passed.### Summary- **Debounce**: Executes the function only after a certain delay has passed since the last call.  
- **Throttle**: Ensures the function is executed at regular intervals, regardless of how often it’s triggered.