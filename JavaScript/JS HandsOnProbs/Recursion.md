

### **38. Write a function to calculate the factorial of a number using recursion.**

#### **Answer:**

```javascript
function factorial(n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}
console.log(factorial(5)); // 120
```


