
### **54. How would you implement a queue data structure in JavaScript?**

#### **Answer:**

```javascript
class Queue {
  constructor() {
    this.items = [];
  }
  enqueue(item) { this.items.push(item); }
  dequeue() { return this.items.shift(); }
  isEmpty() { return this.items.length === 0; }
}
```


