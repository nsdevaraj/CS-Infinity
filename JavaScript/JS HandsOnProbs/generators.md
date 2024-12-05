

### **19. Write a function to generate Fibonacci numbers.**

#### **Answer:**

```javascript
function* fibonacci() {
  let [a, b] = [0, 1];
  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
}
// Usage:
const fib = fibonacci();
console.log(fib.next().value); // 0
console.log(fib.next().value); // 1
```




