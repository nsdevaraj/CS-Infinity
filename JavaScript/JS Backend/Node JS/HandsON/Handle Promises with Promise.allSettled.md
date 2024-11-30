

### **Question 2: Create a Node.js Script to Handle Promises with `Promise.allSettled`**

**Problem:**  
Write a Node.js script that fetches data from three different asynchronous functions:

1. One resolves successfully with some data.
2. One rejects with an error.
3. One resolves after a delay.

Use `Promise.allSettled` to handle all three promises and log the results of each promise, including whether it was fulfilled or rejected.

**Answer:**  
Here’s the implementation:

```javascript
// Simulated asynchronous functions
const fetchData1 = () =>
  new Promise((resolve) => {
    setTimeout(() => resolve('Data from fetchData1'), 1000);
  });

const fetchData2 = () =>
  new Promise((_, reject) => {
    setTimeout(() => reject('Error in fetchData2'), 1500);
  });

const fetchData3 = () =>
  new Promise((resolve) => {
    setTimeout(() => resolve('Data from fetchData3 after delay'), 2000);
  });

// Main script
(async () => {
  const promises = [fetchData1(), fetchData2(), fetchData3()];

  const results = await Promise.allSettled(promises);

  results.forEach((result, index) => {
    console.log(`Promise ${index + 1}:`);
    if (result.status === 'fulfilled') {
      console.log(`  Status: Fulfilled`);
      console.log(`  Value: ${result.value}`);
    } else {
      console.log(`  Status: Rejected`);
      console.log(`  Reason: ${result.reason}`);
    }
  });
})();
```

**Expected Output (after delays):**

```
Promise 1:
  Status: Fulfilled
  Value: Data from fetchData1
Promise 2:
  Status: Rejected
  Reason: Error in fetchData2
Promise 3:
  Status: Fulfilled
  Value: Data from fetchData3 after delay
```

**Explanation:**

- `Promise.allSettled` ensures all promises are handled, regardless of whether they resolve or reject.
- The `status` and `value/reason` of each promise are logged.
- Demonstrates handling complex asynchronous workflows with detailed error and success reporting.

