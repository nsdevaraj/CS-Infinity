

### **Question 3: Build a Simple Event Emitter in Node.js**

**Problem:**  
Create a custom `EventEmitter` class in Node.js with methods for subscribing to events (`on`), emitting events (`emit`), and removing listeners (`off`). Demonstrate its usage with multiple event listeners.

**Answer:**  
Here’s the implementation:

```javascript
class EventEmitter {
  constructor() {
    this.events = {};
  }

  // Subscribe to an event
  on(event, listener) {
    if (!this.events[event]) {
      this.events[event] = [];
    }
    this.events[event].push(listener);
  }

  // Emit an event
  emit(event, ...args) {
    if (this.events[event]) {
      this.events[event].forEach((listener) => listener(...args));
    }
  }

  // Remove a listener
  off(event, listenerToRemove) {
    if (this.events[event]) {
      this.events[event] = this.events[event].filter(
        (listener) => listener !== listenerToRemove
      );
    }
  }
}

// Usage
const emitter = new EventEmitter();

const listener1 = (data) => console.log(`Listener 1 received: ${data}`);
const listener2 = (data) => console.log(`Listener 2 received: ${data}`);

emitter.on('message', listener1);
emitter.on('message', listener2);

console.log('Emitting "message" event...');
emitter.emit('message', 'Hello World!'); // Both listeners should be called

console.log('Removing Listener 1...');
emitter.off('message', listener1);

console.log('Emitting "message" event again...');
emitter.emit('message', 'Hello Again!'); // Only Listener 2 should be called
```

**Expected Output:**

```
Emitting "message" event...
Listener 1 received: Hello World!
Listener 2 received: Hello World!
Removing Listener 1...
Emitting "message" event again...
Listener 2 received: Hello Again!
```

**Explanation:**

- The `on` method adds listeners to a specified event.
- The `emit` method triggers all listeners for a given event, passing arguments as needed.
- The `off` method removes a specific listener for an event, ensuring clean-up.
- Demonstrates core Node.js patterns, useful for event-driven applications.
