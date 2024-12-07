




### **1. Write a polyfill for `Promise.all`.**

**Answer:**

```javascript
Promise.myAll = function (promises) {
  return new Promise((resolve, reject) => {
    let results = [];
    let completed = 0;

    promises.forEach((promise, index) => {
      Promise.resolve(promise)
        .then((value) => {
          results[index] = value; // Store result in order
          completed++;
          if (completed === promises.length) resolve(results);
        })
        .catch(reject); // Reject immediately if any promise fails
    });
  });
};

// Example:
const p1 = Promise.resolve(1);
const p2 = Promise.resolve(2);
const p3 = Promise.resolve(3);
Promise.myAll([p1, p2, p3]).then(console.log); // [1, 2, 3]
```

---

### **2. Write a polyfill for `Promise.race`.**

**Answer:**

```javascript
Promise.myRace = function (promises) {
  return new Promise((resolve, reject) => {
    promises.forEach((promise) => {
      Promise.resolve(promise).then(resolve).catch(reject); // Resolve/reject with the first settled promise
    });
  });
};

// Example:
const p1 = new Promise((resolve) => setTimeout(resolve, 100, 'First'));
const p2 = new Promise((resolve) => setTimeout(resolve, 200, 'Second'));
Promise.myRace([p1, p2]).then(console.log); // "First"
```

---

### **3. Write a polyfill for `Promise.allSettled`.**

**Answer:**

```javascript
Promise.myAllSettled = function (promises) {
  return new Promise((resolve) => {
    let results = [];
    let completed = 0;

    promises.forEach((promise, index) => {
      Promise.resolve(promise)
        .then((value) => {
          results[index] = { status: 'fulfilled', value };
        })
        .catch((reason) => {
          results[index] = { status: 'rejected', reason };
        })
        .finally(() => {
          completed++;
          if (completed === promises.length) resolve(results);
        });
    });
  });
};

// Example:
const p1 = Promise.resolve(1);
const p2 = Promise.reject('Error');
const p3 = Promise.resolve(3);
Promise.myAllSettled([p1, p2, p3]).then(console.log);
// [
//   { status: 'fulfilled', value: 1 },
//   { status: 'rejected', reason: 'Error' },
//   { status: 'fulfilled', value: 3 }
// ]
```

---

### **4. Implement a simple `Promise` class (Polyfill for `Promise`).**

**Answer:**

```javascript
function MyPromise(executor) {
  let onResolve, onReject, isResolved = false, isRejected = false, value;

  this.then = function (callback) {
    onResolve = callback;
    if (isResolved) onResolve(value);
    return this;
  };

  this.catch = function (callback) {
    onReject = callback;
    if (isRejected) onReject(value);
    return this;
  };

  function resolve(val) {
    isResolved = true;
    value = val;
    if (onResolve) onResolve(value);
  }

  function reject(val) {
    isRejected = true;
    value = val;
    if (onReject) onReject(value);
  }

  executor(resolve, reject);
}

// Example:
const p = new MyPromise((resolve, reject) => {
  setTimeout(() => resolve('Success!'), 1000);
});
p.then(console.log); // "Success!"
```

These polyfills are commonly discussed in interviews to test understanding of JavaScript's core concepts like prototypes and promises.




